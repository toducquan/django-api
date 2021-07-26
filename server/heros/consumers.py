from channels.generic.websocket import WebsocketConsumer
import json
from .views import hero_added

class WShero(WebsocketConsumer):
    def connect(self):
        self.accept()
        if len(hero_added) >= 1:
            hero = hero_added[len(hero_added) - 1]
            self.send(json.dumps({
                'hero': hero
            }))
