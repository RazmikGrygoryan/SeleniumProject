from selenium.webdriver.common.by import By


class EcoFriendlyLocators:
    product = (By.CSS_SELECTOR, '[class="item product product-item"]')
    size_option = (By.ID, 'option-label-size-143-item-172')
    color_option = (By.ID, 'option-label-color-93-item-49')
    input_qty = (By.ID, 'qty')
    add_to_cart = (By.ID, 'product-addtocart-button')
    shopping_cart = (By.LINK_TEXT, 'shopping cart')
    size = (By.CSS_SELECTOR, '#shopping-cart-table > tbody > tr.item-info > td.col.item > div > dl > dd:nth-child(2)')
    qty = (By.CSS_SELECTOR, '[class="input-text qty"]')
    delete_item = (By.CSS_SELECTOR, '[class="action action-delete"]')
    filter_size = (By.XPATH, '(//*[@class="filter-options-title"])[3]')
    actual_size = (By.CSS_SELECTOR, '[class="swatch-option text "]')
    filter_value = (By.CSS_SELECTOR, '[class="filter-value"]')
    clear_all = (By.LINK_TEXT, 'Clear All')
    product_item = (By.CSS_SELECTOR, '[class="product-item-info"]')
    compare_button = (By.CSS_SELECTOR, '[class="action tocompare"]')
    product_name = (By.CSS_SELECTOR, '[class="product-item-name"]')
    first_name_product = (By.LINK_TEXT, 'Ana Running Short')
