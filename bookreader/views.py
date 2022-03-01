from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response

import custom_utils.helper_functions as utils
from .models import Book


# Create your views here.

class Books(generics.GenericAPIView):
    """
    Books
    """
    def get(self, request):
        try:
            if request.id:
                book = Book.get_books(id=id)
            else:
                book = Book.get_books()

            return Response({
                "success": True,
                "message": "Books fetched successfully!",
                "status_code": status.HTTP_200_OK,
                "result": book
            })

        except Exception as e:
            return utils.error_response(success=False, status_code=status.HTTP_200_OK, message="Something Went Wrong!")

    def post(self, request):
        try:
            user = request.data['user']
            user = User.objects.get(username=user)
            title = request.data['title']
            description = request.data['description']
            book = Book.create_book(user=user, title=title, description=description)
            if book:
                return Response({
                    "success": True,
                    "status_code": status.HTTP_201_CREATED,
                    "message": "User Activity Saved Successfully!",
                })


        except Exception:
            return utils.error_response(success=False, status_code=status.HTTP_200_OK, message="Something Went Wrong!")
