# Generated by Django 4.0.2 on 2022-06-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_alter_sale_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='tipo',
            field=models.CharField(choices=[('menudeo', 'menudeo'), ('mayoreo', 'mayoreo')], default='menudeo', max_length=100),
        ),
    ]
