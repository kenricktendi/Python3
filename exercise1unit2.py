#Kenrick Tendi
#Exercise 1 unit 2
#3/11/20




def sunny_day():
    print ("Please wear sunglasses")
    
def rainy_day():
    print ("Please wear a raincoat and rainboots")
    
def snowy_day():
    print ("Wear a thick jacket and snowboots")
    

type_of_weather = input("What is the weather? (sunny, rainy, snowy): ")

if type_of_weather == "sunny":
    sunny_day()
elif type_of_weather == "rainy":
    rainy_day()
elif type_of_weather == "snowy":
    snowy_day()
else:
    print ("Invalid option.")
