"""
Module for file writing operations in WeCare Beauty Products system.
This module handles invoice generation and inventory updates.
"""

import datetime
import random


def update_inventory(inventory_list, filename="inventory.txt"):
    """
    Save updated inventory back to file.

    Parameters:
        inventory_list (list): List containing product information.
        filename (str): File to save the inventory to.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        IOError: If error writing to file.
    """
    try:
        file = open(filename, "w")
        # Skip index 0 as it's None
        for pid in range(1, len(inventory_list)):
            product = inventory_list[pid]
            line = ""
            for i, item in enumerate(product):
                line += item
                if i < len(product) - 1:
                    line += ", "
            file.write(line + "\n")
        file.close()
        print("Inventory updated successfully!")
        return True
    except:
        print("Error updating inventory")
        return False


def generate_sale_invoice(customer_name, phone_number, items_purchased, inventory_list):
    """
    Generate an invoice for a sale and update inventory.

    Parameters:
        customer_name (str): Customer name.
        phone_number (str): Customer phone number.
        items_purchased (list): List of dictionaries with 'id' and 'quantity'.
        inventory_list (list): List of product information.

    Returns:
        str: Filename of the generated invoice.
    """
    # Generate a unique filename using current date and time
    now = datetime.datetime.now()
    today = "%s-%s-%s" % (now.year, now.month, now.day)
    time_stamp = "%s%s%s" % (now.hour, now.minute, now.second)
    invoice_number = "SALE-" + str(random.randint(1000, 9999))

    # Create filename without using replace()
    clean_name = ""
    for char in customer_name:
        if char == ' ':
            clean_name += '_'
        else:
            clean_name += char
    filename = invoice_number + "_" + clean_name + "_" + today + "_" + time_stamp + ".txt"

    total_amount = 0
    shipping_cost = 0

    try:
        file = open(filename, "w")
        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
        file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255\n")
        file.write("=" * 80 + "\n\n")
        file.write("Invoice Number: " + invoice_number + "\n")
        file.write("Date: " + today + "\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Phone Number: " + phone_number + "\n\n")
        file.write("-" * 80 + "\n")
        file.write("%-15s %-15s %-5s %-5s %-10s %-10s\n" % ("Product", "Brand", "Qty", "Free", "Price", "Amount"))
        file.write("-" * 80 + "\n")

        # Also print to screen
        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255")
        print("=" * 80 + "\n")
        print("Invoice Number: " + invoice_number)
        print("Date: " + today)
        print("Customer Name: " + customer_name)
        print("Phone Number: " + phone_number + "\n")
        print("-" * 80)
        print("%-15s %-15s %-5s %-5s %-10s %-10s" % ("Product", "Brand", "Qty", "Free", "Price", "Amount"))
        print("-" * 80)

        for item in items_purchased:
            pid = item["id"]
            qty_purchased = item["quantity"]

            product = inventory_list[pid]
            product_name = product[0]
            brand = product[1]
            current_qty = int(product[2])
            cost_price = float(product[3])

            # Calculate free items
            free_items = qty_purchased // 3

            # Calculate selling price (200% markup)
            selling_price = cost_price * 3

            # Calculate amount
            amount = selling_price * qty_purchased
            total_amount += amount

            # Write to file
            file.write("%-15s %-15s %-5s %-5s %-10s %-10s\n" %
                       (product_name, brand, qty_purchased, free_items, str(round(selling_price, 2)), str(round(amount, 2))))

            # Also print to screen
            print("%-15s %-15s %-5s %-5s %-10s %-10s" %
                  (product_name, brand, qty_purchased, free_items, str(round(selling_price, 2)), str(round(amount, 2))))

            # Update inventory
            inventory_list[pid][2] = str(current_qty - (qty_purchased + free_items))

        # Ask about shipping
        shipping_input = input("\nDo you want your products to be shipped? (Y/N): ")
        if shipping_input.upper() == "Y":
            shipping_cost = 500
            file.write("%-45s %s\n" % ("Shipping Cost:", str(round(shipping_cost, 2))))
            print("%-45s %s" % ("Shipping Cost:", str(round(shipping_cost, 2))))

        # Write total
        grand_total = total_amount + shipping_cost
        file.write("-" * 80 + "\n")
        file.write("%-45s %s\n" % ("Total Amount:", str(round(grand_total, 2))))
        file.write("=" * 80 + "\n")
        file.write("\nThank you for shopping with us!\n")
        file.write("Buy 3 Get 1 Free on all products!\n")
        file.close()

        # Also print to screen
        print("-" * 80)
        print("%-45s %s" % ("Total Amount:", str(round(grand_total, 2))))
        print("=" * 80)
        print("\nThank you for shopping with us!")
        print("Buy 3 Get 1 Free on all products!")

        print("\nInvoice generated: " + filename)
        update_inventory(inventory_list)
        return filename

    except:
        print("Error generating sale invoice")
        return None


