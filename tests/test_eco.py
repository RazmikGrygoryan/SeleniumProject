import pytest


@pytest.mark.smoke
def test_product(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.choose_item()
    eco_friendly.check_right_size()
    eco_friendly.check_right_qty()


@pytest.mark.regression
def test_filter(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.filter()
    eco_friendly.check_value_filter()


@pytest.mark.regression
def test_compare_item(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.compare_product()
    eco_friendly.check_name_item()
