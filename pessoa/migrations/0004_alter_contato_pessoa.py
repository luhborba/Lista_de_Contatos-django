# Generated by Django 4.1.3 on 2022-11-06 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='pessoa.pessoa'),
        ),
    ]
