from turtle import *

speed(1) 
color("red")  
begin_fill()  
pensize(3)

left(45)
forward(215)
circle(90, 225)
right(180)
circle(90, 225)
forward(215)

end_fill()  

penup() 
goto(-120, -250)  
color("black")  
write("FELIZ UM ANO DE NAMORO", align="center", font=("Arial", 20, "bold"))  

done() 
