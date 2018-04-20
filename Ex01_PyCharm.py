# Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit
A = input("Enter any number:")

while len(A) > 1:
    S = 0
    for i in range(len(A)):
        S = S + int(A[i])
    A = str(S)

print("Result:",S)
