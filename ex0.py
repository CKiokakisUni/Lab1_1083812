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


url = 'http://python.org/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    print(f"Website headers are {url}\n{response.headers}\n")
    server = response.headers.get("Server")
    print(f"Server: {server}")
    cookies = response.headers.get("Set-Cookie")
    for cookie in response.cookies:
        print(cookie.expires)


