orders = [
    {'order_id': 594526, 'origin': 'Austria', 'value': 185, 'multiplier': 1},
    {'order_id': 559006, 'origin': 'France', 'value': 313, 'multiplier': 1},
    {'order_id': 828446, 'origin': 'France', 'value': 299, 'multiplier': 14},
    {'order_id': 855966, 'origin': 'Moldavia', 'value': 109, 'multiplier': 1},
    {'order_id': 673246, 'origin': 'Russia', 'value': 252, 'multiplier': 16},
    {'order_id': 364126, 'origin': 'Austria', 'value': 452, 'multiplier': 13},
    {'order_id': 224286, 'origin': 'Austria', 'value': 242, 'multiplier': 1},
    {'order_id': 312926, 'origin': 'Moldavia', 'value': 481, 'multiplier': 1},
    {'order_id': 613406, 'origin': 'China', 'value': 353, 'multiplier': 4},
    {'order_id': 143486, 'origin': 'Russia', 'value': 373, 'multiplier': 1},
    {'order_id': 439326, 'origin': 'Spain', 'value': 208, 'multiplier': 1},
    {'order_id': 983646, 'origin': 'Portugal', 'value': 381, 'multiplier': 1},
    {'order_id': 198686, 'origin': 'USA', 'value': 429, 'multiplier': 17},
    {'order_id': 231326, 'origin': 'Spain', 'value': 243, 'multiplier': 1},
    {'order_id': 755166, 'origin': 'Austria', 'value': 133, 'multiplier': 1},
    {'order_id': 290846, 'origin': 'Spain', 'value': 435, 'multiplier': 1},
    {'order_id': 151006, 'origin': 'Portugal', 'value': 491, 'multiplier': 1},
    {'order_id': 109246, 'origin': 'Italy', 'value': 114, 'multiplier': 1},
    {'order_id': 901726, 'origin': 'Portugal', 'value': 398, 'multiplier': 1},
    {'order_id': 420446, 'origin': 'Germany', 'value': 498, 'multiplier': 5},
]

discount = ['Germany', 'France', 'Austria', 'Italy']


def calculate_fees(origin, value, taxes=3):
    fee = 16.00
    if origin in discount:
        fee -= 4.50
    return round(fee + ((value / 100) * taxes), 2)


def pretty_print(data):
    for fee in data:
        print(f"Order: {fee['order_id']}, fees: {fee['fees']}")


if __name__ == '__main__':
    for order in orders:
        if order["multiplier"] != 1:
            order["fees"] = calculate_fees(origin=order["origin"],
                                           value=order["value"], taxes=order["multiplier"])
            continue
        order["fees"] = calculate_fees(origin=order["origin"], value=order["value"])
    pretty_print(orders)
