from django.shortcuts import render

# Create your views here.
def payslip(request):
    # Base values
    gross_salary = 20000
    basic = round(gross_salary * 0.50)
    hra = round(basic * 0.40)
    conveyance = 1600
    incentives = 0
    arrears = 0
    others = 0
    bonus =  0

    # Compute special allowance to balance gross
    earnings_total_so_far = basic + hra + conveyance
    special_allowance = gross_salary - earnings_total_so_far

    # Deductions
    pf_employee = round(basic * 0.12)
    esi_employee = round(gross_salary * 0.0075)
    other_deductions = 1050
    total_deductions = pf_employee + esi_employee + other_deductions

    # Net Salary
    net_salary = gross_salary - total_deductions

    # Employer Contributions
    pf_employer = round(basic * 0.12)
    esi_employer = round(gross_salary * 0.0325)
    ctc = gross_salary + pf_employer + esi_employer

    context = {
        'company': {
            'name': 'Jharkhand IT Solutions',
            'address': 'Riverview Colony, Near Vidya Vikas Public School, Boriya Road, Morabadi, Ranchi - 834006',
            'logo_url': 'images/logo-1.png',
        },
        'employee': {
            'name': 'Your Name',
            'emp_no': 'EMP-001',
            'designation': 'Developer',
            'pan': 'ABCDE1234F',
            'pf_no': 'NA',
            'uan_no': '100200300400',
            'doj': '01-01-2024',
            'lop_days': 0,
            'lop_amt': 0,
            'leaves': 'CL:3 SL:0 LWP:0 ML:0 ML:0 PL:0 SL(D):0 SL(M):0',
            'paid_days': 30,
        },
        'salary': {
            'month': 'May',
            'year': 2025,
            'basic': basic,
            'hra': hra,
            'conveyance': conveyance,
            'special_allowance': special_allowance,
            'bonus': bonus,
            'incentives': incentives,
            'arrears': arrears,
            'others': others,
            'pf': pf_employee,
            'esi': esi_employee,
            'professional_tax': 0,
            'health_insurance': 0,
            'tds': 0,
            'other_deductions': other_deductions,
            'advance': 0,
            'lop': 0,
        },
        'summary': {
            'gross': gross_salary,
            'total_deductions': total_deductions,
            'net_salary': net_salary,
            'employer_pf': pf_employer,
            'employer_esi': esi_employer,
            'parting_benefits': 0,
            'ctc': ctc,
            'credited_date': '31-May-2025'
        }
    }

    return render(request, 'payslip.html', context)