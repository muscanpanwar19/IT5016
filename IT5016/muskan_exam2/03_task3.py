"""
Requisition Approval Decision Based On Conditions
Author : Muskan
"""


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


id_number = input("Enter ID Number:")
ticket_id = input(f"Enter Ticket ID:")
total_value = float(input("Enter Total:"))
requisition_approval(total_value, id_number,ticket_id)



