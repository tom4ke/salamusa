from .models import Article
from rest_framework import viewsets, permissions
from .serializers import ArticleSerializer


# Article Viewset
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArticleSerializer