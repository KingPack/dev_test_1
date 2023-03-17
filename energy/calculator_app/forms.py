from django import forms

class EnergyCalculatorForm(forms.Form):
    consumption_month1 = forms.FloatField(label='Consumption Month 1 (kWh)')
    consumption_month2 = forms.FloatField(label='Consumption Month 2 (kWh)')
    consumption_month3 = forms.FloatField(label='Consumption Month 3 (kWh)')
    tariff = forms.FloatField(label='Tariff')
    tariff_type = forms.ChoiceField(label='Tariff Type',
        choices=[
            ('Residencial', 'Residencial'),
            ('Comercial', 'Comercial'),
            ('industrial', 'Industrial')])
