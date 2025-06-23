# credit_card_app/urls.py
from django.urls import path
from .views import store_credit_card, retrieve_credit_card, index

urlpatterns = [
    path('store_credit_card/', store_credit_card, name='store_credit_card'),
    path('retrieve_credit_card/', retrieve_credit_card, name='retrieve_credit_card'),
    path('',index, name='index'),  # Add this line for the main page
]
