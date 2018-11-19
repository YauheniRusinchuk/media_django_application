from django import forms



class FormComments(forms.Form):
    text = forms.CharField(label="",
        widget = forms.Textarea(attrs={
            'placeholder': 'Введите комментарий...',
            'class': 'input_comment'
        })
    )
