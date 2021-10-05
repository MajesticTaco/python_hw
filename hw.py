import math

print ('Enter the requested inputs to calculate the perpendicular function') 

x1 = float(input('Enter the value of X1: ')) # A
y1 = float(input('Enter the value of Y1: '))
x2 = float(input('Enter the value of X2: ')) # B
y2 = float(input('Enter the value of Y2: ')) 
x3 = float(input('Enter the value of X3: ')) # C
y3 = float(input('Enter the value of Y3: '))

m = (y2-y1)/(x2-x1) # Aprēķina m no y=mx+b
b = y1-m*x1 # Aprēķina m no y=mx+b
m1 = -m/m**2 # Aprēķina m perpendikulārajai funkcijai
b1 = -(m1*x3-y3) # Aprēķina b perpendikulārajai funkcijai

print ('The input function is y =', m,'x +',b,) # Izprintē ABC funkciju, tas nav obligāti jāliek pabeigtajā darbā
print ('The perpendicular function is y =', m1,'x +',b1,) # Izprintē perpendikulāro funkciju
