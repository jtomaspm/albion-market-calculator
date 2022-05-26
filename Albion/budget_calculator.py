import imp
from operator import ge
from re import I
from settings import *

def get_by_location(items,location):
    return [i for i in items if location == i.city]



def ver_se_compensa(items,locations):
    loc_d = {}
    for l in locations:
        loc_d[l] = get_by_location(items,l)
    pass



def get_materials_list():
    dict = []
    for i in refinements["Materials"]:
        material = i
        array1=[]
        x=range(5)
        for j in x: 
            j="T" + str(4+j)+ "_" +material
            array1.append(j)

        for i in range(len(array1)):
            dict.append(array1[i])
            for x in range(3):
                k = array1[i] + "_LEVEL" + str(x+1) + "@" + str(x+1)
                dict.append(k)

    return dict

def get_full_materials_dict(items):
    items_dict = {}
    for elem in items:
        items_dict[elem.item_id] = elem.sell_price_max
    return items_dict

def get_item_price(items,elem):
    if elem == 'T3_FIBER': #Criar um identificador para T3, introduzir na db
        return 51
    elif elem == 'T3_PLANKS':
        return 52
    elif elem == 'T3_ROCK': 
        return 53
    elif elem == 'T3_HIDE':
        return 54
    elif elem == 'T3_ORE':
        return 55

    else:
        list = get_full_materials_dict(items)
    
        return list[elem]

def get_raw_material(items,elem):
    lista = refinements["Materials"]  
    print('____material_____')
    print(elem)
    print()
    print ('______lista_____________-')
    print (lista)
    print()
    index = lista.index(elem)-1  
    print ('_________Index_______')
    print(lista.index(elem))
    print()
    print('_______Index-1_______')
    print( lista[index])
    print()

    return lista[index] 
    


def math_function(items):
    a = {}
    b=[]

    a = get_full_materials_dict(items)
    for elem in a.keys():
        b=elem.split('_')
        tier=int(b[0][1:])
        
        material=b[1]
        get_raw_material(items,material)
        if len(b)==3:
            enchant=b[2]
            Higher_Tier="T" + str(tier) +"_" + get_raw_material(items,material)
            Lower_Tier="T"+str(tier-1) + "_" + get_raw_material(items,material) 
        elif len(b)==2:
            Higher_Tier="T" + str(tier) +"_" + get_raw_material(items,material)
            Lower_Tier="T"+str(tier-1) + "_" + get_raw_material(items,material) 
            #print('_________________Raw_Material________________')
            #print (get_raw_material(items,material))
            #print ()
            #print('_________________tier_normal_________________')
            #print(tier)
            #print()
            #print('_________________tier_normal-1_________________')
            #print(tier-1)
            #print()
            #print('________________Higher Tier_________________')
            #print(Higher_Tier)
            #print()
            #print('________________Lower Tier_________________')
            #print(Lower_Tier)
            #print()
            #print('_________________Preço___________________')
            #print(get_item_price(items,Higher_Tier) +get_item_price(items,Lower_Tier))
            #print()
        else:
            print("Erro length do material")
    print('Preço T5')
    print(get_item_price(items,'T5_FIBER'))
    print(get_item_price(items,'T4_FIBER'))
    print()
    function= get_item_price(items,Higher_Tier) +get_item_price(items,Lower_Tier)




    return function
