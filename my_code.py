class Comparator:
    def compare(self, num1, num2):
        if num1>num2:
            print(str(num1)+" is the bigger number")
        elif num2>num1:
            print(str(num2)+" is the bigger number")
        else:
            print("Both numbers are equal")

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

comp = Comparator()
comp.compare(num1,num2)

