#ReadME
*NB- Mobile automation tests are for android only but if requried can be scaled for iOS platfrom also.

#Setup instructions

##Required installations
*Python 3
*Appium-Python-Client==2.11.1
*requests==2.31.0
*pip==23.1.2
*selenium==4.11.2
*PyYAML==6.0.1
*pytest-html==3.2.0
*urllib3==2.0.4
*setuptools==67.8.0
*adb


##For mobile automation tests
*Pre-requsite - Boltfood app should be installed on the device and user should be logged in.
*Appium server. Run it before running the tests.
*Real device or Emulator should be connected to the machine.
*Conftest.py file contains the details of device/mobile capabilities can be changed there.

##For api tests
*Provide the url, resources and Bearer Token in lib/helpers/api_resources.py

##Running the tests using IDE


*run pytest -v --html={reportname.html} --self-contained-html
*It will generate the test report in html format in root folder, and screenshots of failed steps.
*Delete the existing test report before fresh test run

##automation.log file is captures the logs




