# Generated by Django 4.1.7 on 2023-05-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_images', '0006_myimage_delete_myimages_delete_users_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myimages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('imgurl', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Myimage',
        ),
    ]