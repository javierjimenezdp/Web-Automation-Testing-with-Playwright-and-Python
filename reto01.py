from playwright.sync_api import sync_playwright

def test_demoqa_actions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demoqa.com/")
        
        
        actions = [
            {"xpath": "//div[@class='category-cards']//div[1]//div[1]//div[2]", "action": "click"},
            {"xpath": "//div[@class='element-list collapse show']//li[@id='item-0']", "action": "click"},
            {"xpath": "//input[@id='userName']", "action": "fill", "value": "Javier Jimenez"},
            {"xpath": "//input[@id='userEmail']", "action": "fill", "value": "javier@testqa.com"},
            {"xpath": "//textarea[@id='currentAddress']", "action": "fill", "value": "calle39#2-40"},
            {"xpath": "//textarea[@id='permanentAddress']", "action": "fill", "value": "avenida11#11-05"},
            {"xpath": "//button[@id='submit']", "action": "click"},
            {"xpath": "//div[@class='border col-md-12 col-sm-12']", "action": "is_visible"}
        ]
        
        for element in actions:
            xpath = element["xpath"]
            action = element["action"]
            
            element_locator = page.locator(xpath)
            
            if action == "click":
                element_locator.click()
                print(f"Elemento con XPath '{xpath}' ha sido clickeado.")
                
            elif action == "fill":
                value = element["value"]
                element_locator.fill(value)
                print(f"Elemento con XPath '{xpath}' ha sido llenado con el valor: {value}")
                
            elif action == "is_visible":
                element_locator.scroll_into_view_if_needed()
                is_visible = element_locator.is_visible()
                print(f"Elemento con XPath '{xpath}' es visible: {is_visible}")
        
        page.screenshot(path="clicked_element.png")
        
        browser.close()