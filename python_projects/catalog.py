# Defien the product class

class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

# Example usage

product1 = product("Car", 1200, 5)
product2 = product("House", 800, 10)

# Get the output

print(f"Total value of {product1.name}: ${product1.total_value()}")
print(f"Total value of {product2.name}: ${product2.total_value()}")

