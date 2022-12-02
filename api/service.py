import requests
from .models import Comic


def get_comic_data():
    """
    This function gets the data from the xkcd api
    :return: The data from the api
    :rtype: dict
    """
    for i in range(1, 10):
        response = requests.get(f"https://xkcd.com/{i}/info.0.json")
        # save the data in the database
        print(response.text)
        if not Comic.objects.filter(title=response.json().get("title")).exists():
            pass
            comic = Comic(
                title=response.json().get("title"),
                description=response.json().get("alt"),
                image=response.json().get("img"),
                issue=response.json().get("num"),
                day=response.json().get("day"),
                month=response.json().get("month"),
                year=response.json().get("year"),
            )
            comic.save()
