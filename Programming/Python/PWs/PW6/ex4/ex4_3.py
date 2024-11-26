def fraction(numerator,denominator):
    fraction_dict = {'numerator':numerator,
                     'denominator':denominator}
    
    return fraction_dict

def sign_change(f1):
    f1['numerator'] = -f1['numerator']
    return f1

f1 = fraction(2,5)
f1 = sign_change(f1)
print(f'{f1["numerator"]}/{f1["denominator"]}')