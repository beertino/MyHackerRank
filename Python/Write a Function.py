def is_leap(year):
    leap = False  
    if year-4*(year//4)==0 and year-100*(year//100)!=0:
        leap=True
    else: 
        if year-400*(year//400)==0:
            leap=True
    
    return leap

