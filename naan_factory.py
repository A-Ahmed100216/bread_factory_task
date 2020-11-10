# Create a class
class NaanFactory:

    # Define functions using user stories
    # 1: As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.
    def make_dough(self,ingredient1,ingredient2):
        # If the ingredients are water and flour, returns dough.
        if ingredient1=="water" and ingredient2=="flour":
            return "dough"
        else:
            return "not dough"

    # 2: As a user, I can use the bake dough with dough to get naan.
    def bake_dough(self,dough):
        # If dough, return baked naan
        if dough=="dough":
            return "baked naan"
        else:
            return "baked something"

    # 3: As a user, I can user the run factory with water and flour and get naan.
    def run_factory(self,ingredient3,ingredient4):
        # If the ingredients are water and flour, returns naan factory running.
        if ingredient3=="water" and ingredient4=="flour":
            return "naan factory running"
        else:
            return "not running"

