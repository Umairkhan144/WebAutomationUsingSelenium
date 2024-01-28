# 1. Import the files
import unittest
from testCases.test_Login import LoginTest
from testCases.test_UserForm import UserFormTest
from testCases.test_CategoryForm import CategoryFormTest
from testCases.test_PagesForm import PagesFormTest
from testCases.test_ProductsForm import ProductFormTest

# 2. Create the object of the class using unitTest
LT = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
UF = unittest.TestLoader().loadTestsFromTestCase(UserFormTest)
CF = unittest.TestLoader().loadTestsFromTestCase(CategoryFormTest)
PF = unittest.TestLoader().loadTestsFromTestCase(PagesFormTest)
PP = unittest.TestLoader().loadTestsFromTestCase(ProductFormTest)


# 3. Create TestSuite
regressionTest = unittest.TestSuite([LT,UF,CF,PF,PP])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

