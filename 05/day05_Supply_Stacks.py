#input_text_file = "sample.txt"
input_text_file = "input.txt"

all_details = []
raw_crate_positions = []
top_crates = []
instructions = []


def initialise_stacks(raw_crate_positions, stack_labels):
    # create list for each column
    stack_lists = []
    for stack in range(number_of_stacks):
        stack_lists.append([])
    for row in reversed(raw_crate_positions):
        for n in range(1, len(row), 4):
            if row[n].isalpha():
                stack_lists[int((n - 1) / 4)].append(row[n])
    print("starting positions:  \n")
    for crates in raw_crate_positions:
        print(f"{crates}\n")
    print(f"{stack_labels}")
    print("*****************************************\n")
    return stack_lists

def top_crates(stack_lists):
    top_crates = []
    for n in range(len(stack_lists)):
        top_crates.append(stack_lists[n][-1].strip())
    return top_crates

# def visualise_stacks(stack_lists):
#     continue


def rearrangement_procedure(instructions, stack_lists):
    for index, move in enumerate(instructions):

        list_of_instructions = move.split(" ")
        repeats = int(list_of_instructions[1])
        origin_stack = int(list_of_instructions[3])-1
        destination_stack = int(list_of_instructions[5])-1

        n = 1
        for n in range(repeats):
            lifted_crate = stack_lists[origin_stack].pop(-1)
            stack_lists[destination_stack].append(lifted_crate)
            n += 1

    return stack_lists

if __name__ == '__main__':

    with open(input_text_file) as input_file:
        for index, line in enumerate(input_file):
            stripped_line = str.strip(line)
            all_details.append(line)
            if stripped_line == "":
                divide_line_index = index
            else:
                continue

        assert divide_line_index > 0
        stack_labels = all_details[(divide_line_index - 1)]
        number_of_stacks = int(max(stack_labels))
        diagram_height_rows = divide_line_index
        raw_crate_positions = all_details[0:(divide_line_index - 1)]
        instructions = all_details[(divide_line_index + 1):]

        initial_stack_lists = initialise_stacks(raw_crate_positions, stack_labels)
        print(f"initial top crates: {top_crates(initial_stack_lists)}")

    final_stack_lists = rearrangement_procedure(instructions, initial_stack_lists)

    print(f"final top crates: {top_crates(final_stack_lists)}")
    without_punctuation = "".join(stack[-1] for stack in final_stack_lists)
    print(f"without punctuation: {without_punctuation}")
    #store answer as a comment
    #QNNTGTPFN