# Generated by Django 3.2.8 on 2021-10-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('kakao_url', models.TextField()),
                ('review', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('tag', models.IntegerField(blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category_num', models.IntegerField()),
            ],
        ),
    ]
