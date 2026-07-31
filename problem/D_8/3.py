# Chef has recently moved into an apartment. It takes 30 minutes for Chef to reach the office from the apartment.
# Chef left for the office X minutes before he was supposed to reach. 
# Determine whether or not Chef will be able to reach on time


# cook your dish here

t= int(input())
for i in range(t):
    x= int(input())
    if x>=30:
        print("yes")
    else:
        print("no")