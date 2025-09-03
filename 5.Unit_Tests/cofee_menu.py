class CoffeeMenu:
    def __init__(self):
        self.menu = {
        'espresso': 2.50,
        'latte': 2.75,
        'cappuccino': 3.20,
        'americano': 2.70
        }
    def get_price(self, item_name):
        return self.menu.get(item_name, None)

    def add_item(self, item_name, price):
        if item_name in self.menu:
            raise ValueError(f"{item_name} already exists in the menu.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        self.menu[item_name] = price