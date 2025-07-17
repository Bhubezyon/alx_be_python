# weather_advice.py
# Ask the user to input the current from a predefinedset of conditions:
#What's the weather like today? (sunny, rainy, cold)
# Based on the input, provide advice on what to wear.
def get_weather_advice():
    weather = input("What is the weather like today? (sunny, rainy, cold): ").strip().lower()
    if weather == "sunny":
        print("It's sunny! Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("It's rainy! Don't forget your umbrella and raincoat.")
    elif weather == "cold":
        print("It's cold! Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")