import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartmarkets.settings')
django.setup()

from modernmarket.models import User, Product, Store

def goods():
    Product.objects.create(Product_name="Python Dictionary", price=2.40)
    Product.objects.create(Product_name="How To Succeed in Life", price=2.99)
    Product.objects.create(Product_name="How To Survive in UNIUYO", price=20.99)
    Product.objects.create(Product_name="How To Repair a Torch", price=4.60)
    Product.objects.create(Product_name="About Diminished Chords", price=2.90)
    Product.objects.create(Product_name="About Py50", price=8.70)
    Product.objects.create(Product_name="About Covenant Monday", price=2.50)
    Product.objects.create(Product_name="Ben Carson", price=7.99)
    Product.objects.create(Product_name="A Twist Of Fate", price=2.99)
    Product.objects.create(Product_name="How To Code", price=1.99)
    

    

def signin():
    """Signup Function"""
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    if '.com' not in email:
        print("Invalid Email!")
        return
    
    signup = User.objects.create(name=name, email=email, password=password)
    signup.save()
    print("Account Created Successfully!")
    


def login():
    """Function for login and user authentication"""
    login_choice = input("Account Created Already? y/n \n>> ")
    
    if login_choice == 'n':
        signin()
    else:
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        
        #filter based on email
        confirm = User.objects.filter()
        
        for user in confirm:
            if email == user.email and password == user.password:
                print("Access Granted")
                print(f"Welcome {user.name}")
                return True
        else:
            print("Access Denied! Invalid Email or Password")
            return False



def list_products():
    """This function lists all the product in a particular Store"""
    global product
    product = Product.objects.all()
    
    print('Available_product             Price($)')
    
    for index, each_product in enumerate(product):
        new_index = index + 1
        print(f"{new_index}. {each_product.Product_name}  ----   {each_product.price}")
        
def create_store():
    """Fubction for creating Store"""
    name = input("Enter a name for your store: ")
    description = input("Add a description to your store: ")
    owner = input("Enter Name of Owner: ")
    password = input("Enter Password: ")
    store = Store.objects.create(store_name=name, description=description, owner_name=owner, password=password)
    store.save()
    print("Store Created Successfully!!")

def product_details(stores):
    product_name = input("Enter Product Name \n>> ")
    price = float(input("Enter Selling Price \n>> $"))
    new_product = Product.objects.create(Product_name=product_name, price=price, product_key=stores)
    new_product.save()
    print(f"New Product '{new_product}' Added Successfully to Store: {stores.store_name}")
    
def product_to_delete(store):
    product_no = int(input("Enter Product No \n>> "))
    

def add_product():
    """Function To add products to a particular store"""
    store_items = Store.objects.all()
    for index, stores in enumerate(store_items):
        new_index = index + 1
        print(f"{new_index}. {stores.store_name}")
    authenticate = int(input("Enter store Id no: "))
    password = input("Enter Store Password: ")
    try:
        stores = Store.objects.get(id=authenticate)
    except Store.DoesNotExist:
        print("Invalid Store Number!")
        return
    
    # Condiyions for gaining access to store
    if password != stores.password:
        print("Access Denied. Invalid Password!")
        return
    else:
        no_product = int(input("How many products do you want to add? \n>> "))
        while no_product != 0:
            product_details(stores)
            no_product -= 1
        print("Product Added Successfully")
        

        
def store_properties():
    """Function to list the available products in a store"""
    global store
    global products
    store = Store.objects.filter()
    
    for index, products in enumerate(store):
        new_index = index + 1
        print(f"{new_index}. {products}")
        
