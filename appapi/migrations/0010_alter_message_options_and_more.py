# Generated by Django 4.2.7 on 2023-11-17 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0009_alter_message_options_remove_message_audio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('created_at',)},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]