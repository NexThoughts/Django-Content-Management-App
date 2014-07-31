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

    def clean_comment(self):
        Comment = self.cleaned_data['Comment']
        if (Comment == ''):
            raise forms.ValidationError("Cannot Be Blank")
        else:
            return Comment

    class Meta:
        model = Comments
        fields = ('Comment',)
        widgets = {
          'Comment': forms.Textarea(attrs={'rows':2, 'cols':50,'placeholder': "Add a Comment",'required':'true' }),
        }

