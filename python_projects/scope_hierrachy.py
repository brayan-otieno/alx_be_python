# Global scope
var = "Global variable"

def outer_function():
    # Enclosing scope
    var = "Enclosing variable"
    
    def inner_function():
        # Local scope
        var = "Local variable"
        print("Inside inner function, var =", var)  # Local variable
        print("Accessing enclosing scope, var =", outer_var)  # Enclosing scope variable
    
    # Accessing outer function's variable
    outer_var = var  # This is the global variable saved as outer_var in outer function
    inner_function()
    
    print("Inside outer function, var =", var)  # Enclosing scope variable

# Global scope access
print("Global scope, var =", var)  # Global variable
outer_function()
