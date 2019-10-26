import unittest
from class_definitions_package import student_class as sc


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student('Smith', 'Joe', 'CIS')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Smith')
        self.assertEqual(self.student.first_name, 'Joe')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        student = sc.Student('Smith', 'Joe', 'CIS', 3.5)
        assert student.last_name == 'Smith'
        assert student.first_name == 'Joe'
        assert student.major == 'CIS'
        assert student.gpa == 3.5


if __name__ == '__main__':
    unittest.main()
