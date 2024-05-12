"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Contact:
    number_of_contacts = 0
    def __inti__(self, name, phone_number, email):
        self.name = name 
        self.phone_number = phone_number
        self.email = email
    

# Create at least two instances of the Contact class with different data.
contact1 = Contact("rocco", "0412345678", "rocco@realemail.com")
contact1 = Contact("Michael-Jackson", "0412345678", "Michael-Jackson@realemail.com")

# Write code that prints out the details of each contact you have created.



