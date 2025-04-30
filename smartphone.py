# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_percentage, storage):
        self.brand = brand  # The brand of the smartphone (e.g., Apple, Samsung)
        self.model = model  # The model of the smartphone (e.g., iPhone 13)
        self.battery_percentage = battery_percentage  # Battery level from 0 to 100
        self.storage = storage  # Storage in GB (e.g., 128GB)

    # Method to simulate a phone call
    def call(self, phone_number):
        if self.battery_percentage > 0:
            print(f"Calling {phone_number}...")
            self.battery_percentage -= 2  # Battery drains by 2% on call
            print(f"Battery now at {self.battery_percentage}%")
        else:
            print("Battery is dead. Please charge your phone.")

    # Method to browse the internet
    def browse(self, website):
        if self.battery_percentage > 0:
            print(f"Browsing {website}...")
            self.battery_percentage -= 5  # Battery drains by 5% while browsing
            print(f"Battery now at {self.battery_percentage}%")
        else:
            print("Battery is dead. Please charge your phone.")

    # Method to charge the phone
    def charge(self):
        print("Charging the phone...")
        self.battery_percentage = 100  # Fully charge the battery
        print("Battery is now fully charged!")

    # Method to show the smartphone details
    def show_details(self):
        print(f"Smartphone Details:\nBrand: {self.brand}\nModel: {self.model}\nBattery: {self.battery_percentage}%\nStorage: {self.storage}GB")


# Subclass representing a Smartphone with Camera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, storage, camera_megapixels):
        super().__init__(brand, model, battery_percentage, storage)  # Inherit attributes from Smartphone
        self.camera_megapixels = camera_megapixels  # Camera quality in megapixels

    # Method to simulate taking a picture
    def take_picture(self):
        if self.battery_percentage > 0:
            print(f"Taking a picture with {self.camera_megapixels} MP camera...")
            self.battery_percentage -= 3  # Camera usage drains 3% battery
            print(f"Battery now at {self.battery_percentage}%")
        else:
            print("Battery is dead. Please charge your phone.")

    # Override the show_details method to include camera information
    def show_details(self):
        super().show_details()  # Call the base class method to display basic info
        print(f"Camera: {self.camera_megapixels} MP")


# Creating an instance of Smartphone
iphone = Smartphone("Apple", "iPhone 13", 80, 128)
iphone.show_details()
iphone.call("123-456-7890")
iphone.browse("www.example.com")
iphone.charge()

# Creating an instance of SmartphoneWithCamera
galaxy = SmartphoneWithCamera("Samsung", "Galaxy S21", 50, 256, 108)
galaxy.show_details()
galaxy.take_picture()
galaxy.browse("www.youtube.com")
