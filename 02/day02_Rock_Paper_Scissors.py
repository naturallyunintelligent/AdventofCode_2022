#input_text_file = "sample.txt"
input_text_file = "input.txt"

scores = []

with open(input_text_file) as input_file:
    current_game_score = []
    for index, game in enumerate(input_file):

        if game[2] == "X":
            shape_selected = 1
            if game[0] == "A":
                outcome = 3
            elif game[0] == "B":
                outcome = 0
            elif game[0] == "C":
                outcome = 6

        if game[2] == "Y":
            shape_selected = 2
            if game[0] == "A":
                outcome = 6
            elif game[0] == "B":
                outcome = 3
            elif game[0] == "C":
                outcome = 0

        if game[2] == "Z":
            shape_selected = 3
            if game[0] == "A":
                outcome = 0
            elif game[0] == "B":
                outcome = 6
            elif game[0] == "C":
                outcome = 3

        current_game_score = shape_selected + outcome
        scores.append(current_game_score)
print(sum(scores))
#10310