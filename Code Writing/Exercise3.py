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