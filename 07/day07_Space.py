from collections import defaultdict

#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        terminal_output = []
        for index, line in enumerate(input_file):
            terminal_output.append(line)
    return terminal_output


def add_to_dict(d, keys, value):
    for key in keys[:-1]:
        d = d.get(key)
    d[keys[-1]] = value


def create_dir_tree_dict(terminal_output):
    dir_dict = defaultdict(dict)
    dir_dict["/"] = {}
    working_path = []

    for line in terminal_output:
        line = line.strip()
        words = line.split()
        if words[1] == "cd":
            if words[2] == "..":
                working_path.pop()

            elif words[2] == "/":
                working_path = ["/"]
                # add_to_dict(dir_dict, working_path, {})

            else:
                working_path.append(words[2])
                # add_to_dict(dir_dict, working_path, {})

        elif words[1] == "ls":
            continue

        elif words[0] == "dir":
            working_path.append(words[1])
            add_to_dict(dir_dict, working_path, {})
            working_path.pop()

        else:
            working_path.append(words[1])
            add_to_dict(dir_dict, working_path, int(words[0]))
            working_path.pop()

    return dir_dict


def analyse_dir_sizes(dir_dict):

    chosen_dirs_size = []

    def dir_size(dir_dict):
        current_dir_size = 0
        for dir, content in dir_dict.items():

            if isinstance(content, dict):
                current_dir_size += dir_size(content)
            else:
                current_dir_size += content

        if current_dir_size < 100000:
            chosen_dirs_size.append(current_dir_size)

        return current_dir_size


    dir_size(dir_dict)

    total_size = sum(chosen_dirs_size)



    return total_size

if __name__ == '__main__':

    terminal_output = load_data(input_text_file)

    dir_dict = create_dir_tree_dict(terminal_output)

    sum_of_chosen_dirs = analyse_dir_sizes(dir_dict)

    if input_text_file == "sample.txt":
        assert sum_of_chosen_dirs == 95437

    print(f"sum_of_chosen_dirs: {sum_of_chosen_dirs}")

    #store answer as a comment
    #1453349
    #