# Budget App

A simple Python budget app. You create spending categories (Food, Clothing, Auto, etc.), record deposits and withdrawals, move money between categories, and print a text chart of how your spending is split.

> This project was built while following freeCodeCamp's Python lab: [Build a Budget App](https://www.freecodecamp.org/learn/python-v9/lab-budget-app/build-a-budget-app).

## Features

- Deposit money into a category with an optional description
- Withdraw money (only if the category has enough funds)
- Transfer money from one category to another
- Check the balance of any category
- Print a category as a formatted ledger
- Generate a bar chart showing the percentage spent per category

## Requirements

- Python 3.8 or newer
- No external libraries

## How to run

```bash
git clone https://github.com/adin-ahmed-dev/budget-app.git
cd budget-app
python budget.py
```

## Usage

```python
from budget import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.transfer(50, clothing)

print(food.get_balance())      # 939.85
print(food.check_funds(2000))  # False
print(food)
print(create_spend_chart([food, clothing]))
```

### Methods of `Category`

| Method | What it does |
|---|---|
| `deposit(amount, description="")` | Adds money to the ledger |
| `withdraw(amount, description="")` | Removes money if funds are enough, returns `True` or `False` |
| `transfer(amount, category)` | Moves money to another category, returns `True` or `False` |
| `get_balance()` | Returns the current balance |
| `check_funds(amount)` | Returns `True` if the amount is within the balance |

## Example output

Running `python budget.py` prints a ledger and a spending chart:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|       o  
 50|       o  
 40|       o  
 30| o     o  
 20| o     o  
 10| o     o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

Each ledger line shows the first 23 characters of the description and the amount with two decimals. Percentages in the chart are rounded down to the nearest 10.

## Project structure

```
budget-app/
├── budget.py    # Category class and create_spend_chart function
└── README.md
```

## What I practiced

- Object-oriented programming with classes and methods
- Working with lists of dictionaries
- String formatting with f-strings (alignment, padding, decimals)
- Building text-based charts with loops
- Handling edge cases like insufficient funds and zero spending

## Credits

Based on the [freeCodeCamp](https://www.freecodecamp.org/learn/python-v9/) Python curriculum.

Part of my learning journey: [My freeCodeCamp Profile](https://www.freecodecamp.org/adin-ahmed)
