# Step 1: Input the Hours and Tips
X = 5.44
M = int(input("How many Hours Did you work?:"))
B = int(input("What were your Tips?:"))

#Step 2: Calculate the Average Wage for the Day
Y = (M*X+B)
Average = (Y/M)
#Step 3: Display Results as a percentage.
print ("Your Wages for the Day Are: $",format (Y, ',.2f'))
print ("Your Average Wage for the Day Is: $",format (Average, ',.2f'))
input()
