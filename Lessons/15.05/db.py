d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

# number = int(input("please enter the number"))
number = 4199392609

res = d.get(number)
if res:
    print(f"{res[0][0]} {res[0][1]} from {res[1][0]}, {res[1][1]}")
else:
    print("the number was not found")

print(f"{d[number][0][0]} {d[number][0][1]} from {d[number][1][0]}, {d[number][1][1]}") if d.get(number) else print("the number was not found")

