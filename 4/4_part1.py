import json

with open("input.txt") as f:
    data = [l.replace("\n", " ") for l in f.read().split("\n\n")]
valid = 0
for e in data:
    keys = []
    elements = e.split(" ")
    for var in elements:
        print(var)
        key,value = var.split(":")
        keys.append(key)
    print(keys)
    if "byr" in keys and "iyr" in keys and "eyr" in keys and "hgt" in keys and "hcl" in keys and "ecl" in keys and "pid" in keys:
        valid += 1
print(valid)
