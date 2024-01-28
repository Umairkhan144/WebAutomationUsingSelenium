import time
import unittest
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.ProjectMethods import ProjectMethods
from Utilities.customLogger import LogGen
from pageObjects.GenericMethods import GenericMethods
from Utilities.readProperties import ReadConfig
from Utilities import XLUtilis
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

{% for suite in test_plan %}

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class {{suite.title().replace(' ', '')}}(unittest.TestCase):
    
    # cl = log.customLogger()

    @pytest.fixture(autouse=True)
    def classObjects(self):
        print(type(self.driver))
        self.logger = LogGen.loggen()
        self.gm = GenericMethods(self.driver)
        self.pm = ProjectMethods(self.driver)
 
    {% for test_case in test_plan[suite] %}
    @pytest.mark.run(order={{ test_case['execution_order']}})
    def test_{{test_case['execution_order']}}_{{ test_case['tcase_name']|lower()|replace(" ", "_") }}(self):
        {% if test_case['custom_field_value'] != '' %}{{ test_case['custom_field_value'] }}{% else %}...{% endif %}
        self.logger.info("notes:: Test {{test_case['tcase_name']|lower()}} ended")
    {% endfor %}
{% endfor %}
