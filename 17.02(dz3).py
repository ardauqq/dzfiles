import os

current = os.getcwd()
folder = 'dz'
file_names = ['1.txt', '2.txt', '3.txt']
all_files = {}
for fname in file_names:
    full_path = os.path.join(current, folder, fname)
    with open(full_path, encoding='utf-8') as f:
        a = f.readlines()
        all_files[fname] = a

file_output = 'vivod.txt'
full_path = os.path.join(current, folder, file_output)
with open(full_path, 'w', encoding='utf-8') as out:
    for i in sorted(all_files, key=lambda el: len(all_files[el])):
        out.write(f'{i}\n')
        out.write(f'{str(len(all_files[i]))}\n')
        for j in all_files[i]:
            out.write(f'{j.strip()}\n')
        out.write(f"{'--------------------------------------------------'}\n")