# FILE NAME - convert_C_to_F_02.py

# NAME: Devyn Bagley
# DATE: 10/5/2025
# BRIEF DESCRIPTION:  An application that prompts the user if the want to convert to Fahrenheit or Celcius, then converts the temperature based on their response.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########



def main():
    print('=' * 5, 'Temperature Converter', '=' * 5)
    print()
    print(' 1. Convert from Celsius to Fahrenheit')
    print(' 2. Convert from Fahrenheit to Celsius')
    print()
    def converter():
        conversion = input('Please choose from the above menu: ')
        temperature = int(input('Enter a temperature to convert: '))
        c_to_f = float(temperature * 9/5 +32)
        f_to_c = float((temperature - 32) * 5/9)
        
        if conversion == ('1'):
            print(f'{temperature} degrees Celsius is {c_to_f} degrees Fahrenheit.')

        else:
            print(f'{temperature} degrees Fharenheit is {f_to_c} degrees Celsius.')
    converter()
main()






########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

A lesson I learned in this lab is the order that your write your code is imperative for your program to run correctly.





'''
