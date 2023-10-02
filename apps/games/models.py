from django.db import models
from django.core.validators import MinValueValidator

<<<<<<< HEAD
=======

>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
class Game(models.Model):
    """MY GAME!"""

    name: str = models.CharField(
        verbose_name='игра',
        max_length=200
    )
<<<<<<< HEAD

=======
>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
    price: float = models.DecimalField(
        verbose_name='цена',
        max_digits=11,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message='Мы деньги за игры не даём!')
        ]
    )
    poster: str = models.ImageField(
        verbose_name='постер',
        upload_to='posters'
    )
    rate: float = models.FloatField(
        verbose_name='рейтинг',
        max_length=5
    )
<<<<<<< HEAD
    quantity = models.PositiveIntegerField(
        verbose_name='количество в наличии',
        default=0
    )
=======
>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

<<<<<<< HEAD
=======

>>>>>>> e73de899ad15a5fa3b27a5ab8e0ca020d07c2ee5
