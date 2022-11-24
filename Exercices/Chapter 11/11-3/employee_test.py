import unittest
import Employee as ep 

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        """Creates an Employee object"""
        self.employee = ep.Employee("Joseph", "Ludwig", 30000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        salary=self.employee.annual_salary
        self.assertEqual(salary, 35000)
    def test_give_custom_raise(self):
        self.employee.give_raise(3000)
        salary=self.employee.annual_salary
        self.assertEqual(salary, 33000)
        
if __name__ == "__main__":
    unittest.main()
    
        
          