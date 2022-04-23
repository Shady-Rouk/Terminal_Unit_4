class Seller:
    """Seller is a class that represents an instance of an EzWheels seller user.

    Seller objects are created on successful sign in or sign up attempts with states:
    -firstname
    -lastname
    -email
    -phone
    -password_hash
    -cars

    Attributes:
        first_name: A string that represents the first name of a seller.
        last_name: A string that represents the last name of a seller.
        email: A string that represents the email address of a seller.
        phone: A string that represents the phone number of a seller.
        password_hash: A Binary coded representation of a seller's account password.
        cars: A list of car id's that have been listed by a seller.
    """
    def __init__(self, first_name, last_name, email, phone, password_hash, cars=[]):
        """Constructor for a Seller object. Creates an instance of a seller.

        Args:
            first_name (str): The first name of the seller.
            last_name (str): The last name of the seller.
            email (str): The email address of the seller.
            phone (str): The phone number of the seller.
            password_hash (Binary): The hashed form of a seller's account password.
            cars (list): The list of car id's listed by a seller.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password_hash = password_hash
        self.cars = cars

    @classmethod
    def from_document(cls, document):
        """Creates a Seller object instance from values in a dictionary.

        Args:
            document (dict): The key-value pairs to be used to create a Seller object instance.
        Returns:
            Seller: A Seller object instance constructed with the values from document.
        """
        f_name = document['first_name']
        l_name = document['last_name']
        email = document['email']
        phone = document['phone']
        password_hash = document['password_hash']
        cars = document['cars']
        return Seller(f_name, l_name, email, phone, password_hash, cars)

    def to_document(self):
        """Converts a Seller object instance to JSON format.

        Returns:
            dict: A document representation of the Seller object instance.
        """
        f_name = self.first_name
        l_name = self.last_name
        email = self.email
        phone = self.phone
        password_hash = self.password_hash
        cars = self.cars
        return {'first_name':f_name, 'last_name': l_name, 'email': email, 'phone': phone, 'password_hash': password_hash, 'cars': cars}

    def add_car(self, car_id):
        """Adds a car object id to the cars attribute for an instance of a Seller object.

        Args:
            car_id (str): The id of a car object that makes its identification possible.
        """
        self.cars.append(car_id)