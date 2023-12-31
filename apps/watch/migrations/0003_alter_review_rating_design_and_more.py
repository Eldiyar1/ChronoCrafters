# Generated by Django 4.2.4 on 2023-08-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_alter_image_options_alter_watch_selected_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating_design',
            field=models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Дизайн'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating_functionality',
            field=models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Функциональность'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating_quality',
            field=models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Качество'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating_value',
            field=models.PositiveIntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Соотношения цены и качества'),
        ),
    ]
