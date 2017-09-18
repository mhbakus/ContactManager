class Contacts():
    def __init__(self, name, phone, email, website, birthday, linkedin):
        self.name = name
        self.phone = phone
        self.email = email
        self.website = website
        self.birthday = birthday
        self.linkedin = linkedin

    def get_contact(self):
        print('''
               Name : {}\n
               Phone : {}\n
               Email : {}\n
               Website : {}\n
               Birthday : {}\n
               Linkedin{} : '''.format(self.name,
               self.phone,
               self.email,
               self.website,
               self.birthday,
               self.linkedin ))
print("NEW CONTACT REGISTRATION\n")
name = input("Name : ")
tel = input("Phone : ")
email = input("Email : ")
website = input("Website : ")
birthday = input("Birthday : ")
linkedin = input("Linkedin : ")
jean = Contacts(name,
                tel,
                email,
                website,
                birthday,
                linkedin)
jean.get_contact()
