
# TODO: set up to fetch the daily inputs from AoC webpage

#input_text_file = "sample.txt"
input_text_file = "input.txt"

list_of_all_elves_provisions = []

with open(input_text_file) as day01_sample_input:
    
    current_elfs_items = []

    for index, line in enumerate(day01_sample_input):
        line = line.strip()
        if line != "":
            line = int(line)
        if line == "":
            #print(list_of_all_elves_provisions)
            list_of_all_elves_provisions.append(sum(current_elfs_items))
            current_elfs_items = []
        elif line > 0:
            current_elfs_items.append(line)

top_three_elves_provisions = sorted(list_of_all_elves_provisions)[-3:]
print(sum(top_three_elves_provisions))

# 213159