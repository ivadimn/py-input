import random

def random_item(list_items):
    if not list_items:
        return None
    else:
        return random.choice(list_items)