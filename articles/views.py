from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list_or_create(request):
    print(request)
    if request.method == 'GET':
        articles = Article.objects.order_by('id')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)