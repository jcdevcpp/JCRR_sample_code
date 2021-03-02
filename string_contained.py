#for two strings a and b
#count how many times a can be built with the contents of b
def count_contained_times(a, b):
    list_b=[lett for lett in b]
    a_assemble_count=0
    while True: #iterate until b is depleted from a characters
        for a_char in a:
            found=False #Initialize found indicator for this letter of a
            #traverse b loking for a string character
            for b_char in list_b:
                if a_char == b_char: #found the char to keep the assembling
                    found=True #found one of the pieces to build a
                    list_b.remove(a_char)#take character out
                    break # found it, lets go for the next piece of a
            if not found:
                return a_assemble_count # could not complete string a, return count as is 
        a_assemble_count+=1 # completing the a_char loop, means all letters to assemble a were found

if __name__=="__main__":
    count=count_contained_times("abc", "cbagbbccaabcarthafdtyjubkjhc")
    print(f"{count = }")