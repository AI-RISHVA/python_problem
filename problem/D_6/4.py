# There are only 2 types of denominations in Chefland:
# Coins worth 1 rupee eachNotes worth 10 rupees eachChef wants to pay his friend exactly X rupees. 
# What is the minimum number of coins Chef needs to pay exactly X rupees?

# cook your dish here
t= int(input())
for i in range(t):
    x= int(input())
    print(x %10)