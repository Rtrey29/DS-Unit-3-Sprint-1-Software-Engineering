from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in list(range(num_products)):

        # created names from a random sampling of ADJECTIVE and NOUN lists
        x = sample(ADJECTIVES, k=1) + sample(NOUNS, k=1)
        xstr = ' '.join(x)
        # Declared products with random values
        product = Product(xstr, randint(5, 100), randint(5, 100),
                          uniform(0, 2.5))

        products.append(product)
    return products


def inventory_report(products):
    total_price = 0
    total_weight = 0
    total_flammability = 0
    uniqueset = set()

    for product in products:
        # added items from the products list to a set to return
        # unique values
        uniqueset.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    price_average = total_price / len(products)
    weight_average = total_weight / len(products)
    flammability_average = total_flammability / len(products)

    print('---ACME CORPORATION OFFICIAL INVENTORY REPORT---')
    print('------------------------------------------------')
    print('Unique products:', len(uniqueset))
    print('Average Price:', price_average)
    print('Average weight:', weight_average)
    print('Average flammability:', flammability_average)


if __name__ == '__main__':
    inventory_report(generate_products())
