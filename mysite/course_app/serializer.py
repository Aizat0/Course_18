from rest_framework import serializers
from .models import (UserProfile, Teacher, Student, NetworkStudents,
                     NetworkTeacher, Category, SubCategory, Language,
                     Course, Chapter, Lesson, Assignment, Exam, Question,
                     Option, Certificate, Review, ReviewLike)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'role']

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'role', 'bio', 'phone_number']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class NetworkStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkStudents
        fields = '__all__'

class NetworkTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkTeacher
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'category']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    created_by = TeacherListSerializer(read_only=True)
    average_ratings = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level', 'language', 'price',  'average_ratings', 'count_people',  'created_by', 'course_photo', 'is_certificate']

    def get_average_ratings(self, obj):
        return obj.get_average_ratings()

    def get_count_people(self, obj):
        return obj.get_count_people()


class AssignmentSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(format='%Y-%M %H:%m')
    class Meta:
        model = Assignment
        fields = ['id', 'assignment_name', 'description', 'due_date']

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lesson_name', 'lesson_image']

class LessonDetailSerializer(serializers.ModelSerializer):
    lessons = AssignmentSerializer(read_only=True, many=True)
    class Meta:
        model = Lesson
        fields = ['id', 'lesson_name', 'lesson_image', 'lesson_file', 'content', 'lesson_video', 'lessons']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_name']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        fields = ['id', 'question_name', 'score', 'options']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_name', 'duration']

class ExamDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Exam
        fields = ['id', 'exam_name', 'duration', 'questions']

class ChapterSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(many=True, read_only=True)
    exams = ExamListSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'lessons', 'exams']


class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'certificate_url']

class CertificateDetailSerializer(serializers.ModelSerializer):
    courses = CourseListSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = ['id', 'courses', 'certificate_url', 'issued_at']

class ReviewLikeSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%Y-%H-%m')
    class Meta:
        model = ReviewLike
        fields = ['id', 'like', 'dislike', 'created_date']

class ReviewSerializer(serializers.ModelSerializer):
    review_like = ReviewLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'ratings', 'text', 'created_date', 'review_like']


class CourseDetailSerializer(serializers.ModelSerializer):
    created_by = TeacherDetailSerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    chapter_course = ChapterSerializer(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level', 'language', 'price', 'created_by', 'created_at',
                  'updated_at', 'course_photo', 'is_certificate', 'subcategory', 'chapter_course',
                  'reviews']
