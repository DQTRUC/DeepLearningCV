# Write a Python program to push all zeros to the end of a list.
A = input("Enter any list:")
A=A.split(",")
B=[]
count=0
for i in range(len(A)):
    if int(A[i])!= 0:
        B.append(int(A[i]))

    else:
        count=count+1
for i in range(count):
    B.append(0)
print("Result:",B)
