# Generated by Django 5.2.1 on 2025-05-22 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=50, unique=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_code', models.CharField(max_length=50, unique=True)),
                ('ingredient_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_code', models.CharField(max_length=50, unique=True)),
                ('receipe_name', models.CharField(max_length=100)),
                ('category_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Receipe.category')),
            ],
        ),
        migrations.CreateModel(
            name='ReceipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('wastage', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipe.receipe')),
            ],
        ),
        migrations.AddField(
            model_name='receipe',
            name='ingredients',
            field=models.ManyToManyField(through='Receipe.ReceipeIngredient', to='Receipe.ingredient'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_code', models.CharField(max_length=50, unique=True)),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Receipe.category')),
            ],
        ),
        migrations.AddField(
            model_name='receipe',
            name='subcategory_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Receipe.subcategory'),
        ),
    ]
