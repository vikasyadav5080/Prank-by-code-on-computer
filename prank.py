import rotatescreen
import time 

screen = rotatescreen.get_primary_display()
for i in range(3):
    time.sleep(2)
    screen.rotate_to(i*90 % 360)
/*You can increase the range as per your choice.*/
