# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Category(models.Model):
    """
        Esta Classe define a categoria de Faixa em que certo usuario, seja ele aluno ou professor, se encontra.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='category_name')
    order = models.PositiveIntegerField(db_column='category_order')
    color = models.CharField(max_length=6, db_column='category_color')
    description = models.CharField(
        max_length=256, db_column='category_description')

    class Meta:
        db_table = 'tb_register_category_catalog'


class User(AbstractUser):
    """
        Esta Classe define um usuario dentro do sistema
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        max_length=100, blank=False, db_column='user_first_name')
    last_name = models.CharField(
        max_length=100, blank=False, db_column='user_last_name')
    cbj_id = models.CharField(max_length=100, db_column='cbj_id')
    primary_phone = models.CharField(max_length=100, db_column='primary_phone')
    alternative_phone = models.CharField(
        max_length=100, null=False, db_column='alternative_phone')
    email = models.EmailField(unique=True, db_column='email')
    cpf = models.IntegerField(db_column='cpf_number')
    notes = models.CharField(max_length=1000, db_column='notes', null=True)
    rg = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'tb_register_user'


class Profile(models.Model):
    """
        Esta Classe define os diferentes perfis dentro do sistema.
        Aluno
        Professor
        Secretário
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='profile_name')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_register_profile_catalog'


class UserProfile(models.Model):
    """
        Modelo Relacional entre Usuario, Perfil e Categoria
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        db_table = 'tb_register_user_x_profile'


class Dojo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='dojo_name')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_register_dojo'


class Class(models.Model):
    """
        Relação entre usuários de Perfil professor e usuarios de Perfil Estudante
    """
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='teacher_id',
                                related_name="%(app_label)s_%(class)s_teacher",
                                related_query_name="%(app_label)s_%(class)ss_teacher",
                                )
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='student_id',
                                related_name="%(app_label)s_%(class)s_student",
                                related_query_name="%(app_label)s_%(class)ss_student",
                                )
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, db_column='dojo_id',
                             related_name="%(app_label)s_%(class)s_dojo",
                             related_query_name="%(app_label)s_%(class)ss",
                             )

    class Meta:
        db_table = 'tb_register_class'


class StudentManager(models.Manager):
    """
        Controlador de Buscas a Base filtrado por Alunos
    """

    def get_queryset(self):
        """
        Este Método Filtra o modelo base
        :return: Objeto QuerySet
        """
        return super().get_queryset().filter(profile_id__exact=2)


class Student(UserProfile):
    """
        Classe que controla todos os usuarios que são Alunos
    """
    objects = StudentManager()

    @property
    def teacher(self):
        """
            Retorna um QuerySet com o Professor deste estudante
        :return:
        """
        return self.objects.first().filter(register_class_student=self)

    class Meta:
        proxy = True


class TeacherManager(models.Manager):
    """
        Controlador de Buscas a Base filtrado por Professores
    """

    def get_queryset(self):
        """
        Este Método Filtra o modelo base
        :return: Objeto QuerySet
        """
        return super().get_queryset().filter(profile_id__exact=1)


class Teacher(UserProfile):
    """
        Classe que controla todos os usuarios que são Professores
    """
    objects = TeacherManager()

    @property
    def students(self):
        """
            Retorna um QuerySet com todos os estudantes deste professor
        :return:
        """
        return self.objects.filter(register_class_teacher=self)

    class Meta:
        proxy = True


class Tournament(models.Model):
    """
    Classe que define um Torneio
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_column='tournament_name')
    initial_date = models.DateField()
    end_date = models.DateField()


class TournamentProfiles(models.Model):
    """
    Classe que contém os tipos de Perfis em um Torneio
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Participants(models.Model):
    """
    Class que relaciona os tipos de usuarios em um torneio por perfil
    """
    tournament = models.ForeignKey(Tournament,
                                   on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_tournament",
                                   related_query_name="%(app_label)s_%(class)ss_tournament",
                                   )
    user = models.ForeignKey(User,
                             on_delete=models.deletion.DO_NOTHING,
                             related_name="%(app_label)s_%(class)ss_participant",
                             related_query_name="%(app_label)s_%(class)ss_participant")
    profile = models.ForeignKey(TournamentProfiles,
                                on_delete=models.CASCADE)


class CompetitorManager(models.Manager):
    """
        Controlador de Buscas a Base filtrado por Competidor
    """

    def get_queryset(self):
        """
        Este Método Filtra o modelo base
        :return: Objeto QuerySet
        """
        return super().get_queryset().filter(profile_id__exact=1)


class Competitor(Participants):
    """
        Classe que define um Competidor em um torneio
    """

    objects = CompetitorManager()

    class Meta:
        proxy = True


class RefereeManager(models.Manager):
    """
        Controlador de Buscas a Base filtrado por Arbitro
    """

    def get_queryset(self):
        """
        Este Método Filtra o modelo base
        :return: Objeto QuerySet
        """
        return super().get_queryset().filter(profile_id__exact=2)


class Referee(Participants):
    """
        Classe que define um Arbitro em um torneio
    """

    objects = RefereeManager()

    class Meta:
        proxy = True


class Knockout(models.Model):
    """
    Classe que define um chaveamento em um torneio
    """
    id = models.AutoField(primary_key=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_tournament",
                                   related_query_name="%(app_label)s_%(class)ss_tournament")
    first_match = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                    related_name="%(class)s_first_match",
                                    related_query_name="first_matchs")
    second_match = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                     related_name="%(class)s_second_match",
                                     related_query_name="second_matchs")
    is_initial_match = models.BooleanField(default=True)
    date = models.DateField()
    time = models.TimeField()
    competitor_one = models.ForeignKey(Competitor, on_delete=models.CASCADE,
                                       related_name="%(app_label)s_%(class)s_competitor_one",
                                       related_query_name="%(app_label)s_%(class)ss_competitor_one")
    competitor_two = models.ForeignKey(Competitor, on_delete=models.CASCADE,
                                       related_name="%(app_label)s_%(class)s_competitor_two",
                                       related_query_name="%(app_label)s_%(class)ss_competitor_two")
    winner = models.ForeignKey(Competitor, on_delete=models.CASCADE,
                               related_name="%(app_label)s_%(class)ss_winner",
                               related_query_name="%(app_label)s_%(class)ss_winner")
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)ss_referee",
                                related_query_name="%(app_label)s_%(class)ss_referee")
