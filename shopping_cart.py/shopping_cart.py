class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Create initial products
product1 = Product("Laptop", 999.99, 5)
product2 = Product("Headphones", 199.99, 10)
product3 = Product("Mouse", 49.99, 15)
product4 = Product("Keyboard", 89.99, 8)
product5 = Product("Monitor", 249.99, 6)

# Store them in a list
inventory = [product1, product2, product3, product4, product5]
class Store:
    def __init__(self, products):
        self.products = products

    def display_inventory(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"{product.name} - ${product.price:.2f} ({product.stock} in stock)")

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.stock -= quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Sorry, only {product.stock} of {product.name} left in stock.")

    def remove_product(self, product, quantity):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items[product]
                del self.items[product]
                print(f"Removed all {product.name} from cart.")
            else:
                self.items[product] -= quantity
                product.stock += quantity
                print(f"Removed {quantity} x {product.name} from cart.")
        else:
            print(f"{product.name} is not in your cart.")

    def view_cart(self):
        print("\nYour Cart:")
        if not self.items:
            print("Cart is empty.")
        for product, quantity in self.items.items():
            print(f"{product.name} x{quantity} - ${product.price * quantity:.2f}")

    def get_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def checkout(self):
        total = self.get_total()
        print(f"\nCheckout complete. Total: ${total:.2f}")
        self.items.clear()
def main():
    store = Store(inventory)
    cart = ShoppingCart()

    while True:
        print("\nOptions: view, add, remove, cart, checkout, quit")
        choice = input("What would you like to do? ").lower()

        if choice == "view":
            store.display_inventory()

        elif choice == "add":
            name = input("Enter product name to add: ")
            product = store.find_product(name)
            if product:
                try:
                    qty = int(input("Enter quantity: "))
                    cart.add_product(product, qty)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Product not found.")

        elif choice == "remove":
            name = input("Enter product name to remove: ")
            product = store.find_product(name)
            if product:
                try:
                    qty = int(input("Enter quantity to remove: "))
                    cart.remove_product(product, qty)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Product not found.")

        elif choice == "cart":
            cart.view_cart()
            print(f"Total: ${cart.get_total():.2f}")

        elif choice == "checkout":
            cart.checkout()

        elif choice == "quit":
            print("Thanks for shopping!")
            break

        else:
            print("Invalid option. Try again.")

