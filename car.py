class Seller:
    def __init__(self, first_name, last_name, email, phone, inspect_state, image = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.inspect_state = inspect_state
        self.image = image
    def set_sale_status(self, sale_status):
        
    @classmethod
    def from_document(cls, document):
        f_name = document['first_name']
        l_name = document['last_name']
        email = document['email']
        phone = document['phone']
        inspect_state = document['inspect_state']
        image = document['image']
        return Seller(f_name, l_name, email, phone, inspect_state, image)

    def to_document(self):
        f_name = self.first_name
        l_name = self.last_name
        email = self.email
        phone = self.phone
        inspect_state = self.inspect_state
        image = self.image
        return {'first_name':f_name, 'last_name': l_name, 'email': email, 'phone': phone, 'password_hash': inspect_state, 'cars': image}

    def add_car(self, car):
        pass