from django import forms

from football.models import Team, Match, broadcast_msg, MatchStat


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name','player_number','jersey_color', 'jersey_image', )
