from abc import ABC, abstractmethod

# Abstract Base Class representing a general Library Item
class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self._item_id = item_id
        self._title = title
        self._author = author
        self._is_issued = False

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def is_issued(self):
        return self._is_issued

    def issue_item(self):
        if not self._is_issued:
            self._is_issued = True
            print(f"Success: '{self._title}' has been issued.")
        else:
            print(f"Error: '{self._title}' is already issued.")

    def return_item(self):
        if self._is_issued:
            self._is_issued = False
            print(f"Success: '{self._title}' has been returned.")
        else:
            print(f"Error: '{self._title}' was not checked out.")

    @abstractmethod
    def display_details(self):
        pass


# Subclass: Book
class Book(LibraryItem):
    def __init__(self, item_id, title, author, isbn, pages):
        super().__init__(item_id, title, author)
        self.isbn = isbn
        self.pages = pages

    def display_details(self):
        status = "Issued" if self._is_issued else "Available"
        print(f"[Book] ID: {self._item_id} | Title: {self._title} | Author: {self._author} | ISBN: {self.isbn} | Pages: {self.pages} | Status: {status}")


# Subclass: Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue_number, month):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number
        self.month = month

    def display_details(self):
        status = "Issued" if self._is_issued else "Available"
        print(f"[Magazine] ID: {self._item_id} | Title: {self._title} | Publisher/Author: {self._author} | Issue No: {self.issue_number} | Month: {self.month} | Status: {status}")


# Subclass: Journal
class Journal(LibraryItem):
    def __init__(self, item_id, title, author, volume, research_field):
        super().__init__(item_id, title, author)
        self.volume = volume
        self.research_field = research_field

    def display_details(self):
        status = "Issued" if self._is_issued else "Available"
        print(f"[Journal] ID: {self._item_id} | Title: {self._title} | Researcher/Author: {self._author} | Volume: {self.volume} | Field: {self.research_field} | Status: {status}")


# Library System Manager using polymorphism
class LibrarySystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, item: LibraryItem):
        self.inventory.append(item)
        print(f"Added '{item.title}' to library inventory.")

    def show_catalog(self):
        print("\n--- Current Library Catalog ---")
        for item in self.inventory:
            item.display_details()  # Polymorphic call
        print("-" * 40)

    def process_issue(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                item.issue_item()
                return
        print(f"Item ID {item_id} not found in inventory.")

    def process_return(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                item.return_item()
                return
        print(f"Item ID {item_id} not found in inventory.")


# Driver Code / Demonstration
lib = LibrarySystem()

# Creating various library items
b1 = Book("B001", "Data Structures & Algorithms", "Cormen", "978-0131103627", 800)
m1 = Magazine("M001", "National Geographic", "Various", 45, "October")
j1 = Journal("J001", "IEEE Computer Society", "Dr. A. Turing", 12, "Artificial Intelligence")

# Adding items to the library
lib.add_item(b1)
lib.add_item(m1)
lib.add_item(j1)

# Displaying catalog
lib.show_catalog()

# Performing issue operations
print("\n--- Issue Operations ---")
lib.process_issue("B001")
lib.process_issue("B001")  # Trying to issue already issued item

# Performing return operations
print("\n--- Return Operations ---")
lib.process_return("B001")
lib.process_return("B001")  # Trying to return an available item

# Final catalog state
lib.show_catalog()