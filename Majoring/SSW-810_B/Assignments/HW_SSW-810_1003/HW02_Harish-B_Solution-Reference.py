"""
Assignment: Fraction calculator
Description: An calculator that takes 2 fraction in form of numerator and denominator as an input along with            
the operation to be performed from the user and calculates the result of the operation
Name: Harish Balasubramanian
CWID: 10474753"""

# A Global value used to store list of allowed operations
allowed_operation: str = ['+', '-', '*', '/', '==']

class Fractions:    
    """Fraction class containing of methods used to operate on the input fraction"""    
    
    def __init__(self, numerator: int, denominator: int) -> str:        
        
    # Check if denominator is 0 and throw an error (Since denominator of a fraction cannot be 0)        
        if denominator == 0:            
            raise ValueError("Denominator of the fraction cannot be 0.")        
        self.numerator = numerator        
        self.denominator = denominator    
        
    def plus(self, other: "Fractions") -> "Fractions":        
        """Method used to add two fraction and return the resultant value"""        
        
        new_numerator: int = (self.numerator * other.denominator) + (self.denominator * other.numerator)        
        new_denominator: int = self.denominator * other.denominator        
        return Fractions(new_numerator, new_denominator)    
    
    def minus(self, other: "Fractions") -> "Fractions":        
        """Method used to subtract two fraction and return the resultant value"""        
        
        new_numerator: int = (self.numerator * other.denominator) - (self.denominator * other.numerator)        
        new_denominator: int = self.denominator * other.denominator        
        return Fractions(new_numerator, new_denominator)    
        
    def times(self, other: "Fractions") -> "Fractions":        
        """Method used to multiply two fraction and return the resultant value"""        
        new_numerator: int = self.numerator * other.numerator        
        new_denominator: int = self.denominator * other.denominator        
        return Fractions(new_numerator, new_denominator)    
        
    def divide(self, other: "Fractions") -> "Fractions":        
        """Method used to divide two fraction and return the resultant value"""        
        new_numerator: int = self.numerator * other.denominator        
        new_denominator: int = self.denominator * other.numerator        
        return Fractions(new_numerator, new_denominator)    
        
    def equal(self, other: "Fractions") -> bool:        
        """Method used to check if two fractions are equal or not and return the resultant value"""        
        return self.numerator * other.denominator == self.denominator * other.numerator   
        
    def __str__(self) -> str:

        return f"{self.numerator}/{self.denominator}"
        
def handle_input(prompt) -> int:    
    """Function used to handle input and check if its a int"""    
        
    while True:        
        user_input = input(prompt)        
        try:            
            return int(user_input)        
        except ValueError:            
            print(f"{user_input} is not a number. please enter the number again.")
                
def get_fraction_from_user(fraction_label: str) -> "Fractions":    
    """Function used to take input from user and convert to a fraction"""    
        
    while True:        
        numerator = handle_input(f"Enter {fraction_label} numerator: ")        
        denominator = handle_input(f"Enter {fraction_label} denominator: ")        
        try:            
            fraction = Fractions(numerator, denominator)            
            return fraction        
        except ValueError as e:            
            print(e)
            
def compute(f1, operator, f2) -> "Fractions":    
    """Function used to compute the result of operation performed on fractions"""    
        
    result: "Fractions" = None    
    try:        
        if operator == '+':            
            result = f1.plus(f2)        
                
        elif operator == '-':            
            result = f1.minus(f2)        
            
        elif operator == '*':            
            result = f1.times(f2)        
            
        elif operator == '/':            
            result = f1.divide(f2)        
            
        elif operator == '==':            
            result = f1.equal(f2)        
            
        else:            
            print('Invalid operation!')    
                
    except ValueError as e:        
        print(e)    
        return result
            
