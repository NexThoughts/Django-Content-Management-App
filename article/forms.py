from django import forms
from models import Article, Comments

class AddArticle(forms.ModelForm):

    File = forms.FileField(required=False)
    group_id = forms.CharField(required=False)
    Author_id = forms.CharField(required=False)

    class Meta:
        model = Article
        fields = ('Title', 'Body','File','group_id','Author_id')

    def clean_Title(self):
        Title = self.cleaned_data['Title']
        if (Title == ''):
            raise forms.ValidationError("Cannot Be Blank")
        else:
            return Title
    def clean_Body(self):
        Body = self.cleaned_data['Body']
        if (Body == ''):
            raise forms.ValidationError("Cannot Be Blank")
        else:
            return Body



class AddComments(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('Comment',)
        widgets = {
          'Comment': forms.Textarea(attrs={'rows':2, 'cols':30,'placeholder': "Add a Comment"}),
        }