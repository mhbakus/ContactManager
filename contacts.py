#creating a class called Contacts
class Contact():
    def __init__(self, name, phone, email, website, birthday, linkedin):
        self.name = name
        self.phone = phone
        self.email = email
        self.website = website
        self.birthday = birthday
        self.linkedin = linkedin

    def get_contact(self):
        '''return all the details of a given contact '''
        print('''
               Name : {}\n
               Phone : {}\n
               Email : {}\n
               Website : {}\n
               Birthday : {}\n
               Linkedin : {}'''.format(self.name,
               self.phone,
               self.email,
               self.website,
               self.birthday,
               self.linkedin ))

class ContactBook:
    def __init__(self, contacts = []):
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.get_contact()
        return none
  
    def del_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return 'contact deleted with success'
        return 'the contact didnt exist'
    

mycontacts = ContactBook()

def adding():
    print("NEW CONTACT REGISTRATION\n")
    name = input("Name : ")
    tel = input("Phone : ")
    email = input("Email : ")
    website = input("Website : ")
    birthday = input("Birthday : ")
    linkedin = input("Linkedin : ")
    mycontacts.add_contact(Contact(name,
                                   tel,
                                   email,
                                   website,
                                   birthday,
                                   linkedin))
    print('contact added successfull')
      

exit = False
while not exit:
    answer = input("please type 'add' to add a new contact, 'del' to delete a contact, 'search' to seach a contact or 'quit' to leave the program : \n")
    if answer.lower() == 'add':
        adding()
    elif answer.lower() == 'del':
        contact_name = input('enter the name of contact to delete : ')
        mycontacts.del_contact(contact_name)
    elif answer.lower() == 'search':
        contact_name = input('enter the name of contact : ')
        mycontacts.search_contact(contact_name)
    elif answer.lower() == 'quit':
        print('Bye Bye!')
        exit = True
    else:
        exit = False


  
# print("NEW CONTACT REGISTRATION\n")
# name = input("Name : ")
# tel = input("Phone : ")
# email = input("Email : ")
# website = input("Website : ")
# birthday = input("Birthday : ")
# linkedin = input("Linkedin : ")
# jean = Contacts(name,
#                 tel,
#                 email,
#                 website,
#                 birthday,
#                 linkedin)
# ajout = True
# mycontacts = []
# mycontacts.append(jean)

    		




#jean.get_contact()
