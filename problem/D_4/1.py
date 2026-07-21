
# A blood drive aims to collect N number of blood donations.The drive has collected X donations so far. Find the remaining number of donations needed to reach the target.


# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(n-x)