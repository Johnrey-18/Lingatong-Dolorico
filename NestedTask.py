names = [
    ["Alice","Bob","Charlie"],
    ["David","Eve","Frank"],
    ["Grace","Heidi","Ivan"],
    ["Judy","Ken","Laura"]
]
ngalan = input("Remove alice: ")

if ngalan == "yes":
    ngalan = input("Replace alice: ")
    names.remove(ngalan)
print(hero)

for bwahaha in names:
        for cute in bwahaha:
            print(cute)

new_name = input("Enter name:")
names[0].append(new_name)
print(names)