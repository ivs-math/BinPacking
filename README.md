# BinPacking

This notebook discuses the solution to a particular bin packing problem that requires previous item classification. 

## Obective:
 **Determine the number of cold bags and baskets for each order.**

## Context
Today, orders are not being packed in a very efficient way, thus, the warehouse chief asked you to create an algorithm that can solve for any set of products how many baskets and cold bags are needed to correctly pack an order. 

## Conditions
Each order contains different products that have diverse characteristics.

Each of the products has:

**Dimensions** *(height, length, width)* in centimeters and *Weight* in grams

A **category** that determines if the product can be mixed with other products:

* *Food*

* *Toilet*

* *Pets*

A **storage type** that determines the type of package that will be used for the product

* *Dry*

* *Refrigerated*

* *Frozen*

There are some constraints associated with the type of package to be used when packing a product:

* All Dry products must be packed in a baskets

* All Refrigerated and Frozen products must be packed in a cold bag

* Products cannot be mixed if their categories are different, for example, a food product cannot be packed in the same basket that was used to pack a pet product, and also, a toilet product cannot be packed in the same basket that was used to pack a pet product, and so on.

The baskets have the following characteristics:

* Length: 50 centimeters

* Width: 40 centimeters

* Height: 60 centimeters

* Total weight that it can resit: 25 kilograms


The cold bags have the following characteristics:

* Length: 23 centimeters

* Width: 37 centimeters

* Height: 18 centimeters

* Total weight that it can resit: 5 kilograms

## Dataset

The given dataset is separated in different csv files:

* **orders**: it contains the orders that need the calculation of baskets and cold bags. Also, you can see when the order must be delivered and which warehouse received the order.

* **order_products**: contains what products and how many units of it were on an order from the file “orders”.

* **store_products**: contains information about the storage of the products and a marketing category.

* **products**: contains information about the products, its dimensions and weight, as well as their names and the can_mix category.
