from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

RoleChoices = (
('student', 'student'),
('teacher', 'teacher')
)

class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='user_photo/')
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(80)], null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Teacher(UserProfile):
    role = models.CharField(max_length=20, choices=RoleChoices)
    bio = models.TextField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.role


class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=RoleChoices)

    def __str__(self):
        return self.role

class NetworkTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=32)
    network_url = models.URLField()

    def __str__(self):
        return self.network_name

class NetworkStudents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=32)
    network_url = models.URLField()
    network_teachers = models.OneToOneField(NetworkTeacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.network_name



class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.subcategory_name

class Language(models.Model):
    language_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.language_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    LevelChoices = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('advanced', 'advanced')
    )
    level = models.CharField(max_length=32, choices=LevelChoices)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    course_photo = models.ImageField(upload_to='course_photo/')
    is_certificate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course_name}, {self.price}'

    def get_average_ratings(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(i.ratings for i in ratings) / ratings.count(), 2)
        return 0

    def get_count_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            if ratings.count() > 3:
                return '3+'
            return ratings.count()

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapter_course')

    def __str__(self):
        return self.chapter_name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=120)
    lesson_image = models.ImageField(upload_to='lesson_photo/')
    lesson_file = models.FileField(upload_to='lesson_file/', null=True, blank=True)
    content = models.TextField()
    lesson_video = models.FileField(upload_to='lesson_video/', null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f'{self.lesson_name}{self.chapter}'

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=64)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons')
    due_date = models.DateTimeField(verbose_name='Дедлайн')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.assignment_name} {self.lesson}'

class Exam(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='exams')
    exam_name = models.CharField(max_length=64)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.exam_name} {self.chapter}'

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_name = models.CharField(max_length=150)
    score = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_name = models.CharField(max_length=150, verbose_name='Вариант')
    option_type = models.BooleanField()


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    certificate_url = models.FileField(upload_to='certificate_url/')
    issued_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    ratings = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_like')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)










