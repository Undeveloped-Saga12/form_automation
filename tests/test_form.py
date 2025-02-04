from pages.form_page import FormPage

def test_form_submission(browser):
    form_page=FormPage(browser)
    form_page.open()

    #Fill the with test data
    form_page.fill_form(
        Firstname="Sagar",
        lastname="sridhar",
        email="tghvhjk@gmail.com",
        mobile="1234567890",
        address="123 7th cross"
    )
    form_page.set_date_of_birth("15 nov 2024")

    # submit the form
    form_page.submission()

    # Verify the submission
    assert form_page.is_submitted(),"Form Submission failed"
