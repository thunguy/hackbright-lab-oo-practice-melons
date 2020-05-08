############
# Part 1   #
############



class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, 
                 is_bestseller):
        """Initialize a melon."""
        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairings(self, *pairings):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairings)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    musk.add_pairings("mint")

    cas = MelonType("Casaba", "cas", 2003, "orange", False, False)
    cas.add_pairings("mint", "strawberries")

    cren = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    cren.add_pairings("proscuitto")

    yw = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, True)
    yw.add_pairings("ice cream")

    all_melon_types.extend([musk, cas, cren, yw])

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with:")

        for pairings in melon.pairings:
            print(f"-{pairings}")

print(print_pairing_info(make_melon_types()))



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_codes = {melon.code: melon for melon in melon_types}

    return melon_codes

print(make_melon_type_lookup(make_melon_types()))



############
# Part 2   #
############



class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon instance."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester


    def is_sellable(self):
        """Determine if a melon is sellable"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_codes = make_melon_type_lookup(make_melon_types())
    melons = []

    melon1 = Melon(melon_codes['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_codes['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_codes['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_codes['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_codes['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_codes['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_codes['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_codes['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_codes['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon1, melon2, melon3, melon4, melon5, 
                   melon6, melon7, melon8, melon9])

    return melons

print(make_melons(make_melon_types()))



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        harvester = melon.harvester
        field = melon.field
        sellability = "SELLABLE" if melon.is_sellable() else "NOT SELLABLE" 

        print(f"Harvested by {harvester} from Field #{field}. {sellability}.")

    # for melon in melons:
    #     if melon.is_sellable():
    #         print(f"Harvested by {melon.harvester} from Field #{melon.field}. SELLABLE.")
    #     else:
    #         print(f"Harvested by {melon.harvester} from Field #{melon.field}. NOT SELLABLE.")

print(get_sellability_report(make_melons(make_melon_types())))