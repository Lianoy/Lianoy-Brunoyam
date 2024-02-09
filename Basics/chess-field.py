## Создать массив в виде шахматного поля

def create_chess_field(size,color1='w',color2='b'):
   chess_field=[]
   for i in range(size):
       middle_field=[]
       for j in range(size):
           if (i+j)%2 == 0:
               middle_field.append(color2)
           else:
               middle_field.append(color1)
       chess_field.append(middle_field)
   print (chess_field)

create_chess_field(4)
create_chess_field(16)