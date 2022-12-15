#input_text_file = "sample.txt"
input_text_file = "input.txt"

list_of_group_priorities = []

with open(input_text_file) as input_file:
    number_contained_ranges = 0
    for index, pair in enumerate(input_file):
        pair = pair.strip()
        elf_1_range_ids, elf_2_range_ids = pair.split(",")

        r1_start, r1_end = elf_1_range_ids.split("-")
        r1 = range(int(r1_start), 1+int(r1_end))
        elf_1_range = set(r1)

        r2_start, r2_end = elf_2_range_ids.split("-")
        r2 = range(int(r2_start), 1+int(r2_end))
        elf_2_range = set(r2)

        if elf_1_range.issubset(elf_2_range) or elf_2_range.issubset(elf_1_range):
            number_contained_ranges += 1

print(number_contained_ranges)
#store answer as a comment
#490