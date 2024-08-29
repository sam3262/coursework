#Questions for users, getting inputs
last_name = input("What is your last name? : ")
first_name = input("What is your first name? : ")
street_num = input("What is your street number? : ")
street_name = input("What is your street name? : ")
apartment_box = input("What is your apartment or PO Box number (if applicable)? : ")
user_city = input("What City do you live in? : ")
user_state = input("What State do you live in? (abbreviation) : ")
user_zip = input("What is your Zip Code? (5 digits) : ")

#the tuple filled with all things needed of address
the_address = last_name, first_name, street_num, street_name, apartment_box, user_city, user_state, user_zip 


#if there is input for PO Box/ Apartment Number
if apartment_box:

    #first two lines of the address
    print(f"{the_address[0].title()}, {the_address[1].title()} \n{the_address[2]} {the_address[3].title()}")
    #Last two lines of the addresss
    print(f"{the_address[4].upper()} \n{the_address[5].title()}, {the_address[6].upper()} {the_address[7]}")
else : 
    #Same address without the PO Box to print
    print(f"{the_address[0].title()}, {the_address[1].title()} \n{the_address[2]} {the_address[3].title()}")
    print(f"{the_address[5].title()}, {the_address[6].upper()} {the_address[7]}")  




