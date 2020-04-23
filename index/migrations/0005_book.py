# Generated by Django 2.1.4 on 2019-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190424_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=30)),
                ('authorbook', models.CharField(max_length=120)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('links', models.TextField()),
            ],
        ),
    ]