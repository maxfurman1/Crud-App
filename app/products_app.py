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

def show_products():
    print ("Showing a Product:")

def create_products():
    print ("Creating a Product:")

def update_products():
    print ("Updating a Product")

def destroy_products():
    print ("Destroying a Product")

while True:
    if chosen_operation == "List":
        print ("\n")
        list_products()
        print ("\n")
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print (row["id"], row["name"], row["aisle"], row["department"],row["price"])
            break
    elif chosen_operation == "Show":
        print ("\n")
        show_products()
        print ("\n")
        product_ids = []
        product_id = input ("Ok, please specify the product's indentifier: ")
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for product_id in reader:
                print (column["id"], column["name"], column["aisle"], column["department"],column["price"])
            break

    elif chosen_operation == "Create":
        print ("\n")
        create_products()
    elif chosen_operation == "Update":
        print ("\n")
        update_products()
    elif chosen_operation.title() == "Destroy":
        print ("\n")
        destroy_products()
    else:
        print ("\n")
        print ("ERROR. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

print ("\n")
#print (chosen_operation)

#csv_file_path = "/users/maxfurman/desktop/csv-mgmt/crud-app/data/products.csv"
