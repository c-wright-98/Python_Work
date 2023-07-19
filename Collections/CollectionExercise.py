books = {"Margaret Atwood": ["The Handmaiden's Tale"],
        "J.R.R. Tolkien": ["The Hobbit","The Lord of the Rings"],
        "Roald Dahl": ["Charlie and the Chocolate Factory"]}

author = input("Enter the author name: ")

# Check if the author exists in the 'books' dictionary
if author in books:
    # Get the list of books by the author
    bookls = books[author]
    #Sort list
    bookls.sort()
    #Join books together into string
    bookstr = ", ".join(bookls)
    print(f"Books by {author}: {bookstr}")
#Else statement for if the author is not in the dictionary
else:
    print("Author not found in the books dictionary.")
