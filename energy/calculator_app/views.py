from django.http import HttpResponse
from django.template import loader


def index(request):
    ...


def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    consumption_average = sum(consumption) / len(consumption)

    if consumption_average < 10000:
        coverage = 0.90
        if tax_type == 'Residencial':
            applied_discount = 0.18
        elif tax_type == 'Commercial':
            applied_discount = 0.16
        elif tax_type == 'Industrial':
            applied_discount = 0.12

    elif consumption_average < 20000:
        coverage = 0.95
        if tax_type == 'Residencial':
            applied_discount = 0.22
        elif tax_type == 'Commercial':
            applied_discount = 0.18
        elif tax_type == 'Industrial':
            applied_discount = 0.15

    else:
        coverage = 0.99
        if tax_type == 'Residencial':
            applied_discount = 0.25
        elif tax_type == 'Commercial':
            applied_discount = 0.22
        elif tax_type == 'Industrial':
            applied_discount = 0.18

    cost_monthly = distributor_tax * consumption_average * coverage
    monthly_savings = cost_monthly * applied_discount
    annual_savings = monthly_savings * 12

    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )

