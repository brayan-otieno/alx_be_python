
#_ THIS SCRIPT WILL ASK THE USER ABOUT THE CURRENT WEATHER CONDITIONS AND PROVIDE CLOTHING RECOMMENDATIONS BASED ON THE INPUT. 
#_ THIS TASK AIMS TO DEMONSTRATE THE USE OF IF, ELIF, AND ELSE STATEMENTS TO MAKE DECISIONS IN A PROGRAM.

#* INSTRUCTIONS:

# PROMPT USER FOR WEATHER INPUT:

# ASK THE USER TO INPUT THE CURRENT WEATHER FROM A PREDEFINED SET OF CONDITIONS: “SUNNY”, “RAINY”, OR “COLD”.

weather = input("What's the weather like today? (sunny/rainy/cold):") #! Use the prompt: “What’s the weather like today? (sunny/rainy/cold): ”.

if weather == "sunny":
    print('Wear a t-shirt and sunglasses.')


elif weather == 'rainy': 
    print("Don't forget your umbrella and a raincoat.")

elif weather == 'cold': 
    print('Make sure to wear a warm coat and a scarf.')

else:
    print("Sorry, I don't have recommendations for this weather.") 
