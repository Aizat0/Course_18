import os
import django
from datetime import timedelta
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from course_app.models import (
    Teacher, Student, Category, SubCategory, Language,
    Course, Chapter, Lesson, Assignment, Exam, Question, Option,
    NetworkTeacher, NetworkStudents, UserProfile
)
from django.contrib.auth.hashers import make_password


def create_teachers():
    """Создание учителей"""
    teachers_data = [
        {
            'username': 'ivan_petrov',
            'first_name': 'Иван',
            'last_name': 'Петров',
            'email': 'ivan.petrov@example.com',
            'age': 35,
            'bio': 'Разработчик с 10-летним опытом. Специализируюсь на Python и Django.',
            'phone_number': '+996555123456',
        },
        {
            'username': 'anna_smith',
            'first_name': 'Анна',
            'last_name': 'Смит',
            'email': 'anna.smith@example.com',
            'age': 28,
            'bio': 'Frontend-разработчик, эксперт по React и современным веб-технологиям.',
            'phone_number': '+996555234567',
        },
        {
            'username': 'sergey_web',
            'first_name': 'Сергей',
            'last_name': 'Веб',
            'email': 'sergey.web@example.com',
            'age': 42,
            'bio': 'Fullstack-разработчик, ментор, автор курсов по веб-разработке.',
            'phone_number': '+996555345678',
        },
        {
            'username': 'maria_design',
            'first_name': 'Мария',
            'last_name': 'Дизайнова',
            'email': 'maria.design@example.com',
            'age': 30,
            'bio': 'UI/UX дизайнер с опытом работы в крупных IT-компаниях.',
            'phone_number': '+996555456789',
        },
        {
            'username': 'alex_data',
            'first_name': 'Александр',
            'last_name': 'Данин',
            'email': 'alex.data@example.com',
            'age': 38,
            'bio': 'Data Scientist, специалист по машинному обучению и анализу данных.',
            'phone_number': '+996555567890',
        },
    ]

    teachers = []
    for data in teachers_data:
        teacher, created = Teacher.objects.get_or_create(
            username=data['username'],
            defaults={
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': make_password('password123'),
                'age': data['age'],
                'role': 'teacher',
                'bio': data['bio'],
                'phone_number': data['phone_number'],
            }
        )
        teachers.append(teacher)
        print(f"✓ Учитель: {teacher.first_name} {teacher.last_name}")

    return teachers


def create_categories():
    """Создание категорий"""
    categories_data = [
        'Программирование',
        'Дизайн',
        'Маркетинг',
        'Бизнес',
        'Языки',
    ]

    categories = []
    for name in categories_data:
        cat, created = Category.objects.get_or_create(category_name=name)
        categories.append(cat)
        print(f"✓ Категория: {name}")

    return categories


def create_subcategories(categories):
    """Создание подкатегорий"""
    subcategories_data = [
        ('Web-разработка', categories[0]),
        ('Мобильная разработка', categories[0]),
        ('Data Science', categories[0]),
        ('UI/UX дизайн', categories[1]),
        ('Графический дизайн', categories[1]),
    ]

    subcategories = []
    for name, category in subcategories_data:
        subcat, created = SubCategory.objects.get_or_create(
            subcategory_name=name,
            defaults={'category': category}
        )
        subcategories.append(subcat)
        print(f"✓ Подкатегория: {name}")

    return subcategories


def create_languages():
    """Создание языков"""
    languages_data = ['Русский', 'English', 'Кыргызча', 'Deutsch', 'Español']

    languages = []
    for name in languages_data:
        lang, created = Language.objects.get_or_create(language_name=name)
        languages.append(lang)
        print(f"✓ Язык: {name}")

    return languages


