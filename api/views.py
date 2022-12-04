from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ComicStore.utils.cache import (
    get_comics_from_cache,
    set_comics_to_cache,
    update_comics_in_cache,
    delete_comics_from_cache,
)
from api.models import Comic
from api.serializer import ComicSerializer

import logging

logger = logging.getLogger(__name__)


class ComicView(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        """
        This function returns a comic from the database
        :param request: The request object
        :return: The response object
        :rtype: Response
        :raises: HTTP_200_OK,HTTP_404_NOT_FOUND

        URL Params:
        {
            "title": "string"
        }
        http://localhost:8000/api/comics/?title=Hitler

        """
        comic_title = self.request.GET.get("title")
        # Check if the comic exists in cache
        comic = get_comics_from_cache(comic_title)
        if comic not in [None, ""]:
            return Response(status=status.HTTP_200_OK, data=comic)
        # Check if the comic exists in the database
        if Comic.objects.filter(title=comic_title).exists():
            comic = Comic.objects.get(title=comic_title)
            serializer = ComicSerializer(comic)

            # Set the comic to cache
            set_comics_to_cache(comic_title, serializer.data)

            logger.info("Comic found in database")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If the comic does not exist, return a 404
            logger.error("Comic not found")
            return Response(
                status=status.HTTP_404_NOT_FOUND, data={"message": "Comic not found"}
            )

    def post(self, request) -> Response:
        """
        This function creates a comic in the database
        :param request: The request object
        :return: The response object
        :rtype: Response
        :raises: HTTP_201_CREATED,HTTP_400_BAD_REQUEST
        request body:
        {
            "title": "string",
            "description": "string",
            "image": "string",
            "issue": 0,
            "day": "string",
            "month": "string",
            "year": "string"
        }
        """
        # Check if the comic already exists
        comic_title = request.data.get("title")
        if Comic.objects.filter(title=comic_title).exists():
            logger.error("Comic already exists")
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Comic already exists"},
            )
        # Create the comic
        serializer = ComicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Set the comic to cache
            set_comics_to_cache(comic_title, serializer.data)

            logger.info("Comic created")
            return Response(
                status=status.HTTP_201_CREATED, data={"message": "Comic created"}
            )
        else:
            logger.error("Invalid data")
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid data"}
            )

    def put(self, request) -> Response:
        """
        This function updates a comic in the database
        :param request: The request object
        :return: The response object
        :rtype: Response
        :raises: HTTP_200_OK,HTTP_400_BAD_REQUEST
        request body:
        {
            "title": "string",
            "description": "string",
            "image": "string",
            "issue": 0,
            "day": "string",
            "month": "string",
            "year": "string"
        }
        """
        # Check if the comic exists
        comic_title = request.data.get("title")
        if Comic.objects.filter(title=comic_title).exists():
            comic = Comic.objects.get(title=comic_title)
            serializer = ComicSerializer(comic, data=request.data)
            if serializer.is_valid():
                serializer.save()

                # Update the comic in cache
                update_comics_in_cache(comic_title, serializer.data)

                logger.info("Comic updated")
                return Response(
                    status=status.HTTP_200_OK, data={"message": "Comic updated"}
                )
            else:
                logger.error("Invalid data")

                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid data"}
                )
        else:
            logger.error("Comic not found")

            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": "Comic not found"}
            )

    def delete(self, request) -> Response:
        """
        This function deletes a comic from the database
        :param request: The request object
        :return: The response object
        :rtype: Response
        :raises: HTTP_200_OK,HTTP_400_BAD_REQUEST
        request body:
        {
            "title": "string"
        }
        """
        # Check if the comic exists
        comic_title = request.data.get("title")
        if Comic.objects.filter(title=comic_title).exists():
            comic = Comic.objects.get(title=comic_title)
            comic.delete()
            # Delete the comic from cache
            delete_comics_from_cache(comic_title)

            logger.info("Comic deleted")

            return Response(
                status=status.HTTP_200_OK, data={"message": "Comic deleted"}
            )
        else:
            logger.error("Comic not found")

            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": "Comic not found"}
            )
