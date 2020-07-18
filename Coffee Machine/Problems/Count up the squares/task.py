# put your python code here
sum_ = "False"
sum_1 = 0
square = 0
while sum_ == "False":
    num = int(input())
    sum_1 += num
    square += (num * num)
    if sum_1 == 0:
        print(square)
        sum_ = "True"
