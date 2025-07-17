# weather_advice.py
# Ask the user for weather condinditiond and give clothing advice
def get_weather_advice():
    weather = input("What is the weather like? (sunny, rainy, windy): ").strip().lower()

    if weather == "sunny":
        print("It's sunny! Wear light clothing and sunglasses.")
    elif weather == "rainy":
        print("It's rainy! Don't forget your umbrella and wear waterproof shoes.")
    elif weather == "windy":
        print("It's windy! Wear a windbreaker and secure your hat.")
    else:
        print("Sorry, I don't have advice for that kind of weather.")