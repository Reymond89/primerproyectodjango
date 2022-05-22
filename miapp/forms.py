from django import forms
from django.core import validators

class formArticle(forms.Form):

    title = forms.CharField(
        label = "titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'mete el titulo',
                'class': 'titulo_form_article'
           }
        ),
        validators=[
            validators.MinLengthValidator(4, 'el titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$','el titulo esta mal formado','invalid_title')
            
        ]
    
    )

    content = forms.CharField(
        label ="contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(50, 'has puesto mucho texto')
        ]
        
        )
           

    content.widget.attrs.update({
         'placeholder': 'mete el contenido ya',
                'class': 'contenido_form_article',
                'id':'contenido_form'
            })

    

    public_options = [
        (1, 'si'),
        (0, 'no')
    ]


    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )