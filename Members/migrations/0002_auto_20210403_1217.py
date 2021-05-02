# Generated by Django 3.1.7 on 2021-04-03 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('image', models.ImageField(blank=True, null=True, upload_to='faculty_photo/')),
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('position', models.CharField(choices=[('HOD', 'Head of Department'), ('ASCP', 'Associate Professor'), ('ASSP', 'Assistant Professor'), ('VF', 'Visiting Faculty')], max_length=40)),
                ('dept', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('ETE', 'Electronics and Telecommunication Engineering'), ('ISE', 'Information Science and Engineering'), ('EIE', 'Electronics and Instrumentation Engineering'), ('EEE', 'Electronics and Electrical Engineering'), ('ML', 'Medical Electronics'), ('BT', 'BioTechnology'), ('MECH', 'Mechanical Engineering'), ('CV', 'Civil Engineering'), ('CHE', 'Chemical Engineering'), ('IEM', 'Industrial Engineering and Managment')], max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='core_position',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('SPM', 'Project Manager'), ('PM', 'Project Director'), ('MM', 'Mission Manager'), ('MD', 'Mission Director'), ('TM', 'Team Manager')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('F', 'Founder'), ('C', 'Core Member'), ('M', 'Member')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nontechnical',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.student', unique=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.student', unique=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='subsystem',
            field=models.CharField(choices=[('PL', 'Payload'), ('ADCS', 'ADCS'), ('EPS', 'Power'), ('ODHS', 'ODHS'), ('GC', 'Communication'), ('STR', 'Structure and Thermal')], max_length=5),
        ),
    ]