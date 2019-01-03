from django import forms

from football.models import Team


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name','player_number','jersey_color', 'jersey_image', )
