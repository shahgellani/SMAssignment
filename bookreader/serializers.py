
from rest_framework import serializers


# class BookReaderSerialziers(serializers.Serializer):
#     book = serializers.CharField(Book, on_delete=models.CASCADE)
#     heading = serializers.CharField(max_length=70)
#     content = serializers.CharField(blank=True)
#     slug = serializers.CharField(max_length=50, editable=False)
#     date_created = serializers.CharField(auto_now_add=True)
#     parent = serializers.CharField(
#         'self',
#         on_delete=models.SET_NULL,
#         null=True,
#         default=None,
#         related_name='sub_sections')