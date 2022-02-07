import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClassx")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name,"John Doe")
    

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list) 
    
    def test_get_email(self):
        print("test_get_email")
        self.assertEqual(self.student.email,"john.doe@email.com")
    
    def test_apply_extension(self):
        print("test_apply_extension")
        self.student.apply_extension(15)
        self.assertEqual(self.student.end_date, date.today()+ timedelta(days=380))
    
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")



if __name__ =="__main__":
    unittest.main()