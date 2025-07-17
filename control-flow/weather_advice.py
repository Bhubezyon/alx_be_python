# weather_advice.py
# Ask the user for weather condinditiond and give clothing advice
def get_weather_advice():
    weather = input("What is the weather like? (sunny, rainy, cold): ").strip().lower()
    if weather == "sunny":
        print("It's sunny! Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("It's rainy! Don't forget your umbrella and and raincoat.")
    elif weather == "cold":
        print("It's cold! Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")