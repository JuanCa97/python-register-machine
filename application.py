#! / usr / bin / python
# -*- coding: utf-8 -*-
"""Register Machine"""
import os
import sys
ARTICLIS = {}
DICTIONARI_QUANTITY = {}
def insert_product():
    """function that checks the items entering and validates"""
    limpiar()
    while True:
        option = raw_input("You want to enter a product? y/n: ")
        if option.isalpha() == True:
            if option.lower() == "y":
                while True:
                    limpiar()
                    product = raw_input("Insert a product: ")
                    product = product.lower()
                    if product.isalpha():
                        break
                    else:
                        print"unrecognized data numeric"
                while True:
                    try:
                        price = float(raw_input("Insert the price of the product: "))
                        ARTICLIS[product] = price
                        break
                    except ValueError:
                        print"unrecognized data"
            elif option.lower() == "n":
                break
        else:
            print "unrecognized data"
    for key in ARTICLIS:
        print key, ":", "%.2f\t" %float(ARTICLIS[key])
    raw_input("press enter to continue")
    limpiar()
    menu()
def sell_articles():
    """function that checks items that are stored"""
    articlis2 = []
    if ARTICLIS != {}:
        product = "Key"
        for key in ARTICLIS:
            print key, ":", ARTICLIS[key]
        while  True:
            product = raw_input("products that want to take? ")
            product = product.lower()
            if product == product in ARTICLIS:
                articlis2.append(product)
                print "you choose %s"%(product)
                print "Shopping: " + str(articlis2)
            elif product == "gold" or product == "silver":
                articlis2.append(product)
                print "Shopping: " + str(articlis2)
            elif product != articlis2[0:] and product != "done":
                print "we dont have this product"
            elif product == "Done" or product == "DONE" or product == "done":
                limpiar()
                total_price = 0.00
                for i in ARTICLIS:
                    cot = float(ARTICLIS[i]) * float(articlis2.count(i))
                    unit = articlis2.count(i)
                    if unit > 0:
                        print "Price of your " +str(unit) +" "+ i +"(s) is: $.""%.2f" %float(cot) + "\n"
                        total_price += cot
                print ("Sub Total: $. %.2f\t") % total_price
                if "gold" in articlis2:
                    gold(total_price)
                elif "silver" in articlis2:
                    silver(total_price)
                elif ("gold" in articlis2) and ("silver" in articlis2):
                    gold(total_price)
                elif "gold" != articlis2 and "silver" != articlis2:
                    any1(total_price)
    else:
        print "No existing products"
        raw_input("press enter to continue")
        limpiar()
        menu()
def gold(total_price):
    """invoice with 5%  discount"""
    print "Gold Card"
    print "The client has a 5%  discount"
    iva = total_price * 0.12
    discount = (total_price * 0.05)
    alltotal = total_price + iva - discount
    print "_____________________________________________________________"
    j = True
    while j == True:
        client_name = str(raw_input("Client name:  "))
        if client_name.isalpha() == True:
            raw_input("NIT: ")
            totaiv = total_price + iva
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") %total_price
            print ("iva is:- - - - - - - - - - - - - - - -  %.2f\t") %iva
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") %totaiv
            print ("your discount with the card is:- - - -  %.2f\t") %discount
            print "_____________________________________________________________"
            print ("Total with card discount:- - - - - - -  %.2f\t") %alltotal
            print "_____________________________________________________________"
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()
def silver(total_price):
    """invoice with 2%  discount"""
    print "Silver Card"
    print "The client has a 2%  discount"
    iva = total_price * 0.12
    discount = (total_price * 0.02)
    alltotal = total_price + iva - discount
    print "_____________________________________________________________"
    j = True
    while j == True:
        client_name = raw_input("Client name:  ")
        if client_name.isalpha() == True:
            raw_input("NIT: ")
            totaiv = total_price + iva
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") %total_price
            print ("iva is:- - - - - - - - - - - - - - - -  %.2f\t") %iva
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") %totaiv
            print ("your discount with the card is:- - - -  %.2f\t") %discount
            print "_____________________________________________________________"
            print ("Total with card discount:- - - - - - -  %.2f\t") %alltotal
            print "_____________________________________________________________"
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()
def any1(total_price):
    """invoice with 0%  discount"""
    print "The client has a 0%  discount"
    iva = (total_price * 0.12)
    #alltotal = total_price + iva
    print "_____________________________________________________________"
    j = True
    while j == True:
        client_name = raw_input("Client name:  ")
        if client_name.isalpha() == True:
            raw_input("NIT: ")
            totaiv = total_price + iva
            print "_____________________________________________________________"
            print ("Subtotal without iva is: - - - - - - -  %.2f\t") %total_price
            print ("iva is:- - - - - - - - - - - - - - - -  %.2f\t") %iva
            print "_____________________________________________________________"
            print ("SUbtotal with iva is:- - - - - - - - -  %.2f\t") %totaiv
            print "_____________________________________________________________"
            j = False
            print"Thank you for your purchase, come back soon."
            raw_input("press enter to continue")
            limpiar()
            menu()
def limpiar():
    """clean the screen"""
    os.system("reset")
def salir():
    """you call the exit function to terminate the program"""
    sys.exit()
def menu():
    """displays the menu to select an option"""
    whily = True
    while whily == True:
        print "cash Register"
        print "¿What would you do?"
        print "1.) Insert_product"
        print "2.) Shopping"
        print "3.) Exit"
        opmenu = raw_input("insert numeric of Menu: ")
        limpiar()
        if opmenu.isalpha() == False:
            if opmenu == "1":
                insert_product()
            elif opmenu == "2":
                sell_articles()
            elif opmenu == "3":
                print "Good bye"
                whily = False
                sys.exit()
        elif opmenu != "1"or opmenu != "2" or opmenu != "3":
            print "enter a valid option"
menu()
