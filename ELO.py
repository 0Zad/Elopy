import streamlit as st

def expected(ra,rb,C):
    return 10**(ra/C)/(10**(ra/C)+10**(rb/C))

def classement(elo:dict):
    with open("./equipes.txt", "r") as f_equipe:
        equipes = {line.split(":")[0]: line.split(":")[1].split() for line in f_equipe}    

    for equipe, players in equipes.items():
        avg_elo = sum(elo[player] for player in players) / len(players)
        equipes[equipe] = players + [avg_elo]
    print(equipes)
    return equipes
        

def main(fichier="./matchs.txt"):
    elo = {}
    K, C = 50, 400

    with open(fichier, "r") as f :
        lines = [line.strip() for line in f]

    for line in lines: 

        players = line.split()
        if len(players) % 2 != 0:
            continue
        nb_player = len(players)//2

        for player in players :
            if player not in elo:
                elo[player] = 1500
        
        for player in set(players):
            other_player = set([p for p in players if p != player])
            le = [expected(elo[player], elo[autre], C=C) for autre in other_player]
            e = sum(le)/(nb_player-1)
        
            sa = 0.5
            if nb_player == 2 :
                sa = 1 if player == players[-2] else 0
            
            elif nb_player == 3:
                if player == players[-1]:
                    sa = 0
                elif player == players[-2]:
                    sa = 0.5
                elif player == players[-3]:
                    sa = 1

            elif nb_player == 4:
                if player == players[-1]:
                    sa = 0
                elif player == players[-2]:
                    sa = 0.33
                elif player == players[-3]:
                    sa = 0.66
                elif player == players[-4]:
                    sa = 1
                    
            elo[player] += K*(sa-e)

    return elo

if __name__ == '__main__':
    
    st.write("""
         # Classement flechette !
         """)
    
    if st.button("Individuel"):
        elo_fin = main()
        for player, score in sorted(elo_fin.items(), key=lambda item: item[1], reverse=True):
            # st.write(f'{player} : {elo_fin[player]:.0f}')
            st.write(f'{player} : {score:.0f}')

    if st.button("BMAX premier"):
        elo_fin = main()
        classement_equipe = classement(elo_fin)
        for equipe, score in sorted(classement_equipe.items(), key=lambda item: item[1][-1], reverse=True):
            st.write(f'{equipe} : {score[-1]:.2f}')
