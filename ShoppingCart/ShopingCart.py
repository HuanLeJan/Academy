import time


class Products:
    shop_offer: list = []

    def __init__(self, prod_name: str, price: float, amount: int, tax: float):
        """
        Description :
        :param prod_name: Name of a product
        :param price: Price of a product
        :param amount: Amount of product in magazine
        :param tax: Tax % included in price
        """

        self.prod_name = prod_name
        self.price = price
        self.amount = amount
        self.tax = round(price * tax, 2)
        self.shop_offer.append(self)

    def __str__(self):
        return f'Product name: {self.prod_name}, price: {self.price} pln, amount: {self.amount}, tax: {self.tax} pln'


# products:
prod_01 = Products(prod_name='Pencil', price=4.99, amount=50, tax=0.23)
prod_02 = Products(prod_name='Pen', price=8.99, amount=45, tax=0.23)
prod_03 = Products(prod_name='Rubber', price=2.99, amount=70, tax=0.23)
prod_04 = Products(prod_name='Black Marker', price=9.99, amount=50, tax=0.23)
cart: list = []


def menu():
    """
    This function prints menu and wait
    """
    print('-' * 30)
    print('Welcome to our python shop menu !')
    option = input('Select: \n 0. Show available products \n 1. Add product to your cart \n 2. Delete product from '
                   'your cart\n 3. Change amount of products in \n 4. Show cart \n 5. Delete whole cart \n 6. End '
                   'shopping \n Press from 0 to 6 : ')
    print('-' * 30)
    return option


def show_list_of_prod():
    """
    This function prints list of product which is in offer
    """
    print('List of products :')
    for count, item in enumerate(Products.shop_offer):
        print(count, item)


def add_item(cart):
    """
    This function adds product to the cart
    """
    prod_index = int(input('Choose product to be added to cart, provide product index: '))
    prod_amount_add = int(input('How many products you want to add: '))
    if prod_index >= 0:
        try:
            cart.append([Products.shop_offer[prod_index].prod_name, prod_amount_add,
                         Products.shop_offer[prod_index].price * prod_amount_add,
                         Products.shop_offer[prod_index].tax * prod_amount_add])
        except:
            print('Wrong index, please try again')


def delete_item(cart):
    """
    This function delete product from cart
    """
    try:
        cart_item_id = int(input('Provide product id from cart, to be deleted :'))
        cart.pop(cart_item_id)
    except:
        print('Oops something went wrong, please try again !')


def change_cart(cart):
    """
    This function changes product quantity in the cart
    """
    cart_item_id = int(input('Provide product id from cart, to change its quantity :'))
    cart_item_quant = int(input('Provide new quantity of product:'))
    try:
        cart[cart_item_id][1] = cart_item_quant
    except:
        print('Oops something went wrong, please try again !')


def show_cart(cart):
    """
    This function show what products are inside the cart
    """
    print('----- Cart ------')
    if cart == []:
        print('Cart is empty')
    else:
        for index, item in enumerate(cart):
            print(f'id:{index}  Product: {item[0]}, quantity: {item[1]}')


def delete_cart(cart):
    """
    This function delete all products from the card
    """
    if cart == []:
        print('Cart is already empty')
    else:
        cart.clear()
        print('Cart has been deleted')


def end_shopping(cart):
    """
    This function ends shopping and shows amount off money that user has to pay
    """
    sum = 0
    taxes = 0
    if cart == []:
        print('Cart is empty\n See you soon !')
    else:
        for item in cart:
            sum += item[2]
            taxes += item[3]
        print('In total u have to pay: {0:.2f} pln, including {1:.2f} pln in taxes'.format(sum, taxes))


def main():
    while True:
        time.sleep(2.5)
        option = menu()
        if option == '0':
            show_list_of_prod()
            continue
        elif option == '1':
            add_item(cart)
            continue
        elif option == '2':
            delete_item(cart)
            continue
        elif option == '3':
            change_cart(cart)
            continue
        elif option == '4':
            show_cart(cart)
            continue
        elif option == '5':
            delete_cart(cart)
            continue
        elif option == '6':
            end_shopping(cart)
            break
        else:
            print('Incorrect value')
            continue


main()
