items = [{'Name': 'dress', 'Quantity':'5','Unit':'pcs','Unit_price (PLN)':'120'},
    {'Name': 'jacket', 'Quantity':'7','Unit':'pcs','Unit_price (PLN)':'150'},
    {'Name': 'short', 'Quantity':'9','Unit':'pcs','Unit_price (PLN)':'50'},
    {'Name': 'skirt', 'Quantity':'4','Unit':'pcs','Unit_price (PLN)':'60'}]


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("____________________________________________" )
    for j in range (0, len(items)):
        print(f"{items[j]['Name']}\t   {items[j]['Quantity']}    \t {items[j]['Unit']}  \t  {items[j]['Unit_price (PLN)']}")


get_items()
