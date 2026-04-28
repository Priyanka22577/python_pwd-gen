import random
import string
import sys

length = int(sys.argv[1])
count = int(sys.argv[2])

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print(f"Password {i+1}: {password}")
