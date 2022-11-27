#Q1: Use else block to display a message Done” after successful execution of for loop.

# pin = int(input("type your pin "))
# for var in range(9):
#     if pin != var:
#         continue
#     else:
#         print("Done")

#Q2: Write a program to display all prime numbers within a range.

# l = int(input("Type a number: "))
# u = int(input("Type a number: "))

# for num in range(l, u+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(f'{num} is a prime number')

# #Q3: Use a loop to display elements from a given list present at odd index positions.

# num_list = list(range(1, 9))
# for num in num_list:
#     if num % 2 != 0:
#         print(num_list[num])
#     continue
 
# #Q4: Calculate the cube of all numbers from 1 to a given number

# num = list(range(1, 9))
# num_cubes = [*map(lambda x: (x, x**3), num)]
# print(num_cubes)

