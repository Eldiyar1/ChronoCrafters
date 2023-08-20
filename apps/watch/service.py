from PIL import Image


def get_average_rating(self, obj):
    from .models import Review
    reviews = Review.objects.filter(watch=obj)
    if reviews:
        total_rating = sum([
            (review.design +
             review.functionality +
             review.quality +
             review.value) / 4
            for review in reviews
        ])
        average_rating = total_rating / len(reviews)
        return round(average_rating, 1)
    return 0


def compress_image(self):
    img = Image.open(self.room_image.path)
    img = img.convert('RGB')
    img.thumbnail((800, 800))
    img.save(self.room_image.path, 'JPEG', quality=90)
