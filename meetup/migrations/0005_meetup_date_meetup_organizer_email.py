# Generated by Django 4.0 on 2021-12-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_participant_meetup_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]