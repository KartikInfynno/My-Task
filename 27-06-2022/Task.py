d_mart = {
    "Inventory": {


        "Clothes": {
            "shirt": {

                "Quantity": 50,
                "price": 200
            },
            "Jeans": {

                "Quantity": 30,
                "price": 250
            }

        },
        "Groceries": {
            "oil": {
                "Quantity": 45,
                "price": 2000,
            },
            "rice": {
                "Quantity": 205,
                "price": 100,
            },
            "wheat": {
                "Quantity": 69,
                "price": 1000,
            }
        },
        #         "Groceries1": {
        #             "oil": {
        #                 "Quantity": 45,
        #                 "price": 2000,
        #             },
        #             "rice": {
        #                 "Quantity": 205,
        #                 "price": 100,
        #             },
        #             "wheat": {
        #                 "Quantity": 69,
        #                 "price": 1000,
        #             }
        #         },
        #         "Groceries2": {
        #             "oil": {
        #                 "Quantity": 45,
        #                 "price": 2000,
        #             },
        #             "rice": {
        #                 "Quantity": 205,
        #                 "price": 100,
        #             },
        #             "wheat": {
        #                 "Quantity": 69,
        #                 "price": 1000,
        #             }
        #         },

    }
}

i = d_mart.values()
for j in i:
    k = j.values()
    for j in i:
        k = j.values()
        for l in k:
            for k1, v2 in l.items():
                for k, v in v2.items():
                    #                     print( k, v)
                    if k == "price" and v > 200:
                        print(k1, ':', k, v)
                    if k == 'price' and v > 200:
                        if v <= 250:
                            dis_am = (10*v)/100
                            dis = v - dis_am
                            print(k1, ':', k, int(dis), '10% discount')
                        elif v >= 2000:
                            dis_am = (10*v)/100
                            dis = v - dis_am
                            print(k1, ':', k, int(dis), '10% discount')
                        elif v == 1000:
                            dis_am = (10*v)/100
                            dis = v - dis_am
                            print(k1, ':', k, int(dis), '10% discount')
                        else:
                            print(k1, ':', k, v, 'not in discount')
