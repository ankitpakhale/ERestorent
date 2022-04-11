# Generated by Django 2.1.5 on 2020-02-05 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(default='', max_length=100)),
                ('meal_qty', models.PositiveIntegerField(default=1)),
                ('meal_price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Site_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('m_no', models.PositiveIntegerField(default=0)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=100)),
                ('meal_qty', models.PositiveIntegerField(default=1)),
                ('meal_price', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Site_User'),
        ),
    ]
