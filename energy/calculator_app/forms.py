from django import forms


class Energy(forms.Form):
    invoice_one = forms.FloatField()
    invoice_two = forms.FloatField()
    invoice_three = forms.FloatField()
    tax_value = forms.FloatField()
    type_tax = forms.CharField(max_length=20)