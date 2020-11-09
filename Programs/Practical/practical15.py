class Student:
    def __init__(self,name,hindi,eng,math):
        self.name = name
        self.hindi = hindi
        self.eng = eng
        self.math = math
        self.avg = (hindi+eng+math)/3

    def __del__(self):
        print("Object Deleted")

    def Display(self):
        print(f'''
        Name          : {self.name}
        Hindi         : {self.hindi}
        English       : {self.eng}
        Maths         : {self.math}
        Average Marks : {self.avg}
        ''')

def main():
    name = input("Name : ")
    hindi = int(input("Hindi : "))
    eng = int(input("English : "))
    math = int(input("Math : "))
    student = Student(name,hindi,eng,math)
    student.Display()
    del student

if __name__ == "__main__":
    main()
