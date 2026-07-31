# DAIICT college students want to attend an IPL match. A total of N students from the college want to go, 
# while only M tickets are available for the match.
# Determine how many students won't be able to book tickets.

# cook your dish here
t= int(input())
for i in range(t):
    n,m = map(int,input().split())
    if n>m:
        print(n-m)
    else:
        print(0)