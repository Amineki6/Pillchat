# Generated by Django 4.2 on 2023-10-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_table_200_rows_delete_drugs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table_200_rows',
            options={'ordering': ['title'], 'verbose_name_plural': 'table_200_ROWS'},
        ),
        migrations.AlterField(
            model_name='table_200_rows',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
