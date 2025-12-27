from .models import (NetworkStudents,
                     NetworkTeacher, Category, SubCategory, Language,
                     Course, Chapter, Lesson, Assignment, Exam, Question,
                     Option)
from modeltranslation.translator import TranslationOptions,register

@register(NetworkStudents)
class NetworkStudentsTranslationOptions(TranslationOptions):
    fields = ('network_name',)

@register(NetworkTeacher)
class NetworkTeacherTranslationOptions(TranslationOptions):
    fields = ('network_name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name',)

@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('language_name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Chapter)
class ChapterTranslationOptions(TranslationOptions):
    fields = ('chapter_name',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_name', 'content')

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('assignment_name', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_name',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_name',)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name',)




