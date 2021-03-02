
#3) Use Generators to read the file And Print all the words in a file.
def read_large_file(file_handler):
    
    for line in file_handler:
        
        word_arr= []
        for i in line:
            if(i != " " and i != "/n"):
                word_arr.append(i)

            else:
                yield word_arr
                word_arr = []




with open('/Python practice/Problems on deco and gen/text_content.txt', 'r') as file_handler:
    x =  read_large_file(file_handler)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    
    
        