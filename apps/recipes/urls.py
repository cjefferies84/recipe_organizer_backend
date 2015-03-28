from django.conf.urls import patterns, url
from django.conf import settings
from views import *


urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-list'),
    url(r'^add-recipe$', AddRecipe.as_view(), name='add-recipe'),
    url(r'^add-comments$', AddComments.as_view(), name='add-comments'),

    # Handling media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

