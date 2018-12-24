# Generated by Django 2.1.4 on 2018-12-23 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_auto_20181213_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date_D',
            field=models.CharField(choices=[['First', '1st'], ['Second', '2nd'], ['Third', '3rd'], ['Forth', '4th'], ['Fifth', '5th'], ['Sixth', '6th'], ['Seventh', '7th'], ['Eighth', '8th'], ['Ninth', '9th'], ['Tenth', '10th'], ['Eleventh', '11th'], ['Twelfth', '12th'], ['Thirteenth', '13th'], ['Fourteenth', '14th'], ['Fifteenth', '15th'], ['Sixteenth', '16th'], ['Seventeenth', '17th'], ['Eighteenth', '18th'], ['Nineteenth', '19th'], ['Twentieth', '20th'], ['Twenty-first', '21st'], ['Twenty-second', '22nd'], ['Twenty-third', '23rd'], ['Twenty-fourth', '24th'], ['Twenty-fifth', '25th'], ['Twenty-sixth', '26th'], ['Twenty-seventh', '27th'], ['Twenty-eighth', '28th'], ['Twenty-ninth', '29th'], ['Thirtieth', '30th'], ['Thirty-first', '31st']], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='date_M',
            field=models.CharField(choices=[['Jan', '1'], ['Feb', '2'], ['Mar', '3'], ['Apl', '4'], ['May', '5'], ['Jun', '6'], ['Jul', '7'], ['Aug', '8'], ['Sep', '9'], ['Oct', '10'], ['Nov', '11'], ['Dec', '12']], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='date_Y',
            field=models.CharField(choices=[['2019', '2019'], ['2020', '2020'], ['2021', '2021'], ['2022', '2022'], ['2023', '2023'], ['2024', '2024']], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='location',
            field=models.CharField(choices=[['NTU SPN', 'NTU Sports Center(New)'], ['NTU SPO', 'NTU Sports Center(Old)'], ['NTU PG', 'NTU Playground'], ['NTUST SP', 'NTUST Sports Center'], ['NTUST PG', 'NTUST Playground']], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
