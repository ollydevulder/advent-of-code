import sys
from hashlib import md5
def check(hashed, zeros):
    return hashed[0:zeros] == '0'*zeros
secret_code, zeros = input("Secret code:"), int(input("Amount of zeros:"))
counter = 0
while True:
    counter += 1
    code = secret_code + str(counter)
    hashed = md5(code.encode()).hexdigest()
    if check(hashed, zeros):
        break
    sys.stdout.write("\r{} : {}".format(code, hashed))
    sys.stdout.flush()
print("\nAnswer is {}!".format(counter))
