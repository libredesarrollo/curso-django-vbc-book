from django.urls import path

from .views import BookCreateFormView, BookSaveFormView, BookSaveFormSuccessView, BookUpdateFormView, BookDeleteFormView, BookDetailFormView, BookListFormView

urlpatterns = [
    path('management/save',BookSaveFormView.as_view()),
    path('management/update/<int:pk>',BookUpdateFormView.as_view()),
    path('management/create',BookCreateFormView.as_view()),
    path('management/delete/<int:pk>',BookDeleteFormView.as_view()),
    path('management/detail/<int:pk>',BookDetailFormView.as_view()),
    path('management/index/',BookListFormView.as_view()),
    path('namagement/save/success',BookSaveFormSuccessView.as_view()),
]