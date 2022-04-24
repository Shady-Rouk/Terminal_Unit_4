import unittest

from seller import *
from car import *


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

if __name__ == "__main__":
    unittest.main()
