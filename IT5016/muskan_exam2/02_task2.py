s"""
calculating ferry total...
Author: Muskan
"""

def ferry_servicetotal():
    service_list = []  #it is a list that stores value. 
    total_value = 0
    while True:
        item = input("Enter the name of the item(or type'done'to finish):")
        if item.lower() == 'done':
            break

        try:
            price = float(input(f"Enter the price of '{item}':"))
            service_list.append((item,price))
            total_price += price


        except ValueError:
            print("Invalid input.please enter a numeric value for the price.")

    return service_list,total,total_price


def main():
    print("welcome to the service list program") 
    service_list, total_price = ferry_servicetotal()


    if not service_list:
        print("\nservice list:")
        for item,price in service_list:

            print("{item},${price:.2f}")
            
        print(f"\nTotal price :${total_price}:.2f")


main()





    










