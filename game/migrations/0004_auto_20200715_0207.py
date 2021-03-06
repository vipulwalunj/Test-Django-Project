# Generated by Django 3.0.8 on 2020-07-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200715_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('average', models.FloatField(null=True)),
                ('strike_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slot3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('average', models.FloatField(null=True)),
                ('strike_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slot4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('average', models.FloatField(null=True)),
                ('strike_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Player',
            new_name='Slot1',
        ),
    ]
