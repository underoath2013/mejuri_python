from page_objects.main_page import MainPage
from time import sleep


# already registered user: eeo24667@omeie.com pass: Qq123456
def test_login_search_add_to_wishlist(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.click_nav_bar_user_button()
    main_page.click_on_sing_in_button()
    sleep(2)
    main_page.input(main_page.find_email_input(), "eeo24667@omeie.com")
    main_page.input(main_page.find_password_input(), "Qq123456")
    main_page.click_continue_button()
    sleep(5)
    main_page.input(main_page.find_birthday_input(), "12/12/2000")
    main_page.click_on_save_birthday_button()
    sleep(5)
    main_page.click_search_icon()
    sleep(5)
    main_page.input(main_page.find_search_input_field(), "Honey Mini Signet")
    sleep(4)
    search_result = main_page.find_search_result()
    sleep(2)
    assert search_result.text == "Honey Signet", "Wrong search result"
    main_page.click(search_result)
    sleep(2)
    product_size = main_page.find_product_size()
    assert product_size.text == "Ring Size", "Product is not a ring"
    wishlist_button = main_page.find_wishlist_button()
    sleep(2)
    main_page.click(wishlist_button)
