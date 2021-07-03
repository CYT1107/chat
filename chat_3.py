lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] #取出13:32Allen的前五個東西01234
    name = s[0][5:] #取出13:32Allen的第五個東西之後56789...
    print(time, ' ', name)