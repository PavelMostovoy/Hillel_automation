import pytest
import requests


def save_to_file(data: str):
    with open("test.log", "a+") as f:
        f.write(f"{data}\n")


class TestFunctional:

    def setup(self):
        print("preconditions")

    def teardown(self):
        print("postconditions")

    def setup_class(cls):
        response = requests.get("https://www.google.com")
        assert response.status_code == 404
        print("Connect to the internet")

    def teardown_class(cls):
        print("Disconnect from internet")

    # def setup_method(self, method):
    #     print("method setup")
    #
    # def teardown_method(self, method):
    #     print("method teardown")

    def test_google(self):
        response = requests.get("https://www.google.com")
        print("first test")
        assert response.status_code == 201, save_to_file(
                f"Failed with code {response.status_code}")
        save_to_file(str(response.status_code))

    def test_google_filure(self):
        response = requests.get("https://www.google.com/_")
        print("second test")
        save_to_file(str(response.status_code))
        assert response.status_code == 404

    def test_google_filure_new(self):
        print("third test")
        with pytest.raises(ZeroDivisionError):
            var = 1 / 10