def create_courses(teachers, subcategories, languages):
    """Создание курсов"""
    courses_data = [
        {
            'course_name': 'Python для начинающих',
            'description': 'Полный курс по Python с нуля. Изучите основы программирования, работу с данными и создание приложений.',
            'subcategory': subcategories[0],
            'level': 'easy',
            'price': Decimal('4999.00'),
            'created_by': teachers[0],
            'language': languages[0],
            'is_certificate': True,
        },
        {
            'course_name': 'Django: создание веб-приложений',
            'description': 'Научитесь создавать современные веб-приложения на Django. REST API, аутентификация, базы данных.',
            'subcategory': subcategories[0],
            'level': 'medium',
            'price': Decimal('7999.00'),
            'created_by': teachers[0],
            'language': languages[0],
            'is_certificate': True,
        },
        {
            'course_name': 'React - современная frontend-разработка',
            'description': 'Освойте React, hooks, Redux и создавайте интерактивные пользовательские интерфейсы.',
            'subcategory': subcategories[0],
            'level': 'medium',
            'price': Decimal('8999.00'),
            'created_by': teachers[1],
            'language': languages[1],
            'is_certificate': True,
        },
        {
            'course_name': 'UI/UX дизайн: от идеи до прототипа',
            'description': 'Полный курс по UI/UX дизайну. Figma, принципы дизайна, создание прототипов и юзабилити-тестирование.',
            'subcategory': subcategories[3],
            'level': 'easy',
            'price': Decimal('6499.00'),
            'created_by': teachers[3],
            'language': languages[0],
            'is_certificate': True,
        },
        {
            'course_name': 'Data Science с Python',
            'description': 'Анализ данных, машинное обучение, pandas, numpy, scikit-learn. Практические проекты.',
            'subcategory': subcategories[2],
            'level': 'advanced',
            'price': Decimal('12999.00'),
            'created_by': teachers[4],
            'language': languages[1],
            'is_certificate': True,
        },
        {
            'course_name': 'Fullstack разработка: JavaScript + Node.js',
            'description': 'Станьте fullstack-разработчиком. Express, MongoDB, React, deployment на реальных проектах.',
            'subcategory': subcategories[0],
            'level': 'advanced',
            'price': Decimal('11999.00'),
            'created_by': teachers[2],
            'language': languages[0],
            'is_certificate': True,
        },
    ]

    courses = []
    for data in courses_data:
        course, created = Course.objects.get_or_create(
            course_name=data['course_name'],
            defaults=data
        )
        courses.append(course)
        print(f"✓ Курс: {course.course_name} - {course.price} сом")

    return courses


def create_chapters(courses):
    """Создание глав для курсов"""
    chapters_data = {
        'Python для начинающих': [
            'Введение в Python',
            'Условия и циклы',
            'Функции и модули',
            'Работа с файлами',
            'ООП в Python',
        ],
        'Django: создание веб-приложений': [
            'Основы Django',
            'Модели и базы данных',
            'Views и Templates',
            'Django REST Framework',
            'Деплой приложения',
        ],
        'React - современная frontend-разработка': [
            'Основы React и JSX',
            'Компоненты и Props',
            'State и Hooks',
            'React Router',
            'Redux и управление состоянием',
        ],
    }

    chapters = []
    for course in courses[:3]:  # Создаем главы для первых 3 курсов
        if course.course_name in chapters_data:
            for chapter_name in chapters_data[course.course_name]:
                chapter, created = Chapter.objects.get_or_create(
                    chapter_name=chapter_name,
                    course=course
                )
                chapters.append(chapter)
                print(f"  ✓ Глава: {chapter_name}")

    return chapters


