"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts


class Contact:
    number_of_contacts = 0
    
    def __init__(self, name, email, phone):
        self.name = name 
        self.phone = phone
        self.email = email
        Contact.number_of_contacts += 1
        
    def check_email(self):
        if "@" in self.email:
            print("good")
            return True
        
        else:
            print("bad")
            return False
        
        
    def __str__(self):
        return (f"{self.name}, {self.email}, {self.phone}")
    
    @classmethod
    def get_contact_count(cls):
        print(Contact.number_of_contacts)
        return Contact.number_of_contacts


contact1 = Contact("rocco", "rocco@realemail.com", "0412345678")
contact2 = Contact("Michael-Jackson", "Michael-Jackson@realemail.com", "0412345678")















