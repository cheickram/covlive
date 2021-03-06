# Generated by Django 3.0.6 on 2020-06-05 08:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
    ]
