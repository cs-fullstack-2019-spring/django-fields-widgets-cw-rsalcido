from django import forms
from .models import supeHero



STATUS= (
    ('RICH', 'SUPERPOWERS'),

)

WHAT_SUPERPOWER= (
    ('Flight', 'Speed'),
    ('Invisibility', 'Telekenetic'),
    ('Healing', 'Other')
)


CHARACTERICS= (
    ('Good', 'kinda good'),
    ('neutral', 'a little evil'),
    ('evil')
)

class supeHeroForm(forms.ModelForm):
    class Meta:
        model = supeHero
        fields = "__all__"
        labels ={
            "name": forms.CharField(max_length=20),
            "text": forms.CharField(max_length=200)
         }

        widgets = {

            "dropDown": forms.SelectMultiple(choices=STATUS),
            "dropDown2":forms.RadioSelect(choices=WHAT_SUPERPOWER),
            "dropDown3":forms.RadioSelect(choices=CHARACTERICS),

}

