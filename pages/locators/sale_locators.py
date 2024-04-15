from selenium.webdriver.common.by import By


class SaleLocators:
    main_promo = (By.CSS_SELECTOR, '[class="block-promo sale-main"]')
    page_title = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    sales_men = (By.CSS_SELECTOR, '[class="block-promo sale-mens"]')
    sales_women = (By.CSS_SELECTOR, '[class="block-promo sale-women"]')