# Alice wrote an exam containing N true-or-false questions. Each question is worth 1 mark, and there is no negative marking.
#  Alice scored K marks out of N.

# cook your dish here
t= int(input())
for i in range(t):
    k,n = map(int,input().split())
    print(k-n)