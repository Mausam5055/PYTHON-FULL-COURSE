def find_leap_year(year1, year2):
    while year1 < year2:
        if (year1%4 == 0 and year1%100 !=0) or (year1%400 == 0) :
            print(year1, end = " ")
        year1 +=1

find_leap_year(1900,2022)
