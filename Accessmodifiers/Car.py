class Car:
    def __init__(self, brand, model, price):
        self.brand = brand        # public: no leading underscore -> accessible anywhere
        self._model = model       # protected: single leading underscore -> convention only, accessible within class/subclasses
        self.__price = price      # private: double leading underscore -> name-mangled, harder to access outside class

    # Getter for the private price attribute
    def get_price(self):
        return self.__price

    # Setter for price (optional, but good practice for private attributes)
    def set_price(self, price):
        self.__price = price

    # Display all values from inside the class -- has access to everything
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: {self.__price}")


# --- Testing the class ---
my_car = Car("Toyota", "Corolla", 25000.00)

# public attribute -> accessible directly
print("Brand (direct access):", my_car.brand)

# protected attribute -> still accessible directly in Python (it's just convention),
# but by convention should only be touched within the class or a subclass
print("Model (direct access):", my_car._model)

# private attribute -> NOT accessible directly via my_car.__price
# print(my_car.__price)  # this would raise an AttributeError
print("Price (via getter):", my_car.get_price())

print("\n--- Using display_details() method ---")
my_car.display_details()