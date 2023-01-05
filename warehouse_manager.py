items = {"Name": [" dresses"," jackets", "jeans"], 
"Quantity":["5","4","7"] ,
"Unit":["pcs","pcs","pcs"],
"Unit_Price (PLN)":["100","160","120"]
}
print("What would you like to do?")
if __name__ == "__main__":
    text = input()
    
    if text == "exit":
        print("Exiting...Bye!")
        
    elif text == "show":
        print("Name\tQuantity\tUnit\tUnit Price (PLN)")
        break
    
        

