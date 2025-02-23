from django.contrib import admin

from image_gallery import models


# Register your models here.

class InlineImage(admin.TabularInline):
    model = models.Image


@admin.register(models.Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]
