# assignment1.py

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# Inheritance Example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game} 🎮")


# Testing
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "S24 Ultra", 256)
    phone1.info()
    phone1.call("+254797585552")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 8", 512, "Adreno GPU")
    gaming_phone.info()
    gaming_phone.play_game("Call of Duty Mobile")
