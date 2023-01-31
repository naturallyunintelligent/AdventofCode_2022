
#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        trees = []
        for index, line in enumerate(input_file):
            trees.append(line.strip())
    return trees


def count_edges(tree_heights):
    row_count = 0

    for line in tree_heights:
        row_length = len(line)
        row_count += 1

    edge_trees = (row_length * 2) + ((row_count - 2) * 2)

    return edge_trees

def count_visible_interior_trees(tree_heights):
    visible_trees = 0
    northern_max_heights = []
    for tree in tree_heights[0]:
        northern_max_heights.append(tree)
    southern_max_heights = []

    for i, line in enumerate(tree_heights):
        for tree, height in enumerate(line):
            if i == 0:
                southern_max_heights.append([])
            else:
                southern_max_heights[tree].append(height)

    for i, line in enumerate(tree_heights):

        if i == 0 or i == len(tree_heights)-1:
            continue
        else:
            for tree, height in enumerate(line):
                southern_max_heights[tree].pop(0)
                if tree == 0 or tree == len(line)-1:
                    continue
                if max(line[:tree]) < height or max(line[(tree+1):]) < height:
                    visible_trees += 1
                elif northern_max_heights[tree] < height:
                    visible_trees += 1
                elif max(southern_max_heights[tree]) < height:
                    visible_trees += 1
                northern_max_heights[tree] = max(northern_max_heights[tree], height)


    return visible_trees

if __name__ == '__main__':

    tree_heights = load_data(input_text_file)

    edge_trees = count_edges(tree_heights)

    visible_interior_trees = count_visible_interior_trees(tree_heights)

    total_visible_trees = edge_trees + visible_interior_trees

    if input_text_file == "sample.txt":
        assert total_visible_trees == 21

    print(f"total_visible_trees: {total_visible_trees}")

    #store answer as a comment
    #
    #