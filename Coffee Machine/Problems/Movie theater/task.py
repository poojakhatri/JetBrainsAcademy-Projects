num_of_halls = int(input())
capacity = int(input())
number_of_views = int(input())

if number_of_views > (num_of_halls * capacity):
    print("False")
else:
    print("True")