def update_product():
    """To update the product name or price"""
    store_items = Store.objects.all()
    for index, stores in enumerate(store_items):
        new_index = index + 1
        print(f"{new_index}. {stores}")
    authenticate = int(input("Enter store Id no: "))
    password = input("Enter Store Password: ")
    # trial and except to check if user entered an invalid store number
    try:
        stores = Store.objects.get(id=authenticate)
    except Store.DoesNotExist:
        print("Invalid Store Number!")
        return
    
    # Conditions for gaining access to store
    if password != stores.password:
        print("Access Denied. Invalid Password!")
        return
    else:
        store_products = Product.objects.filter(product_key=stores)
        
        for no, items in enumerate(store_products):
            new_no = no + 1
            print(f"{new_no}. {items}")
        choice = int(input("Which Product Do you Wanna Update? \n>> ")) - 1
        if choice < 0 or choice > len(store_products):
            print("Invalid Product Number")
            return
        else:
            updated_product = store_products[choice]
            update_choice = input("Do you want to update the name or the price or both? \nEnter 'n' for Name, 'p' for price, 'b' for both \n>> ").lower()
            if update_choice == 'n':
                try:
                    new_name = input("Enter new name for the product. \n>> ")
                except ValueError:
                    print("Name error!")
                    return
                confirm_newname = input(f"You want to replace '{updated_product.Product_name}' with '{new_name}'. Kindly Enter 'y' to continue \n>> ").lower()
                if confirm_newname == 'y':
                    updated_product.Product_name = new_name
                    updated_product.save()
                    print("Product Updated Successfully!")
                else:
                    return
            elif update_choice == 'p':
                try:
                    new_price = float(input("Enter a new price for the product \n>> "))
                except ValueError:
                    print("Price cant be a combination of letters and numbers")
                    return
                confirm_newprice = input(f"You want to replace '{updated_product.price}' with '{new_price}'. Kindly Enter 'y' to continue \n>> ").lower()
                if confirm_newprice == 'y':
                    updated_product.price = new_price
                    updated_product.save()
                    print("Product Updated Successfully!")
                else:
                    return
            elif update_choice == 'b':
                try:
                    anew_name = input("Enter new name for the product. \n>> ")
                    anew_price = float(input("Enter a new price for the product \n>> "))
                except ValueError:
                    print("Name Or Price Error")
                    return
                confirm_all = input(f"You want to replace '{updated_product.Product_name}' with '{anew_name}'. \nYou want to replace '{updated_product.price}' with '{anew_price}'. \nKindly Enter 'y' to continue \n>> ").lower()
                if confirm_all == 'y':
                    updated_product.Product_name == anew_name and updated_product.price == anew_price
                    updated_product.save()
                    print("Product Updated Successfully!")
                else:
                    return
                
            
def del_products():
    """This function is meant to delete a product from a particular store"""
    store_items = Store.objects.all()
    for index, stores in enumerate(store_items):
        new_index = index + 1
        print(f"{new_index}. {stores}")
    authenticate = int(input("Enter store Id no: "))
    password = input("Enter Store Password: ")
    
    #using trial and except to check for invalid store number
    try:
        stores = Store.objects.get(id=authenticate) 
    except Store.DoesNotExist:
        print("Invalid Store Number! ")
        return
    
    # Condiyions for gaining access to store
    if password != stores.password:
        print("Access Denied. Invalid Password!")
        return
    else:
        store_products = Product.objects.filter(product_key=stores)
        
        for no, items in enumerate(store_products):
            new_no = no + 1
            print(f"{new_no}. {items}")
            
        del_choice = int(input("Enter Product No of the product you want to delete \n>> ")) - 1
        
        if del_choice < 0 or del_choice > len(store_products):
            print("Invalid Product Number")
            return
        else:
            deleted_product = store_products[del_choice]
            last_chance = input("Are you sure you want to delete this product?  y/n \n>> ")
            if last_chance == "y":
                deleted_product.delete()
                print(f"Product: '{deleted_product}' Deleted Successfully!!")
                return
            elif last_chance == "n":
                print("Operation Cancelled!")
                return
            else:
                print("Invalid Choice!")
                return
        
def stores():
    print("WELCOME TO THE LOGICAL MARKET")
    print("Please Login to continue: ")
    
    # check for successful login
    login_successful = False
    while not login_successful: 
        login_successful = login()
        
    market_on = True
    

    while market_on:
        print('\n' * 2)
        # print('\n' * 3)
        print("1. Create a New Store")
        print("2. Add Products")
        print("3. Delete a Product")
        print("4. Update a Product")
    
    
        print("To close, Enter 'close'. ")
        choice = input("What would you like to do: ")
        
        if choice == "1":
            create_store()
        elif choice == "2":
            add_product()
        elif choice == "3":
            del_products()
        elif choice == "close":
            market_on = False
        elif choice == "4":
            update_product()
            
stores()