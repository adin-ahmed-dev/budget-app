class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]
        for item in self.ledger:
            desc = item["description"][:23]
            amount = item["amount"]
            lines.append(f"{desc:<23}{amount:>7.2f}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spent = []
    for category in categories:
        spent.append(sum(-i["amount"] for i in category.ledger if i["amount"] < 0))

    total = sum(spent)

    # Avoid division by zero when nothing has been spent yet
    if total == 0:
        percentage = [0] * len(categories)
    else:
        percentage = [int(s / total * 10) * 10 for s in spent]

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        row = f"{level:>3}|"
        for p in percentage:
            row += " o " if p >= level else "   "
        row += " "
        lines.append(row)

    lines.append("    " + "-" * (3 * len(categories) + 1))

    max_name_len = max(len(category.name) for category in categories)
    for i in range(max_name_len):
        row = "     "
        for category in categories:
            row += (category.name[i] if i < len(category.name) else " ") + "  "
        lines.append(row)

    return "\n".join(lines)


if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    food.transfer(50, clothing)
    auto.deposit(500, "initial deposit")
    auto.withdraw(150, "car repair")

    print(food)
    print()
    print(create_spend_chart([food, clothing, auto]))
