# Apple considers any iPhone with a battery health of 
# 80% or above, to be in optimal condition.
# Given that your iPhone has X% battery health, find whether it is in optimal condition.


# cook your dish here
t = int(input())
for _ in range(t):
    x =int(input())
    if x>=80:
        print("YES")
    else:
        print("NO")