import os


def open_file(file):
    count = 0 
    if len(file) < 2:

        print('File is not correct')
    else:

        with open(file, 'r') as file1:
            
            for line in file1:

                if line.startswith("From "):
   
                    words = line.split()
                    if len(words) >= 2:
                        print(words[1])

                    count += 1
    
    print("There were", count, "lines in the file with From as the first word")


open_file("mbox-short1.txt")







