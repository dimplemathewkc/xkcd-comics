from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class TestApi(TestCase):
    def setUp(self) -> None:
        """
        The setUp method is executed before each test
        """
        self.client = APIClient()
        # get token
        self.user = User.objects.create_user(username="test", password="test123")
        self.user.save()
        self.token = (
            self.client.post("/get_token/", {"username": "test", "password": "test123"})
        ).data
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        self.client.post(
            "/api/comics/",
            {
                "title": "string",
                "description": "string",
                "image": "https://encrypted-tbn0.gstatic.com/",
                "issue": 0,
                "day": "string",
                "month": "string",
                "year": "string",
            },
            header={"Authorization": "Token " + self.token},
            format="json",
        )

    def test_create_comic(self):
        """
        The test creates a comic in the database
        """
        response = self.client.post(
            "/api/comics/",
            {
                "title": "string2",
                "description": "string2",
                "image": "https://encrypted-tbn0.gstatic.com/",
                "issue": 1,
                "day": "string2",
                "month": "string2",
                "year": "string2",
            },
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))

    def test_create_already_exists(self):
        """
        Test checks if the comic already exists
        """
        response = self.client.post(
            "/api/comics/",
            {
                "title": "string",
                "description": "string",
                "image": "https://encrypted-tbn0.gstatic.com/",
                "issue": 0,
                "day": "string",
                "month": "string",
                "year": "string",
            },
            format="json",
        )
        self.assertTrue(status.is_client_error(response.status_code))

    def test_get_comic(self):
        """
        Test validates get comic
        """
        response = self.client.get("/api/comics/?title=string", format="json")
        self.assertTrue(status.is_success(response.status_code))

    def test_get_comic_not_found(self):
        """
        Test validates get comic not found
        """
        response = self.client.get("/api/comics/?title=string3", format="json")
        self.assertTrue(status.is_client_error(response.status_code))

    def test_update_comic(self):
        """
        Test validates update comic
        """
        response = self.client.put(
            "/api/comics/",
            {
                "title": "string",
                "description": "string",
                "image": "https://encrypted-tbn0.gstatic.com/",
                "issue": 0,
                "day": "string",
                "month": "string",
                "year": "string",
            },
            format="json",
        )

        assert response.data == {"message": "Comic updated"}

    def test_update_comic_not_found(self):
        """
        Test validates update comic not found
        """
        response = self.client.put(
            "/api/comics/",
            {
                "title": "string4",
                "description": "string",
                "image": "https://encrypted-tbn0.gstatic.com/",
                "issue": 0,
                "day": "string",
                "month": "string",
                "year": "string",
            },
            format="json",
        )
        self.assertTrue(status.is_client_error(response.status_code))

    def test_delete_comic(self):
        """
        Test validates delete comic
        """
        response = self.client.delete(
            "/api/comics/",
            {
                "title": "string",
            },
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))

    def test_delete_comic_not_found(self):
        """
        Test validates delete comic not found
        """
        response = self.client.delete(
            "/api/comics/",
            {
                "title": "string3",
            },
            format="json",
        )
        self.assertTrue(status.is_client_error(response.status_code))
