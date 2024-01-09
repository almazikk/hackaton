from django.urls import path
from .views import ChatListCreateView, MessageListCreateView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
]