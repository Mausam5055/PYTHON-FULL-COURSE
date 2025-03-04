# Creating inventory dictionary
inventory = {
    101: {"name": "Laptop", "price": 800, "stock": 10},
    102: {"name": "Mouse", "price": 25, "stock": 50},
    103: {"name": "Keyboard", "price": 40, "stock": 30}
}

# 1. Add a New Product
inventory[104] = {"name": "Monitor", "price": 150, "stock": 20}
print(f"Product Monitor added with ID 104.")

# 2. Add the product with setdefault
inventory.setdefault(105, {"name": "Headset", "price": 50, "stock": 15})
print(f"Product Headset added or ensured with defaults using ID 105.")

# 3. Check Product Availability
product_id = 101
if product_id in inventory:
    print(f"Product ID {product_id} is available: {inventory[product_id]}")
else:
    print(f"Product ID {product_id} is not available.")

# 4. List All Products
print("Listing all products in inventory:")
for product_id, details in inventory.items():
    print(f"ID: {product_id}, Details: {details}")

# 5. Retrieve a Product's Price
product_id = 102
if product_id in inventory:
    print(f"Price of Product ID {product_id}: {inventory[product_id]['price']}")
else:
    print(f"Product ID {product_id} not found.")

# 6. Update the Stock
product_id = 103
if product_id in inventory:
    inventory[product_id]["stock"] += 10  # Increase stock by 10
    print(f"Updated stock for Product ID {product_id}: {inventory[product_id]['stock']}")
    inventory[product_id]["stock"] -= 5   # Decrease stock by 5
    print(f"Updated stock for Product ID {product_id} after decrease: {inventory[product_id]['stock']}")
else:
    print(f"Product ID {product_id} not found.")

# 7. Remove a Product
product_id = 104
if product_id in inventory:
    removed_product = inventory.pop(product_id)
    print(f"Product ID {product_id} removed: {removed_product}")
else:
    print(f"Product ID {product_id} not found.")

# 8. Clear Inventory
inventory.clear()
print("Inventory cleared. No products remain.")

# # Listing all products after clearing inventory
# print("Listing all products after clearing inventory:")
# for product_id, details in inventory.items():
#     print(f"ID: {product_id}, Details: {details}")
