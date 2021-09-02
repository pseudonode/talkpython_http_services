import requests


def main():
    user, repo = get_repo_info()

    url = f"https://api.github.com/repos/{user}/{repo}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error whilst accesing repository. Please check username or repo name!!!")
        return

    repo_data = response.json()
    clone = repo_data.get('clone_url', 'Error: No clone URL found!')
    print(f"To clone {user}'s repo named {repo}")
    print("The command is: ")
    print()
    print(f"git clone {clone}")


def get_repo_info():
    user = input("Please insert Github user: ")
    repo = input("Please insert repository name: ")
    return user, repo


if __name__ == "__main__":
    main()
