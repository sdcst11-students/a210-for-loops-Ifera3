#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

n = int(input("enter a number less then ten: "))
sum = 0
add = 0

if 10 > n > 0:
    for i in range(n):
        add = (add * 10) + 1
        sum = sum + add
    else:
        print(f"the sum of the serise is {sum}")
else:
    print("invalid anser")