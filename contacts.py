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
jean = Contacts('jean',
                '+22545785896',
                'jean@mail.fr',
                'www.jean.com',
                '15/08/1990',
                'linkedin.com/in/jean')
jean.get_contact()
