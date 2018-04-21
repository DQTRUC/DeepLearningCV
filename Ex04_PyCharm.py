# Write a Python program to find majority element in a list
A = input("Enter a list:")
A=A.split(",")
B=[0 for i in range(len(A))]
for i in range(len(A)):

    for j in range(i,len(A)):
        if A[i] == A[j]:
            B[i]=B[i]+1

C=B.index(max(B))
print("majority number:",A[C])
