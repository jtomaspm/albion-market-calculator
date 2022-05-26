import requests 
from market_item import *
from budget_calculator import *
import json


def main():
    api_link = "https://www.albion-online-data.com/api/v2/stats/prices/"



    def get_parametros(items,params=None):
        r = "" 
        for item in items:
            r+=item+',' 
        r=r[:-1]
        if params:
            r+='?'
            for key,val in params.items():
                r+=key+'='+val+'&'
                r=r[:-1]
        return r

    def get_location_str(locations):
        r = ''
        for l in locations:
            r+=l+',' 
        return r[:-1]

    parametros={
        'locations' : get_location_str([
            'Bridgewatch',
            'Caerleon',
        ])
    }    
    p = get_parametros(items=get_materials_list(),params=parametros)

    r = requests.get(api_link+p)
    market_items = []
    s = ''
    for i in r.json():
        s+=i['item_id']
        s+='\n'
        s+='\n'
        s+=json.dumps(i)
        s+='\n'
        s+='\n'
        s+='\n'
        s+='\n'
        market_items.append(market_item(i))

    #print(p)
    #print(market_items[0].get_min_max_dif())

    test = get_by_location(market_items,'Caerleon')
    for k in test:
        print(k.item_id, k.city)

    with open('db.txt', 'w') as f:
        f.write(s)
    with open('mat.txt', 'w') as f:
        f.write(json.dumps(get_full_materials_dict(market_items)))
    #print(get_full_materials_dict(market_items))
    #print()
    #print()
    #print()
    #print()
    print(math_function(market_items))

if __name__ == "__main__":
    main()
 