# Generated by Django 4.2.1 on 2023-06-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0005_remove_pengunjung_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Laporan',
        ),
        migrations.AlterField(
            model_name='pengunjung',
            name='tanggal',
            field=models.DateField(auto_now_add=True),
        ),
    ]
