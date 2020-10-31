from django import forms


class SubsRegistrationForm(forms.Form):
    age = forms.IntegerField(max_value=90, min_value=15)
    weight = forms.DecimalField(decimal_places=2, min_value=20.00, max_value=600.00)
    height = forms.DecimalField(decimal_places=2, max_value=9.00)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    goal = forms.ChoiceField(choices=[('weight-gain', 'Weight-Gain'), ('Weight-loss', 'Weight-loss')])
    bmi = forms.DecimalField(decimal_places=2, min_value=13, max_value=60)

