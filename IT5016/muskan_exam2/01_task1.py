"""
collecting user data
Author: Muskan
"""

def customer_booking_info(unique_id=20000):
    form_of_id= input("Enter your form_of_id")
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







