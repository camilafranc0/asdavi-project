# Generated by Django 5.0.6 on 2024-05-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asdavi', '0002_aluno_condicoes_familiar_aluno_nome_enfermidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='autorizacao',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Sim', max_length=50),
        ),
        migrations.AddField(
            model_name='aluno',
            name='interesse_educacional',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='necessidade_especial',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
