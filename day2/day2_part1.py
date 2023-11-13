# Code for Advent of Code 2022 Day 2

ROCK = ('A', 'X')
PAPER = ('B', 'Y')
SCISSORS = ('C', 'Z')

WIN = 6
DRAW = 3

results = list()

def evaluate_round(strategy):
    opponent_tool = strategy[0]
    my_tool = strategy[1]
    if opponent_tool in ROCK and my_tool in ROCK:
        # Draw 
        results.append(int(DRAW + 1))
    if opponent_tool in ROCK and my_tool in PAPER:
        # Won
        results.append(int(WIN + 2))
    if opponent_tool in ROCK and my_tool in SCISSORS:
        # Lost
        results.append(3)
    if opponent_tool in PAPER and my_tool in PAPER:
        # Draw
        results.append(int(DRAW + 2))
    if opponent_tool in PAPER and my_tool in SCISSORS:
        # Won
        results.append(int(WIN + 3))
    if opponent_tool in PAPER and my_tool in ROCK:
        # Lost
        results.append(1)
    if opponent_tool in SCISSORS and my_tool in SCISSORS:
        # Draw
        results.append(DRAW + 3)
    if opponent_tool in SCISSORS and my_tool in ROCK:
        # Win
        results.append(WIN + 1)
    if opponent_tool in SCISSORS and my_tool in PAPER:
        # Lost
        results.append(2)
    

with open('input_file.txt', 'r') as input_file:
    strategy_guide = input_file.readlines()

parsed_strategy_guide = [unparsed_strategy.split() for unparsed_strategy in strategy_guide]
for strategy in parsed_strategy_guide:
    if strategy:
        evaluate_round(strategy)


print(sum(results))
