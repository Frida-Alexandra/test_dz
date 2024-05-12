import requests


def folder_creation(folder_name, ya_token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"OAuth {ya_token}",
    }
    params = {"path": f"{folder_name}", "overwrite": "false"}
    response = requests.put(url=url, headers=headers, params=params)
    print(response.status_code)
    return response.status_code


if __name__ == "__main__":
    folder_name = "test"
    ya_token = ""
    folder_creation(folder_name, ya_token)
