import random
from teams import teams, play_game

print("---------------")
print("NCAA Basketball")
print("---------------")
print()
print()

n_games = 30

user_input = True

if user_input == True:
    Team_name = input("Select Team")
else:
    Team_name = "De fault"
user_team = {"Team":Team_name, "Results":[], "Team Points":[]}
print
print("Start of Regular Season")
print("-----------------------")
for i in range(n_games):
    print(f"Game {i+1}:")
    random_team = random.choice(teams)
    print(Team_name, 'vs', random_team)
    print()
    if user_input == True:
        input("Press Enter to see result")
    print()

    user_team_score, other_team_score, extra = play_game(Team_name, random_team)
        
    if user_team_score > other_team_score:
        result = "Win"
    elif user_team_score < other_team_score:
        result = "Loss"
        
    print(f"{Team_name}:{user_team_score}-{random_team}:{other_team_score} {extra}")
    print()
    print(f"{Team_name} get the {result}")
    user_team["Results"].append(result)
    l = user_team["Results"].count("Loss")   
    w = user_team["Results"].count("Win")
    pct = user_team["Results"].count("Win") / len(user_team["Results"])
    print (f"{w}-{l}")
    print(f"Win Percentage: {round(pct, 3)}")
    
    if pct > .600:
        print(f"{Team_name} (20)")
    
    
    
    
    
    print("-----------------------")
    
print()

l = user_team["Results"].count("Loss")   
w = user_team["Results"].count("Win")
pct = user_team["Results"].count("Win") / len(user_team["Results"])
print('End Of Season')
print()
wins = (user_team["Results"]).count("Win") 
losses = (user_team["Results"]).count("Loss") 
print(' Wins-Losses')
print(f"   {wins}-{losses}")
print()
print(f"Win Percentage: {round(pct, 3)}")
print()

if w > 14:
        print('You have Qualified For MARCH MADNESS!')

if w > 18:
        print('You Have Been Ranked in the NCAA Top 25!')
        
if w > 21:
        print('You Have Won Your Conference!')
        
if w < 15:
        print('You have missed March Madness! Better Luck Next Season!')


        
