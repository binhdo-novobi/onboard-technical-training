# Exercise 1:
def exercise_1(price_list, *args):
    result = {}
    for order in args:
        for item in order:
            product = list(item.keys())[0]
            if product in result.keys():
                result[product] += item[product] * price_list[product]
            else:
                result[product] = item[product] * price_list[product]
    return result


# Exercise 2
def exercise_2(order, delivery_order):
    for item_del in delivery_order:
        for item_ord in order:
            if item_ord["product"] == item_del["product"]:
                item_ord["delivered_qty"] = item_del["delivered_qty"]
                break


# Exercise 3
def exercise_3(order):
    sum_order = {}
    for item in order:
        if item["product"] in sum_order.keys():
            sum_order[item["product"]] += item["ordered_qty"]
        else:
            sum_order[item["product"]] = item["ordered_qty"]
    result = []
    for key, value in sum_order.items():
        result.append({
            "product": key,
            "ordered_qty": value
        })
    return result


if __name__ == "__main__":
    print("Exercise 1:")
    price_list = {
        "PowerCore": 790000,
        "PowerLine": 200000,
        "PowerPort": 750000
    }
    order_1 = [{"PowerCore": 1}, {"PowerLine": 1}]
    order_2 = [{"PowerLine": 2}]
    order_3 = [{"PowerCore": 1}, {"PowerPort": 2}]
    result = exercise_1(price_list, order_1, order_2, order_3)
    print(result)

    print("\nExercise 2:")
    order = [
        {
            "product": "PowerCore",
            "ordered_qty": 2,
            "delivered_qty": 0
        },
        {
            "product": "PowerLine",
            "ordered_qty": 5,
            "delivered_qty": 0
        },
        {
            "product": "PowerPort",
            "ordered_qty": 3,
            "delivered_qty": 0
        }
    ]
    delivery_order = [
        {
            "product": "PowerCore",
            "delivered_qty": 2
        },
        {
            "product": "PowerLine",
            "delivered_qty": 3
        }
    ]
    exercise_2(order, delivery_order)
    print(order)

    print("\nExercise 3:")
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
        }
    ]
    result = exercise_3(order)
    print(result)
