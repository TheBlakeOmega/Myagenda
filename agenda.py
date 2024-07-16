class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

    def __str__(self):
        return "[ " + self.date + ": " + self.title + " (" + self.description + ")]"


class Agenda:
    def __init__(self):
        self.EventDict = dict()

    def add_event(self, title, date, description):
        self.EventDict[title] = Event(title, date, description)      
        print("\n\n")

    def remove_event(self, title):
        if title in self.EventDict.keys():
            del self.EventDict[title]
        else:
            print("Event not found")
        print("\n\n")

    def list_events(self):
        for key in self.EventDict.keys():
            print(self.EventDict[key])
        print("\n\n")


if __name__ == "__main__":
    agenda = Agenda()
    print(
        """
     _____      _ _           _                                _       
    |  __ \    | (_)         (_)     /\                       | |      
    | |__) |__ | |_ _ __ ___  _     /  \   __ _  ___ _ __   __| | __ _ 
    |  ___/ _ \| | | '_ ` _ \| |   / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |
    | |  | (_) | | | | | | | | |  / ____ \ (_| |  __/ | | | (_| | (_| |
    |_|   \___/|_|_|_| |_| |_|_| /_/    \_\__, |\___|_| |_|\__,_|\__,_|
                                          __/ |                       
                                         |___/                        
    
    Welcome to the Polimi Agenda Application!
    """
    )
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. List Events")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter your title: ")
            date = input("Enter your date: ")
            description = input("Enter your description: ")
            agenda.add_event(title,date,description)
        elif choice == "2":
            title = input("Enter your title to delete: ")
            agenda.remove_event(title)
        elif choice == "3":
            agenda.list_events()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
