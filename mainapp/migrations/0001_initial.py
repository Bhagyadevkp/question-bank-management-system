# Generated by Django 4.1 on 2022-08-17 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='feedback_m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='university',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='questionanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('answer', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=25)),
                ('year', models.IntegerField()),
                ('show', models.BooleanField(default=False)),
                ('timesAsked', models.CharField(blank=True, max_length=2, null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('important', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject')),
                ('university_select', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.university')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.university'),
        ),
    ]
