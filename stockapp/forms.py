
from django import forms 
from . models import Things

class CalcForm( forms.Form):
    amount = forms.IntegerField(initial=10);

#class Things( models.Model):
 #   amount = models.IntegerField();
  #  name = models.CharField( max_length=30)

class ThingForm( forms.ModelForm):
    class Meta:
        model = Things
        fields = ['amount', 'name']