a=int(input("enter the new loaves soid:"))
b=int (input(" enter the one day loaves sold:"))
if (a<=0):
 print("enter a positive  number greater then zero")
else:
     c=a*185
     d=(b*185)*60/100
print("regular price=185")
print("amount of new loaves",float(c))
print ("amount of old day loaves ", float(d))
print ("total amoount",float(c+d))
