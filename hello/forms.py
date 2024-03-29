# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:45:15 2019

@author: chiribiz2
"""

from django import forms
from.models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        
class HelloForm(forms.Form):        
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
    
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)
    
class CheckForm(forms.Form):
    str = forms.CharField(label='String')
    
    def claen(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        friend = ['title', 'content', 'friend']