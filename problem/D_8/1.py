# Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.The meeting platform supports a meeting of maximum 30 minutes
#  without a subscription and a meeting of unlimited duration with a subscription.Determine whether Chef needs to take a subscription or not for setting up the meet.


# cook your dish here
t= int(input())
for i in range(t):
    x= int(input())
    if x>30:
        print("yes")
    else:
        print("no")