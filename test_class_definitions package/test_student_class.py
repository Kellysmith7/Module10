import unittest
from class_definitions_package import student_class as sc


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student('Smith', 'Joe', 'CIS')

    def tearDown(self):
        del self.student

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Smith')
        self.assertEqual(self.student.first_name, 'Joe')
        self.assertEqual(self.student.major, 'CIS')


if __name__ == '__main__':
    unittest.main()
