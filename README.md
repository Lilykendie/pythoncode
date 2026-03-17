 KLAK Automation Test Suite

 Project Overview
This project contains automated test scripts developed to validate the functionality and reliability of the KLAK web application. The tests focus on verifying critical user flows and ensuring that core features of the system work as expected.

The automation framework was built using Python and Selenium to simulate real user interactions with the application.

 Objectives
- Automate regression testing for key application features
- Improve testing efficiency and reduce manual testing effort
- Ensure high-quality and reliable user experience

 Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Git & GitHub

 Project Structure
klak-automation-tests/
│
├── tests/
│ ├── test_login.py
│ ├── test_dashboard.py
│
├── pages/
│ ├── login_page.py
│ ├── dashboard_page.py
│
├── requirements.txt
├── README.md

 Test Coverage
The automated tests cover the following areas:

- User login functionality
- Navigation to dashboard
- Verification of key UI elements
- Basic workflow validations

 Installation
1. Clone the repository
git clone https://github.com/Lilykendie/klak-automation-tests.git

2. Navigate to the project directory
cd klak-automation-tests

3. Install the required dependencies
pip install -r requirements.txt

Running the Tests

Run the following command to execute the test suite:
pytest
Automation Framework Design

The automation framework follows the Page Object Model (POM) design pattern to improve maintainability and readability.

Key principles used:

- Page Objects – Each page of the application is represented by a class containing its elements and actions.
- Test Separation – Test logic is separated from page interaction logic.
- Reusable Method – Common actions are implemented as reusable functions.

Benefits of this structure include:
- Easier test maintenance
- Improved scalability of the test suite
- Cleaner and more readable test scripts
   Test Strategy

The automation suite focuses on validating critical user workflows and high-risk functionality of the application. The following testing approach was used:

- Functional Testing – Ensuring key features behave as expected.
- Regression Testing  – Automating repeatable test cases to catch regressions after updates.
- UI Testin – Verifying user interface elements and navigation.
- End-to-End Testin – Simulating real user journeys across the application.

Test cases were selected based on frequently used features and areas with high user interaction.
 CI/CD Integration

The project is designed to support integration with CI/CD pipelines such as GitHub Actions.

Automated tests can be triggered:
- On every code push
- During pull requests
- Before deployment
Test Execution Example

Below is an example of the automated tests running unsuccessfully.

![Test Execution](Billing Screenshort.png)

This helps ensure that new changes do not introduce regressions into the application.

 Future Improvements
- Add API test automation
- Integrate automated tests into a CI/CD pipeline
- Increase test coverage for additional modules
- Implement test reporting and screenshots for failed tests

Author
Lilian Akinyi  
Software Quality Assurance Engineer
