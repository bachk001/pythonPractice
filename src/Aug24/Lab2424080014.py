# Create a program to sum of three number from the user input

num1 = int(input("Enter the the number 1")) # 100
num2 = int(input("Enter the the number 2")) # 200
num3 = int(input("Enter the the number 3")) # 300


def sum_of_three_number(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_number(100, 200, 300)
print(result)




def sum_of_two_number(a, b):
    return a + b


result_sum1 = sum_of_two_number(10, 30)
result_sum2 = sum_of_two_number(20, 50)
print(result_sum1)
print(result_sum2)


def sum_of_three_number(a=5, b=10, c=15):
    return a + b + c


# result = sum_of_three_number(10, 20, 30)
# result = sum_of_three_number(10, 20)
# result = sum_of_three_number(10)
# result = sum_of_three_number()
result = sum_of_three_number(a=78, c=67)
print(result)