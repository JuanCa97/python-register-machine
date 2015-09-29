#! / usr / bin / python
# -*- coding: utf-8 -*-
"""Register Machine"""
import sys
import os

ARTICLES={}
TOTALONE=06

def ingreso_productos():
    BOX=True
    while BOX==True:
        OPTION =raw_input("You want to enter a product? y/n: ")
        try:
            if OPTION.isalpha()==True:
                if OPTION.lower()=="y":
                    PRODUCT=raw_input("Insert a product: ")
                    PRICE=int(raw_input("Insert the price of the product: "))
                    ARTICLES[PRODUCT]=PRICE
                elif OPTION.lower()=="n":
                    BOX=False
                else:
                    print"unrecognized data"
            else:
                print"unrecognized data numeric"
        except:
            BOX=True
    print "their existing articles are:"
    for KEY in ARTICLES:
        print KEY,":",ARTICLES[KEY]

def shopping():
	if len(ARTICLES)>0:
	    BOXTWO=True
	    TOTAL=0
	    while BOXTWO==True:
	        for KEY in ARTICLES:
	        	print KEY,":",ARTICLES[KEY]
	        PRODUCT=raw_input("Products that want to take?")
	        for ELEMENT in ARTICLES:
	            if ELEMENT==PRODUCT:
	                print "you chose %s"%(ELEMENT)
	                QUANTITY=input("any amounts desired product?")
	                CANT=QUANTITY*ARTICLES[ELEMENT]
	                TOTAL=TOTAL+CANT
	                
	                print "article %s: quantity %s: subtotal invoice Q.%s "%(ELEMENT, QUANTITY,TOTAL )
	                RESPONSE=True
	                while RESPONSE==True:
	                    FOLLOW=raw_input("To select a different item y/n:")
	                    if FOLLOW.lower()=="y":
	                        BOXTWO=True
	                        RESPONSE=False
	                    elif FOLLOW.lower()=="n":
	                        BOXTWO=False
	                        RESPONSE=False
	                        return TOTAL
	                    else:
	                        print "option invalidates"
	                        RESPONSE=True
	else:
		print "No existing products"

def BILL():
    BOXTWO=True
    while BOXTWO==True:
        print "1)Gold"
        print "2)Silver"
        print "3)Any"
        CARD=raw_input("What kind of card do you have?: ")
        try:
            if CARD.isalpha()==False:
                #ingreso de producto
                if CARD=="1":
					print "Gold"
					print u"The client has a 5%  discount:"
					print "The subtotal of the invoice is Q.%s" %(TOTALONE)
					IVA = (TOTALONE*0.12)
					DISCOUNT = (TOTALONE*0.05)
					ALLTOTAL = TOTALONE + IVA - DISCOUNT
					print "should: %s"%(TOTALONE)
					print "______________________"
					CLient_name = raw_input("Client name:  ")
					nit = raw_input("NIT: ")
					CASH = input("CASH :  ")
					CHANGE = CASH - TOTALONE
					print "__________________________"
					print ("Price       %.2f\t") % TOTALONE
					print ("IVA          %.2f\t") % IVA
					print ("Total        %.2f\t") % ALLTOTAL
					print ("CASH     %.2f\t") % CASH
					print "__________________________"
					print "CHANGE:   %s"%(CHANGE)
					break
					#compra
                elif CARD=="2":
                    print "Silver"
                    print "The client has a 2%  discount:"
                    print "El subtotal de la factura esQ.%s"%(TOTALONE)
                    IVA = (TOTALONE*0.12)
                    DISCOUNT = (TOTALONE*0.02)
                    ALLTOTAL = TOTALONE + IVA - DISCOUNT
                    # aqui comienza facturación
                    print "should: ",ALLTOTAL
                    print ("______________________")
                    CLient_name = raw_input("Nombre Del Cliente: ")
                    nit = raw_input("NIT: ")
                    CASH = input("CASH :  ")
                    CHANGE = CASH - ALLTOTAL
                    print ("__________________________")
                    print ("Price       %.2f\t") % TOTALONE
                    print ("IVA          %.2f\t") % IVA
                    print ("Total        %.2f\t") % ALLTOTAL
                    print ("CASH     %.2f\t") % CASH
                    print ("__________________________")
                    print ("CHANGE:   "),CHANGE
                    BOXTWO=False