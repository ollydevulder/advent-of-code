from hashlib import md5
secret_code, zeros = "inputcode", 5
counter = 0
while True:
    counter += 1
    hashed = md5((secret_code + str(counter)).encode()).hexdigest()
    if hashed[0:zeros] == '0'*zeros:
        break
print(counter)
