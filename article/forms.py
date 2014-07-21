from django import forms
from models import Article, Comments
from django.forms import Textarea
class AddArticle(forms.ModelForm):


    Link = forms.CharField(required=False)
    File = forms.FileField(required=False)
    #pub_date=forms.DateTimeField(required=False)
    group_id = forms.CharField(required=False)
    Author_id = forms.CharField(required=False)
    class Meta:
        model = Article
        fields = ('Title', 'Body', 'Link','File','group_id','Author_id')

class AddComments(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('Comment',)
        widgets = {
          'Comment': forms.Textarea(attrs={'rows':2, 'cols':30,'placeholder': "Add a Comment"}),
        }