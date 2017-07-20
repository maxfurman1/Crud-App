import os
import csv

csv_file_path = "/users/maxfurman/desktop/csv-mgmt/crud-app/data/products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

other_file_path = "/users/maxfurman/desktop/csv-mgmt/crud-app/data/other-products.csv"
with open(other_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

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
    product_id = input("Please specify the product's ID:")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Here is your result:", product)
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
        #product_ids = []
        #product_id = ("Ok, please specify the product's indentifier: ")
        #chosen_product = input(product_id)
        #def lookup_product_by_id(product_id):
        #    matching_products = [product for product in products if product["id"] == product_id] #create a new variable, and in it, filter the list we have and store the results of the list comprehension.
            #we want any individual items in that list of items that match the following condition (i.e. product_id was input) if that given product_id is equal to some variable we specify
        #    return matching_products [0] # because the line above gives us a list and we want to return a single item. this limits the results to one product per product_id
        #    print (matching_products)
        #chosen_product = input(product_id)
    #    if chosen_product == products["id"]:
        #    product_ids.append(row)
        #    print (product_ids[0])
        #with open(csv_file_path, "r") as csv_file:
            #reader = csv.DictReader(csv_file)
            #if chosen_product == product["id"]:
            #    print (row["id"], row["name"], row["aisle"], row["department"],row["price"])
            #for chosen_product in reader:
                #print (row["id"], row["name"], row["aisle"], row["department"],row["price"])
            #break

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
