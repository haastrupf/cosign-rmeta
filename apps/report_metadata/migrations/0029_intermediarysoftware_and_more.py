# Generated by Django 5.0.2 on 2024-03-15 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0028_programareatype_alter_anonyomizeddataneed_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediarySoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=255, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('version', models.CharField(blank=True, default='', max_length=255)),
                ('vendor_name', models.CharField(blank=True, default='', max_length=255)),
                ('vendor_poc', models.TextField(blank=True, default='', max_length=2048, verbose_name='Vendor Point of Contact')),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Software:  Intermediary',
                'verbose_name_plural': 'Software: Intermediaries',
            },
        ),
        migrations.AlterField(
            model_name='sourcesystem',
            name='output_data_other_types',
            field=models.ManyToManyField(blank=True, related_name='source_other_supported_output_data_types', to='report_metadata.healthdatatype'),
        ),
        migrations.AlterField(
            model_name='sourcesystem',
            name='output_data_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_data_output_type', to='report_metadata.healthdatatype'),
        ),
        migrations.AlterField(
            model_name='sourcesystem',
            name='output_transport_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_transport_out', to='report_metadata.datatransporttype'),
        ),
        migrations.CreateModel(
            name='IntermediarySystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=255, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('vendor_name', models.CharField(blank=True, default='', max_length=255)),
                ('vendor_poc', models.TextField(blank=True, default='', max_length=2048, verbose_name='Vendor Point of Contact')),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('input_data_other_types', models.ManyToManyField(blank=True, related_name='intermediary_input_data_other_types', to='report_metadata.healthdatatype')),
                ('input_data_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_main_data_input_type', to='report_metadata.healthdatatype')),
                ('input_transport_other_types', models.ManyToManyField(blank=True, related_name='intermediaryimport_transport_other_types', to='report_metadata.datatransporttype')),
                ('input_transport_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_transport_in', to='report_metadata.datatransporttype')),
                ('output_data_other_types', models.ManyToManyField(blank=True, related_name='intermediary_other_supported_output_data_types', to='report_metadata.healthdatatype')),
                ('output_data_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_data_output_type', to='report_metadata.healthdatatype')),
                ('output_transport_other_types', models.ManyToManyField(blank=True, related_name='intermediaryoutput_data_other_types', to='report_metadata.datatransporttype')),
                ('output_transport_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_transport_out', to='report_metadata.datatransporttype')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_software', to='report_metadata.intermediarysoftware')),
                ('source_system', models.ForeignKey(blank=True, help_text='Leave blank if original source (ie. not an intermediary system)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary_source_system', to='report_metadata.sourcesoftware')),
            ],
            options={
                'verbose_name': 'System: Intermediary',
                'verbose_name_plural': 'Systems: Intermediaries',
            },
        ),
    ]
