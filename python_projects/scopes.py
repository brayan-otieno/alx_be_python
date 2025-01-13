# Global scope
var = "I am a global variable"

def my_function():
    # Local scope
    var = "I am a local variable"
    print("Inside the function, var =", var)  # This will print the local variable

# Outside the function
print("Outside the function, var =", var)  # This will print the global variable

my_function()
