
# input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        trees = []
        for index, line in enumerate(input_file):
            trees.append(line.strip())
    return trees


def analyse_scenery(tree_heights):
    max_scenic_score = 0
    for y, line in enumerate(tree_heights):
        print("")
        for x, height in enumerate(line):
            EastCount = 0
            EastView = x + 1

            while EastView < len(line):
                EastCount += 1
                if line[EastView] >= height:
                    break
                else:
                    EastView += 1

            # print(EastCount, end="")

            WestCount = 0
            WestView = x - 1
            while WestView >= 0:
                WestCount += 1
                if line[WestView] >= height:
                    break
                else:
                    WestView -= 1
            # print(WestCount, end="")


            NorthCount = 0
            NorthView = y - 1
            while NorthView >= 0:
                NorthCount += 1
                if tree_heights[NorthView][x] >= height:
                    break
                else:
                    NorthView -= 1
            # print(NorthCount, end="")

            SouthCount = 0
            SouthView = y + 1
            while SouthView < len(tree_heights):
                SouthCount += 1
                if tree_heights[SouthView][x] >= height:
                    break
                else:
                    SouthView += 1
            # print(SouthCount, end="")


            scenic_score = NorthCount * SouthCount * EastCount * WestCount

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

            scenic_score = 0

    return max_scenic_score

if __name__ == '__main__':

    tree_heights = load_data(input_text_file)

    max_scenic_score = analyse_scenery(tree_heights)

    if input_text_file == "sample.txt":
        assert max_scenic_score == 8

    print(f"max_scenic_score: {max_scenic_score}")

    #store answer as a comment
    #519064
    #