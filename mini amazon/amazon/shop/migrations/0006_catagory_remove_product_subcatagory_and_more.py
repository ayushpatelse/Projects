# Generated by Django 4.2.2 on 2023-07-03 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_brand_product_subcatagory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sname', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcatagory',
        ),
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.catagory'),
        ),
    ]
