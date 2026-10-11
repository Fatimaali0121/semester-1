# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music_database = {"taylor swift": ["Londonboy", "All too well"], "Majed Al-muhandis": ["JanantGalbi", "Al bedaa"]}


# Pretty-print the data structure
pprint(music_database)


# Display details of one album recorded by a specific artist
print(music_database["taylor swift"])



#(selftask) add a key-value pair and let the value to be a set
music_database["Drake"] = ["scream"]
pprint(music_database)

#(selftask) apply slide36
print(len(music_database))
print(max(music_database))
print(min(music_database))
