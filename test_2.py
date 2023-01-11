items = {"Name": [" dresses"," jackets", "jeans"], 
"Quantity":["5","4","7"] ,
"Unit":["pcs","pcs","pcs"],
"Unit_Price (PLN)":["110","160","120"]
}
print("What would you like to do?")

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")      
    print("dresses\t5       \tpcs     \t110")
    print("jackets\t4       \tpcs     \t160")
    print("jeans\t7         \tpcs      \t120" )
    
def add_items():
    
    name=input("Input the name:")
    quantity=input("Input the quantity:")
    unit=input("Input the unit:")
    price=input("Input price:")
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")      
    print("dresses\t5       \tpcs     \t110")
    print("jackets\t4       \tpcs     \t160")
    print("jeans\t7         \tpcs      \t120" )
    print(str(name) +"\t"+str(quantity)+ "       \t"+ str(unit) + "        \t" +str(price))

def sell_items():
    name=input("Name of the item:")
    quantity_new =input("Quantity to sell:")
    a =input("Successfully sold:")
    quantity_final = int(quantity-quantity_new)
  
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")      
    print("dresses\t5       \tpcs     \t110")
    print("jackets\t4       \tpcs     \t160")
    print("jeans\t7         \tpcs      \t120" )
    print(str(name) +"\t"+str(quantity_final)+ "       \t"+ str(unit) + "        \t" +str(price))
  
    

    
if __name__ == "__main__":    
    while True:
        text = input()
        if text == "exit":
            print("Exiting...Bye!")
            break
        elif text ==  "show":
            get_items()
            print(input("What would you like to do?"))
            break
        elif text == "add":
            add_items()
            print(input("What would you like to do?"))
            break
        elif text == "sell":
            sell_items()
            print(input("What would you like to do?"))
            break    