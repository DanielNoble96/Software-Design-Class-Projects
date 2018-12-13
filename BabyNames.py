#  File: BabyNames.py 

#  Description: This program creates a database of the 1000 most popular baby names in the U.S.
#               per decade from 1900 to 2000. It provides the user various options to query the
#               databases and returns the corresponding output

#  Student Name: Daniel A. Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10th September 2018

#  Date Last Modified: 14th September 2018


def name_exists(input_name, names_dictionary):
    # Check for the existence of a name in the dictionary
    if input_name in names_dictionary:
        return True
    else:
        return False

def highest_rank_decade(input_name, names_dictionary):
    # Check which decade had the highest rank for a given name
    decade_list = names_dictionary[input_name]
    max_index = decade_list.index(min(decade_list))
    decade = max_index * 10 + 1900
    return decade

def all_rankings(input_name, names_dictionary):
    # Return all rankings across decades for a given name
    return names_dictionary[input_name]

def one_decade_only(input_decade, names_dictionary):
    # Return lists of all names and their rank that appear in only one decade
    names_list = []
    ranks_list = []
    
    index = (input_decade - 1900) // 10
    # For each key, increment counter when a rank appears
    for name in names_dictionary:
        counter = 0
        for rank in names_dictionary[name]:
            if rank != 1000:
                counter += 1
        # Add name to list if it appeared only once and in the correct decade
        if (names_dictionary[name][index] != 1000) and (counter == 1):
            names_list.append(name)
            ranks_list.append(names_dictionary[name][index])                            
    return names_list, ranks_list

def all_decades(names_dictionary):
    # Return a list of all names that appear in all decades
    names_list = []
    for name in names_dictionary:
        counter = 0
        for rank in names_dictionary[name]:
            # Increment counter for every decade that the name is ranked
            if rank != 1000:
                counter += 1
        # Add name to list if ranked in all decades
        if counter == 11:
            names_list.append(name)           
    return names_list

def more_popular(names_dictionary):
    # Return a list of all names that were more popular in every decade
    names_list =[]
    for name in names_dictionary:
        false_counter = 0
        for index in range(1, len(names_dictionary[name])):
            # Count number of times that name was not more popular in subsequent decade
            if (names_dictionary[name][index] >= names_dictionary[name][index - 1]):
                false_counter += 1
        # Add name to list if it was always more popular in subsequent decades
        if false_counter == 0:
            names_list.append(name)
                       
    return names_list

def less_popular(names_dictionary):
    # Return a list of all names that were less popular in every decade
    names_list = []
    for name in names_dictionary:
        false_counter = 0
        for index in range(1, len(names_dictionary[name])):
            # Count number of times that name was not less popular in subsequent decade
            if (names_dictionary[name][index] <= names_dictionary[name][index - 1]):
                false_counter += 1
        # Add name to list if it was always less popular in subsequent decades
        if false_counter == 0:
            names_list.append(name)

    return names_list

    
def main():
    # Open the file for reading
    file_name = open("names.txt", "r")

    # Create dictionary 
    names_dictionary = {}
    
    try:
        for line in file_name:
            # Separate file entries where a space appears for each line where
            # name is the key and ranks are the values to be put into a list
            (name, rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9, rank10, rank11) = line.split(' ')
            ranks = [rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9, rank10, rank11]

            for i in range(len(ranks)):
                ranks[i] = int(ranks[i])
                #replace 0's with 1000's to aid future algorithms
                if ranks[i] == 0:
                    ranks[i] = 1000

            # Populate the dictionary
            names_dictionary[name] = ranks

    except:
        for line in file_name:
            # Encode values 
            line = str (line, encoding = 'utf8')
            # Separate file entries where a space appears for each line where
            # name is the key and ranks are the values to be put into a list
            (name, rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9, rank10, rank11) = line.split(' ')
            ranks = [rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9, rank10, rank11]

            for i in range(len(ranks)):
                ranks[i] = int(ranks[i])
                #replace 0's with 1000's to aid future algorithms
                if ranks[i] == 0:
                    ranks[i] = 1000

            # Populate the dictionary
            names_dictionary[name] = ranks

    finally:
        # Close file
        file_name.close()
        
                         
    while True:
        print('Options.')
        print('Enter 1 to search name.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.\n')

        input_value = int(input('Enter choice: '))

        # Option 1: check for existence of name in dictionary
        if input_value == 1:
            input_name = input('Enter name: ')
            if name_exists(input_name, names_dictionary) is True:
                print('The matches with their highest ranking decade are: ')
                decade = highest_rank_decade(input_name, names_dictionary)
                print(input_name, decade, '\n')
            else:
                print(input_name, 'does not appear in any decade.\n')

        # Option 2: display data for one name
        elif input_value == 2:
            input_name = input('Enter name: ')
            if name_exists(input_name, names_dictionary) is True:
                # get a list of the rankings
                values = all_rankings(input_name, names_dictionary)
                # replace 1000s with 0s for the purpose of the output
                for i in range(len(values)):
                    if values[i] == 1000:
                        values[i] = 0
                    values[i] = str(values[i])

                # Print all name's rankings as a string
                strng_values = ' '.join(values)
                print(input_name + ': ' + strng_values)

                # Print ranking with each corresponding decade
                decade = 1900                   
                for i in range(len(values)):
                    print(str(decade) + ': ' + str(values[i]))
                    decade += 10
                print()
            else:
                print(input_name, 'does not appear in any decade.\n')

        # Option 3: display all names that appear in only one decade
        elif input_value == 3:
            input_decade = int(input('Enter decade: '))
            if (input_decade % 10 == 0) and (1900 <= input_decade <= 2000):
                names_list, ranks_list = one_decade_only(input_decade, names_dictionary)
                print('The names are alphabetical order')
                for i in range(len(names_list)):
                    print((str(names_list[i]) + ': ').ljust(15) + format(str(ranks_list[i])))
                print()
            else:
                print(input_decade, 'is not a valid decade.\n')
                
        # Option 4: display all names that appear in all decades
        elif input_value == 4:
            names_list = all_decades(names_dictionary)
            counter = 0
            for i in range(len(names_list)):
                counter+= 1
            print(str(counter) + ' names appear in every decade. The names are: ')
            for i in range(len(names_list)):
                print(names_list[i])
            print()
           
        # Option 5: display all names that are more popular in every decade        
        elif input_value == 5:
            names_list = more_popular(names_dictionary)
            name_counter = 0
            for i in range(len(names_list)):
                name_counter += 1
            print(str(name_counter) + ' names are more popular in every decade.')
            for i in range(len(names_list)):
                print(names_list[i])
            print()

        # Option 6: display all names that are less popular in every decade
        elif input_value == 6:
            names_list = less_popular(names_dictionary)
            name_counter = 0
            for i in range(len(names_list)):
                name_counter += 1
            print(str(name_counter) + ' names are less popular in every decade.')
            for i in range(len(names_list)):
                print(names_list[i])
            print()

        # Option 7: quit if 7 or any other value is input
        else:
            print('\n\nGoodbye.')
            break
    

if __name__ == "__main__":
    main()
