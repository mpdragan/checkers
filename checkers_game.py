import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([450,450])
pygame.display.set_caption('Checkers Game')


screen.fill((0,100,255))

array=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

flag = 0

flag_hod = True

# малюємо дошку
for column in range(8):
   for row in range(4):
       if (column%2==0):
          rect_white = pygame.Rect(20+50*2*row,20+50*column,50,50)
          x_rect_black_02468 = 20+50+50*2*row
          y_rect_black_02468 = 20+50*column
          rect_black = pygame.Rect(x_rect_black_02468,y_rect_black_02468,50,50)
          
          pygame.draw.rect(screen,(100,255,0),rect_white,0)
          pygame.draw.rect(screen,(255,0,100),rect_black,0)
          # if
       else:
              rect_white = pygame.Rect(20+50+50*2*row,20+50*column,50,50)
              x_rect_black_1357 = 20+50*2*row
              y_rect_black_1357 = 20+50*column
              rect_black = pygame.Rect(x_rect_black_1357,y_rect_black_1357,50,50)

              pygame.draw.rect(screen,(100,255,0),rect_white,0)
              pygame.draw.rect(screen,(255,0,100),rect_black,0)
              # if
# малюємо шашки
# def draw_checkers():
for column_check_black in range(3):
      for row_check_black in range(4):
         if (column_check_black%2==0):
            pygame.draw.circle(screen,(255,0,255),(20+50+50*2*row_check_black+25,20+50*column_check_black+25),25)
            array[column_check_black][row_check_black*2+1] = 2
         else:
            pygame.draw.circle(screen,(255,0,255),(20+50*2*row_check_black+25,20+50*column_check_black+25),25)
            array[column_check_black][row_check_black*2] = 2
       
#print(array)

for column_check_white in range(5,8):
      for row_check_white in range(4):
         if (column_check_white%2==0):
            pygame.draw.circle(screen,(0,255,255),(20+50+50*2*row_check_white+25,20+50*column_check_white+25),25)
            array[column_check_white][row_check_white*2+1] = 1
         else:
            pygame.draw.circle(screen,(0,255,255),(20+50*2*row_check_white+25,20+50*column_check_white+25),25)
            array[column_check_white][row_check_white*2] = 1

