import mimetypes
import os

from django.http import HttpResponseBadRequest, HttpResponse, Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from .HeaderAuthentication import HeaderAuthentication
from .models import Category, Recipe, Tag
from .serializers import RecipesSerializer, CategorySerializer, TagsSerializer
from foodie_be import settings


class SearchRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    pagination_class = PageNumberPagination
    serializer_class = RecipesSerializer
    queryset = Recipe.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Categories(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None


class CategoryRecipes(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer
    pagination_class = None

    def get_queryset(self):
        return Recipe.objects.select_related('category').filter(category_id=self.kwargs['pk'])


class TrendingRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer
    pagination_class = None

    def get_queryset(self):
        results_pks = [x.pk for x in Recipe.objects.all() if x.is_trending == True][:15]
        return Recipe.objects.filter(pk__in=results_pks)


class FavoriteRecipes(ModelViewSet):
    authentication_classes = [HeaderAuthentication]
    http_method_names = ['get', 'patch']
    serializer_class = RecipesSerializer
    queryset = Recipe.objects.filter(is_favorite=True)

    @action(detail=True, methods=['patch'])
    def favorite(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
        if recipe.is_favorite:
            recipe.is_favorite = False
        else:
            recipe.is_favorite = True
        recipe.save()

        return Response(data="Success", status=HTTP_201_CREATED)


class Tags(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = TagsSerializer
    queryset = Tag.objects.all()
    pagination_class = None

class TagsRecipies(ListAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = RecipesSerializer

    def get_queryset(self):
        recipies_pks = [x.pk for x in get_list_or_404(Recipe, tag__pk=self.kwargs['pk'])]
        return Recipe.objects.filter(pk__in=recipies_pks)


def media(request, file_path=None):
    media_root = getattr(settings, 'MEDIA_ROOT', None)
    if not media_root:
        return HttpResponseBadRequest('Invalid Media Root Configuration')

    if not file_path:
        return HttpResponseBadRequest('Invalid File Path')

    full_file_path = os.path.join(media_root, file_path)

    if not os.path.exists(full_file_path):
        raise Http404("File not found")

    try:
        with open(full_file_path, 'rb') as doc:
            mime_type, _ = mimetypes.guess_type(full_file_path)
            response = HttpResponse(doc.read(), content_type=mime_type or 'application/octet-stream')
            response['Content-Disposition'] = f'inline; filename={file_path.split("/")[-1]}'
            return response
    except FileNotFoundError:
        raise Http404("File not found")