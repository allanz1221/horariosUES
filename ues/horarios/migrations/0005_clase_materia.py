# Generated by Django 4.1.2 on 2022-11-19 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0004_materia_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='horarios.materia'),
            preserve_default=False,
        ),
    ]
