# weather_advice.py
# Ask the user to input the current from a predefinedset of conditions:
#What's the weather like today? (sunny, rainy, cold)
# Based on the input, provide advice on what to wear.
def get_weather_advice():
    weather = input("What is the weather like today? (sunny/rainy/cold): ")
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")