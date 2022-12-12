def funcs(fullname, *args):
    fullname = fullname.__name__.replace("_", " ").upper() + ":"
    print(fullname, *args)

    def open_browser(browser_name):
        funcs(open_browser, browser_name)

        def go_to_companyname_homepage(page_url):
            funcs(go_to_companyname_homepage, page_url)

        def find_registration_button_on_login_page(page_url, button_text):
            funcs(find_registration_button_on_login_page, page_url, button_text)

        open_browser("Chrome")
        go_to_companyname_homepage("https:/google.com")
        find_registration_button_on_login_page("URL", "Login")
