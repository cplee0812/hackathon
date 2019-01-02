from django.contrib import admin
from .models import Team
from .models import Player
from .models import Match
from .models import MatchStat
from .models import broadcast_msg
# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(MatchStat)
admin.site.register(broadcast_msg)