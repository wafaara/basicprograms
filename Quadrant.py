
x=int(input("Enter x:"))
y=int(input("Enter y:"))

if (x > 0 and y > 0):
     print("x and y lies in 1st quadrant")
elif (x < 0 and y > 0):
     print("x and y lies in 2nd quadrant")
elif (x < 0 and y < 0):
     print("x and y lies in 3rd quadrant")
elif (x > 0 and y < 0):
     print("x and y lies in 4th quadrant")
elif (x > 0 and y == 0):
     print("lies in +ve x-axis")
elif (x < 0 and y == 0):
     print("lies in -ve x-axis")
elif (y > 0 and x == 0):
     print("lies in +ve y-axis")
elif (y < 0 and x == 0):
     print("lies in -ve y-axis")
else:
     print(" x and y is at origin")