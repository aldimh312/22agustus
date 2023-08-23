from django import forms
from website_app.models import Rating


class RatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bintang'].widget.attrs.update({'class': 'form-control'})
        self.fields['pesan'].widget.attrs.update({'class': 'form-control', 'rows': 2})
        self.fields['kesan'].widget.attrs.update({'class': 'form-control', 'rows': 2})

    class Meta:
        model = Rating
        fields = ['bintang', 'pesan', 'kesan']
        labels = {
            'bintang': 'Bintang',
            'pesan': 'Pesan',
            'kesan': 'Kesan',
        }


