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
        return 'the contact didnt exist'
  
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
    answer = input('''
       __  __ _____ _   _ _   _ 
      |  \/  | ____| \ | | | | |
      | |\/| |  _| |  \| | | | |
      | |  | | |___| |\  | |_| |
      |_|  |_|_____|_| \_|\___/ 
      \n\n\n         
      1 .  add a new contact\n
      2 .  delete a contact \n
      3 .  seach a contact \n
      4 .  leave the program : \n\n
      ''')
    if answer.lower() == '1':
        adding()
    elif answer.lower() == '2':
        contact_name = input('enter the name of contact to delete : ')
        mycontacts.del_contact(contact_name)
    elif answer.lower() == '3':
        contact_name = input('enter the name of contact : ')
        print(mycontacts.search_contact(contact_name))
    elif answer.lower() == '4':
        print('Bye Bye!')
        exit = True
    else:
        exit = False

