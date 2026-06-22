class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("Mama Mia's", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Reusing the Restaurant class from 9-1
restaurant1 = Restaurant("Mama Mia's", "Italian")
restaurant2 = Restaurant("Kati Kati", "Ugandan")
restaurant3 = Restaurant("Tokyo Bites", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()