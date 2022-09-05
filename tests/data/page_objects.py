class LoginPage:
    submit_button_id = '//*[@id="login-form"]/div[3]/input'
    login_field_id = 'id_username'
    password_field_id = '//*[@id="id_password"]'


class AdminPage(LoginPage):
    page_header_id = '//*[@id="site-name"]/a'

# User_data

# Reporting page
