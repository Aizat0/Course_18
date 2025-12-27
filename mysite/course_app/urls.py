from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, TeacherListAPIView, TeacherDetailAPIView, StudentViewSet, NetworkStudentsViewSet,
                     NetworkTeacherViewSet, CategoryViewSet, SubCategoryViewSet, LanguageViewSet,
                     CourseListAPIView, CourseDetailAPIView, ChapterViewSet, LessonListAPIView, LessonDetailAPIView,
                    AssignmentViewSet, ExamListAPIView, ExamDetailAPIView, QuestionViewSet,
                     OptionViewSet, CertificateListAPIView, CertificateDetailAPIView, ReviewViewSet, ReviewLikeViewSet,
                    RegisterView, CustomLoginView, LogoutView)


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'student', StudentViewSet)
router.register(r'network_students', NetworkStudentsViewSet)
router.register(r'network_teacher', NetworkTeacherViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'sub_category', SubCategoryViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'chapter', ChapterViewSet)
router.register(r'assignment', AssignmentViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'review_like', ReviewLikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('exam/', ExamListAPIView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
    path('certificate/', CertificateListAPIView.as_view(), name='certificate-list'),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate-detail'),
]