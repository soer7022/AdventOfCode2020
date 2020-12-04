import json

with open("input.txt") as f:
    data = [l.replace("\n", " ") for l in f.read().split("\n\n")]
valid = 0
correct_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for e in data:
    keys = []
    elements = e.split(" ")
    invalid = False
    for var in elements:
        key,value = var.split(":")
        keys.append(key)
        if key == "byr":
            value = int(value)
            if value > 2002 or value < 1920:
                invalid = True
        elif key == "iyr":
            value = int(value)
            if value < 2010 or value > 2020:
                invalid = True
        elif key == "eyr":
            value = int(value)
            if value < 2020 or value > 2030:
                invalid = True
        elif key == "hgt":
            if value.endswith("cm"):
                value = int(value.split("c")[0])
                if value < 150 or value > 193:
                    invalid = True
            else:
                value = int(value.split("i")[0])
                if value < 59 or value > 76:
                    invalid = True
        elif key == "hcl":
            if len(value) != 7:
                invalid = True
            if value[0] != "#":
                invalid = True
        elif key == "ecl":
            if value not in correct_ecl:
                invalid = True
        elif key == "pid":
            if len(value) != 9:
                invalid = True
    if not invalid and"byr" in keys and "iyr" in keys and "eyr" in keys and "hgt" in keys and "hcl" in keys and "ecl" in keys and "pid" in keys:
        valid += 1
print(valid)
