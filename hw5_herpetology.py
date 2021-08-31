"""
This program allows the user to look for data from SSAR.
The data for this assigment has been taken from Society for the Study of Amphibians and Reptiles (SSAR) ssarherps.org
@Shweta Chaurasia
"""


def csvToDictOfLists(filename):
    """
    Accepts a filename as paramter and returns a dictionary of lists
    First element is the key and the rest of comma separated values are linked to the key
    Header of the file is ignored
    """
    with open (filename) as file_read_list:
        list_csv = []
        for row in file_read_list:
            temp_row = row.strip().split(",")
            key = temp_row.pop(0)
            i = [key, temp_row]
            list_csv.append(i)
        list_csv.pop(0)
        dict_csv = dict(list_csv)
        return(dict_csv)

def filterKeys(dict1, input_str):
    """
    Accepts a dictionary and a string
    Returns a list of keys for all string matches
    """
    input_str = input_str.lower()                         #convert into lowercase
    filter_list = []
    for i in dict1.items():
        if input_str in i[0].lower():
            filter_list.append(i[0])
        else:
            for val in i[1]:
                if input_str in val.lower():
                    filter_list.append(i[0])
    return(filter_list)
        
def columnToSet(dict1, col_idx):
    """
    Accepts a dictionary and a column index
    Returns a set with all values from that column index
    """
    col_idx_set = set()
    for i in dict1.values():
        col_val = i[col_idx]
        col_idx_set.add(col_val)
    return(col_idx_set)

def filterByColumn(dict1, col_idx, input_str):
    """
    Accepts a dictionary, a column index and a string value
    Returns a list of keys which matches the string value in the given column index elements
    """
    input_str = input_str.lower()                         #convert into lowercase
    filter_key_list = []
    for i in dict1.items():
        new_i_val = (i[1][col_idx]).lower()
        if input_str in new_i_val:     #checks if input string is in values in dictionary for the input column index
            filter_key_list.append(i[0])
    return(filter_key_list)

def singleMatch(dict1, find_list):
    """
    Accepts a dictionary and a key value
    Prints the attributes of that key from the dictinary
    """
    find_list = find_list[0]
    com_name = dict1[find_list][0]
    species = dict1[find_list][1]
    subspecies = dict1[find_list][2]
    major_type = dict1[find_list][3]
    print("\nCommon Name: ", find_list,"\nGenus: ", com_name, "\nSpecies: ", species, "\nSubspecies: ", subspecies, "\nMajor Common Type: ", major_type,"\n")
            
def main():
    """
    Main body of your code below.
    """
    dict_list = csvToDictOfLists("ssar-common-names-2021.csv")  #importing the file to a local dictionary

    print("Welcome to the society for the study of Amphibians and Reptiles Database")
    
    flag = ('Y' or 'y')     #flag is to check if the user wants to continue. It is Y by default when the program starts
   
    while flag == 'Y' or flag == 'y':
        inp1 = input("Enter 0 for Genus, 1 for Species, 2 for Subspecies, 3 for Types, or a name: ") 
  
        try:                  #to execute if the input value is a number
            inp1 = int(inp1)
            if inp1 not in [0,1,2,3]:
                print("No animals exist for the entered value")
            else:
                inp_col_set = columnToSet(dict_list, inp1)
            
                print ("Here are your options (duplicates removed):",inp_col_set,"\n:: ")
                inp_str = input()                  #stores the input string into this variable
                find_list = filterByColumn(dict_list, inp1, inp_str)   #returns the key matches

                if len(find_list) == 0:          #if there is no match, print the following message
                    print("No animals exist for the entered value")
                
                elif (find_list) == 1:
                    singleMatch(dict_list,find_list)  #if there is only one match, print the attributes of the match calling this function

                else:                                 #if there are more than one matches, print the list of key values
                    for i in find_list:             
                        print (i)
                
            flag = input("\nWould you like to continue? (Y/N): ")
        
        except:                                          #to execute if the users enters a string, 
            find_list = filterKeys(dict_list, inp1)
            
            if len(find_list) == 0:                     #if there is no match, print the following message
                print("No animals exist for the entered value")
            
            elif len(find_list) == 1:                   #if there is only one match, print the attributes of the match calling this function
                singleMatch(dict_list,find_list)
               
            else:                                       #if there are more than one matches, print the list of key values
                for item in find_list:
                    print (item)
            
            flag = input("\nWould you like to continue? (Y/N): ")

    print("Have a nice day!")
    


if __name__ == "__main__":
    main()
