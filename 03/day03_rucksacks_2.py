#input_text_file = "sample.txt"
input_text_file = "input.txt"

list_of_group_priorities = []

with open(input_text_file) as input_file:
    group_member = 1
    group_rucksacks = []
    for index, rucksack in enumerate(input_file):
        item_priority = []
        rucksack = rucksack.strip()
        group_rucksacks.append(rucksack)
        if group_member < 3:
            group_member = group_member + 1
        elif group_member == 3:
            badge = set.intersection(set(group_rucksacks[0]), set(group_rucksacks[1]), set(group_rucksacks[2]))
            assert len(badge) == 1
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for item in badge:
                badge_priority = 1 + alphabet.find(item)
            list_of_group_priorities.append(badge_priority)
            group_member = 1
            group_rucksacks = []



print(sum(list_of_group_priorities))
#store answer as a comment
#2363