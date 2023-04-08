# Generated by Django 4.2 on 2023-04-06 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(help_text="Bo'lim nomini kiriting.....", max_length=500)),
            ],
            options={
                'verbose_name': "Bo'lim",
                'verbose_name_plural': "Bo'limlar",
            },
        ),
        migrations.CreateModel(
            name='Hodim_haqida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tug_yil', models.IntegerField()),
                ('millati', models.CharField(help_text='Millati.....', max_length=500)),
                ('malumoti', models.CharField(help_text="Ma'lumotini kiriting.....", max_length=500)),
                ('tamomlagan', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('mutaxasislik', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('ilmiy_daraja', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('til_bilish', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('mukofot', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('mehnat_faoliyati', models.TextField()),
            ],
            options={
                'verbose_name': 'Hodim haqida',
                'verbose_name_plural': "Hodim haqida ma'lumot",
            },
        ),
        migrations.CreateModel(
            name='Qarindoshlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qarindoshligi', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('qarindosh_ismi', models.CharField(help_text='Qarindoshni kiriting.....', max_length=500)),
                ('qarindosh_tug_yil', models.DateField()),
                ('yashash_joyi', models.CharField(help_text='Yashash manzil...', max_length=500)),
                ('ish_joyi', models.CharField(help_text='Ish manzil...', max_length=500)),
                ('hodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hodim_haqida')),
            ],
            options={
                'verbose_name': 'Hodim qarindoshi',
                'verbose_name_plural': 'Hodim qarindoshlari',
            },
        ),
        migrations.CreateModel(
            name='Hodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_sharifi', models.CharField(help_text='Hodim ism sharifini kiriting.....', max_length=200)),
                ('lavozimi', models.CharField(help_text='Lavozimni kiriting.....', max_length=200)),
                ('stavka', models.FloatField()),
                ('bolimi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bolimlar')),
            ],
            options={
                'verbose_name': 'Hodim',
                'verbose_name_plural': 'Hodimlar',
            },
        ),
        migrations.AddField(
            model_name='hodim_haqida',
            name='ism_sharifi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hodimlar'),
        ),
    ]
