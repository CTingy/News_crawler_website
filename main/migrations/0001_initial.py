# Generated by Django 2.1 on 2018-08-14 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('pub_time', models.DateTimeField(blank=True, null=True)),
                ('crawl_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.TextField(blank=True, null=True)),
                ('src', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.News')),
            ],
        ),
    ]
