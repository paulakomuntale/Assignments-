class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User("Paula", "Nakato", 21, "paula@example.com", "Kampala")
user2 = User("James", "Okello", 24, "james@example.com", "Entebbe")
user3 = User("Grace", "Achan", 19, "grace@example.com", "Gulu")

for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()
    print()  # blank line between users for readability