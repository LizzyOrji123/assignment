#openfile = open(".\story.txt", "r")

def read_file_content(filename):
    #[assignment] Add your code here
    with open(filename, "r") as f:
         file = f.read()
         return(file)

output = read_file_content(".\story.txt")
print(output)
        

def count_words():
    text = read_file_content(".\story.txt")
    counts = dict()
    words = text.split(" ")
    
    
    for word in words:
        if word in counts:
             counts[words] += 1
        else:
                 counts[word] = 1
                 print(counts)

                 print(count_words)
    
     