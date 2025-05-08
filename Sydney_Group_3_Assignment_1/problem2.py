#Group: Sydney_Group_3
#Ayan Roy - S388800
#Pronab Sarker - S388867
#Ahmed Zabir Hussain - S387391
#Shashika Mihiranga Puwakdandawe Gam Acharige - S385832




user_input=input('please enter integer as lenght of square:')

try:
    integer_number=int(user_input)
except ValueError:
    try:
        float_value=float(user_input)
        integer_number = abs(round(float_value))
    except ValueError:
        ascii_values1=[ord(char) for char in user_input]
        print('converted ascii values:', ascii_values1)
        rounded_input1=round (sum(ascii_values1))
        integer_number=abs (int (rounded_input1))
        if type(integer_number)!= int or integer_number<=0:
          integer_number=5
          print(' the size has been changed to the default value', integer_number)

for i in range(integer_number):
    if i==0 or i==integer_number-1:
        print('*'*integer_number)
    else:
        print('*'+' '*(integer_number-2)+'*')