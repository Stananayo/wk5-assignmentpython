# Assignment 1: Design Your Own Class! 🏗️

## Table of Contents
- [Introduction](#introduction)
- [Class Definitions](#class-definitions)
  - [Smartphone Class](#smartphone-class)
  - [Tablet Class (Inheriting from Smartphone)](#tablet-class-inheriting-from-smartphone)
- [Usage Example](#usage-example)
- [Key Concepts](#key-concepts)
  - [Encapsulation](#encapsulation)
  - [Inheritance and Polymorphism](#inheritance-and-polymorphism)
- [Installation](#installation)
- [License](#license)

## Introduction
This project involves creating a class representing a concept or object of your choice using Python's object-oriented programming (OOP) principles. In this implementation, we represent a **Smartphone** and a **Tablet**, encapsulating properties and methods to demonstrate functionality and leveraging inheritance for code reuse.

## Class Definitions

### Smartphone Class
The `Smartphone` class includes the following attributes and methods:

#### Attributes:
- `brand`: The brand name of the smartphone (public attribute).
- `model`: The model of the smartphone (public attribute).
- `__storage`: The storage capacity of the smartphone in GB (private attribute).
- `__battery_capacity`: The battery capacity in mAh (private attribute).

#### Methods:
- `make_call(contact)`: Simulates making a call to a contact.
- `send_message(contact, message)`: Sends a message to a specified contact.
- `check_storage()`: Returns the available storage.
- `charge_battery()`: Simulates charging the smartphone.
- `get_battery_info()`: Returns the battery capacity.

### Tablet Class (Inheriting from Smartphone)
The `Tablet` class extends the functionality of the `Smartphone` class to demonstrate polymorphism.

#### Additional Attributes:
- `screen_size`: The size of the tablet's screen in inches (unique attribute).

#### Additional Methods:
- `browse_internet()`: Simulates browsing the internet on the tablet.
- `use_note_app()`: Simulates using a note-taking application.

## Usage Example
Below is an example of how to create instances of the `Smartphone` and `Tablet` classes:

```python
# Creating a Smartphone instance
my_phone = Smartphone("Apple", "iPhone 14", 128, 3279)
my_phone.make_call("Alice")
my_phone.send_message("Bob", "Hello!")
print(my_phone.check_storage())
print(my_phone.get_battery_info())
my_phone.charge_battery()

# Creating a Tablet instance
my_tablet = Tablet("Samsung", "Galaxy Tab S8", 256, 8000, 11)
my_tablet.make_call("Charlie")
my_tablet.browse_internet()
my_tablet.use_note_app()
print(my_tablet.check_storage())
print(my_tablet.get_battery_info())
my_tablet.charge_battery()

## Key Concepts
## Encapsulation
- Encapsulation is demonstrated by making certain attributes private (__storage and __battery_capacity). This protects the internal state of an object and controls access through public methods.
- Inheritance and Polymorphism
- The Tablet class inherits from the Smartphone class, allowing it to reuse the methods defined in the Smartphone class while also adding unique features. This shows polymorphism as the tablet can call methods from its parent
 ## Code sample
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

## Class Definition: Tablet (Inheriting from Smartphone)

Now let's create a Tablet class that inherits from the Smartphone class. It will have some similar properties and methods but also include some unique attributes and methods.

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


##class.rint(my_tablet.get_battery_info())
my_tablet.charge_battery()
