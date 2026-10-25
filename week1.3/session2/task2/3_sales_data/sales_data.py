# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
try:

    with open("sales.csv", "r") as infile:
        #initilizing variabels before the loop 
        highest_sale_amount = 0
        sale_sum = 0
        row_count = 0
        total_sale_region = 0
        #dictionary to store each product with it's unit sold
        widget_total = {}
        next(infile)           #to ignore the header 
        for line in infile:
            
            part = line.split(",")

            current_sale_amount = int(part[2])    # to turn the stringe into intger so it can do math operations

            if current_sale_amount > highest_sale_amount:   #confusion how we introduced highest sale as = 0 then it worked?
                highest_sale_amount = current_sale_amount
                sale_day = part[0]

            sale_sum += current_sale_amount        #did this inside the for loop because we need it to add all numbers each iteration
            row_count+= 1                          #same confusion in here

            product = part[1]
            units_sold = int(part[3])

            if product in widget_total:                  # if this product has went throgh the loop before we add the current to the precious saved unit of this product
                widget_total[product] += units_sold   
            else:                                        # if this product new just save it's unit  
                widget_total[product] = units_sold

        
        average_sale = sale_sum / row_count         # outside the loop so it calculates the overall average not the average after each iteration
        max_sold_product = max(widget_total, key = widget_total.get)       # we used this function not widget_total.value() because this function returns the highest value but does not give us the name of the key -product- thats why we used this function to get name of the key(product) with highest value(sold units)

        print(f"The highest sale amount is: {highest_sale_amount} on {sale_day}")  # we printed it ouside the loop cuz we need the answer once the answer of overall not in each iteration
        print(f"The average sale amount is: {average_sale}")
        print(widget_total)
        print(f"Most sold widget is widget {max_sold_product}, with {widget_total[max_sold_product]} units sold")   #remember that name_of_dictionary[name_of_key] returns the value 

except FileNotFoundError:
    print("Error: file not found")
# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows