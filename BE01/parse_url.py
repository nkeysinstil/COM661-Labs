from urllib.parse import urlparse

def print_info(data):
    print("Information:")
    for key, value in data.items():
        # Capitalize the key and print it along with the value
        print(f"{key.capitalize():<10}: {value}")

stringUrl = input("Input Url: ")
urlParams = {}

queryParams = urlparse(stringUrl).query

keyValuePairs = queryParams.split("&")

for pair in keyValuePairs:
    key, value = pair.split("=")
    urlParams[key] = value

print_info(urlParams)
