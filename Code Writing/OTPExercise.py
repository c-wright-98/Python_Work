# Using the secrets module to generate six digit OTP

import secrets as sc

generator = sc.SystemsRandom()

#generate the six digit code, can't use 000000 as python won't register it nor would it 0000001
otp = generator.randrange(100000, 999999)

print(f"Your OTP is: {otp}")