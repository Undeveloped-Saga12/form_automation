# Form Automation Project 📝

Automate form submissions using **Python**, **Selenium**, and **pytest**. This project fills out and submits the [DemoQA Practice Form](https://demoqa.com/automation-practice-form) and validates successful submissions.

## Technologies Used
- **Python 3**
- **Selenium WebDriver**
- **pytest** (for test orchestration)
- **ChromeDriver** (for browser automation)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/form-automation.git
cd form-automation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Create `requirements.txt` with `pip freeze > requirements.txt` if missing)*

### 3. Download ChromeDriver
- Download the latest [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version.
- Place `chromedriver` in the project root or update the path in `conftest.py`.

## Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run a specific test
pytest tests/test_form.py -v
```

## Project Structure
```
form-automation/
├── tests/               # Test scripts
│   └── test_form.py     # Form submission tests
├── pages/               # Page Object Model (POM) classes
│   └── form_page.py     # Form page interactions
├── utils/               # Configurations and helpers
│   └── config.py        # URLs and constants
├── conftest.py          # Pytest fixtures (browser setup)
├── README.md            # Project documentation
└── .gitignore           # Files/folders to exclude from Git
```

## Example Test Run
```bash
========================= test session starts =========================
collected 1 item

tests/test_form.py::test_form_submission PASSED                 [100%]

========================== 1 passed in 12.34s =========================
```

## Features
- Automates text fields, radio buttons, checkboxes, and dropdowns.
- Handles dynamic elements and waits.
- Uses the **Page Object Model** for maintainable code.

## License
MIT License

---

**Happy Testing!** 🚀  
Feel free to contribute or report issues [here](https://github.com/your-username/form-automation/issues).
