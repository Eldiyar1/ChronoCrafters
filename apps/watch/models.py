from django.core.validators import MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField

from apps.users.models import CustomUser
from apps.watch.constants import CONDITION_CHOICES, STYLE_CHOICES, GENDER_CHOICES, CASE_MATERIAL_CHOICES, COLOR_CHOICES, \
    STRAP_MATERIAL_CHOICES, CASE_SHAPE_CHOICES, WATER_RESISTANCE_CHOICES, MOVEMENT_CHOICES, GLASS_CHOICES, CHOICES, \
    RATING_CHOICES
from apps.watch.service import compress_image


class Watch(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    country = models.CharField(max_length=100, verbose_name='Страна производитель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска', validators=[MinValueValidator(1900)])
    selected_options = MultiSelectField(max_length=255, choices=CHOICES, blank=True, null=True,
                                        verbose_name='Выбранные опции')

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class WatchCategory(models.Model):
    watch = models.OneToOneField(Watch, on_delete=models.CASCADE, verbose_name='Часы', related_name="category")
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Пол')
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, verbose_name='Стиль')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=100, verbose_name='Состояние')
    glass = models.CharField(max_length=15, choices=GLASS_CHOICES, verbose_name='Стекло')
    case_material = models.CharField(max_length=100, choices=CASE_MATERIAL_CHOICES, verbose_name='Материал корпуса')
    dial_color = models.CharField(max_length=100, choices=COLOR_CHOICES, verbose_name='Цвет циферблата')
    band_color = models.CharField(max_length=100, choices=COLOR_CHOICES, verbose_name='Цвет ремешка/браслета')
    strap_material = models.CharField(max_length=100, choices=STRAP_MATERIAL_CHOICES,
                                      verbose_name='Материал ремешка/браслета')
    case_shape = models.CharField(max_length=100, choices=CASE_SHAPE_CHOICES, verbose_name='Форма корпуса')
    diameter = models.PositiveIntegerField(verbose_name='Диаметр корпуса (мм)')
    water_resistance = models.CharField(max_length=100, choices=WATER_RESISTANCE_CHOICES,
                                        verbose_name='Водонепроницаемость')
    movement = models.CharField(max_length=100, choices=MOVEMENT_CHOICES, verbose_name='Механизм')

    class Meta:
        verbose_name = 'Характеристикa'
        verbose_name_plural = 'Характеристики'


class Image(models.Model):
    images = models.ImageField(upload_to='watches', verbose_name='Изображение')
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Изображение места питания {self.watch.brand}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def compress_image(self):
        return compress_image(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_image()


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, verbose_name='Часы')
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name='Комментарий')
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата")
    design = models.PositiveIntegerField(choices=RATING_CHOICES, verbose_name='Дизайн')
    functionality = models.PositiveIntegerField(choices=RATING_CHOICES, verbose_name='Функциональность')
    quality = models.PositiveIntegerField(choices=RATING_CHOICES, verbose_name='Качество')
    value = models.PositiveIntegerField(choices=RATING_CHOICES,
                                               verbose_name='Соотношения цены и качества')

    def __str__(self):
        return f"Отзыв от {self.user} на {self.watch}"
