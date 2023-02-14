#!/usr/bin/env python3
# first parth of the challenge
# emails_test.py
import unittest
from emails import find_email
class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

    def test_two_name(self):
        testcase = [None, "John", "Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)


if __name__ == "__main__":
    unittest.main()

# second part of the challenge

# emails.py
#!/usr/bin/env python3
import csv
import sys
def populate_dictionary(filename):
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict

def find_email(argv):
    try:
        fullname = str(argv[1] + " " + argv[2])
        email_dict = populate_dictionary("/home/student-03-9a9f05634f33/data/user_emails.csv")
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
       # email_dict = populate_dictionary("/home/student-03-9a9f05634f33/data/user_emails.csv")
       # return email_dict.get(fullname.lower())
    except IndexError:
        return "Missing parameters"

def main():
    print(find_email(sys.argv))

if __name__ == "__main__":
    main()