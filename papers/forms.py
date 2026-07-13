from django import forms
from papers.models import Paper, Author, Topic, ReadingNote, Experiment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'affiliation']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'authors', 'year', 'venue',
                  'arxiv_id', 'status', 'rating', 'topics', 'abstract']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'arxiv_id': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'topics': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ReadingNoteForm(forms.ModelForm):
    class Meta:
        model = ReadingNote
        fields = ['content', 'page_number']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'page_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['title', 'status', 'result_notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'result_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }