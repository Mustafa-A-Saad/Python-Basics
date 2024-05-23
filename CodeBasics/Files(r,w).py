""" # Basics

#f=open("F:\\Python WorkShop\\CodeCamp\\funny.txt","r")
with open("F:\\Python WorkShop\\CodeCamp\\funny.txt","r") as f: # same as above and doesn't need to do f.close
    f_out = open("F:\\Python WorkShop\\CodeCamp\\funny_wc.txt", "w")
    for line in f:
        tokens = line.split(" ")  # splits every word between spaces into tokens puts them in an array
                                  # Detects when there is a " " space
        f_out.write("word count: " + str(len(tokens)) + " || " + line)
        print(tokens)  # displays each word as an array
        print(len(tokens))  # displays how many words in the sentence
    # print(line) # Reads each line alone
    # f.close()
    f_out.close()

"""
import os.path

""" # Word Count Project

word_stats={}

with open("PPoem.txt","r") as f:
    for lines in f:
        words = lines.split(" ")
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())  # Prints a list of the dictionary values only
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(f'"{word}" with a count of "{max_count}"')

"""


# Exercise 13 read_write_files , download Excel or SpreadSheet and try again

with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n") # writes the columns name
    next(f)  # This will skip first line in the file which is a header ( company name ,prices ,etc..) ( not reliance and etc..)
    for line in f:
        tokens = line.split(",") # jumps to the next column ( from col 1 to col 2 etc..)
        stock_name = tokens[0] # copys the company name from stocks to output in [0]
        price = float(tokens[1]) # this is the price col
        eps = float(tokens[2]) # earns per sharing col
        book = float(tokens[3]) # book value col
        pe = round(price / eps, 2) # the round () , the second args is the number of digits after a decimal
        pb = round(price / book, 2)
        out.write(f"{stock_name},{pe},{pb}\n")




