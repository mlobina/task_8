file_dict = {}
lines_dict = {}
sorted_file_dict = {}
with open('1.txt') as f:
    lines1 = f.readlines()
    lines1_count = len(lines1)
    file_dict.setdefault('1.txt', lines1_count)
    lines_dict.setdefault('1.txt', lines1)

with open('2.txt') as f:
    lines2 = f.readlines()
    lines2_count = len(lines2)
    file_dict.setdefault('2.txt', lines2_count)
    lines_dict.setdefault('2.txt', lines2)

with open('3.txt') as f:
    lines3 = f.readlines()
    lines3_count = len(lines3)
    file_dict.setdefault('3.txt', lines3_count)
    lines_dict.setdefault('3.txt', lines3)

print(file_dict)
print(lines_dict)

def by_value(item):
    return item[1]
for k, v in sorted(file_dict.items(), key=by_value):
    sorted_file_dict.setdefault(k, v)
print(sorted_file_dict)


for key, value in sorted_file_dict.items():
    # for k, v in lines_dict.items():
    text = lines_dict[key]
    with open('4.txt', 'a') as f:
        f.write(key + '\n')
        f.write(str(sorted_file_dict[key]) +'\n')
        f.writelines(i for i in text)
        f.write('\n')

