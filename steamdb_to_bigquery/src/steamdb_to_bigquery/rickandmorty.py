import requests

base_url = "https://rickandmortyapi.com/api/"
character_url = base_url + "character/"
location_url = base_url + "location/"
episode_url = base_url + "episode/"

class Base():
    @staticmethod
    def api_info():
        try:
            response = requests.get(base_url)
            response.raise_for_status()  # Lança exceção para erros HTTP
            return response.json()
        except requests.RequestException as e:
            print("Error fetching API info:", e)
            return None

    @staticmethod
    def schema():
        try:
            temp = requests.get(character_url).json()
            return temp['info'].keys()
        except requests.RequestException as e:
            print("Error fetching schema:", e)
            return None


class Character():
    @staticmethod
    def get_all_characters():
        url = character_url
        all_characters = []

        while url:
            response = requests.get(url)
            data = response.json()
            all_characters.extend(data["results"])
            url = data["info"]["next"]

        return all_characters

    @staticmethod
    def get_all():
        try:
            response = requests.get(character_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error fetching all characters:", e)
            return None

    @staticmethod
    def get_page(number):
        try:
            response = requests.get(character_url + '?page=' + str(number))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error fetching characters page:", e)
            return None

    @staticmethod
    def get(id=None):
        try:
            if id is None:
                raise ValueError("You need to pass the ID of the character to get output.")
            response = requests.get(character_url + str(id))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error fetching character:", e)
            return None

    @staticmethod
    def filter(**kwargs):
        try:
            query_params = '&'.join([f"{key}={value}" for key, value in kwargs.items()])
            final_url = f"{character_url}?{query_params}"
            response = requests.get(final_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error filtering characters:", e)
            return None

    @staticmethod
    def schema():
        try:
            temp = requests.get(character_url).json()
            return temp['results'][0].keys()
        except requests.RequestException as e:
            print("Error fetching schema:", e)
            return None


# As outras classes (Location, Episode) seguem um padrão semelhante
