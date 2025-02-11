# Generated by Django 4.1 on 2024-05-23 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pan.models
import pan.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('secret_key', models.CharField(db_index=True, max_length=10, verbose_name='Поделиться ключом')),
                ('signature', models.CharField(max_length=70, verbose_name='Цифровая подпись')),
                ('expire_time', models.DateTimeField(verbose_name='Срок годности')),
                ('summary', models.CharField(blank=True, max_length=100, verbose_name='Поделиться дополнительным описанием')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'Общий доступ к файлам',
                'verbose_name_plural': 'Общий доступ к файлам',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('type_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('suffix', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Суффикс')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'Тип файла',
                'verbose_name_plural': 'Тип файла',
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('limit_name', models.CharField(max_length=50, verbose_name='Ограниченное имя')),
                ('limit_key', models.CharField(max_length=50, unique=True, verbose_name='Ограниченные символы')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'условия',
                'verbose_name_plural': 'условия',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('role_name', models.CharField(max_length=50, verbose_name='Имя персонажа')),
                ('role_key', models.CharField(max_length=50, unique=True, verbose_name='Характер')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'роль',
                'verbose_name_plural': 'роль',
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='имя пользователя')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='IP-адрес :')),
                ('browser', models.CharField(max_length=200, verbose_name='браузер')),
                ('os', models.CharField(max_length=30, verbose_name='операционная система')),
                ('action', models.CharField(choices=[('0', 'войти'), ('1', 'опубликовывать'), ('2', 'Ошибка входа')], max_length=1, verbose_name='действия')),
                ('msg', models.CharField(max_length=100, verbose_name='данные')),
                ('action_time', models.DateTimeField(auto_now_add=True, verbose_name='время')),
            ],
            options={
                'verbose_name': 'Журнал посещений пользователя',
                'verbose_name_plural': 'Журнал посещений пользователя',
            },
        ),
        migrations.CreateModel(
            name='ShareRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('anonymous', models.GenericIPAddressField(blank=True, null=True, verbose_name='Анонимный пользователь')),
                ('file_share', models.ForeignKey(on_delete=models.SET(pan.models.get_deleted_file_share), to='pan.fileshare', verbose_name='Общий доступ к файлам')),
                ('recipient', models.ForeignKey(null=True, on_delete=models.SET(pan.models.get_deleted_user), to=settings.AUTH_USER_MODEL, verbose_name='получатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'Запись приема файла',
                'verbose_name_plural': 'Запись приема файла',
            },
        ),
        migrations.CreateModel(
            name='RoleLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('value', models.BigIntegerField(verbose_name='значение')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.limit', verbose_name='ограничение')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.role', verbose_name='роль')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'Ролевые ограничения',
                'verbose_name_plural': 'Ролевые ограничения',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('avatar', models.ImageField(default='default/user.svg', upload_to=pan.utils.get_unique_filename, verbose_name='аватар')),
                ('gender', models.CharField(blank=True, choices=[('0', 'Жен'), ('1', 'Муж')], max_length=1, verbose_name='пол')),
                ('role', models.ForeignKey(on_delete=models.SET(pan.models.get_deleted_role), to='pan.role', verbose_name='роль')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профиль пользователя',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('title', models.CharField(max_length=50, verbose_name='подпись')),
                ('content', models.TextField(verbose_name='Содержание уведомления')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'уведомление',
                'verbose_name_plural': 'уведомление',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('action', models.CharField(choices=[('0', 'сообщение'), ('1', 'заявление')], max_length=1, verbose_name='тип')),
                ('state', models.CharField(choices=[('0', 'Неподтвержденный'), ('1', 'Принятый'), ('2', 'Неудачный')], default='0', max_length=1, verbose_name='состояние')),
                ('content', models.TextField(verbose_name='Содержание сообщения')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщение',
            },
        ),
        migrations.CreateModel(
            name='GenericFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('remark', models.TextField(blank=True, verbose_name='Замечания')),
                ('file_name', models.CharField(max_length=100, verbose_name='Имя файла')),
                ('file_uuid', models.UUIDField(default=pan.utils.get_uuid, unique=True, verbose_name='Номер файла')),
                ('file_cate', models.CharField(choices=[('0', 'документ'), ('1', 'папка')], max_length=1, verbose_name='Классификация файлов')),
                ('file_size', models.BigIntegerField(default=0, verbose_name='Размер файла')),
                ('file_path', models.CharField(db_index=True, max_length=500, verbose_name='Путь к файлу')),
                ('del_flag', models.CharField(choices=[('0', 'Не собранный'), ('1', 'Переработанный')], default='0', max_length=1, verbose_name='Логотип')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
                ('file_type', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_file_type), to='pan.filetype', verbose_name='Тип файла')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', to_field='file_uuid', verbose_name='Улучшенный каталог')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления')),
            ],
            options={
                'verbose_name': 'Пользовательский файл',
                'verbose_name_plural': 'Пользовательский файл',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='fileshare',
            name='user_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', verbose_name='документ'),
        ),
        migrations.CreateModel(
            name='UserApproval',
            fields=[
            ],
            options={
                'verbose_name': 'Пользовательское приложение',
                'verbose_name_plural': 'Пользовательское приложение',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.message',),
        ),
        migrations.CreateModel(
            name='UserDir',
            fields=[
            ],
            options={
                'verbose_name': 'Папка пользователя',
                'verbose_name_plural': 'Папка пользователя',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.genericfile',),
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
            ],
            options={
                'verbose_name': 'Пользовательский файл',
                'verbose_name_plural': 'Пользовательский файл',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.genericfile',),
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
            ],
            options={
                'verbose_name': 'Сообщение пользователя',
                'verbose_name_plural': 'Сообщение пользователя',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.message',),
        ),
    ]
