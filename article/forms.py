from django import forms
from models import Article, Comments

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
    Comment = forms.CharField(required=True)

    class Meta:
        model = Comments
        fields = ('Comment',)
