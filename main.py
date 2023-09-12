with open('1.txt', 'r', encoding='utf-8') as file:
    lines_1 = len(file.readlines())

with open('2.txt', 'r', encoding='utf-8') as file:
    lines_2 = len(file.readlines())

with open('3.txt', 'r', encoding='utf-8') as file:
    lines_3 = len(file.readlines())

files_lens = [lines_1, lines_2, lines_3]
files_lens_sort = sorted(files_lens)

with open('united.txt', 'a', encoding='utf-8') as file:
    file.write(f'2.txt\n{str(files_lens_sort[0])}\n')

with open('2.txt', 'r', encoding='utf-8') as first_file, open('united.txt', 'a', encoding='utf-8') as second_file:
    for line in first_file:
        second_file.write(line)
    second_file.write('\n')

with open('united.txt', 'a', encoding='utf-8') as file:
    file.write(f'1.txt\n{str(files_lens_sort[1])}\n')

with open('1.txt', 'r', encoding='utf-8') as first_file, open('united.txt', 'a', encoding='utf-8') as second_file:
    for line in first_file:
        second_file.write(line)
    second_file.write('\n')

with open('united.txt', 'a', encoding='utf-8') as file:
    file.write(f'3.txt\n{str(files_lens_sort[2])}\n')

with open('3.txt', 'r', encoding='utf-8') as first_file, open('united.txt', 'a', encoding='utf-8') as second_file:
    for line in first_file:
        second_file.write(line)
    second_file.write('\n')