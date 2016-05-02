"""
upc.py
=====

"""
def generate_bar_widths(s):
    """Takes a barcode number as a string and translates it to a series
    of bar widths.
    
    :param s: the number to be translated to a series of bar widths
    :type s: str
    :return: a string representing the width of each bar, including the
    start, middle and end patterns (111, 11111, and 111)
    :rtype: str
    """
    # conversions for digits
    dict = {
            '0' : '3211',
            '1' : '2221',
            '2' : '2122',
            '3' : '1411',
            '4' : '1132',
            '5' : '1231',
            '6' : '1114',
            '7' : '1312',
            '8' : '1213',
            '9' : '3112',
    };
    translated = '';
    #add starting bars
    translated += '111';
    for i in range ((len(s)//2)):
        translated += dict[s[i]];
    
    #add center bars
    translated += '11111';
    
    for i in range ((len(s)//2), (len(s))):
        translated += dict[s[i]];
    
    #add end bars
    translated += '111';
    return translated;

def valid_barcode(s):
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit.
    
    Argument s is a string representing a barcode number.
    Return value is true if barcode is valid and false if barcode is invalid
    """
    # discard any invalid sizes
    if(len(s) != 12):
        return False;
    #Find odd and even totals, apply appropriate weights
    odd_val=0;
    for i in range(0,11,2):
        odd_val+= int(s[i]);
    odd_val = (odd_val * 3);
    
    even_val=0;
    for i in range(1,11,2):
        even_val+= int(s[i]);
    total_val=odd_val+even_val;
    #calculate the check digit and compare it to final item
    if(total_val % 10 == 0):
        print("Total val is %d"%total_val);
        if(s[-1] != '0'):
            return False;
    else:
        modu= (total_val % 10);
        check_dig = 10-modu;
        if(s[-1] != str(check_dig)):
            return False;
    #if no flags have been triggered, the return value is True
    return True;
