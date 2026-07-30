# Write a program to find the remainder when an integer A is divided by an integer B.

# cook your dish here
t= int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(a% b)