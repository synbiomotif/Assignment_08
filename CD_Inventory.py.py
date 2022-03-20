#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Songli Zhu, 2022-Mar-18, add codes with classes and objects of OOP
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODONE Add Code to the CD class
    # == Constructor == #
    def __init__(self, intID, strTitle, stArtist):
        self.__id = intID
        self.__title = strTitle
        self.__artist = stArtist
  
    # -- Properities -- #
    @property
    def cd_id(self):
        return self.__id
    
    @property
    def cd_title(self):
        return self.__title

    @property    
    def cd_artist(self):
        return self.__artist


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODONE Add code to process data from a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """save current inventory into the file

        Args:
            file_name (string):  name of file used to save the data from list of CD objects
            lst_Inventory (list): list of CD objects that holds the data during runtime

        Returns:
            None

        """
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            lst = []
            lst.extend([row.cd_id, row.cd_title, row.cd_artist])
            lst[0] = str(lst[0])
            objFile.write(','.join(lst) + '\n')
        objFile.close()
    
    # TODONE Add code to process data to a file
    @staticmethod
    def load_inventory(file_name):
        """load data from file into the list of inventory

        Args:
            file_name: (string): name of file which includes the CD data

        Returns:
            None

        """
        lstOfCDObjects.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            cd_info = CD(data[0], data[1], data[2])
            lstOfCDObjects.append(cd_info)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODONE add docstring
    """Handling Input / Output
    
    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> None
        show_inventory(): -> None
        cd_data(): -> (a CD object)

    """
    # TODONE add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu:\n\n[d] Display Current Inventory\n[a] Add CD\n[s] Save Inventory') 
        print('[l] Load Inventory\n[x] Exit Program\n')
               
    # TODONE add code to captures user's choice   
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices d, a, s, l or x

        """
        choice = ' '
        while choice not in ['d', 'a', 's', 'l', 'x']:
            choice = input('Which operation would you like to perform? [d, a, s, l or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice        

    # TODONE add code to display the current data on screen
    @staticmethod
    def show_inventory(lstOfCDObjects):
        """Displays current inventory table

        Args:
            lstOfCDObjects (list of CD objects): list of CD objects that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstOfCDObjects:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================\n')

    # TODONE add code to get CD data from user
    @staticmethod
    def cd_data():
        """Gets user input for cd information

        Args:
            None.

        Returns:
            cd_info (object): an instance of class CD store cd information from user input 
        """
        flag = 1
        while flag:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                flag = 0
            except:
                print('\nID cannot be a string!\nPlease try again!')
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        cd_info = CD(strID, strTitle, stArtist)
        return cd_info

# -- Main Body of Script -- #
# TODONE Add Code to the main body
# Load data from file into a list of CD objects on script start
try:
    FileIO.load_inventory(strFileName) # it won't work if the file exist and empty causing out of range
except FileNotFoundError:
    print('file does not exist!\n')

# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    # show user current inventory
    if strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        cd = IO.cd_data()
        lstOfCDObjects.append(cd)
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n') # add extra \n 
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user exit program
    elif strChoice == 'x':
        break
    else:
        print("\nSorry, but", strChoice, "isn't a valid choice.")
