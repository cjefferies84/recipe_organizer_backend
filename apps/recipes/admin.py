from django.contrib import admin
from models import *

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Comment)

