def sales():
    week1 = int(input('enter sales in first week '))
    week2 = int(input('enter sales in second week '))
    week3 = int(input('enter sales in third week '))
    week4 = int(input('enter sales in fourth week '))
    monthlysale = week1+week2+week3+week4
    commission = "No Commission"
    if monthlysale >50000:
        commission = float(monthlysale*0.05)
    if monthlysale >= 80000:
        remark = 'Excellent'
    elif monthlysale >= 60000:
        remark = 'Good'
    elif monthlysale >= 40000:
        remark = 'Average'
    else :
        remark = 'work hard'
    salesman = (monthlysale,commission,remark)
    print('Monthly sale =',monthlysale,'Commission =',commission,'Remark =',remark)

sales()

