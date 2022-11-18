# Generated by Django 4.1.3 on 2022-11-18 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='dia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='horarios.dia'),
            preserve_default=False,
        ),
    ]