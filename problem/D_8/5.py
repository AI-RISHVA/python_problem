# A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
# Chef was only able to sleep X hours yesterday. Determine if he is sleep deprived or not.

# cook your dish here

t= int(input())
for i in range(t):
    x= int(input())
    
    if x<7:
        print("yes")
    else:
        print("no")