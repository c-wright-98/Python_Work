### Exercise 1: Reverse each word of a string

    def R_Word(string):
        words = string.split()
        rev_words = [i[::-1] for i in words]
        rev_string = " " .join(rev_words)
        return rev_string
    input_str = input(Write someting to reverse: )
    reveresed = R_Word(input_str)
    print(reveresed)

### Exercise 3: Remove items from a list while iterating
In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50


