from django.core.validators import MinLengthValidator
from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,

    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 'Software Developer'
    QA_ENGINEER = 'QA Engineer'
    MARKETING_SPECIALIST = 'Marketing Specialist'

    JOB_TITLES = (
        SOFTWARE_DEVELOPER,
        QA_ENGINEER,
        MARKETING_SPECIALIST,
    )

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    AMAZON = 'Amazon'

    COMPANIES = (
        SOFT_UNI,
        GOOGLE,
        AMAZON,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
        validators=(
            MinLengthValidator(10),
        )
    )

    job_title = models.CharField(
        max_length=max(len(j) for j in JOB_TITLES),
        choices=(
            (j, j) for j in JOB_TITLES
        ),

    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=(
            (c, c) for c in COMPANIES
        ),
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('first_name', )


class User(models.Model):
    email = models.EmailField()

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee,
    )

