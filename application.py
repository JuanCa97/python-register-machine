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
