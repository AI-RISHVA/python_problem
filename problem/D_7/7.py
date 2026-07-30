# Pooja would like to withdraw X US Dollars from an ATM. 
# The cash machine will only accept the transaction if X is a multiple of 5 and
# Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
# For each successful withdrawal, the bank charges 0.50 US Dollars

# cook your dish here
x,y = map(float,input().split())
if x%5 ==0 and x+0.50 <= y:
    y -=x+0.50
print(f"{y:.2f}")