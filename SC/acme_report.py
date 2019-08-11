from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in list(range(num_products)):

        x = sample(ADJECTIVES, k=1) + sample(NOUNS, k=1)
        xstr = ' '.join(x)
        product = Product(name=xstr)
 
        for i in list(range(randint(0, 1))):
            product.stealability()

        for j in list(range(randint(0, 50))):
            product.explode()
        
        
        products.append(product)
    return products


def inventory_report(products):
    total_price = 0
    total_weight = 0
    total_flammability = 0
    unique_list = []
    
    for product in products:
        total_price  += product.price
        total_weight += product.weight
        total_flammability += product.flammability
        
        if product not in unique_list:
            unique_list.append(product)
            
    price_average = total_price / len(products)
    weight_average = total_weight / len(products)
    flammability_average = total_flammability / len(products)
    
       
    print('---ACME CORPORATION OFFICIAL INVENTORY REPORT---')
    print('------------------------------------------------')
    print('Unique products:', unique_list)
    print('Average Price:', price_average)
    print('Average weight:', weight_average)
    print('Average flammability:', flammability_average)

if __name__ == '__main__':
    inventory_report(generate_products())
    