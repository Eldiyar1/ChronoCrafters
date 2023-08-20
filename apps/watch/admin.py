from django.contrib import admin

from apps.watch.models import Watch, WatchCategory, Image, Review


class ImageInline(admin.TabularInline):
    model = Image
    min_num = 3
    max_num = 10
    extra = 0


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'watch', 'comment', 'date_added', 'design', 'functionality',
                    'quality', 'value')
    list_filter = ('design', 'functionality', 'quality', 'value')
    search_fields = ('user__username', 'watch__brand', 'watch__model')


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'year', 'selected_options')
    list_filter = ('brand', 'model', 'price', 'year')
    search_fields = ('brand', 'model', 'price', 'year')
    inlines = (ImageInline,)


@admin.register(WatchCategory)
class WatchCategoryAdmin(admin.ModelAdmin):
    list_display = ('condition', 'style', 'gender', 'case_material', 'dial_color', 'band_color',
                    'strap_material', 'case_shape', 'water_resistance', 'movement')
    list_filter = ('condition', 'style', 'gender', 'case_material')
    search_fields = ('watch__brand', 'watch__model')
