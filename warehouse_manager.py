items = [{'Name': 'dress', 'Quantity':'5','Unit':'pcs','Unit_price (PLN)':'120'},
    {'Name': 'jacket', 'Quantity':'7','Unit':'pcs','Unit_price (PLN)':'150'},
    {'Name': 'short', 'Quantity':'9','Unit':'pcs','Unit_price (PLN)':'50'},
    {'Name': 'skirt', 'Quantity':'4','Unit':'pcs','Unit_price (PLN)':'60'}]


sold_items = []


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("_"*4 + "   " + "_" * 8 + "         " + "_" * 4 +"   " + "_" * 15 )
    for j in range (0, len(items)):
        print(f"{items[j]['Name']}\t   {items[j]['Quantity']}    \t {items[j]['Unit']}  \t  {items[j]['Unit_price (PLN)']}")


def add_item(name,quantity,init,unit_price):
    items.append({'Name':name, 'Quantity':quantity,'Unit':unit, 'Unit_price (PLN)': unit_price})


def sell_item(name_sell, quantity_sell):
    print(f"Successfully sold {quantity_sell} {name_sell}")
    for j in range (0,len(items)):
        if name_sell == items[j]['Name']:
            items[j]['Quantity'] = items[j]['Quantity']-quantity_sell
            sold_items.append({'Name':name_sell, 'Quantity':quantity_sell, 'Unit':items[j]['Unit'], 'Unit_price (PLN)': items[j]['Unit_price (PLN)']})


def get_costs():
    costs = sum ([sold_items[j]['Quantity'] * sold_items[j]['Unit_price (PLN)'] for j in range(0,len(sold_items))]) 
    return  round(costs,2)  


def get_income():
    income = sum([sold_items[j]['Quantity'] * sold_items[j]['Unit_price (PLN)'] for j in range (0, len(sold_items))])
    return round(income,2)


def show_revenue():
    print(f"Income : {get_income()}")
    print(f"Costs: {get_costs()}")
    print("_" * 8)
    revenue = get_income() - get_costs()
    return round(revenue,2)


def export_items_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Quantity', 'Unit', 'Unit_price (PLN)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 
        for j in range (0,len(items)):
            writer.writerow({'Name': item[j]['Name'],'Quantity':items[j]['Quantity'],'Unit':items[j]['Unit'],'Unit_price (PLN)' : ítems[j]['Unit_price (PLN)']})


def export_sales_to_csv():


if __name__ == "__main__":
    text = input()
    
    while text == "exit":
        print("Exiting...Bye!")
        break
    else:
        get_items()
        