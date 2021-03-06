# Generated by Django 3.2.3 on 2021-05-20 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataSchemaPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_separator', models.CharField(choices=[(',', 'Comma'), (';', 'Semicolon')], max_length=128)),
                ('string_character', models.CharField(choices=[("'", 'Single Quote'), ('"', 'Double Quote')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='schema/sets/')),
                ('rows', models.IntegerField()),
                ('status', models.CharField(choices=[('Ready', 'Ready'), ('Processing', 'Processing'), ('Not Ready', 'Not Ready')], default='Not Ready', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='data_schemas.dataschema')),
            ],
        ),
        migrations.CreateModel(
            name='DataSchemaColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('name', 'Full Name'), ('email', 'Email'), ('phone_number', 'Phone Number'), ('date', 'Date'), ('company', 'Company Name')], max_length=128)),
                ('order', models.IntegerField()),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='data_schemas.dataschema')),
            ],
        ),
        migrations.AddField(
            model_name='dataschema',
            name='preferences',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schema', to='data_schemas.dataschemapreferences'),
        ),
    ]
