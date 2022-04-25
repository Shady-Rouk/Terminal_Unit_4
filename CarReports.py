
class CarReports:

    def __init__(self, car_id, details, features, date, verified=False, unverified_details = []):

        self.car_id = car_id
        self.details = details 
        self.features = features
        self.verified = verified
        self.unverified_details = unverified_details
        self.date = date

    def isDetailsVerified(self):
        is_verified = True
        for value in self.details.values():
            if value == False:
                is_verified = False
        self.verified = is_verified
        return is_verified

    def getUnverified(self):
        output = []
        for key, value in self.details.items():
            if value == False:
                output.append(key)
        self.unverified_details = output
        return output

        
    # do splitting outside of class
    # def updateFeatures(self):

    #     if type(self.features) == str:
    #         features = self.features.split(',')
    #         self.features = features
    #         return
    # def getUnverifiedFeatures(self):
    #     output = []
    #     for item in self.features:
    #         if self.features[item] == False:
    #             output.append(item)
    #     return output

    # def getVerifiedFeatures(self):
    #     output = []
    #     for item in self.features:
    #         if self.features[item] == True:
    #             output.append(item)
    #     return output

    def to_document(self):
        return {'car_id': self.car_id, 
        'is_verified': self.verified, 
        'details': self.details, 
        'unverified_details': self.unverified_details, 
        'features': self.features,
        'date': self.date}

    @classmethod
    def from_document(cls, document):
        keys = []
        for key in document.keys():
            if type(key) == str and key.isalpha():
                keys.append(key.lower())
            else:
                keys.append(key)

        return CarReports(document['car_id'], document['details'], document['features'],  document['date'], document['is_verified'], document['unverified_details'])