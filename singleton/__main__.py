from .classes import Configuration


configuration = Configuration.get_instance()
configuration.api_url = "http://some_url.com"
print(f"Configuration instance at {id(configuration)}.")
print(f"API URL configuration is {configuration.api_url}.")

configuration2 = Configuration.get_instance()
print(f"Configuration instance at {id(configuration)}.")
print(f"API URL configuration is {configuration2.api_url}.")
