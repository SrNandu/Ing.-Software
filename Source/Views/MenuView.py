from Views.View import View
from Controllers.Controller import Controller


class MenuView(View):

    def __init__(self, controller: Controller):
        super().__init__(controller)
