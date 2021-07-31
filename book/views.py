from rest_framework import filters, generics
from rest_framework.response import Response

from book.models import Book, Category
from book.serializers import (
    BookAndRelatedSerializer,
    BookSerializer,
    CategoryAndRelatedSerializer,
    CategorySerializer,
)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAndRelatedSerializer
    search_fields = ["title"]
    filter_backends = [filters.SearchFilter]

    def get(self, request, *args, **kwargs):
        """Get book list, support filter books by title"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAndRelatedSerializer

    def put(self, request, *args, **kwargs):
        """Update book, assume that category cannot be changed"""
        instance = self.get_object()
        serializer = BookSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().get(request, *args, **kwargs)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        """Get category list, can display a list of related books"""
        show = request.query_params.get("related")
        if show and show == "more":
            serializer = CategoryAndRelatedSerializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        return super().get(request, *args, **kwargs)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
