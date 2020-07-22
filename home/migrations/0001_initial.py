# Generated by Django 3.0.7 on 2020-07-21 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweredQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('player', models.CharField(max_length=30)),
                ('playerName', models.CharField(max_length=50)),
                ('response', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('following', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('player', models.CharField(max_length=30)),
                ('playerName', models.CharField(max_length=50)),
                ('response', models.CharField(max_length=300)),
                ('answered', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('playerName', models.CharField(max_length=50)),
                ('following', models.BooleanField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flw', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
