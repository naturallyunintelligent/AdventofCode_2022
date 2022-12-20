from collections import defaultdict

input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        terminal_output = []
        for index, line in enumerate(input_file):
            terminal_output.append(line)
    return terminal_output


def add_to_dict(d, keys, value):
    for key in keys[:-1]:
        d[key] = d.setdefault(key, {})
    d[keys[-1]] = value


def create_dir_tree_dict(terminal_output):
    dir_dict = defaultdict(dict)
    working_path = []

    for line in terminal_output:
        line = line.strip()
        words = line.split()
        if words[1] == "cd":
            if words[2] == "..":
                working_path.pop()

            elif words[2] == "/":
                working_path = ["/"]
                add_to_dict(dir_dict, working_path, {})

            else:
                working_path.append(words[2])
                add_to_dict(dir_dict, working_path, {})

        elif words[1] == "ls":
            continue

        elif words[0] == "dir":
            working_path.append(words[1])
            add_to_dict(dir_dict, working_path, {})
            working_path.pop()

        else:
            working_path.append(words[1])
            add_to_dict(dir_dict, working_path, words[0])
            working_path.pop()

    return dir_dict


def analyse_sizes(dir_dict):
    # https://www.tutorialspoint.com/How-to-recursively-iterate-a-nested-Python-dictionary
    # def iterdict(d):
    #     for k, v in d.items():
    #         if isinstance(v, dict):
    #             iterdict(v)
    #         else:
    #             print(k, ":", v)
    #
    # iterdict(D1)

    chosen_dirs_size = []
    for dir in dir_dict:
        current_dir_size = []
        #recursively sum files
        for subdir in dir:
            for file in subdir:
                current_dir_size += file["size"]
        if current_dir_size < 100000:
            chosen_dirs_size += current_dir_size

    return chosen_dirs_size

if __name__ == '__main__':

    terminal_output = load_data(input_text_file)

    dir_dict = create_dir_tree_dict(terminal_output)

    sum_of_dir_total_sizes = analyse_sizes(dir_dict)

    if input_text_file == "sample.txt":
        assert sum_of_dir_total_sizes == 10

    print(f"sum_of_dir_total_sizes: {sum_of_dir_total_sizes}")

    #store answer as a comment
    #
    #