def main():    
    """Function used for interactive fraction calculation"""    
    print("---- Interactive ---- \n Welcome to the fraction calculator! \n ")    
    
    fraction_1: "Fractions" = get_fraction_from_user("fraction 1")    
    
    while True:        
        try:            
            operation_selected = input(f"Select an operation to be performed {allowed_operation}:")            
            allowed_operation.index(operation_selected)

        except ValueError:            
            print(f"{operation_selected} is an invalid operator!")        
            
        else:            
            break    
        
    fraction_2: "Fractions" = get_fraction_from_user("fraction 2") 

    result: "Fractions" = compute(fraction_1, operation_selected, fraction_2)    
    
    if result:        
        print(f"The result is => {fraction_1} {operation_selected} {fraction_2} = {result}")

def test_suite():    
    """Function used as a test case"""    
        
    print("-----TEST SUITE 1 ----- \n Welcome to the fraction calculator! \n ")    
        
    fraction_1: "Fractions" = Fractions(1, 2)    
    fraction_2: "Fractions" = Fractions(4, 4)    
    fraction_3: "Fractions" = Fractions(12, 8)    
    fraction_4: "Fractions" = Fractions(3, 2)    
    fraction_5: "Fractions" = Fractions(1, 1) 

    result1: "Fractions" = compute(fraction_1, allowed_operation[0], fraction_1) 
    if result1:        
        print(f"Expected result 1/2 + 1/2 = 4/4")        
        print(f"Computed result {fraction_1} {allowed_operation[0]} {fraction_1} = {result1} \n")    
    
    result2: "Fractions" = compute(fraction_2, allowed_operation[1], fraction_1)  
    if result2:        
        print(f"Expected result 4/4 - 1/2 = 4/8")        
        print(f"Computed result {fraction_2} {allowed_operation[1]} {fraction_1} = {result2} \n")    
    
    result3: "Fractions" = compute(fraction_1, allowed_operation[0], fraction_2)       
    if result3:        
        print(f"Expected result 1/2 + 4/4 = 12/8")        
        print(f"Computed result {fraction_1} {allowed_operation[0]} {fraction_2} = {result3} \n")    
        
    result4: "Fractions" = compute(fraction_3, allowed_operation[4], fraction_4)    
    if result4:        
        print(f"Expected result 12/8 == 3/2 = True")        
        print(f"Computed result {fraction_3} {allowed_operation[4]} {fraction_4} = {result4} \n")   

    result5: "Fractions" = compute(fraction_1, allowed_operation[2], fraction_4)    
    if result5:        
        print(f"Expected result 1/2 * 3/2 = 3/4")        
        print(f"Computed result {fraction_1} {allowed_operation[2]} {fraction_4} = {result5} \n")    
    
    result6: "Fractions" = compute(fraction_2, allowed_operation[3], fraction_2)     
    if result6:        
        print(f"Expected result 4/4 / 4/4 = 16/16")        
        print(f"Computed result {fraction_2} {allowed_operation[3]} {fraction_2} = {result6} \n")    
        print(f"Expected result 1/2 / 0/1  Error")

    result7: "Fractions" = compute(fraction_1, allowed_operation[3], fraction_5)    
    if result7:        
        print(f"Computed result {fraction_1} {allowed_operation[3]} {fraction_5} = {result7} \n")
            
def test_suite_2():    
    """Function used as a test case for adding 3 fractions"""

    print("-----TEST SUITE 2 ----- \n Welcome to the fraction calculator! \n")  

    fraction_1: "Fractions" = Fractions(1, 2)    
    fraction_2: "Fractions" = Fractions(3, 4)    
    fraction_3: "Fractions" = Fractions(4, 4)    
    result1: "Fractions" = compute(fraction_1, allowed_operation[0], fraction_2)    
    result2: "Fractions" = compute(result1, allowed_operation[0], fraction_3)    
        
    if result2:        
        print(f"Expected result 1/2 + 3/4 + 4/4 = 72/32")        
        print(f"Computed result {fraction_1} {allowed_operation[0]} {fraction_2} {allowed_operation[0]} {fraction_3} = {result2} \n")
            
if __name__ == '__main__':    
    test_suite()    
    #test_suite_2()    
    main()