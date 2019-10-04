from django.urls import path
from .views import SubmitTootView

urlpatterns = [
    # ...
    path('', SubmitTootView.as_view(), name='submit-toot'),
    #path('thanks', AuthorUpdate.as_view(), name='author-update'),
]
