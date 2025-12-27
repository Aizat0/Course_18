from django.contrib import admin
from .models import (UserProfile, Teacher, Student, NetworkStudents,
                     NetworkTeacher, Category, SubCategory, Language,
                     Course, Chapter, Lesson, Assignment, Exam, Question,
                     Option, Certificate, Review, ReviewLike)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = SubCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NetworkStudentsInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = NetworkStudents
    extra = 1


@admin.register(NetworkTeacher)
class NetworkTeacherAdmin(TranslationAdmin):
    inlines = [NetworkStudentsInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Language, Course, Chapter, Lesson, Assignment, Exam, Question, Option)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(ReviewLike)


