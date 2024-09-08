from django.urls import path

from .views import Categories, TrendingRecipies, CategoryRecipes, FavoriteRecipies, Tags, TagsRecipies, SearchRecipies

app_name = "foodie"

urlpatterns = [
    path("category", Categories.as_view()),
    path("trending", TrendingRecipies.as_view()),
    path("category/<int:pk>/recipes", CategoryRecipes.as_view()),
    path("favorites", FavoriteRecipies.as_view()),
    path("tags", Tags.as_view()),
    path("tag/<int:pk>/recipes", TagsRecipies.as_view()),
    path("", SearchRecipies.as_view())
]