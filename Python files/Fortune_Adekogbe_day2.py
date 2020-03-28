import random as rd
import string

def password_generator(length):
    '''
    This function takes in the desired pass word length as its parameter and
    returns the generated password.
    This password can contain digits, upper and lower case alphabets
    '''
    assert type(length)==int and length>0, 'An invalid length has been parsed in'
    strength = 'This password is weak' if length < 8 else ''
    characters = string.ascii_letters+string.digits
    password = rd.choices(characters,k=length)
    return ''.join(password)+'\n'+strength
print(f'Your password is {password_generator(5)}')