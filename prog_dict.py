import csv
# shows menu with available options
print("""Dictionary for a little programmer, press a number for desired option:
1) search explanation by appellation
2) add new definition
3) show all appellations alphabetically
0) exit""")
# allow user to input desired option
option = input()

# open dictionary to file to read
f = open("./dictionary.csv", "r")
# create a dictionary for data read from file
dictionary = {}
for line in f:
    # process each line from file into dictionary, with explanation and source as a tuple
    line = line.strip()
    line = line.split(' | ')
    dictionary[line[0]] = (line[1], line[2])

# if statements for different options entered
if option == "1":
    word = input("Enter searched appellation: ")
    # returns an item from 'dictionary' with 'word' as its key
    searched_word = dictionary.get(word)
    print(searched_word)
elif option == "2":
    # three variables allowing user to input new line to dictionary file
    appellation = input("Enter appellation: ")
    explanation = input("Enter explanation: ")
    source = input("Enter source: ")
    # formatting new line for dictionary file
    new_dict_item = (appellation + " | " + explanation + " | " + source)
    # opening and writing new line into dictionary
    f = open("./dictionary.csv", "a")
    f.write(new_dict_item + "\n")
elif option == "3":
    # sorting and printing dictionary appellations alphabetically in a list
    print(sorted(dictionary.keys()))
elif option == "0":
    exit
