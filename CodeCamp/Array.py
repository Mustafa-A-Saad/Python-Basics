"""
# Arrays ( Lists )
luckynum = [40 , 15, 15 , 16 , 23 , 42.3]
friends = ["Kevin","Jim","Karen","Jim","Oscar","Toby"]
friends.append("Koby") # adds at the end
friends.insert(0,"Kelly") # doesn't replace , it adds and moves everything to the right
friends.remove("Oscar")
luckynum[3] = 25
#friends.clear()
friends.pop() # pops the last element
# friends.sort() # sort Aphelbtically
luckynum.reverse() # reverses the list
# luckynum.sort() # sort from least to high
# friends2 = friends.copy() # identical copy of it
friends.extend(luckynum) # extends another list
print(luckynum.count(15)) # counts How many () in the list
print(friends) # lists all the array
print(friends.index("Kevin")) # index of()
print(friends.count("Jim")) # Counts how many
print(friends[1]) # shows [] index.name
print(friends[1:5]) # 5 isn't included
print(friends[1:]) # starts from 1 to all

"""

# 2D arrays

number_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# print(number_list[0][2])

for row in number_list: # For Each row in ()
    print(row)
    for col in row: # for each col in row in ()
        print(col)
