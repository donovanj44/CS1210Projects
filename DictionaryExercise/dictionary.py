d = {
    "eporcupi": ["Porcupine", "Egbert", "CS", ["CS1210", "CS1080", "MATH2055", "ANTH1100"]],
    "epickle": ["Pickle", "Edwina", "BIOL", ["BIOL1450", "BIOL1070", "MATH2248", "CHEM1150"]],
    "wquux": ["Quux", "Winston", "ARTS", ["ARTS2100", "ARTS2750", "CS1210", "ARTH1990"]],
    "mgarply": ["Garply", "Mephista", "ENSC", ["ENSC2300", "GEOG1170", "FS2020", "STAT2870"]]
}

print(d["wquux"][2])

count = 0

for i, x in enumerate(d):
    for j, y in enumerate(x[3]):
        if y == "CS1210":
            count = count + 1
print(count)
