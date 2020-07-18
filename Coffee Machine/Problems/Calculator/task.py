# put your python code here
num_1 = float(input())
num_2 = float(input())
op_ = input()

if op_ == '+':
    print(num_1 + num_2)
elif op_ == '*':
    print(num_1 * num_2)
elif op_ == '/':
    if num_2 == 0.0:
        print("Division by 0!")
    else:
        print(num_1 / num_2)
elif op_ == '-':
    print(num_1 - num_2)
elif op_ == 'mod':
    if num_2 != 0.0:
        print(num_1 % num_2)
    else:
        print("Division by 0!")
elif op_ == 'pow':
    print(num_1 ** num_2)
elif op_ == 'div':
    if num_2 != 0.0:
        print(num_1 // num_2)
    else:
        print("Division by 0!")
