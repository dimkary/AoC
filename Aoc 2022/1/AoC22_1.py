with open("./input.txt") as f:
    a = f.read().split("\n\n")
dic = {}
for i in (range(len(a))):
    dic[i] = sum([int(x) for x in a[i].split()])

calories = sorted(list(dic.values()), reverse=True)

print(calories[0])
print(sum(calories[0:3]))