def generate_restock_invoice(supplier_name, items_restocked, inventory_list):
    """
    Generate an invoice for restocking products and update inventory.

    Parameters:
        supplier_name (str): Supplier name.
        items_restocked (list): List of dictionaries with 'id', 'quantity', and optional 'new_cost'.
        inventory_list (list): List of product information.

    Returns:
        str: Filename of the generated invoice.
    """
    # Generate a unique filename using current date and time
    now = datetime.datetime.now()
    today = "%s-%s-%s" % (now.year, now.month, now.day)
    time_stamp = "%s%s%s" % (now.hour, now.minute, now.second)
    invoice_number = "RESTOCK-" + str(random.randint(1000, 9999))

    # Create filename without using replace()
    clean_name = ""
    for char in supplier_name:
        if char == ' ':
            clean_name += '_'
        else:
            clean_name += char
    filename = invoice_number + "_" + clean_name + "_" + today + "_" + time_stamp + ".txt"

    total_amount = 0

    try:
        file = open(filename, "w")
        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
        file.write("\t \t \t \t RESTOCK INVOICE\n")
        file.write("=" * 80 + "\n\n")
        file.write("Invoice Number: " + invoice_number + "\n")
        file.write("Date: " + today + "\n")
        file.write("Supplier: " + supplier_name + "\n\n")
        file.write("-" * 80 + "\n")
        file.write("%-15s %-15s %-5s %-10s %-10s\n" % ("Product", "Brand", "Qty", "Cost Price", "Amount"))
        file.write("-" * 80 + "\n")

        # Also print to screen
        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
        print("\t \t \t \t RESTOCK INVOICE")
        print("=" * 80 + "\n")
        print("Invoice Number: " + invoice_number)
        print("Date: " + today)
        print("Supplier: " + supplier_name + "\n")
        print("-" * 80)
        print("%-15s %-15s %-5s %-10s %-10s" % ("Product", "Brand", "Qty", "Cost Price", "Amount"))
        print("-" * 80)

        for item in items_restocked:
            pid = item["id"]
            qty_restocked = item["quantity"]
            new_cost = item.get("new_cost", None)

            product = inventory_list[pid]
            product_name = product[0]
            brand = product[1]
            current_qty = int(product[2])

            # Update cost price if provided
            if new_cost:
                product[3] = str(new_cost)

            cost_price = float(product[3])
            amount = cost_price * qty_restocked
            total_amount += amount

            # Write to file
            file.write("%-15s %-15s %-5s %-10s %-10s\n" %
                       (product_name, brand, qty_restocked, str(round(cost_price, 2)), str(round(amount, 2))))

            # Also print to screen
            print("%-15s %-15s %-5s %-10s %-10s" %
                  (product_name, brand, qty_restocked, str(round(cost_price, 2)), str(round(amount, 2))))

            # Update inventory
            inventory_list[pid][2] = str(current_qty + qty_restocked)

        # Write total
        file.write("-" * 80 + "\n")
        file.write("%-45s %s\n" % ("Total Amount:", str(round(total_amount, 2))))
        file.write("=" * 80 + "\n")
        file.close()

        # Also print to screen
        print("-" * 80)
        print("%-45s %s" % ("Total Amount:", str(round(total_amount, 2))))
        print("=" * 80)

        print("\nRestock invoice generated: " + filename)
        update_inventory(inventory_list)
        return filename

    except:
        print("Error generating restock invoice")
        return None