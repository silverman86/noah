# Generated by Django 3.0.8 on 2020-09-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_tag_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='bg_color',
            field=models.CharField(default='#c41fff', max_length=7, verbose_name='Background Color'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description (optional)'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='fg_color',
            field=models.CharField(default='#FFFFFF', max_length=7, verbose_name='Foreground Color'),
        ),
    ]
