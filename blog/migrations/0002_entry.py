# Generated by Django 2.2.13 on 2020-08-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionTitle', models.CharField(max_length=200)),
                ('organisation', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
