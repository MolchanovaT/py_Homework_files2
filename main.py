f1 = 'files/1.txt'
f2 = 'files/2.txt'
f3 = 'files/3.txt'
list_txt = [f1, f2, f3]
list_lines = []
for f in list_txt:
    with open(f, encoding='utf-8') as fp:
        lines = len(fp.readlines())
        list_lines.append(lines)
ziped_dict = dict(zip(list_lines, list_txt))
sorted_dict = dict(sorted(ziped_dict.items(), key=lambda x: x[0]))

final_f = 'files/final.txt'
with open(final_f, 'w', encoding='utf-8') as final:
    for f in sorted_dict:
        final.write(sorted_dict.get(f).lstrip('files/') + '\n')
        final.write(str(f) + '\n')
        with open(sorted_dict.get(f), encoding='utf-8') as fp:
            lines = fp.readlines()
            for line in lines:
                final.write(line + '\n')
