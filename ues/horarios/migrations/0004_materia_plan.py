# Generated by Django 4.1.3 on 2022-11-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0003_materia_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='plan',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