#print(array)
# функція - задаємо оновленний масив і в результаті отримуємо нові намальовані шашки
def onovlennja_checkers(array):
   # малюємо дошку
   for column in range(8):
      for row in range(4):
         if (column%2==0):
            rect_white = pygame.Rect(20+50*2*row,20+50*column,50,50)
            x_rect_black_02468 = 20+50+50*2*row
            y_rect_black_02468 = 20+50*column
            rect_black = pygame.Rect(x_rect_black_02468,y_rect_black_02468,50,50)
          
            pygame.draw.rect(screen,(100,255,0),rect_white,0)
            pygame.draw.rect(screen,(255,0,100),rect_black,0)
            # if
         else:
              rect_white = pygame.Rect(20+50+50*2*row,20+50*column,50,50)
              x_rect_black_1357 = 20+50*2*row
              y_rect_black_1357 = 20+50*column
              rect_black = pygame.Rect(x_rect_black_1357,y_rect_black_1357,50,50)

              pygame.draw.rect(screen,(100,255,0),rect_white,0)
              pygame.draw.rect(screen,(255,0,100),rect_black,0)
              # if
   # малюємо шашки
   for colunm in range(8):
      for row in range(8):
         if array[row][colunm]==1:
            
            x_circle_white=20+50*colunm
            y_circle_white=20+50*row
            pygame.draw.circle(screen,(0,255,255),(x_circle_white+25,y_circle_white+25),25)
         
         if array[row][colunm]==2:
            x_circle_black=20+50*colunm
            y_circle_black=20+50*row
            pygame.draw.circle(screen,(255,0,255),(x_circle_black+25,y_circle_black+25),25)
       
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            
            x_koord_rect=20+50*((x_mouse-20)//50)
            y_koord_rect=20+50*((y_mouse-20)//50)

            flag = flag+1

            #if flag==2:
                # ходимо білими - малюємо кружок з новими координатами, а старий стираємо.
                # онулюємо флаг
                #flag=0

            # малюємо дошку
            for column in range(8):
               for row in range(4):
                  if (column%2==0):
                     rect_white = pygame.Rect(20+50*2*row,20+50*column,50,50)
                     x_rect_black_02468 = 20+50+50*2*row
                     y_rect_black_02468 = 20+50*column
                     rect_black = pygame.Rect(x_rect_black_02468,y_rect_black_02468,50,50)
          
                     pygame.draw.rect(screen,(100,255,0),rect_white,0)
                     pygame.draw.rect(screen,(255,0,100),rect_black,0)

                     
                     # порівнюємо нажатий квадрат з темним квадратом 
                     #if (x_koord_rect==x_rect_black_02468) and (y_koord_rect==y_rect_black_02468):
                     #    rect_naz = pygame.Rect(x_koord_rect,y_koord_rect,50,50)
                     #    pygame.draw.rect(screen,(255,255,100),rect_naz,0)
                         
                  else:
                     rect_white = pygame.Rect(20+50+50*2*row,20+50*column,50,50)
                     x_rect_black_1357 = 20+50*2*row
                     y_rect_black_1357 = 20+50*column
                     rect_black = pygame.Rect(x_rect_black_1357,y_rect_black_1357,50,50)

                     pygame.draw.rect(screen,(100,255,0),rect_white,0)
                     pygame.draw.rect(screen,(255,0,100),rect_black,0)
              
                     # порівнюємо нажатий квадрат з темним квадратом
                     #if (x_koord_rect==x_rect_black_1357) and (y_koord_rect==y_rect_black_1357):
                     #   rect_naz = pygame.Rect(x_koord_rect,y_koord_rect,50,50)
                     #   pygame.draw.rect(screen,(255,255,100),rect_naz,0)

            
            # малюємо шашки
            # чорні
            for column_check_black in range(3):
                for row_check_black in range(4):
                   if (column_check_black%2==0):
                      pygame.draw.circle(screen,(255,0,255),(20+50+50*2*row_check_black+25,20+50*column_check_black+25),25)
                   else:
                      pygame.draw.circle(screen,(255,0,255),(20+50*2*row_check_black+25,20+50*column_check_black+25),25)
            # білі
            for column_check_white in range(5,8):
               for row_check_white in range(4):
                  if (column_check_white%2==0):
                      x_radius_white_02468 = 20+50+50*2*row_check_white+25
                      y_radius_white_02468 = 20+50*column_check_white+25
                      pygame.draw.circle(screen,(0,255,255),(x_radius_white_02468,y_radius_white_02468),25)

                      x_circle_white_02468 = x_radius_white_02468-25
                      y_circle_white_02468 = y_radius_white_02468-25

                      # порівнюємо білу шашку з квадратом нажатим мишкою і підсвічуємо
                      #if (x_circle_white_02468==x_koord_rect) and (y_circle_white_02468==y_koord_rect):
                          #if (x_koord_rect)
                      #   rect_podsvetka = pygame.Rect(x_koord_rect-50,y_koord_rect-50,50,50)
                      #   pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)

                     #  rect_podsvetka = pygame.Rect(x_koord_rect+50,y_koord_rect-50,50,50)
                      #   pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                      
                  else:
                      x_radius_white_1357 = 20+50*2*row_check_white+25
                      y_radius_white_1357 = 20+50*column_check_white+25
                      pygame.draw.circle(screen,(0,255,255),(x_radius_white_1357,y_radius_white_1357),25)

                      x_circle_white_1357 = x_radius_white_1357-25
                      y_circle_white_1357 = y_radius_white_1357-25

                      # порівнюємо білу шашку з квадратом нажатим мишкою і підсвічуємо
                      #if (x_circle_white_1357==x_koord_rect) and (y_circle_white_1357==y_koord_rect):
                          #if (x_koord_rect)
                       #  rect_podsvetka = pygame.Rect(x_koord_rect-50,y_koord_rect-50,50,50)
                       #  pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                         
                       #  rect_podsvetka = pygame.Rect(x_koord_rect+50,y_koord_rect-50,50,50)
                        # pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)

            # визиваємо функцію створення шашок оновлених ходами
            onovlennja_checkers(array)
            
            # Хід білих
            #x_circle_white = x_radius_white-25
            #y_circle_white = y_radius_white-25
            if flag_hod==True:
               if flag==1:
                  # нажимаємо на білу шашку - якщо нажатий квадрат співпадає з білою шашкою і якщо є свободні клітинка або клітинки куди можна ходити або треба бити,
                  # то перебігаємо - підсвічується біла шашка і ходи для неї
                  # шукаємо білі шашки у масиві під номером 1
                  for colunm in range(8):
                     for row in range(8):
                         if array[row][colunm]==1:
                            x_circle_white=20+50*colunm
                            y_circle_white=20+50*row
                            #print(x_circle_white)
                            #print(y_circle_white)
                            # підсвічується нажата біла шашка (нажатий квадрат)
                            if (x_koord_rect==x_circle_white) and (y_koord_rect==y_circle_white):
                               rect_naz = pygame.Rect(x_koord_rect,y_koord_rect,50,50)
                               pygame.draw.rect(screen,(255,255,100),rect_naz,0)
                               # оновлюємо поле, щоб було видно білу шашку - функція малювання оновлених шашок (чи просто шашок)
                               #onovlennja_checkers(array)
                               pygame.draw.circle(screen,(0,255,255),(x_koord_rect+25,y_koord_rect+25),25)
                               
                               #print(x_koord_rect)
                               #print(y_koord_rect)
                               #print(row)
                               #print(colunm)
                            # якщо є вільна чи вільні квадрати куди можна ходити або треба бити, то підсвічуємо можливі ходи - перевіряємо ячійки масиву на пустий (0) чи чорний (2)
                               colunm_1 = ((x_koord_rect-50)-20)//50
                               row_1= ((y_koord_rect-50)-20)//50

                               colunm_2 = ((x_koord_rect+50)-20)//50
                               row_2 = ((y_koord_rect-50)-20)//50
                            
                               if (row_1>=0) and (colunm_1>=0) and array[row_1][colunm_1]==0:
                               #if array[row_1][colunm_1]==0:
                                  #print(row_1)
                                  #print(colunm_1)
                                  rect_podsvetka = pygame.Rect(x_koord_rect-50,y_koord_rect-50,50,50)
                                  pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                  x_rect_podsvetka_lev = x_koord_rect-50
                                  y_rect_podsvetka_lev = y_koord_rect-50

                               if (row_2<8) and (colunm_2<8) and (array[row_2][colunm_2]==0):
                                  #print(row_2)
                                  #print(colunm_2)
                                  rect_podsvetka = pygame.Rect(x_koord_rect+50,y_koord_rect-50,50,50)
                                  pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                  x_rect_podsvetka_prav = x_koord_rect+50
                                  y_rect_podsvetka_prav = y_koord_rect-50

                               x_rect_podsvetka_lev_lev = x_koord_rect-50-50
                               y_rect_podsvetka_lev_lev = y_koord_rect-50-50
                               if array[row_1][colunm_1]==2:
                                  colunm_1_1 = ((x_koord_rect-50-50)-20)//50
                                  row_1_1= ((y_koord_rect-50-50)-20)//50
                                  if array[row_1_1][colunm_1_1]==0:
                                     rect_podsvetka = pygame.Rect(x_koord_rect-50-50,y_koord_rect-50-50,50,50)
                                     pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                     x_rect_podsvetka_lev_lev = x_koord_rect-50-50
                                     y_rect_podsvetka_lev_lev = y_koord_rect-50-50

                               x_rect_podsvetka_prav_prav = x_koord_rect+50+50
                               y_rect_podsvetka_prav_prav = y_koord_rect-50-50
                               if array[row_2][colunm_2]==2:
                                  colunm_2_2 = ((x_koord_rect+50+50)-20)//50
                                  row_2_2= ((y_koord_rect-50-50)-20)//50
                                  if array[row_2_2][colunm_2_2]==0:
                                     rect_podsvetka = pygame.Rect(x_koord_rect+50+50,y_koord_rect-50-50,50,50)
                                     pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                     x_rect_podsvetka_prav_prav = x_koord_rect+50+50
                                     y_rect_podsvetka_prav_prav = y_koord_rect-50-50
                           
               
               #flag_hod=False
            
               if flag==2:
                                   # ходимо білими - малюємо кружок з новими координатами, а старий стираємо.
                                   # онулюємо флаг
                                   #print(x_koord_rect)
                                   #print(y_koord_rect)
                                   if ((x_koord_rect== x_rect_podsvetka_lev) and (y_koord_rect== y_rect_podsvetka_lev)):
                                      pygame.draw.circle(screen,(0,255,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=1
                                      #print(array)
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect+50,y_koord_rect+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect+50 - 20)//50
                                      colunm_del = (y_koord_rect+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   if ((x_koord_rect== x_rect_podsvetka_prav) and (y_koord_rect== y_rect_podsvetka_prav)):
                                      pygame.draw.circle(screen,(0,255,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=1
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect-50,y_koord_rect+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect-50 - 20)//50
                                      colunm_del = (y_koord_rect+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   #print(x_rect_podsvetka_lev_lev)
                                   if ((x_koord_rect== x_rect_podsvetka_lev_lev) and (y_koord_rect== y_rect_podsvetka_lev_lev)):
                                      pygame.draw.circle(screen,(0,255,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=1
                                      #print(array)
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect+50+50,y_koord_rect+50+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect+50+50 - 20)//50
                                      colunm_del = (y_koord_rect+50+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      rect_delete_circle_black = pygame.Rect(x_koord_rect+50,y_koord_rect+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect+50 - 20)//50
                                      colunm_del = (y_koord_rect+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   if ((x_koord_rect== x_rect_podsvetka_prav_prav) and (y_koord_rect== y_rect_podsvetka_prav_prav)):
                                      pygame.draw.circle(screen,(0,255,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=1
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect-50-50,y_koord_rect+50+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect-50-50 - 20)//50
                                      colunm_del = (y_koord_rect+50+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      rect_delete_circle_black = pygame.Rect(x_koord_rect-50,y_koord_rect+50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect-50 - 20)//50
                                      colunm_del = (y_koord_rect+50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   flag=0
                                   flag_hod=False
            #print(array)
            
            # Хід чорних
            if flag_hod==False:
               #print(flag_hod)
               #print(flag)
               if flag==1:
                  #print(flag)
                  # нажимаємо на чорну шашку - якщо нажатий квадрат співпадає з чорною шашкою і якщо є свободні клітинка або клітинки куди можна ходити або треба бити,
                  # то перебігаємо - підсвічується чорна шашка і ходи для неї
                  # шукаємо чорні шашки у масиві під номером 2
                  for colunm in range(8):
                     for row in range(8):
                         if array[row][colunm]==2:
                            x_circle_black=20+50*colunm
                            y_circle_black=20+50*row
                            #print(x_circle_white)
                            #print(y_circle_white)
                            # підсвічується нажата біла шашка (нажатий квадрат)
                            #print(x_circle_black)
                            #print(y_circle_black)
                            #print(x_koord_rect)
                            #print(y_koord_rect)
                            if (x_koord_rect==x_circle_black) and (y_koord_rect==y_circle_black):
                               rect_naz_black = pygame.Rect(x_koord_rect,y_koord_rect,50,50)
                               pygame.draw.rect(screen,(255,255,100),rect_naz_black,0)
                               # оновлюємо поле, щоб було видно чорну шашку - функція малювання оновлених шашок (чи просто шашок)
                               #onovlennja_checkers(array)
                               pygame.draw.circle(screen,(255,0,255),(x_koord_rect+25,y_koord_rect+25),25)
                               
                               #print(x_koord_rect)
                               #print(y_koord_rect)
                               #print(row)
                               #print(colunm)
                            # якщо є вільна чи вільні квадрати куди можна ходити або треба бити, то підсвічуємо можливі ходи - перевіряємо ячійки масиву на пустий (0) чи чорний (2)
                               colunm_1 = ((x_koord_rect-50)-20)//50
                               row_1= ((y_koord_rect+50)-20)//50

                               colunm_2 = ((x_koord_rect+50)-20)//50
                               row_2 = ((y_koord_rect+50)-20)//50
                            
                               if (row_1>=0) and (colunm_1>=0) and array[row_1][colunm_1]==0:
                               #if array[row_1][colunm_1]==0:
                                  #print(row_1)
                                  #print(colunm_1)
                                  rect_podsvetka = pygame.Rect(x_koord_rect-50,y_koord_rect+50,50,50)
                                  pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                  x_rect_podsvetka_lev = x_koord_rect-50
                                  y_rect_podsvetka_lev = y_koord_rect+50

                               if (row_2<8) and (colunm_2<8) and (array[row_2][colunm_2]==0):
                                  #print(row_2)
                                  #print(colunm_2)
                                  rect_podsvetka = pygame.Rect(x_koord_rect+50,y_koord_rect+50,50,50)
                                  pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                  x_rect_podsvetka_prav = x_koord_rect+50
                                  y_rect_podsvetka_prav = y_koord_rect+50

                               x_rect_podsvetka_lev_lev = x_koord_rect-50-50
                               y_rect_podsvetka_lev_lev = y_koord_rect+50+50
                               if array[row_1][colunm_1]==1:
                                  colunm_1_1 = ((x_koord_rect-50-50)-20)//50
                                  row_1_1= ((y_koord_rect+50+50)-20)//50
                                  if array[row_1_1][colunm_1_1]==0:
                                     rect_podsvetka = pygame.Rect(x_koord_rect-50-50,y_koord_rect+50+50,50,50)
                                     pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                     x_rect_podsvetka_lev_lev = x_koord_rect-50-50
                                     y_rect_podsvetka_lev_lev = y_koord_rect+50+50

                               x_rect_podsvetka_prav_prav = x_koord_rect+50+50
                               y_rect_podsvetka_prav_prav = y_koord_rect+50+50
                               if array[row_2][colunm_2]==1:
                                  colunm_2_2 = ((x_koord_rect+50+50)-20)//50
                                  row_2_2= ((y_koord_rect+50+50)-20)//50
                                  if array[row_2_2][colunm_2_2]==0:
                                     rect_podsvetka = pygame.Rect(x_koord_rect+50+50,y_koord_rect+50+50,50,50)
                                     pygame.draw.rect(screen,(255,255,100),rect_podsvetka,0)
                                     x_rect_podsvetka_prav_prav = x_koord_rect+50+50
                                     y_rect_podsvetka_prav_prav = y_koord_rect+50+50

               if flag==2:
                                   # ходимо чорними - малюємо кружок з новими координатами, а старий стираємо.
                                   # онулюємо флаг
                                   #print(x_koord_rect)
                                   #print(y_koord_rect)
                                   if ((x_koord_rect== x_rect_podsvetka_lev) and (y_koord_rect== y_rect_podsvetka_lev)):
                                      pygame.draw.circle(screen,(255,0,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=2
                                      #print(array)
                                      
                                      rect_delete_circle_black = pygame.Rect(x_koord_rect+50,y_koord_rect-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect+50 - 20)//50
                                      colunm_del = (y_koord_rect-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   if ((x_koord_rect== x_rect_podsvetka_prav) and (y_koord_rect== y_rect_podsvetka_prav)):
                                      pygame.draw.circle(screen,(255,0,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=2
                                      
                                      rect_delete_circle_black = pygame.Rect(x_koord_rect-50,y_koord_rect-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect-50 - 20)//50
                                      colunm_del = (y_koord_rect-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)

                                   #print(x_rect_podsvetka_lev_lev)
                                   if ((x_koord_rect== x_rect_podsvetka_lev_lev) and (y_koord_rect== y_rect_podsvetka_lev_lev)):
                                      pygame.draw.circle(screen,(255,0,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=2
                                      #print(array)
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect+50+50,y_koord_rect-50-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect+50+50 - 20)//50
                                      colunm_del = (y_koord_rect-50-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      rect_delete_circle_black = pygame.Rect(x_koord_rect+50,y_koord_rect-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect+50 - 20)//50
                                      colunm_del = (y_koord_rect-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)
                                      
                                   if ((x_koord_rect== x_rect_podsvetka_prav_prav) and (y_koord_rect== y_rect_podsvetka_prav_prav)):
                                      pygame.draw.circle(screen,(255,0,255),(x_koord_rect+25,y_koord_rect+25),25)
                                      # добавляємо в масив нову шашку і удаляємо стару. оновлюємо новий масив.
                                      row = (x_koord_rect-20)//50
                                      colunm = (y_koord_rect-20)//50
                                      array[colunm][row]=2
                                      
                                      rect_delete_circle_white = pygame.Rect(x_koord_rect-50-50,y_koord_rect-50-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_white,0)

                                      row_del = (x_koord_rect-50-50 - 20)//50
                                      colunm_del = (y_koord_rect-50-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      rect_delete_circle_black = pygame.Rect(x_koord_rect-50,y_koord_rect-50,50,50)
                                      pygame.draw.rect(screen,(255,0,100),rect_delete_circle_black,0)

                                      row_del = (x_koord_rect-50 - 20)//50
                                      colunm_del = (y_koord_rect-50 - 20)//50
                                      array[colunm_del][row_del] = 0

                                      onovlennja_checkers(array)

                                      
                                   flag=0
                                   flag_hod=True
            
    pygame.display.flip()

    
