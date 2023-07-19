def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True

test1 = is_prime(2)
test2 = is_prime(3)
test3 = is_prime(4)
test4 = is_prime(5)
test5 = is_prime(6)
test6 = is_prime(7)
test7 = is_prime(15)
test8 = is_prime(20)
test9 = is_prime(25)

print(test1,test2,test3,test4,test5,test6,test7,test8,test9)