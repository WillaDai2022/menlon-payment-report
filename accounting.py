melon_cost = 1.00
def print_payment_info(customer_info):
    """Calculate cost of melon and decide which customers are underpaid""" 

    info_file = open(customer_info)  #open the file with the info

    #iterater over the file
    for line in info_file:
        #split each line with "|" to get a list of string
        info_list = line.split("|")
        #get customer's full name
        full_name = info_list[1]
        #get customer's first name
        first_name = full_name.split(" ")[0]
        #get the quantity of menlon
        menlon_quantity = float(info_list[2])
        #calculate the expected payment
        customer_expected = melon_cost* menlon_quantity
        #get the actual payment
        customer_paid = float(info_list[3])

        #print geneal infomation
        if customer_expected != customer_paid:
            print(f"{first_name} paid ${customer_paid:.2f},",
                f"expected ${customer_expected:.2f}"
                )

        #print customer payment status
        if customer_expected < customer_paid:
            print(f"{first_name} is overpaid")
        if customer_expected > customer_paid:
            print(f"{first_name} is underpaid")

    info_file.close()

print_payment_info("customer-orders.txt")
