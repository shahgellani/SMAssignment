# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from rest_framework import status
from rest_framework.response import Response


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_book(cls, title, user, description):
        try:
            book = cls.objects.create(title=title, user=user, description=description)
            return book
        except:
            return Response({
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Book couldn't created",
            })

    @classmethod
    def get_books(cls, id=None):
        try:
            if id:
                Book.objects.get(id=id)
            else:
                Book.objects.all()
        except Book.DoesNotExist:
            print("Object does not exist")


class Section(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    heading = models.CharField(max_length=70)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='sub_sections')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'heading'], name='book_heading')
        ]

    def __str__(self):
        return '{}-{}'.format(str(self.parent), self.heading)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(Section, self).save(*args, **kwargs)
