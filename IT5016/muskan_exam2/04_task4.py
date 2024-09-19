"""
Display of ticket booking and total requisition
Author : Muskan
"""

def customer_booking_info(unique_id=20000):
    form_of_id = input("Enter your form_ofid")
    id_number = input("Enter your ID number")
    passenger_name = input("Enter your name")


    ticket_id = unique_id + 1
    unique_id + ticket_id


    print(f"\nprinting booking information:")
    print(f"form_of_id :{form_of_id}")
    print(f"id_number : {id_number}")
    print(f"passenger_name :{passenger_name}")
    print(f"ticket_id :{ticket_id}")


    return unique_id


unique_id = 20000
customer_booking_info = customer_booking_info(unique_id)


def ferry_servicetotal():
    service_list = []  #it is alist that stores value. 
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

            

def ticket_approval(total_value,id_number,ticket_id):
    
    if total_value > 0:
        status = "Approved"
        Reference_Number  = id_number,ticket_id 


    else:
        status = "Pending"

    print(f"Requisition Approval:")
    print(f"Total:${total_value:.2f}")
    print(f"Status: {Status}")
    print(f"Approval Reference Number :{Reference_Number}")

    return status, Reference_Number


def display_requisitions(form_of_id,ticket_id,passenger_name,total_value,status,reference_number):


    print(f"\nprinting Requisition:")
    print(f"form_of_id:{form_of_id}")
    print(f"ticket_id: {ticket_id}")
    print(f"passenger_name : {passenger_name}")
    print(f"total_value: {total_value:.2f}")
    print(f"status: {status}")
    print(f"Approval Reference Number:{reference_number}")



def main():
    unique_ticket = 20000
    form_of_id,ticket_id,passenger_name,unique_id = customer_booking_info(unique_id)
    print(f"\nRequisition Items(type'finish' to end):")
    total_value = requisition_total()
    status,Reference_Number = requisition_approval(total_value,form_of_id,ticket_id)
    display_requisitions(form_of_id,ticket_id,passenger_name,total_value,status,reference_number)


main()
    









    










