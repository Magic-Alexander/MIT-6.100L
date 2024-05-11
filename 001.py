#decimal to binary converter

result = ''
num = int(input("Enter decimal number you want to convert to binary: "))

if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2

print(result)