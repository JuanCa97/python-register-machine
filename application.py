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

