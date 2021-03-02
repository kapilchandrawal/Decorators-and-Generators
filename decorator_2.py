
#Decorators Problems:
# Problem 2:
#Standardize Mobile Number Using Decorators
#You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:
#The given mobile numbers may have +91,91, 
#or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

number_list = [input() for _ in range(int(input()))]

def wrapper(f):
    def phone(number_list):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in number_list])
    return phone

@wrapper
def sort_phone(number_list):
    print(*sorted(number_list), sep='\n')

sort_phone(number_list)