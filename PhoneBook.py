class ContactInfo (object):
    # constructor
    def __init__ (self, street = '', city = '', state = '', zip = '', country = '', phone = '', email = ''):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.phone = phone
        self.email = email


    # string representation of Contact Info
    def __str__ (self):
        return ('Address: ' + str(self.street) + '; City: ' + str(self.city) + '; State: ' + str(self.state) + '; Zip Code: ' +
                str(self.zip) + '; Country: ' + str(self.country) + '; Phone: ' + str(self.phone) + '; Email: ' + str(self.email))

# Define global dictionary to hold all the contact information
phone_book = {}

# This function takes the input name as a paramenter and checks if it already
# exists in the phone book, returning either True or False
def name_exists(input_name):
    if input_name in phone_book:
        return True
    else:
        return False

# This function adds the contact information of a new person in the
# dictionary
def add_person():
    # Prompt the user to enter the name of the new person
    name = input('Enter name: ')

    # Check if name exists in phone book. If it does print a message
    # to that effect and return
    if name_exists == True:
        print('This name already exists in the phone book.')
        print()
        return

    # Prompt the user to enter the required contact information
    street = input('Enter street: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    zip = input('Enter zip: ')
    country = input('Enter country: ')
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')

    # Create the ContactInfo object
    contactObj = ContactInfo (street, city, state, zip, country, phone, email)

    # Add the name and the contact information to the phone dictionary
    phone_book[name] = contactObj

    # Print message that the information was added successfully
    print('The entry has been succesfully added.')
    print()

# This function deletes an existing person from the phone dictionary
def delete_person():
    # Prompt the user to enter the name of the person
    name = input("Enter name: ")

    # If the name exists in phone book delete it.
    # Print message as to the action.
    if name_exists(name) == True:
        phone_book.pop(name)
        print(name + 'was deleted from the phone book.')
        print()
        return

    else:
        print(name + 'does not exist in the phone book.')
        print()
        return

# This function updates the information of an existing person
def update_person():
    # Prompt the user to enter the name of the person
    name = input('Enter name: ')

    # Check if name exists in phone book. If it does prompt
    # the user to enter the required information.
    if name_exists(name) == False:
        print(name + ' does not exist in the phone book.')
        print()
        return

    street = input('Enter street: ')

    if street != '':
        phone_book[name].street = street

    city = input('Enter city: ')

    if city != '':
        phone_book[name].city = city

    state = input('Enter state: ')

    if state != '':
        phone_book[name].state = state

    zip = input('Enter zip: ')

    if zip != '':
        phone_book[name].zip = zip

    country = input('Enter country: ')

    if country != '':
        phone_book[name].country = country

    phone = input('Enter phone number: ')

    if phone != '':
        phone_book[name].phone = phone

    email = input('Enter emaiL address: ')

    if email != '':
        phone_book[name].email = email


# This function prints the contact information of an existing person
def search_person():
    # Prompt the user to enter the name of the person
    name = input('Enter name: ')

    # Check if name exists in phone book. If it does print the
    # information in a neat format.
    if name_exists(name) == True:
        print('Name: ' + name + phone_book(name))
        print()
        return

    # If the name does not exist print a message to that effect.
    else:
        print(name + ' does not exist in the phone book')
        print()
        return

# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
    # Open file for writing
    file = open("./phone.txt", "w")

    # Iterate through the dictionary and write out the items in the file
    for name in phone_book:
        file.write(name)
        file.write(phone_book[name].street)
        file.write(phone_book[name].city)
        file.write(phone_book[name].state)
        file.write(phone_book[name].zip)
        file.write(phone_book[name].country)
        file.write(phone_book[name].phone)
        file.write(phone_book[name].email)
        file.write('\n')

    # Close file
    file.close()
    # Print  message

# This function prints the menu, prompts the user for his/her selection
# and returns it.
def menu():
    print('\n1. Add a Person')
    print('\n2. Delete a Person')
    print('\n3. Search for a Person')
    print('\n4. Update Information on a Person')
    print('\n5. Quit\n')

    selection = int(input('Enter your selection: '))
    print()
    return selection

# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
    # Open file for reading
    in_file = open ("./phone.txt", "r")

    # Read first line (name)
    line = in_file.readline()
    line = line.strip()

    # Loop through the entries for each person
    while (line != ""):
        # Remove the space between first and last name
        name = line

        # Read street
        line = in_file.readline()
        line = line.strip()
        street = line

        # Read city
        line = in_file.readline()
        line = line.strip()
        city = line

        # Read state
        line = in_file.readline()
        line = line.strip()
        state = line

        # Read zip
        line = in_file.readline()
        line = line.strip()
        zip = line

        # Read country
        line = in_file.readline()
        line = line.strip()
        country = line

        # Read phone number
        line = in_file.readline()
        line = line.strip()
        phone = line

        # Read e-mail address
        line = in_file.readline()
        line = line.strip()
        email = line

        # Read blank line
        line = in_file.readline()
        line = line.strip()
        street = line

        # Read first line of the next block of data
        line = in_file.readline()
        line = line.strip()

        # Create ContactInfo object
        original_contact = ContactInfo(street, city, state, zip, country, phone, email)

        # Add to phone dictionary
        phone_book[name] = original_contact

    # Close file
    in_file.close()


def main():

    # Read file and create phone book dictionary
    create_phone_book()

    while True:
        # Print logo
        print "Phone Book"

        # Print menu and get selection
        selection = menu()

        # Process request, print menu and prompt again and again
        # until the user types 5 to quit.
        if selection == 1:
            add_person()

        elif selection == 2:
            delete_person()

        elif selection == 3:
            search_person()

        elif selection == 4:
            update_person()

        elif selection == 5:
            # Save and quit
            save_quit()

            # Goodbye message
            print
            print "Thank you for using the Phone Book.\n"
            break

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
