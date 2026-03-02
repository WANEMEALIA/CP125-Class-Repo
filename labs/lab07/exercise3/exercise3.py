def compare_prices(store_a, store_b):
    only_a = []
    a_cheaper = []
    b_cheaper = []
    for i in store_a :
        if i not in store_b :
            only_a.append(i)

        else: 
            if store_a[i] < store_b[i]:
                a_cheaper.append(i)
            elif store_a[i] > store_b[i]:
                b_cheaper.append(i)
    return {
        "only_a" : sorted(only_a),
        "a_cheaper" : sorted(a_cheaper),
        "b_cheaper" : sorted(b_cheaper)
    }

store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
