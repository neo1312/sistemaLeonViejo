# Generated by Django 4.0.2 on 2022-02-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_client_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tipo',
            field=models.CharField(choices=[('menudeo', 'menudeo'), ('mayoreo', 'mayoreo')], default='menudeo', max_length=150, verbose_name='Type'),
        ),
    ]
