

try:
   numerator = int(input("Enter a numerator: "))
   denominator = int(input("Enter denominator: "))
   if numerator / denominator * denominator == numerator:
     print ("Divides evenly!")
   else:
     print ("Doesn't divide evenly.")

except ZeroDivisionError:
   print ("Can not divide by zeros.")