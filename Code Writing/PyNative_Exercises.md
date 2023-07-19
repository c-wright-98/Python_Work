### Exercise 1: Reverse each word of a string ###

    def R_Word(string):
        words = string.split()
        rev_words = [i[::-1] for i in words]
        rev_string = " " .join(rev_words)
        return rev_string
    input_str = input(Write someting to reverse: )
    reveresed = R_Word(input_str)
    print(reveresed)

### Exercise 3: Remove items from a list while iterating ###
In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50

    nums = []

    while True:
        Uinput = input("Add a intger to your list, press q to quit")

        if Uinput.isdigit():
            nums.append(int(Uinput))
        else:
            break

    print(f"This is your list: {nums}")

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > 50:
            del nums[i]

    print(f"This is the fixed list: {nums}")

The -1-1-1 in the for loop makes the loop check the list in reverse so as items are removed it still checks every item

### Exercise 3: Generate 6 digit random secure OTP

