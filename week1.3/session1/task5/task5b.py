# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items():
    print(c, r)      # we can't di print(c) to print the keys because the last key saved is york and so it will only print york


# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
for keys in rivers:
    print(keys)   #here it prints the first thing in the dicts

for values in rivers:
    print(rivers[values])     # while for the values we have to use rivers[values] so it assigns them to values brcause the computer do not understand which one values which one keys 
# hint: we looked at built in function for dicts last session

""" two ways to print the keys, for me second one is more convenient and more organized"""

for keys in rivers.keys():       # we write brackets after keys because it is a method and writing it without the bracket would cause an error output anything think of it like a vending machine and writing the bracket is pressing the bottun
    print(keys)

for values in rivers.values():
    print(values)