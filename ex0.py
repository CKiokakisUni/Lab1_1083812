import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input("URL: ")

if not url.startswith("http"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    print(f"\nWebsite headers for {url}:\n\n{response.headers}\n")

    server = response.headers.get("Server")
    print(f"Server: {server if server else 'No server found'}\n")

    cookies = response.headers.get("Set-Cookie")
    print(f"This website {'uses' if cookies else 'does not use'} cookies\n")
    for cookie in response.cookies:
        print("Name:", cookie.name)
        print("Expires:", cookie.expires)


