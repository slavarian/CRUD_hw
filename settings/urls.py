from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from games.views import GameView
=======
from games.views import GameView 
>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
from user.views import UserView , CommentView


urlpatterns = [
    path('admin/', admin.site.urls),
    *GameView.as_my_view('game'),
    *UserView.as_my_view('user'),
<<<<<<< HEAD
    *CommentView.as_my_view('comment')
=======
    *CommentView.as_my_view('comment'),
>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
]
