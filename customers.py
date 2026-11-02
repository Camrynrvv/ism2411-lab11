# Reflection Question 1:
# I would use .get() when a key might not exist because it allows the
# program to continue running and return a default value. I use bracket
# notation when I know the key should exist and I want Python to alert
# me with a KeyError if something is wrong.

# Reflection Question 2:
# This pattern is similar to creating a PivotTable or using SUMIF in Excel
# because it groups and totals values by category. Python is more useful
# for large datasets because the process can be automated and repeated
# easily on thousands of records.

# EXERCISE 1 - One customer

customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 2500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# EXERCISE 2 - Update and add

customer["phone"] = "813-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# EXERCISE 3 - Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email field does not exist")

# EXERCISE 4 - Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns keys.
for key in customer:
    print(key)

# EXERCISE 5 - Lookup table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate:.0%}")
print(f"Final Price: ${final_price:.2f}")

# EXERCISE 6 - List of dicts

customers = [
    {
        "name": "Alice Johnson",
        "tier": "platinum",
        "ytd_spend": 2500
    },
    {
        "name": "Bob Smith",
        "tier": "gold",
        "ytd_spend": 1500
    },
    {
        "name": "Carol Davis",
        "tier": "silver",
        "ytd_spend": 800
    }
]

for cust in customers:
    rate = tier_discounts.get(cust["tier"], 0)
    discount_amount = 300 * rate

    print(
        f"{cust['name']} | "
        f"Tier: {cust['tier']} | "
        f"Discount on $300 purchase: ${discount_amount:.2f}"
    )

# EXERCISE 7 - Nested catalog

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {details['stock']} left")

# EXERCISE 8 - Sales by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 250},
    {"region": "West", "amount": 100}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")