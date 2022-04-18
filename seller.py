class Seller:
    def __init__(self, first_name, last_name, email, phone, password_hash, cars={}):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password_hash = password_hash
        self.cars = cars

    @classmethod
    def from_document(cls, document):
        f_name = document['first_name']
        l_name = document['last_name']
        email = document['email']
        phone = document['phone']
        password_hash = document['password_hash']
        cars = document['cars']
        return Seller(f_name, l_name, email, phone, password_hash, cars)

    def to_document(self):
        f_name = self.first_name
        l_name = self.last_name
        email = self.email
        phone = self.phone
        password_hash = self.password_hash
        cars = self.cars
        return {'first_name':f_name, 'last_name': l_name, 'email': email, 'phone': phone, 'password_hash': password_hash, 'cars': cars}

    def add_car(self, car):
        pass