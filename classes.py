# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Dialing {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending '{message}' to {number} from {self.brand} {self.model}."

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"

# Subclass
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, refresh_rate):
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.refresh_rate = refresh_rate

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU at {self.refresh_rate}Hz."

    def __str__(self):
        return f"{super().__str__()} (Gaming Features: GPU: {self.gpu}, Refresh Rate: {self.refresh_rate}Hz)"

# Test the classes
phone = Smartphone("Apple", "iPhone 15", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1199, "Adreno 730", 144)

print(phone)
print(phone.make_call("123-456-7890"))
print(gaming_phone)
print(gaming_phone.play_game("PUBG"))
