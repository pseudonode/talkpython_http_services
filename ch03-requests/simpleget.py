import requests


def main():
    url = "https://talkpython.fm"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successful response from: {url}")
            print(f"Status Code from URL was:  {response.status_code}")
            print(response.text[:500])
    except requests.exceptions.ConnectionError:
        print("Issues connecting to URL")


if __name__ == "__main__":
    main()