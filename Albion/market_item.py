"""
{
    'item_id': 'T4_BAG',
    'city': 'Bridgewatch', 
    'quality': 2, 
    'sell_price_min': 2731, 
    'sell_price_min_date': '2022-05-24T19:10:00', 
    'sell_price_max': 2739, 
    'sell_price_max_date': '2022-05-24T19:10:00', 
    'buy_price_min': 2268, 
    'buy_price_min_date': '2022-05-24T14:30:00', 
    'buy_price_max': 2476, 
    'buy_price_max_date': '2022-05-24T14:30:00'}
"""



import re


class market_item:
    def __init__(self, item_json):
        self.item_id = item_json['item_id']
        self.city = item_json['city']
        self.quality = item_json['quality']
        self.sell_price_min = item_json['sell_price_min']
        self.sell_price_min_date = item_json['sell_price_min_date']
        self.sell_price_max = item_json['sell_price_max']
        self.sell_price_max_date = item_json['sell_price_max_date']
        self.buy_price_min = item_json['buy_price_min']
        self.buy_price_min_date = item_json['buy_price_min_date']
        self.buy_price_max = item_json['buy_price_max']
        self.buy_price_max_date = item_json['buy_price_max_date']

    def get_min_max_dif(self):
        return int(self.sell_price_max) - int(self.sell_price_min)
