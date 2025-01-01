# weather_advice.py

def main():
    # Ask the user about the current weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Provide clothing recommendations based on weather conditions
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the script if it's the main program
if __name__ == "__main__":
    main()
