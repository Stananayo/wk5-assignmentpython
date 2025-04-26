class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand                   # Public attribute
        self.model = model                   # Public attribute
        self.__storage = storage             # Private attribute
        self.__battery_capacity = battery_capacity  # Private attribute

    def make_call(self, contact):
        print(f"Calling {contact} using {self.brand} {self.model}.")

    def send_message(self, contact, message):
        print(f"Sending message to {contact}: {message}")

    def check_storage(self):
        return f"Available storage: {self.__storage}GB"

    def charge_battery(self):
        print(f"Charging {self.brand} {self.model}'s battery...")

    def get_battery_info(self):
        return f"Battery capacity: {self.__battery_capacity}mAh"

# Example usage:
my_phone = Smartphone("Apple", "iPhone 14", 128, 3279)
my_phone.make_call("Alice")
my_phone.send_message("Bob", "Hello!")
print(my_phone.check_storage())
print(my_phone.get_battery_info())
my_phone.charge_battery()


class Tablet(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, screen_size):
        super().__init__(brand, model, storage, battery_capacity)
        self.screen_size = screen_size  # Unique attribute for Tablet

    def browse_internet(self):
        print(f"Browsing the internet on the {self.brand} {self.model} with a {self.screen_size}-inch screen.")

    def use_note_app(self):
        print(f"Using the note-taking app on {self.brand} {self.model}.")

# Example usage:
my_tablet = Tablet("Samsung", "Galaxy Tab S8", 256, 8000, 11)
my_tablet.make_call("Charlie")  # Inherited method
my_tablet.browse_internet()      # Tablet-specific method
my_tablet.use_note_app()         # Tablet-specific method
print(my_tablet.check_storage())  # Inherited method
print(my_tablet.get_battery_info())  # Inherited method
my_tablet.charge_battery()        # Inherited method