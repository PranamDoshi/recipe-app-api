# Generated by Django 4.0.6 on 2022-10-17 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Ingredients',
        ),
    ]
