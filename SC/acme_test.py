#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        prod = Product('Test product', 10, 20)
        prod2 = Product('Test product 2', 20, 20)
        prod3 = Product('Test product 3', 5, 20)

        self.assertEqual(prod.stealability(), 'Kinda stealable')
        self.assertEqual(prod2.stealability(), 'Very stealable!')
        self.assertEqual(prod3.stealability(), 'Not so stealable')

    def test_explode(self):
        prod = Product('Test product', 10, 20)
        prod2 = Product('Test product 2', 2, 3)
        prod3 = Product('Test product 3', 10, 45, 2)

        self.assertEqual(prod.explode(), '...boom!')
        self.assertEqual(prod2.explode(), '...fizzle.')
        self.assertEqual(prod3.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    def test_legal_names(self):
        product_list = generate_products()
        for prod in product_list:
            prod_name = prod.name.split()
            self.assertIn(prod_name[0], ADJECTIVES)
            self.assertIn(prod_name[1], NOUNS)

    def test_default_num_products(self):
        prod_count = len(generate_products())
        self.assertEqual(prod_count, 30)


if __name__ == '__main__':
    unittest.main()
