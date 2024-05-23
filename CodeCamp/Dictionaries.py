# Dictionary = special structure that lets u store info as key value pairs
# Jan -> January ex:

MonthConverse = {
    "Jan": "January", # "Key": "Value"
    "Feb": "February",
    "Mar": "March",
    "Nov": "November",
    "Aug": "August",
    0: "December"
}

print(MonthConverse["Nov"]) # Same as below
print(MonthConverse.get("Aug")) # this is better
print(MonthConverse.get("Dec","Not a value")) # if key isn't found it display the defualt message mentioned ()
print(MonthConverse.get(0))
