from abstracts.views import CRUDView
from games.models import Game 
from games.forms import CreateForm 


class GameView(CRUDView):
    model = Game
    form = CreateForm
    template_create = 'create_game.html'
<<<<<<< HEAD
    template_list = 'list_game.html'
=======
    template_list = 'list_game.html'


>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
