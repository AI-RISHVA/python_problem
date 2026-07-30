# Chef classifies a day to be either rainy, cloudy, or clear.In a particular week, Chef finds X days to be rainy and Y days to be cloudy. 
# Find the number of clear days in the week.

# cook your dish here
x,y= map(int,input().split())
print(7-(y+x))