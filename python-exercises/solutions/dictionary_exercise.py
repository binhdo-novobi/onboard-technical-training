def exercise_1(pricelist, order_1, order_2, order_3):

    result = {}

    for rec in (order_1, order_2, order_3):
        for product in rec:

            (key, values), = product.items()           
            if key not in result:
                result[key] = values * pricelist[key]
            else:
                result[key] += values * pricelist[key]

    return result

def exercise_2(order, delivery_order):

    temp = {}

    # Create a temp dict to store info about product and delivered quantity extracted from delivery order
    for item in delivery_order:
        if item['product'] not in temp:
            temp[item['product']] = item['delivered_qty']
        else: 
            temp[item['product']] += item['delivered_qty']
    
    # Update the delivered quantity in order
    for item in order:
        if item['product'] in temp:
            item['delivered_qty'] = temp[item['product']]

    return order
    
def exercise_3(orders):

    consolidated_order = {}
        
    # Check if the order's product exist in the consolidated order dict. 
    # If no then add it to the dict.
    # If yes then update the quantity 
    for order in orders:

        if order['product'] not in consolidated_order:
            consolidated_order[order['product']] = order
        else:
            consolidated_order[order['product']]['ordered_qty'] += order['ordered_qty']

    return consolidated_order

if __name__ == "__main__":

    # Exercise 1
    order_1 = [{"PowerCore": 1}, {"PowerLine": 1}]
    order_2 = [{"PowerLine": 2}]
    order_3 = [{"PowerCore": 1}, {"PowerPort": 2}]

    price_list = {
        "PowerCore": 790000,
        "PowerLine": 200000,
        "PowerPort": 750000
    }

    result = exercise_1(price_list, order_1, order_2, order_3)
    print(f"Exercise 1: {result}")

    # Exercise 2
    order = [
        {"product": "PowerCore", "ordered_qty": 2, "delivered_qty": 0},
        {"product": "PowerLine", "ordered_qty": 5, "delivered_qty": 0},
        {"product": "PowerPort", "ordered_qty": 3, "delivered_qty": 0},
    ]

    delivery_order = [
        {"product": "PowerCore", "delivered_qty": 2},
        {"product": "PowerLine", "delivered_qty": 3},
    ]

    updated_order = exercise_2(order, delivery_order)
    print(f"Exercise 2: {updated_order}")

    # Exercise 3
    order = [
        {
            "product": "PowerCore",
            "ordered_qty": 2,
        },
        {
            "product": "PowerLine",
            "ordered_qty": 5,
        },
        {
            "product": "PowerPort",
            "ordered_qty": 3,
        },
        {
            "product": "PowerCore",
            "ordered_qty": 1,
        },
        {
            "product": "PowerPort",
            "ordered_qty": 1,
        },
    ]

    res = exercise_3(order)
    consolidated_order_list = list(res.values())
    print(f"Exercise 3: {consolidated_order_list}")



