# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
file_name = input("Enter the name of the file: ")

# open and read the file
total_word_count = 0               #we do this because in a loop and reading line by line we need to count the words line by line and then find the sum
with open (file_name, "r") as infile:
    for line in infile:
        print(line)
        word_count1 = len(line.split())   #this counts the word count of each line
        total_word_count += word_count1   #this finds the sum
print(f"Total word count = {total_word_count}")   
     #Thus, use the second reading way for easier code for word counting





with open("story.txt", "r") as infile:
    text = infile.read()
    print(text)               #not required
words = text.split()
word_count = len(words)
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings


# display the wordcount
print(f" Total words: {word_count}")
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210

