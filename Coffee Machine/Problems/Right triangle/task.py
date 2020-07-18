import math


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
a_ = RightTriangle(input_c, input_b, input_a)

hyp_ = a_.c
leg_1_ = a_.b
leg_2_ = a_.a

squ = leg_2_ ** 2 + leg_1_ ** 2

if hyp_ ** 2 == squ:
    print((leg_2_ * leg_1_) / 2)

else:
    print("Not right")
