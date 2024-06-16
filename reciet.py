def generate(items, prices):
    total = sum(prices)
    
    re = "Receipt\n"
    re+= "-------------------------\n"
    
    for item, price in zip(items, prices):
        re += f"{item:<20} Rs{price:.2f}\n"
    
    re += "-------------------------\n"
    re += f"Total:               Rs{total:.2f}/-\n"
    
    return re
def main():
    items = []
    prices = []
    
    while True:
        item = input("Enter item purchased (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        
        price = float(input("Enter the price: "))
        
        items.append(item)
        prices.append(price)
    
    re = generate(items, prices)
    
    print("\nGenerated Receipt:\n")
    print(re)
    
   
if __name__ == "__main__":
    main()
    