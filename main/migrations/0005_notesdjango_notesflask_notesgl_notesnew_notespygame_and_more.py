# Generated by Django 4.1.4 on 2022-12-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_data_notes_data_django_notes_data_flask_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotesDjango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_django', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NotesFlask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_flask', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NotesGL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_git_linux', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NotesNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_new', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NotesPygame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pygame', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NotesPyqt5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pyqt5', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
