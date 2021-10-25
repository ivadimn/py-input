def calc_payment(summa, period, percent):
    i = percent / 100.0
    k = (i * ((1 + i) ** period)) / round((((1 + i) ** period) - 1), 2)
    return k * summa

def summa_percent(ostatok, percent):
    return ostatok * percent / 100

def get_payments(credit, ostatok, period, percent):
    summa_p = summa_percent(ostatok, percent)
    payment = calc_payment(credit, period, percent) - summa_p
    return payment, summa_p

def doWork(credit, period, percent, lenp):
    ostatok = credit
    p = 1
    while p <= lenp:
        print("\nПериод:", p)
        print("Остаток долга на начало периода:", ostatok)
        payment, summa_p = get_payments(credit, ostatok, period, percent)
        print("Выплачено процентов:", summa_p)
        print("Выплачено тела кредита:", payment)
        ostatok -= payment
        p += 1
    return ostatok

credit  = float(input("Введите сумму кредита: "))
period  = int(input("На сколько лет выдан? "))
percent = float(input("Сколько процентов годовых? "))

ostatok = doWork(credit, period, percent, 3)
print("\nОстаток долга:", ostatok)

print("\n==============================\n")
delta_period = int(input("На сколько лет продляется договор? "))
percent = float(input("Увеличение ставки до: "))
period += delta_period
ostatok = doWork(ostatok, period - 3, percent, period - 3)
print("\nОстаток долга:", ostatok)





