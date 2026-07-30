# Chef recently started selling a special fruit. 
# He has been selling the fruit for X rupees (where X is a multiple of 100). 
# He currently earns a profit of Y rupees on selling the fruit.Chef decided to increase the selling price by 10%. 
# Please help him calculate his new profit after the increase in selling price.
#     Note that only the selling price has been increased, and the buying price remains the same.

# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    n= y +(x//10)
    print(n)