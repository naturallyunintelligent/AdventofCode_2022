#input_text_file = "sample.txt"
input_text_file = "input.txt"

scores = []

with open(input_text_file) as input_file:
    current_game_score = []
    for index, game in enumerate(input_file):

        if game[2] == "X":
            outcome = 0
            if game[0] == "A":
                shape_selected = 3
            elif game[0] == "B":
                shape_selected = 1
            elif game[0] == "C":
                shape_selected = 2

        if game[2] == "Y":
            outcome = 3
            if game[0] == "A":
                shape_selected = 1
            elif game[0] == "B":
                shape_selected = 2
            elif game[0] == "C":
                shape_selected = 3

        if game[2] == "Z":
            outcome = 6
            if game[0] == "A":
                shape_selected = 2
            elif game[0] == "B":
                shape_selected = 3
            elif game[0] == "C":
                shape_selected = 1

        current_game_score = shape_selected + outcome
        scores.append(current_game_score)
print(sum(scores))
#14859