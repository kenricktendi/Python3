my_string = "hello!"

#This one works
my_string = "H" + my_string[1:]

#This one doesn't work 
\my_string[0] = "h"

print (my_string)
