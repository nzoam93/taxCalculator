def federalTaxOwed(origSalary, contributions):
    #assuming that the contributions are given as a percentage of the salary (i.e. 10%)
    salary = origSalary * (1 - contributions / 100)
    fedTaxOwed = 0
    if salary <= 0:
        fedTaxOwed = 0
    elif salary > 0 and salary <= 11000:
        fedTaxOwed = 0.1 * salary
    elif salary > 11000 and salary <= 44725:
        fedTaxOwed = 1100 + 0.12 * (salary - 11000)
    elif salary > 44725 and salary <= 95375:
        fedTaxOwed = 5147 + 0.22 * (salary - 44725)
    elif salary > 95375 and salary <= 182100:
        fedTaxOwed = 16290 + 0.24 * (salary - 95375)
    elif salary > 182101 and salary < 231250:
        fedTaxOwed = 37104 + 0.32 * (salary - 182100)
    elif salary > 231251 and salary < 578125:
        fedTaxOwed = 52838 + 0.35 * (salary - 231250)
    else:
        fedTaxOwed = 174238.25 + 0.37 * (salary - 578125)
    return round(fedTaxOwed, 2) #rounds to 2 decimal places

def californiaTaxOwed2022(origSalary, contributions):
    #assuming that the contributions are given as a percentage of the salary (i.e. 10%)
    salary = origSalary * (1 - contributions / 100)
    caliTaxOwed = 0
    if salary <= 0:
        caliTaxOwed = 0
    elif salary > 0 and salary <= 10099:
        caliTaxOwed = 0.01 * salary
    elif salary > 10099 and salary <= 23942:
        caliTaxOwed = 101 + 0.02 * (salary - 10099)
    elif salary > 23942 and salary <= 37788:
        caliTaxOwed = 377.85 + 0.04 * (salary - 23942)
    elif salary > 37788 and salary <= 52455:
        caliTaxOwed = 931.69 + 0.06 * (salary - 37788)
    elif salary > 52455 and salary <= 66295:
        caliTaxOwed = 1811.71 + 0.08 * (salary - 52455)
    elif salary > 66295 and salary <= 338639:
        caliTaxOwed = 2918.91 + 0.093 * (salary - 66295)
    elif salary > 338639 and salary <= 406364:
        caliTaxOwed = 28246.9 + 0.103 * (salary - 338639)
    elif salary > 406364 and salary <= 677275:
        caliTaxOwed = 35222.58 + 0.113 * (salary - 406364)
    else:
        caliTaxOwed = 65835.52 + 0.123 * (salary - 677275)
    return round(caliTaxOwed, 2) #rounds to two decimal places

def ficaTaxes(salary):
    #comprised of 6.2% social security and 1.45% medicare (total of 7.65%)
    return 0.0765 * salary

def totalTaxesOwed(salary, contributions):
    return federalTaxOwed(salary, contributions) + californiaTaxOwed2022(salary, contributions) + ficaTaxes(salary)

def actualPercentage(salary, contributions):
    return round((totalTaxesOwed(salary, contributions) / salary * 100), 2)

def diffInSalaries(salary1, contributions1, salary2, contributions2):
    salaryDiff = salary1 * (1 - contributions1 / 100) - salary2 * (1 - contributions2 / 100)
    taxesDiff = totalTaxesOwed(salary1, contributions1) - totalTaxesOwed(salary2, contributions2)
    return salaryDiff - taxesDiff

def netIncome(salary, contributions):
    income = salary - (salary * contributions / 100) - totalTaxesOwed(salary, contributions)
    return round(income, 2)

print(totalTaxesOwed(54000, 0))
print(totalTaxesOwed(126000, 22))
print(diffInSalaries(126000, 22, 54000, 0))
print(actualPercentage(126000, 22))
print(netIncome(126000, 22))
