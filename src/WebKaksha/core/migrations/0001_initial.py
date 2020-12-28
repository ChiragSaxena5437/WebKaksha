# Generated by Django 3.1.4 on 2020-12-27 09:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stu_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Enter your class(ex 10) ')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('class_st', models.IntegerField()),
                ('d_o_b', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('Bio', models.TextField(help_text='Tell others something about you', max_length=1000)),
                ('Pref_type', models.CharField(help_text='Left for now', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('class_st', models.IntegerField()),
                ('d_o_b', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('Bio', models.TextField(help_text='Tell others something about you', max_length=1000)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular student across whole staff', primary_key=True, serialize=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.student')),
            ],
        ),
    ]
