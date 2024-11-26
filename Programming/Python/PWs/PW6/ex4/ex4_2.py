def fraction(numerator,denominator):
    fraction_dict = {'numerator':numerator,
                     'denominator':denominator}
    
    return fraction_dict

f1 = fraction(2,5)
print(f'{f1["numerator"]}/{f1["denominator"]}')