# Generated by Django 5.1.2 on 2024-11-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_knowledgeitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowledgeitem',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='knowledgeitem',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
