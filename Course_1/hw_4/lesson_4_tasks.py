line = "13fet35kk54"

numbers = 0
letters = 0

for symbol in line:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        numbers += 1
        
print(f"Всего чисел: {numbers}\nВсего букв: {letters}")

############

line = "abcdefghijklmnopqrstuvwxyz"

user_input = input().split('-')

i_1 = int(user_input[0])
i_2 = int(user_input[1])

print(line[i_1:i_2+1])

###########


