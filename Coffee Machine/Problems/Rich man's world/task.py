deposit = int(input())
years = 0
while deposit < 700000:
    deposit = deposit + deposit * 0.071
    years += 1
print(years)
