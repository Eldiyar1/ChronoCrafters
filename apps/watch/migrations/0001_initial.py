# Generated by Django 4.2.4 on 2023-08-19 19:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Марка')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('country', models.CharField(max_length=100, verbose_name='Страна производитель')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900)], verbose_name='Год выпуска')),
                ('selected_options', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Коробка', 'Коробка'), ('Документы', 'Документы'), ('Гарантия', 'Гарантия')], max_length=255, null=True, verbose_name='Выбранные опции')),
            ],
            options={
                'verbose_name': 'Часы',
                'verbose_name_plural': 'Часы',
            },
        ),
        migrations.CreateModel(
            name='WatchCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Мужские', 'Мужские'), ('Женские', 'Женские'), ('Унисекс', 'Унисекс')], max_length=100, verbose_name='Пол')),
                ('style', models.CharField(choices=[('Повседневные', 'Повседневные'), ('Официальные', 'Официальные'), ('Спортивные', 'Спортивные'), ('Люкс', 'Люкс'), ('Винтаж', 'Винтаж'), ('Дайверские', 'Дайверские')], max_length=100, verbose_name='Стиль')),
                ('condition', models.CharField(choices=[('Хорошее', 'Хорошее'), ('Идеальное', 'Идеальное'), ('Новое', 'Новое')], max_length=100, verbose_name='Состояние')),
                ('glass', models.CharField(choices=[('Сапфировое', 'Сапфировое'), ('Минеральное', 'Минеральное'), ('Пластиковое', 'Пластиковое'), ('Кристалл', 'Кристалл'), ('Акриловое', 'Акриловое')], max_length=15, verbose_name='Стекло')),
                ('case_material', models.CharField(choices=[('Нержавеющая сталь', 'Нержавеющая сталь'), ('Золото', 'Золото'), ('Титан', 'Титан'), ('Керамика', 'Керамика'), ('Углеволокно', 'Углеволокно')], max_length=100, verbose_name='Материал корпуса')),
                ('dial_color', models.CharField(choices=[('Серебристый', 'Серебристый'), ('Черный', 'Черный'), ('Белый', 'Белый'), ('Серый', 'Серый'), ('Жёлтый', 'Жёлтый'), ('Зеленый', 'Зеленый'), ('Золотой', 'Золотой'), ('Коричневый', 'Коричневый'), ('Фиолетовый', 'Фиолетовый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Голубой', 'Голубой')], max_length=100, verbose_name='Цвет циферблата')),
                ('band_color', models.CharField(choices=[('Серебристый', 'Серебристый'), ('Черный', 'Черный'), ('Белый', 'Белый'), ('Серый', 'Серый'), ('Жёлтый', 'Жёлтый'), ('Зеленый', 'Зеленый'), ('Золотой', 'Золотой'), ('Коричневый', 'Коричневый'), ('Фиолетовый', 'Фиолетовый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Голубой', 'Голубой')], max_length=100, verbose_name='Цвет ремешка/браслета')),
                ('strap_material', models.CharField(choices=[('Кожа', 'Кожа'), ('Нержавеющая сталь', 'Нержавеющая сталь'), ('Резина', 'Резина'), ('Металлический', 'Металлический')], max_length=100, verbose_name='Материал ремешка/браслета')),
                ('case_shape', models.CharField(choices=[('Круглый', 'Круглый'), ('Квадратный', 'Квадратный'), ('Прямоугольный', 'Прямоугольный'), ('Восьмиугольный', 'Восьмиугольный'), ('Асимметричный', 'Асимметричный')], max_length=100, verbose_name='Форма корпуса')),
                ('diameter', models.PositiveIntegerField(verbose_name='Диаметр корпуса (мм)')),
                ('water_resistance', models.CharField(choices=[('30 метров', '30 метров'), ('50 метров', '50 метров'), ('100 метров', '100 метров'), ('200 метров', '200 метров'), ('300 метров и выше', '300 метров и выше')], max_length=100, verbose_name='Водонепроницаемость')),
                ('movement', models.CharField(choices=[('Автоматический', 'Автоматический'), ('Кварцевый', 'Кварцевый'), ('Механический', 'Механический'), ('Цифровой', 'Цифровой')], max_length=100, verbose_name='Механизм')),
                ('watch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='watch.watch', verbose_name='Часы')),
            ],
            options={
                'verbose_name': 'Характеристикa',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='watches', verbose_name='Изображение')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='watch.watch')),
            ],
            options={
                'verbose_name': 'Изображени',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
