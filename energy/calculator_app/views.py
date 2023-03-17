from .forms import EnergyCalculatorForm
from .calculator import calculator
from django.shortcuts import render


def energy_calculator_view(request):
    if request.method == 'POST':
        form = EnergyCalculatorForm(request.POST)

        if form.is_valid():
            # Get the form data
            consumption_month1 = form.cleaned_data['consumption_month1']
            consumption_month2 = form.cleaned_data['consumption_month2']
            consumption_month3 = form.cleaned_data['consumption_month3']
            tariff = form.cleaned_data['tariff']
            tariff_type = form.cleaned_data['tariff_type']

            result_calculator = calculator(
                    [consumption_month1, consumption_month2, consumption_month3],
                     tariff, tariff_type)

            # Render the results template
            return render(request, 'result.html', {'result_calculator': result_calculator})
    else:
        form = EnergyCalculatorForm()

    return render(request, 'index.html', {'form': form})
