#-------------------------------------function defenitions ------------------------------------------


#number simplifier (fractions)
def simplify_fraction(numer, denom):

     '''
     Simplifys a fraction

     Args:
     numer - numerater - integer
     denom - denomenator - integer
     
     returns the simplified fraction
     '''
     if denom == 0:
        return "You can't divide by 0, incompetent buffoon"

    #factor the diddly damn gcf
     common_divisor = gcd(numer, denom)
     (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
     if common_divisor == 1:
        return (numer, denom)
     else:
        # bunch of bs to make sure demon is negative
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)

#quadratic formula for factoring
def quadraticFunction(a,b,c):
     '''
     the quadratic formula in a functon
     
     args:
     a - as in the a value in the quadratic function - integer
     b - b value in quadratic function
     c - c value in quadratic function

     returns a formatted, factored version of the input
     
     ex.
     assuming a = 1, b =2, c = 1, it returns (1x+1)(1x+1)
     '''
     if (b**2-4*a*c >= 0):
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction(a,mult1)
        (num2,den2) = simplify_fraction(a,mult2)
        if ((num1 > a) or (num2 > a)):
            # simplify fraction will make too large of num and denom to try to make a sqrt work
            print("number_too_large!")
        else:
            #doing signs
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            print("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
     else:
        #if the part under the sqrt is negative, you have a solution with i
        print("You can't do this, it contains i.")
     return

#exit check function
def exitCheck():
     '''
     checks to see if the user is done with what they are doing
     
     no args

     returns nothing

     '''
     exitCheckInt = input('Is that all? (y/n) ') 
     if exitCheck == 'y':
          stillcalculating = False
     if exitCheck == 'n':
          pass
