class Car:
    def __init__(self, make, model, year, color, price, phone, email, picture, sold=False, verified = False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.phone = phone
        self.email = email
        self.picture = picture
        self.sold = sold
        self.verified = verified
        
    @classmethod
    def from_form(cls, form):
        """Creates a Car object instance from values in a dictionary.
        Args:
            form (dict): The key-value pairs to be used to create the Car object.
        Errors:
            Raises ValueError if document is None.
            Raises TypeError is name isnt all alphabetic
            Raises TypeError if the datatypes are not strings
            Raises ValueError if phone number is not within range
        Returns:
            Car: A Car object instance built with the values from document.
        """
        if form == None:
            raise ValueError("Form data must be provided")
        if type(form['phone']) != str or type(form['email']) != str or type(form['picture']) != str or type(form['make']) != str or type(form['model']) != str or type(form['price']) != str or type(form['year']) != str or type(form['color']) != str: 
            raise TypeError("Invalid format")
        if not(form['price'].isnumeric()):
            raise ValueError("Price not the right format")
        if not(form['year'].isnumeric()):
            raise ValueError("Year not the right format")
        elif int(form['phone']) > 10000000000 or int(form['phone']) <= 999999999:
            raise ValueError("Number not the right format")
        else:
            form['sold'] = False
            return cls(form['make'], form['model'], form['year'], form['color'], form['price'], form['phone'], form['email'], form['picture'])

     
    @classmethod
    def from_document(cls,document):
        """Creates a Car object instance from values in a dictionary.
        Args:
            document (dict): The key-value pairs to be used to create the Car object.
        Errors:
            Raises ValueError if document is None.
        Returns:
            or
            Car: A Car object instance built with the values from document.
        """
        if document == None:
            raise ValueError("Form data must be provided")
        return cls(document['make'], document['model'], document['year'], document['color'], document['price'], document['phone'], document['email'], document['picture'], document['sold'], document['verified'])

    def to_document(self):
        """Converts a Car object instance to a dictionary format.
        Returns:
            dict: A document representation of the Car object instance.
        """
        return {'make':self.make, 'model':self.model, 'year':self.year, 'color':self.color, 'price':self.price, 'phone':self.phone, 'email':self.email, 'picture': self.picture, 'sold':self.sold, 'verified': self.verified}


    
