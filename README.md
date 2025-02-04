# Form Automation with Selenium & Pytest

## 📌 Overview

This project automates the process of filling out and submitting a web form using Selenium WebDriver. It includes:
- A `FormPage` class for interacting with the form elements.
- A test script using `pytest` to validate form submission.


## 🔧 Setup Instructions

### 1️⃣ Install Dependencies
Make sure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
2️⃣ Run the Test
Execute the test script using:
pytest tests/test_form.py

🛠 Features
Uses Selenium WebDriver for browser automation.
Implements the Page Object Model (POM) for maintainable test scripts.
Supports Pytest for test execution and validation.

📌 Key Files
form_page.py
Defines methods to:
Fill out form fields.
Select options from dropdowns.
Submit the form.
Verify successful submission.

test_form.py
Calls FormPage methods.
Verifies that form submission is successful using pytest.
