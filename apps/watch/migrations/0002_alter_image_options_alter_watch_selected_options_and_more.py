# Generated by Django 4.2.4 on 2023-08-20 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='watch',
            name='selected_options',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Коробка', 'Коробка'), ('Документы', 'Документы'), ('Гарантия', 'Гарантия'), ('Футляр', 'Футляр'), ('Зарядное устройство', 'Зарядное устройство'), ('Кабель USB', 'Кабель USB')], max_length=255, null=True, verbose_name='Выбранные опции'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='case_material',
            field=models.CharField(choices=[('Нержавеющая сталь', 'Нержавеющая сталь'), ('Золото', 'Золото'), ('Титан', 'Титан'), ('Пластик', 'Пластик'), ('Дерево', 'Дерево')], max_length=100, verbose_name='Материал корпуса'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='case_shape',
            field=models.CharField(choices=[('Круглый', 'Круглый'), ('Квадратный', 'Квадратный'), ('Прямоугольный', 'Прямоугольный'), ('Восьмиугольный', 'Восьмиугольный'), ('Овальный', 'Овальный')], max_length=100, verbose_name='Форма корпуса'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='condition',
            field=models.CharField(choices=[('Хорошее', 'Хорошее'), ('Идеальное', 'Идеальное'), ('Новое', 'Новое'), ('Б/у', 'Б/у'), ('Требует восстановления', 'Требует восстановления')], max_length=100, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='gender',
            field=models.CharField(choices=[('Мужские', 'Мужские'), ('Женские', 'Женские'), ('Унисекс', 'Унисекс'), ('Детские', 'Детские')], max_length=100, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='movement',
            field=models.CharField(choices=[('Автоматический', 'Автоматический'), ('Кварцевый', 'Кварцевый'), ('Механический', 'Механический'), ('Цифровой', 'Цифровой'), ('Смарт-механизм', 'Смарт-механизм')], max_length=100, verbose_name='Механизм'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='strap_material',
            field=models.CharField(choices=[('Кожа', 'Кожа'), ('Нержавеющая сталь', 'Нержавеющая сталь'), ('Резина', 'Резина'), ('Металлический', 'Металлический'), ('Силикон', 'Силикон')], max_length=100, verbose_name='Материал ремешка/браслета'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='style',
            field=models.CharField(choices=[('Повседневные', 'Повседневные'), ('Официальные', 'Официальные'), ('Спортивные', 'Спортивные'), ('Дайверские', 'Дайверские'), ('Ретро', 'Ретро'), ('Умные', 'Умные'), ('Классические', 'Классические')], max_length=100, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='water_resistance',
            field=models.CharField(choices=[('30 метров', '30 метров'), ('50 метров', '50 метров'), ('100 метров', '100 метров'), ('200 метров', '200 метров'), ('300 метров и выше', '300 метров и выше'), ('Не водонепроницаемые', 'Не водонепроницаемые')], max_length=100, verbose_name='Водонепроницаемость'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('rating_design', models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Рейтинг дизайна')),
                ('rating_functionality', models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Рейтинг функциональности')),
                ('rating_quality', models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Рейтинг качества')),
                ('rating_value', models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Рейтинг цены и соотношения качества')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.watch', verbose_name='Место питания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]