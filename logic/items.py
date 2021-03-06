"""
Module to create items
"""
import random
from . import constants


class Item:
    """
    Create an item

    """
    def __init__(self, image, stage):
        """
        Init method for the Item class

        Parameters
        ----------
        image : str
            From the Images Directory
        stage : obj
            From Stage class in stage.py

        """
        self.image = image
        self.stage = stage
        random_coordonates_for_path = random.choice(
            [ele for ele in self.stage.get_sprites_for_path()
             if ele != constants.FIRST_SPRITE
             and ele != constants.LAST_SPRITE])
        self.x = random_coordonates_for_path[0]
        self.y = random_coordonates_for_path[1]


class Pack_of_items:
    """
    Create a pack of 4 items

    """
    def __init__(self, item1, item2, item3, item4):
        """
        Init method for the Pack_of_items class

        Parameters
        ----------
        item1 : obj
            From Item class in items.py
        item2 : obj
            From Item class in items.py
        item3 : obj
            From Item class in items.py
        item4 : obj
            From Item class in items.py

        """
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.items_to_display = [self.item1,
                                 self.item2, self.item3, self.item4]
