import os
import csv

csv_file_path = "/users/maxfurman/desktop/csv-mgmt/crud-app/data/products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print ("-------------------------")
print ("PRODUCTS APPLICATION")
print ("-------------------------")
print ("Welcome " + os.getlogin() + "!")
print ("\n")

menu = "There are " + str(len(products)) + " products in the database. Please select an operation:"

print ("     operation    |    description")
print ("     ---------    |    -----------")
print ("     'List'       |    Display a list of product indentifiers.")
print ("     'Show'       |    Show information about a product.")
print ("     'Create'     |    Add a new product.")
print ("     'Update'     |    Edit an existing product.")
print ("     'Destroy'    |    Delete an existing product.")
print ("\n")

chosen_operation = input(menu).title()

def list_products():
    print ("Listing Products:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print (row["id"], row["name"], row["aisle"], row["department"],row["price"])
            print ("Good-bye!")

def show_products():
    print ("Showing a Product:")
    product_id = input("Please specify the product's ID:")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Here is your result:", product,)
        print ("Good-bye!")
    else:
        print("No product found", product)

def create_products():
    print ("Creating a Product:")
    product_name = input ("Please input the new product's name:")
    product_aisle = input ("Please input the new product's aisle:")
    product_department = input ("Please input the new product's department:")
    product_price = input ("Please input the new product's price:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle":  product_aisle,
        "department": product_department,
        "price": product_price
        }
    print ("New product is ", new_product)
    products.append(new_product)
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)
        print ("\n")
        print ("New product added. Good-bye!")

def update_products():
    print ("Updating a Product")
    updated_product_id = input ("Please input the ID of the product you'd like to update:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        if updated_product_id == row["id"]:
            return updated_product_id
            updated_product_name = input ("Please change name from " , + products["name"], + " to:")
            updated_product_aisle = input ("Please change aisle from " , + products["aisle"], + " to:")
            updated_product_department = input ("Please change department from " , + products["department"], + " to:")
            updated_product_price = input ("Please change name price " , + products["price"], + " to:")
            replaced_product = {
                "id": updated_product_id,
                "name": updated_product_name,
                "aisle":  updated_product_aisle,
                "department": updated_product_department,
                "price": updated_product_price
                }
            print ("Updated product is ", replaced_product)
        else:
            print ("Unrecognized ID. Please try again.")

def destroy_products():
    print ("Destroying a Product")

while True:
    if chosen_operation == "List":
        print ("\n")
        list_products()
        break

    elif chosen_operation == "Show":
        print ("\n")
        show_products()
        break

    elif chosen_operation == "Create":
        print ("\n")
        create_products()
        break

    elif chosen_operation == "Update":
        print ("\n")
        update_products()
        break

    elif chosen_operation.title() == "Destroy":
        print ("\n")
        destroy_products()
        break

    else:
        print ("\n")
        print ("ERROR. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
        break

print ("\n")
