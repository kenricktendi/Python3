#Kenrick Tendi
#Exercise7 unit 2 

num = 0 

while num <= 0:
    try:    
        num = int(input('enter a positive number:'))
    except ValueError:
        print("Not a positive number!")
    
def retrieve_positive_number():
        if num == 0:
            print("Zero is not a positive number.")
        elif num < 0:
            print("Number is not a positive.")
        elif num > 0:
            print("Thats a positive number.")
            return num 

retrieve_positive_number()
        