from django.shortcuts import get_list_or_404
from rest_framework import filters
from rest_framework.generics import ListAPIView

from .HeaderAuthentication import HeaderAuthentication
from .models import Category, Recipe, Tag
from .serializers import RecipesSerializer, CategorySerializer, TagsSerializer


class SearchRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer
    queryset = Recipe.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Categories(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRecipes(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer

    def get_queryset(self):
        recipies_pks = [x.pk for x in get_list_or_404(Recipe, category__pk=self.kwargs['pk'])]
        return Recipe.objects.filter(pk__in=recipies_pks)


class TrendingRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer

    def get_queryset(self):
        results_pks = [x.pk for x in Recipe.objects.all() if x.is_trending == True][:15]
        return Recipe.objects.filter(pk__in=results_pks)


class FavoriteRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer
    queryset = Recipe.objects.filter(is_favorite=True)


class Tags(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = TagsSerializer
    queryset = Tag.objects.all()


class TagsRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer

    def get_queryset(self):
        recipies_pks = [x.pk for x in get_list_or_404(Recipe, tag__pk=self.kwargs['pk'])]
        return Recipe.objects.filter(pk__in=recipies_pks)
