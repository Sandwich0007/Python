'''
Q11. Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points)
Video Solution is given just after this resource
'''

games_played=int(input("Enter the number of games of you have played in the tournament = "))
games_won=int(input("Number of games you won = "))
games_lost=int(input("Number of games you lost = "))

games_tie=games_played-games_won-games_lost
total_points=(games_won*4)+(games_tie*2)
print("Match Tie = ",games_tie)
print("Total point = ",total_points)
