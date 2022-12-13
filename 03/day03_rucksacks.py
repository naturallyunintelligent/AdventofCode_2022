#input_text_file = "sample.txt"
input_text_file = "input.txt"

list_of_item_priorities = []

with open(input_text_file) as input_file:

    for index, rucksack in enumerate(input_file):
        item_priority = []
        rucksack = rucksack.strip()
        compartment_size = int(len(rucksack)/2)
        comp_1 = rucksack[:compartment_size]
        comp_2 = rucksack[compartment_size:]
        comp_intersection = set(comp_1).intersection(set(comp_2))
        assert len(comp_intersection) == 1
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for item in comp_intersection:
            item_priority = 1 + alphabet.find(item)
        list_of_item_priorities.append(item_priority)

print(sum(list_of_item_priorities))
#8105