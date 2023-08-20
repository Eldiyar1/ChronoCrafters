from rest_framework import serializers
from .models import Watch, WatchCategory, Image, Review
from .service import get_average_rating


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class WatchCategorySerializer(serializers.ModelSerializer):
    diameter = serializers.SerializerMethodField()

    class Meta:
        model = WatchCategory
        fields = ('gender', 'style', 'condition', 'glass', 'case_material', 'dial_color', 'band_color',
                  'strap_material', 'case_shape', 'diameter', 'water_resistance', 'movement')

    def get_diameter(self, obj):
        return f"{obj.diameter} мм"


class WatchSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    category = WatchCategorySerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Watch
        fields = ('images', 'brand', 'model', 'description', 'price', 'average_rating', 'country', 'year', 'selected_options',
        'category')

    def get_average_rating(self, obj):
        return get_average_rating(self, obj)