def create_lessons(chapters):
    """Создание уроков"""
    if not chapters:
        return []

    lessons_data = [
        {
            'lesson_name': 'Установка Python и первая программа',
            'content': 'В этом уроке вы узнаете, как установить Python на свой компьютер и напишете первую программу Hello World.',
            'chapter': chapters[0],
        },
        {
            'lesson_name': 'Переменные и типы данных',
            'content': 'Изучаем основные типы данных Python: int, float, str, bool. Работа с переменными и операции.',
            'chapter': chapters[0],
        },
        {
            'lesson_name': 'Условные конструкции if-elif-else',
            'content': 'Узнаете, как использовать условные операторы для создания логики в программах.',
            'chapter': chapters[1],
        },
        {
            'lesson_name': 'Циклы for и while',
            'content': 'Изучаем циклы для повторения действий и обработки коллекций данных.',
            'chapter': chapters[1],
        },
        {
            'lesson_name': 'Создание и вызов функций',
            'content': 'Научитесь создавать переиспользуемый код с помощью функций. Параметры и возвращаемые значения.',
            'chapter': chapters[2],
        },
    ]

    lessons = []
    for data in lessons_data:
        lesson, created = Lesson.objects.get_or_create(
            lesson_name=data['lesson_name'],
            defaults=data
        )
        lessons.append(lesson)
        print(f"    ✓ Урок: {lesson.lesson_name}")

    return lessons


def create_exams(chapters):
    """Создание экзаменов"""
    if not chapters:
        return []

    exams_data = [
        {
            'exam_name': 'Финальный тест: Основы Python',
            'chapter': chapters[0],
            'duration': timedelta(minutes=30),
        },
        {
            'exam_name': 'Проверка знаний: Условия и циклы',
            'chapter': chapters[1],
            'duration': timedelta(minutes=25),
        },
        {
            'exam_name': 'Тест по функциям',
            'chapter': chapters[2],
            'duration': timedelta(minutes=20),
        },
    ]

    exams = []
    for data in exams_data:
        exam, created = Exam.objects.get_or_create(
            exam_name=data['exam_name'],
            chapter=data['chapter'],
            defaults={'duration': data['duration']}
        )
        exams.append(exam)
        print(f"      ✓ Экзамен: {exam.exam_name}")

    return exams


def create_questions_and_options(exams):
    """Создание вопросов и вариантов ответов"""
    if not exams:
        return

    questions_data = [
        {
            'exam': exams[0],
            'question_name': 'Что выведет print(type(5))?',
            'score': 2,
            'options': [
                ('<class "int">', True),
                ('<class "float">', False),
                ('<class "str">', False),
                ('int', False),
            ]
        },
        {
            'exam': exams[0],
            'question_name': 'Какой оператор используется для возведения в степень?',
            'score': 1,
            'options': [
                ('**', True),
                ('^', False),
                ('pow', False),
                ('*', False),
            ]
        },
        {
            'exam': exams[1],
            'question_name': 'Какой цикл выполнится ровно 5 раз?',
            'score': 3,
            'options': [
                ('for i in range(5):', True),
                ('for i in range(1, 5):', False),
                ('while i < 5:', False),
                ('for i in [1,2,3,4]:', False),
            ]
        },
    ]

    for q_data in questions_data:
        question, created = Question.objects.get_or_create(
            question_name=q_data['question_name'],
            exam=q_data['exam'],
            defaults={'score': q_data['score']}
        )

        for option_text, is_correct in q_data['options']:
            Option.objects.get_or_create(
                question=question,
                option_name=option_text,
                defaults={'option_type': is_correct}
            )
        print(f"        ✓ Вопрос: {question.question_name}")


def main():
    print("=== Начало заполнения базы данных ===\n")

    print("1. Создание учителей...")
    teachers = create_teachers()

    print("\n2. Создание категорий...")
    categories = create_categories()

    print("\n3. Создание подкатегорий...")
    subcategories = create_subcategories(categories)

    print("\n4. Создание языков...")
    languages = create_languages()

    print("\n5. Создание курсов...")
    courses = create_courses(teachers, subcategories, languages)

    print("\n6. Создание глав...")
    chapters = create_chapters(courses)

    print("\n7. Создание уроков...")
    lessons = create_lessons(chapters)

    print("\n8. Создание экзаменов...")
    exams = create_exams(chapters)

    print("\n9. Создание вопросов и ответов...")
    create_questions_and_options(exams)

    print("\n=== Готово! Данные успешно загружены ===")
    print(f"Создано: {len(teachers)} учителей, {len(courses)} курсов")


if __name__ == '__main__':
    main()