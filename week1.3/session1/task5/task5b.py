# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items():
    print(c, r)


# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
for keys in rivers:
    print(keys)   #here it prints the first thing in the dicts

for values in rivers:
    print(rivers[values])     # while for the values we have to use rivers[values] so it assigns them to values brcause the computer do not understand which one values which one keys 
# hint: we looked at built in function for dicts last session