class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + birth_year
        # calculate the id here


f_name = input()
l_name = input()
year = input()
stud = Student(f_name, l_name, year)

print(f'{stud.id}')
