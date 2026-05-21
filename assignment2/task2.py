# Task: Cricket Stats Analyzer
# ● Objective: Write a script to analyze cricket stats for a team.
# ● Hints:
# ○ Prompt the user to input the runs scored by each of the five players in a
# cricket match.
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they
# scored.
# ○ Calculate the total runs scored by all players and the average runs.
# ○ Display the total runs and average runs to the user.

total_runs = 0  
for i in range(1, 6):
    runs = int(input(f"Enter runs scored by Player {i}: "))
    total_runs += runs
average_runs = total_runs / 5
print(f"Total Runs: {total_runs}")

print(f"Average Runs: {average_runs:.2f}")
