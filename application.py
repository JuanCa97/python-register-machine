#! / usr / bin / python
# -*- coding: utf-8 -*-
"""Register Machine"""
import os
import sys

ARTICLis={}
TOTALONE=06


def insert_product():
    limpiar()
    BOX = True
    while BOX == True:
        limpiar()
        OPTION =raw_input("You want to enter a product? y/n: ")
        if OPTION.isalpha()==True:
            if OPTION.lower()=="y":
                while True:
                    limpiar()
                    PRODUCT=raw_input("Insert a product: ")
                    if PRODUCT.isalpha():
                        break
                    else:
                        print"unrecognized data numeric"
                        
                while True:
                    try:
                        PRICE=float(raw_input("Insert the price of the product: "))
                        ARTICLis[PRODUCT]=PRICE
                        break
                    except ValueError:
                        print"unrecognized data"
            elif OPTION.lower()=="n":
                BOX=False
        else:
            print "their existing articlis  are:"

    for KEY in ARTICLis:
        print KEY,":",ARTICLis[KEY]


def shopping():
    limpiar()
    if len(ARTICLis)>0:
        BOXTWO=True
        TOTAL=0
        while BOXTWO==True:
            for KEY in ARTICLis:
                print KEY,":",ARTICLis[KEY]
            PRODUCT=raw_input("Products that want to take?")
            for TheEMENT in ARTICLis:
                if TheEMENT==PRODUCT:
                    print "you chose %s"%(TheEMENT)
                    QUANTITY=input("any amounts ofsired product?")
                    CANT=QUANTITY*ARTICLis[TheEMENT]
                    TOTAL=TOTAL+CANT
                    
                    print "article %s: quantity %s: subtotal invoice Q.%s "%(TheEMENT, QUANTITY,TOTAL )
                    RisPONSE=True
                    FOLLOW=raw_input("To Stheect a different item y/n:")
                    if FOLLOW.lower()=="y":
                        BOXTWO=True
                        RisPONSE=False
                    elif FOLLOW.lower()=="n":
                        BOXTWO=False
                        RisPONSE=False
                        return TOTAL
                        
                    else:
                        print "option invalidatis"
                        RisPONSE=True
        else:
            print "No existing products"
def ASD():
    CASH = ""
    while type(CASH) == str:
        try:
            #a = raw_input("entre al while")
            CASH = int(raw_input("CASH :  "))
        except Exception, e:
            pass

    return CASH

def BILL():
    limpiar()
    BOXTWO=True
    while BOXTWO==True:
        print "1)Gold"
        print "2)Silver"
        print "3)Any"
        CARD=raw_input("What kind of card do you have?: ")
        try:
            if CARD.isalpha()==False:
                #ingreso of producto
                if CARD=="1":
                    print "Gold"
                    print u"The client has a 5%  discount:"
                    print "The subtotal of the invoice is Q.%s" %(TOTALONE)
                    IVA = (TOTALONE*0.12)
                    DISCOUNT = (TOTALONE*0.05)
                    ALLTOTAL = TOTALONE + IVA - DISCOUNT
                    print "should: %s"%(TOTALONE)
                    print "______________________"
                    j = True
                    while j == True:
                        CLient_name = raw_input("Client name:  ")
                        if CLient_name.isalpha()== True:
                            nit = raw_input("NIT: ")
                            CASH = ASD()
                            CHANGE = CASH - TOTALONE
                            print "__________________________"
                            print ("Price       %.2f\t") % TOTALONE
                            print ("IVA          %.2f\t") % IVA
                            print ("Total        %.2f\t") % ALLTOTAL
                            print ("CASH     %.2f\t") % CASH
                            print "__________________________"
                            print "CHANGE:   %s"%(CHANGE)
                            j = False
                            BOXTWO = False

                                
                        else:
                            print "esta malo"
                            j = True

                #compra
                elif CARD=="2":
                    print "Silver"
                    print "The client has a 2%  discount:"
                    print "The subtotal of the bill is Q.%s"%(TOTALONE)
                    IVA = (TOTALONE*0.12)
                    DISCOUNT = (TOTALONE*0.02)
                    ALLTOTAL = TOTALONE + IVA - DISCOUNT
                    # aqui comienza billción
                    print "should: ",ALLTOTAL
                    print ("______________________")
                    j = True
                    while j == True:
                        CLient_name = raw_input("Client name: ")
                        if CLient_name.isalpha() == True:
                            nit = raw_input("NIT: ")
                            CASH = ASD()
                            CHANGE = CASH - ALLTOTAL
                            print ("__________________________")
                            print ("Price       %.2f\t") % TOTALONE
                            print ("IVA          %.2f\t") % IVA
                            print ("Total        %.2f\t") % ALLTOTAL
                            print ("CASH     %.2f\t") % CASH
                            print ("__________________________")
                            print ("CHANGE:   "),CHANGE
                            j = False
                            BOXTWO=False
                        else:
                            print "error"
                            j = True
#bill
                elif CARD =="3":
                    IVA = (TOTALONE*0.12)
                    ALLTOTAL = TOTALONE + IVA 
                    #  aqui comienza billción
                    print "should: ",ALLTOTAL
                    print ("______________________")
                    j = True
                    while j == True:
                        CLient_name = raw_input("Client name:  ")
                        if CLient_name.isalpha()== True:
                            nit = raw_input("NIT: ")
                            CASH = ASD()
                            CHANGE = CASH - TOTALONE

                            print ("__________________________")
                            print ("Price       %.2f\t") % TOTALONE
                            print ("IVA          %.2f\t") % IVA
                            print ("Total        %.2f\t") % ALLTOTAL
                            print ("CASH     %.2f\t") % CASH
                            print ("__________________________")
                            print ("CHANGE:   "),CHANGE
                            j = False
                            BOXTWO = False
                        else:
                            print "esta malo"
                            j = True
                else:
                    print "Option invalidates"
            else:
                print "Unrecognized data numeric"
        except:
            opcion3=True
    print"Thank you for your purchase, come back soon."

def limpiar():
    os.system("reset")


def salir():
    sys.exit()
#menú

salir=False
while salir==False:
    print "Cash Register"
    print "¿What would you do?"
    print "1.) Insert_product"
    print "2.) Shopping"
    print "3.) Exit"
    opmenu = raw_input("insert numeric of Menu: ")
    try:
        if opmenu.isalpha()==False:
            if opmenu =="1":
                
                insert_product()
                opcionmenu=raw_input("To return to the menu y/n: ")
                if opcionmenu.lower()=="y":
                    salir=False
                else:
                    break
            elif opmenu =="2":
                limpiar()
                TOTALONE= shopping()
                print TOTALONE
                print BILL()
                opcionmenu=raw_input("To return to the menu y/n: ")
                if opcionmenu.lower()=="y":
                    limpiar()
                    salir=False
                else:
                    break
            elif opmenu =="3":
                break
                sys.exit()
            
    except:
        'enter a valid option'