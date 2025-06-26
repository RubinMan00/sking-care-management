"""
Module for reading inventory data from files.
This module handles loading and displaying inventory information.
"""


def read_inventory(filename="inventory.txt"):
    """
    Read inventory data from a file and return as a list.

    Parameters:
        filename (str): Name of the inventory file to read.

    Returns:
        list: List of product information with index+1 representing product ID.

    Raises:
        FileNotFoundError: If inventory file doesn't exist and cannot be created.
    """
    try:
        # Open and read the file
        file = open(filename, "r")
        data = file.readlines()
        file.close()

        # Prepare inventory list
        inventory_list = []
        # Add empty first element to make indexing start from 1
        inventory_list.append(None)

        for line in data:
            line = line.replace("\n", "").split(",")  # Remove newline and split by comma
            # Clean up whitespace
            cleaned_line = []
            for item in line:
                if len(item) > 0 and item[0] == ' ':
                    item = item[1:]
                if len(item) > 0 and item[-1] == ' ':
                    item = item[:-1]
                cleaned_line.append(item)
            inventory_list.append(cleaned_line)

        return inventory_list

    except:
        print("Inventory file '" + filename + "' not found. Creating a new one with sample data.")
        create_inventory_file(filename)
        return read_inventory(filename)  # Try reading again after creating


def create_inventory_file(filename="inventory.txt"):
    """
    Create an inventory file with sample data.

    Parameters:
        filename (str): Name of the inventory file to create.

    Returns:
        None

    Raises:
        IOError: If file cannot be created or written to.
    """
    products = [
        "Vitamin C Serum, Garnier, 200, 1000, France",
        "Skin Cleanser, Cetaphil, 100, 280, Switzerland",
        "Sunscreen, Aqualogica, 200, 700, India",
    ]

    try:
        file = open(filename, "w")
        for product in products:
            file.write(product + "\n")
        file.close()

        print("Inventory file created successfully!")
    except:
        print("Error creating inventory file")


def display_inventory(inventory_list):
    """
    Display the inventory in a formatted table.

    Parameters:
        inventory_list (list): List containing product information.

    Returns:
        None
    """
    # Print header
    print("*" * 80)
    print("ID\t\tName\t\t\tBrand\t\tQty\tCost Price\tSelling Price\tOrigin")
    print("*" * 80)

    # Print values (skip index 0 as it's None)
    for i in range(1, len(inventory_list)):
        try:
            value = inventory_list[i]
            selling_price = float(value[3]) * 3  # 200% markup
            print(str(i) + "\t" + value[0] + "\t\t" + value[1] + "\t\t" + value[2] + "\t" + value[3] + "\t\t" + str(
                round(selling_price, 2)) + "\t\t" + value[4])
        except:
            print("Error displaying product " + str(i))