# Generated by Django 4.0.2 on 2022-02-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_client_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='cost',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
