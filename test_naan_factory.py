
# Import relevant libraries and classes
from naan_factory import NaanFactory
import unittest
import pytest

class TestNaanFactory(unittest.TestCase):
    # Instantiate the class
    naan_factory=NaanFactory()

    # define the function for test make_dough
    def test_make_dough(self):
        # If the ingredients are "water" and "flour", returns "dough" therefore passes
        self.assertEqual(self.naan_factory.make_dough("water","flour"),"dough")
        # Check the else statement works. If the ingredients are anything other than flour and water, should return "not dough"
        self.assertEqual(self.naan_factory.make_dough("flower","water"),"not dough")

    # Define the function to test bake_dough
    def test_bake_dough(self):
        self.assertEqual(self.naan_factory.bake_dough("dough"),"baked naan")

    # Define the function to test run_factory
    def test_run_factory(self):
        self.assertEqual(self.naan_factory.run_factory("water","flour"),"naan factory running")


