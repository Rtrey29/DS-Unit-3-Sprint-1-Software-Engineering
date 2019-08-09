from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
      x= str(random.sample(ADJECTIVES,1))+ str(random.sample(NOUNS,1))
      products.append(x)
    return products


def inventory_report(products):
    
    
if __name__ == '__main__':
    inventory_report(generate_products())
    