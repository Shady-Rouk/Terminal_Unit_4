class Seller:
    def __init__(self, firstname, lastname, email, phone, picture, sold=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.picture = picture
        self.sold = sold
    def set_sale_status(self, sale_status):
        pass
        
    @classmethod
    def from_form(cls, form):
        """Creates a Seller object instance from values in a dictionary.
        Args:
            form (dict): The key-value pairs to be used to create the Seller object.
        Errors:
            Raises ValueError if document is None.
            Raises TypeError is name isnt all alphabetic
            Raises TypeError if the datatypes are not strings
            Raises ValueError if phone number is not within range
        Returns:
            Seller: A Seller object instance built with the values from document.
        """
        if form == None:
            raise ValueError("Form data must be provided")
        if not(all(letter.isalpha() or letter.isspace() for letter in form['firstname'])):
            raise TypeError("Name not the right format")
        if not(all(letter.isalpha() or letter.isspace() for letter in form['lastname'])):
            raise TypeError("Name not the right format")
        if type(form['phone']) != str or type(form['email']) != str or type(form['picture']) != str: 
            raise TypeError("Invalid format")
        elif int(form['phone']) > 10000000000 or int(form['phone']) <= 999999999:
            raise ValueError("Number not the right format")
        else:
            form['sold'] = False
            return cls(form['firstname'], form['lastname'], form['phone'], form['email'], form['picture'], form['sold'])

     
    @classmethod
    def from_document(cls,document):
        """Creates a Seller object instance from values in a dictionary.
        Args:
            document (dict): The key-value pairs to be used to create the GeneralReview object.
        Errors:
            Raises ValueError if document is None.
        Returns:
            or
            Seller: A Seller object instance built with the values from document.
        """
        if document == None:
            raise ValueError("Form data must be provided")
        return cls(document['firstname'], document['lastname'], document['phone'], document['email'], document['picture'], document['sold'])

    def to_document(self):
        """Converts a GeneralReview object instance to a dictionary format.
        Returns:
            dict: A document representation of the GeneralReview object instance.
        """
        return {'firstame':self.firstname, 'lastname':self.lastname, 'phone':self.phone, 'email':self.email, 'picture': self.picture, 'sold':self.sold}


    
