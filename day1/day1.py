elves = list()

with open('input.txt', 'r') as input_file:
    input_contents = input_file.readlines()
    elf_cal = list()
    for record in input_contents:
        if record == "\n":
            elves.append(elf_cal)
            elf_cal = list()
            continue
        cal_value = int(record.strip())
        elf_cal.append(cal_value)

sum_list = [sum(elf) for elf in elves]
sum_list.sort()

top_three_sum = int(sum_list[-1] + sum_list[-2] + sum_list[-3])

print(f'Most calories: {sum_list[-1]}, sum of top three: {top_three_sum}')
