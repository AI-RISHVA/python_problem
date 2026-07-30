# Chef considers the climate HOT if the temperature is above 20, 
# otherwise he considers it COLD. You are given the temperature C, find whether the climate is HOT or COLD.

# cook your dish here
t = int(input())
for i in range(t):
    c= int(input())
    if c>20:
        print("HOT")
    else:
        print("COLD")