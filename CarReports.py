
class CarReports:
    '''
    CarReports is a class that represents the instance of a Report for a Seller's car. 

    CarReports objects can be generated and each instance has 6 instances:

    - car_id
    - details
    - features
    - verified
    - unverified_details
    - date

    Attributes:

    car_id: a string that represents the id of a specific car for sale in the collection/datbase.
    details: a dictionary that contains general characteristics about the car (for example year, make, model, color) as keys,
    and booleans as values - True if the characteristic is verified and False if the characteristic isn't.  
    features: a string that represents additional features of the car for sale in the collection/database.
    verified: a boolean that has a default value of False but is changed to True if all the values in details are True
    unverified_details: a list that represents the general characteristics of the car (in details) for sale in the database that were not verified.
    date: a string that represents the date that the report was made/conducted.

    '''

    def __init__(self, car_id, details, features, date, verified=False, unverified_details = []):
        '''
        Constructor for a CarReports object. Creates an instance of a report for a car for sale.

        Args:
            car_id (string): represents the unique id of the car for sale in the collection/ database 
            details (dictionary): represents core characteristics of the car for sale (strings) as keys and whether or not the core
            characteristic is verified (booleans) as values. 
            features (string): represents the additional features of the car for sale that are not part of the core characteristics. 
            each feature is seperated by a comma or some delimiter.
            date (string): represents the date that the report of the car was created 
            verified (boolean): a boolean that represents whether or not the car is overall verified (all of the core characteristics are true in details)
            unverified_details (list): represents a list of the unverified core characteristics of the car. 

        Returns:
            no return (void)
        '''

        if type(car_id) != str:
            raise TypeError("car_id must be of type string")
        if type(details) != dict:
            raise TypeError("details must be a dictionary")
        if type(features) != list:
            raise TypeError("features must be of type string")
        if type(date) != str:
            raise TypeError("date must be of type string")
        if type(verified) != bool:
            raise TypeError("verified must be type bool")
        if type(unverified_details) != list:
            raise TypeError("unverified_details should be a list")


        self.car_id = car_id
        self.details = details 
        self.features = features
        self.verified = verified
        self.unverified_details = unverified_details
        self.date = date

    def isDetailsVerified(self):

        '''
        Checks to see if all the core characteristics of the car for sale have a True value in the attribute details. 
        
        Args:
            None

        Returns:
            a boolean value that represents whether or not all the core characteristics are verified. 
        '''

        is_verified = True
        for value in self.details.values():
            if value == False:
                is_verified = False
        self.verified = is_verified
        return is_verified


    def getUnverified(self):

        '''
        Gets the unverified core characteristics of the car for sale. 

        Args:
            None

        Returns:
            A list of all the core characteristics of the car for sale that were not verified. 
        '''
        output = []
        for key, value in self.details.items():
            if value == False:
                output.append(key)
        self.unverified_details = output
        return output


    def to_document(self):

        '''
        Converts a CarReports object instance to a dictionary format

        Returns:
            dictionary:  a document representation of the CarReports object instance

        '''
        return {'car_id': self.car_id, 
        'is_verified': self.verified, 
        'details': self.details, 
        'unverified_details': self.unverified_details, 
        'features': self.features,
        'date': self.date}

    @classmethod
    def from_document(cls, document):

        '''
        Creates a CarReports object instance from values in a dictionary.

        Args:
            document (dicitonary): The key-value pairs to be used to create the CarReports object.

        Returns:
            CarReports: A CarReports object instance built with the values from document
        '''
        keys = []
        for key in document.keys():
            if type(key) == str and key.isalpha():
                keys.append(key.lower())
            else:
                keys.append(key)

        if 'car_id' not in keys:
            raise KeyError("The key 'car_id' does not exist in the document")
        if 'details' not in keys:
            raise KeyError("The key 'details' does not exist in the document")
        if 'features' not in keys:
            raise KeyError("The key 'features' does not exist in the document")
        if 'date' not in keys:
            raise KeyError("The key 'date' does not exist in the document")
        if 'is_verified' not in keys:
            raise KeyError("The key 'is_verified' does not exist in the document")
        if 'unverified_details' not in keys:
            raise KeyError("The key 'unverified_details' does not exist in the document")

        return CarReports(document['car_id'], document['details'], document['features'],  document['date'], document['is_verified'], document['unverified_details'])