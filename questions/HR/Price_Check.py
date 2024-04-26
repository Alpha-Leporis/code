'''
There is a shop with old-style cash registers. Rather than scanning items and pulling the price from a
database, the price of each Item is typed in manually. This rnethod sometimes leads to errors. Given a
list of items and their correct prices, compare the prices to those entered when each item was sold.
Determine the number of errors in selling prices.

Example
products = [ 'eggs', milk', cheese']
productPr,ces = [2.89, 3.29, 5.79]
productSodd = [ 'eggs','eggs', cheese', milk']
soldPnce = [2.89, 2.89, 5.79, 3.29]

			price

Product		Actual		Expected	Error
eggs		2.89		2.89
eggs		2.99		2.89		1
cheese		5.97		5.79		1
milk		3.29		3.29


The second sale of eggs has a wrong price, as does the sale of cheese. There are 2 errors in pricing.

'''

'''
To solve this problem in Python, you can iterate through the lists of sold products and their prices, 
compare the actual sold prices with the expected prices, and count the number of errors.

In this code:
    1. We define the function priceCheck that takes four lists as input: products, productPrices, productSold, and soldPrices.
    2. We create a dictionary price_dict to map each product to its corresponding price.
    3. We iterate through the list of sold products (productSold) and compare each sold price (soldPrices) with its expected price (price_dict[productSold[i]]).
    4. If the sold price doesn't match the expected price, we increment the errors count.
    5. Finally, we return the total number of errors in pricing.

Time complexity is O(n + m), where n is the number of products and m is the number of sold products.
Space complexity is O(n), where n is the number of products.
'''

def priceCheck(products, productPrices, productSold, soldPrices):
    errors = 0
    price_dict = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        expected_price = price_dict[productSold[i]]
        if expected_price != soldPrices[i]:
            errors += 1
    return errors

# Example usage:
products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrices = [2.89, 2.99, 5.79, 3.29]

errors = priceCheck(products, productPrices, productSold, soldPrices)
print("Number of errors in pricing:", errors)

# optimized solution:

'''
To optimize the solution by using a dictionary to directly map products to their prices.
This eliminates the need for nested loops and improves the lookup time for prices, resulting in a more efficient solution.
In this optimized solution:

    We construct a dictionary price_dict that maps each product to its corresponding price using zip.
    We iterate through the lists of sold products and their prices using zip.
    For each sold product, we directly look up its price in the price_dict.
    If the sold price doesn't match the expected price, we increment the errors count.

This optimized solution reduces the time complexity by eliminating nested loops 
and improves efficiency by using dictionary lookup for prices.

Time complexity is O(n + m), where n is the number of products and m is the number of sold products.
Space complexity is O(n), where n is the number of products. This is due to the space used by the price_list list to store product prices.
'''

def priceCheck(products, productPrices, productSold, soldPrices):
    price_dict = dict(zip(products, productPrices))
    errors = 0
    for sold_product, sold_price in zip(productSold, soldPrices):
        if price_dict.get(sold_product) != sold_price:
            errors += 1
    return errors

# Example usage:
products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrices = [2.89, 2.99, 5.79, 3.29]

errors = priceCheck(products, productPrices, productSold, soldPrices)
print("Number of errors in pricing:", errors)


