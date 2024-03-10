from playwright.sync_api import sync_playwright
import time

# def test_has_title():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto("https://www.minddig.com/")
#         button = page.locator('button[data-ga="jk-click"]')
#         button.click()
#         browser.close()

def test_has_title(page):
    page.goto("https://www.minddig.com/")
    # Locate the button by class name
    button = page.locator('button[data-ga="join-click"]')
    button.click()
    # Wait for the element to appear
    page.wait_for_selector('#form-form-join-email')
    # Assert the presence of the element
    assert page.is_visible('#form-form-join-email')
    
    # Fill the input field
    input_field_email = page.locator('#input-join-email')
    input_field_email.fill('lukas.renstrom@minddig.com')
    
    input_field_password = page.locator('#input-password')
    input_field_password.fill('Minddig123')

    next_button = page.locator('button[data-ga="fastlane-register"]')
    # Click the button
    next_button.click()
    time.sleep(2)


