### Exercise 1: Reverse each word of a string

    def R_Word(string):
        words = string.split()
        rev_words = [i[::-1] for i in words]
        rev_string = " " .join(rev_words)
        return rev_string
    input_str = input(Write someting to reverse: )
    reveresed = R_Word(input_str)
    

