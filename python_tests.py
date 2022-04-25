import unittest

from seller import *
from car import *
from CarReports import *

class Test_Car(unittest.TestCase):
    def setUp(self):
        #self, make, model, year, color, price, email, phone, picture, sold=False, verified = False)
        self.car1 = Car("Toyota", "Corolla", "2020", "Black", "30000", "8192104615", "david300@gmail.com", "https://www.seegertoyota.com/static/dealer-12152/MY20_Corolla_L_tcom_0209_001_DS_Front_7_8.png")
        self.car2 = Car("Toyota", "Corolla", "2020", "Black", "30000", "2428072021", "david@gmail.com", "https://www.seegertoyota.com/static/dealer-12152/MY20_Corolla_L_tcom_0209_001_DS_Front_7_8.png")
        self.car3 = Car("Honda", "Accord", "2018", "Red", "15000", "2428072021", "david@gmail.com", "https://www.motortrend.com/uploads/sites/11/2017/09/2018-Honda-Accord-2-0T-Sport-front-three-quarter-in-motion-02.jpg?fit=around%7C875:492")
        self.car4 = Car("Tesla", "Model Y", "2020", "Red", "10000", "2028062020", "waw@gmail.com", "https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png")
        self.car5 = Car("Tesla", "Model Y", "2020", "Red", "10000", "2028062444", "waw@yahoo.com", "https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png")
    
    def test_from_form(self):
        self.assertRaises(TypeError, self.car5.from_form, {'make':2020, 'model':'Model Y', 'year': '2020', 'color': 'Red', 'price': '10000', 'phone':'800405212', 'email':'jonathan@techexchange.in', 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(TypeError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': '2020', 'color': 'Red', 'price': 10000, 'phone':'800405212', 'email':'jonathan@techexchange.in', 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(TypeError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': '2020', 'color': 'Red', 'price': '10000', 'phone':800405212, 'email':"jonathan@techexchange.in", 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(TypeError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': 2020, 'color': 'Red', 'price': '10000', 'phone':800405212, 'email':"jonathan@techexchange.in", 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(ValueError, self.car5.from_form, None)
        self.assertRaises(ValueError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': '2020', 'color': 'Red', 'price': 'adam', 'phone':'800405212', 'email':'jonathan@techexchange.in', 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(ValueError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': 'adam', 'color': 'Red', 'price': '10000', 'phone':'800405212', 'email':'jonathan@techexchange.in', 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})
        self.assertRaises(ValueError, self.car5.from_form, {'make':'Tesla', 'model':'Model Y', 'year': '2020', 'color': 'Red', 'price': '10000', 'phone':'8004052', 'email':'jonathan@techexchange.in', 'picture':"https://www.electrifying.com/files/NJrro9CgrZQIS_WL/TeslaModelY.png", 'sold' : False, 'verified': False})        
    
    def test_from_document(self):
        self.assertRaises(ValueError, self.car5.from_document, None)
    
    def test_to_document(self):
        self.assertEqual(self.car1.to_document(), {'make':'Toyota', 'model':'Corolla', 'year': '2020', 'color': 'Black', 'price': '30000', 'phone':'8192104615', 'email':'david300@gmail.com', 'picture':"https://www.seegertoyota.com/static/dealer-12152/MY20_Corolla_L_tcom_0209_001_DS_Front_7_8.png", 'sold' : False, 'verified': False})
        self.assertEqual(self.car2.to_document(), {'make':'Toyota', 'model':'Corolla', 'year': '2020', 'color': 'Black', 'price': '30000', 'phone':'2428072021', 'email':'david@gmail.com', 'picture':"https://www.seegertoyota.com/static/dealer-12152/MY20_Corolla_L_tcom_0209_001_DS_Front_7_8.png", 'sold' : False, 'verified': False})
        self.assertEqual(self.car3.to_document(), {'make':'Honda', 'model':'Accord', 'year': '2018', 'color': 'Red', 'price': '15000', 'phone':'2428072021', 'email':'david@gmail.com', 'picture':"https://www.motortrend.com/uploads/sites/11/2017/09/2018-Honda-Accord-2-0T-Sport-front-three-quarter-in-motion-02.jpg?fit=around%7C875:492", 'sold' : False, 'verified': False})


class Test_Seller(unittest.TestCase):
    def setUp(self):
        self.assertRaises(TypeError, Seller, "David", "Ajayi", "david@gmail.com", 2028062020, "BHjkaloduhfn3443ndww9nwdwdjksk")
        self.assertRaises(TypeError, Seller, "Anthony", "Mackie", ["anthy@gmail.com"], "2428072021", "B3ndww9nwdwdjkskw9nwdwdjksk")
        self.assertRaises(TypeError, Seller, "David", 300, "david300@gmail.com", "2028062020", "BHfn3443ndwwuhfn3443ndww9njksk")
        self.assertRaises(TypeError, Seller, ["Walter"], "White", "waw@gmail.com", "2028062020", "BHjkaloduhfn3443ndwfn3443ndww")
        self.assertRaises(ValueError, Seller, "Michael", "Jack", "mij@gmail.com", "20280620", "BHjkalod3ndww9nwdwdjkskdwdjksk")
        self.assertRaises(ValueError, Seller, "David", "John", "da.j@gmail.com", "202a062020", "BHjkalofn3443ndwww9nwdwdjksk")
        self.assertRaises(TypeError, Seller, "David", "Mayi", "mdvd@gmail.com", "2028062020", "BHjkaloduhfn3443ndww9nwdwdjksk", "carid1")

        self.Seller1 = Seller("John", "Doe", "jdoe@gmail.com", "2028062120", "BHjkalodu52sss6a2sdsnwdwdjk")
        self.Seller2 = Seller("Jane", "Dore", "jn.dore@gmail.com", "4028072221", "BHklamdjddneew55wwcadwdjk")

    def test_from_document(self):
        self.assertRaises(TypeError, Seller.from_document, {"first_name":"David", "last_name":"Ajayi", "email":"david@gmail.com", "phone":2028062020, "password_hash":"BHjkaloduhfn3443ndww9nwdwdjksk"})
        self.assertRaises(TypeError, Seller.from_document, {"first_name":"Anthony", "last_name":"Mackie", "email":["anthy@gmail.com"], "phone":"2428072021", "password_hash":"B3ndww9nwdwdjkskw9nwdwdjksk"})
        self.assertRaises(TypeError, Seller.from_document, {"first_name":"David", "last_name":300, "email":"david300@gmail.com", "phone":"2028062020", "password_hash":"BHfn3443ndwwuhfn3443ndww9njksk"})
        self.assertRaises(TypeError, Seller.from_document, {"first_name":["Walter"], "last_name":"White", "email":"waw@gmail.com", "phone":"2028062020", "password_hash":"BHjkaloduhfn3443ndwfn3443ndww"})
        self.assertRaises(ValueError, Seller.from_document, {"first_name":"Michael", "last_name":"Jack", "email":"mij@gmail.com", "phone":"20280620", "password_hash":"BHjkalod3ndww9nwdwdjkskdwdjksk"})
        self.assertRaises(ValueError, Seller.from_document, {"first_name":"David", "last_name":"John", "email":"da.j@gmail.com", "phone":"202a062020", "password_hash":"BHjkalofn3443ndwww9nwdwdjksk"})
        self.assertRaises(TypeError, Seller.from_document, {"first_name":"David", "last_name":"Mayi", "email":"mdvd@gmail.com", "phone":"2028062020", "password_hash":"BHjkaloduhfn3443ndww9nwdwdjksk", "cars":"carid1"})

        sample_user = Seller.from_document({"first_name":"James", "last_name":"Bond", "email":"j.bond@gmail.com", "phone":"4708062223", "password_hash":"Bhkamdinef6551qd6wwdwdjksk", "cars":["s5ascas6as2dasaccaridva51"]})
        self.assertEqual(sample_user.first_name, "James")
        self.assertEqual(sample_user.last_name, "Bond")
        self.assertEqual(sample_user.email, "j.bond@gmail.com")
        self.assertEqual(sample_user.phone, "4708062223")
        self.assertEqual(sample_user.password_hash, "Bhkamdinef6551qd6wwdwdjksk")
        self.assertEqual(sample_user.cars, ["s5ascas6as2dasaccaridva51"])

    def test_to_document(self):
        self.assertEqual(self.Seller1.to_document(), {'first_name': 'John', 'last_name': 'Doe', 'email': 'jdoe@gmail.com', 'phone': '2028062120', 'password_hash': 'BHjkalodu52sss6a2sdsnwdwdjk', 'cars': ["020220xxsa841carid56205"]})

    def test_add_car(self):
        self.assertRaises(TypeError, self.Seller1.add_car, 210262051626202550)
        self.assertRaises(TypeError, self.Seller2.add_car, ["02361151841carid56205"])

        self.Seller1.add_car("020220xxsa841carid56205")
        self.assertIn("020220xxsa841carid56205", self.Seller1.cars)
        self.assertNotIn("020hvhv5841carid56205", self.Seller2.cars)        


class Test_CarReports(unittest.TestCase):

    def setUp(self):

        self.assertRaises(TypeError, CarReports, 803829382938, {'make': True, 'model': True, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022")
        self.assertRaises(TypeError, CarReports, '6265c76284e23511b9d08193', True, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022")
        self.assertRaises(TypeError, CarReports, '6265c76284e23511b9d08193', {'make': True, 'model': True, 'color': True, 'year': True}, 'Leather Seats, All Wheel Drive, Cruise Control', "04/24/2022")
        self.assertRaises(TypeError, CarReports, '6265c76284e23511b9d08193', {'make': True, 'model': True, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], ["04/24/2022"])
        self.assertRaises(TypeError, CarReports, '6265c76284e23511b9d08193', {'make': True, 'model': True, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022", "True")
        self.assertRaises(TypeError, CarReports, '6265c76284e23511b9d08193', {'make': True, 'model': True, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022", True, "color, model")

        self.car_1 = CarReports('6265c76284e23511b9d08193', {'make': True, 'model': False, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022")
        self.car_2 = CarReports('6265c76284e23511b9d08193', {'make': True, 'model': True, 'color': True, 'year': True}, ['Leather Seats', 'All Wheel Drive', 'Cruise Control'], "04/24/2022")        
    
    def test_isDetailsVerified(self):

        self.assertFalse(self.car_1.isDetailsVerified())
        self.assertTrue(self.car_2.isDetailsVerified())
        self.assertEqual(self.car_1.verified,False)
        self.assertEqual(self.car_2.verified, True)

    def test_getUnverified(self):

        self.assertEqual(self.car_1.getUnverified(), ['model'])
        self.assertEqual(self.car_2.getUnverified(), [])
        self.assertEqual(self.car_1.unverified_details, ['model'])
        self.assertEqual(self.car_2.getUnverified(), [])


if __name__ == "__main__":
    unittest.main()
