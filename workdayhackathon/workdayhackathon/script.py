import curses
from time import sleep
import inputlol
from score import Scorer
stdscr = curses.initscr()

#written by : Dylan Lewis and Emmet Leahy 
# W,A,S,D correspond to Up,Down,Left, Right
# arrows respectively. These scroll down the screen
# and pass through a lin. Press the arrow's corresponding
# key as it through the line if you do you earn points, if
#not you lose a life until all lives are depeleted. 


#creates pads to draw arrows on
pad = curses.newwin(50, 10, 0, 0)
pad2 = curses.newwin(50, 20, 0,10)
pad3 = curses.newwin(50, 20, 0,20)
pad4 = curses.newwin(50, 20, 0,30)
pad5 = curses.newwin(50, 20, 0,40)
pad6 = curses.newwin(50, 20, 0,50)

keys = {'D' : 115,'U' : 119, 'R' : 100, 'L' : 97 , 'Q' : 113, 'N' : 114 } # w a s d and Q
def init():
    curses.noecho()
    curses.nocbreak()
    stdscr.keypad(True)
    stdscr.nodelay(1)

def print_left(pad,y):
	pad.addstr(y,1,  ' /|____')
	pad.addstr(y+1,1,'/      |')
	pad.addstr(y+2,1,'\  ____|')
	pad.addstr(y+3,1,' \|     ')

def print_down(pad,y):
	pad.addstr(y,1,  '  ___')
	pad.addstr(y+1,1,' |   |')
	pad.addstr(y+2,1,'_!   !_')
	pad.addstr(y+3,1,'\     /')
	pad.addstr(y+4,1,' \   /')
	pad.addstr(y+5,1,'  \ /')
	pad.addstr(y+6,1,'   Y')

def print_up(pad,y):
	pad.addstr(y,1,  '   ^')
	pad.addstr(y+1,1,'  / \\')
	pad.addstr(y+2,1,' /   \\')
	pad.addstr(y+3,1,'/_   _\\')
	pad.addstr(y+4,1,' |   |')
	pad.addstr(y+5,1,' |___|')

def print_right(pad,y):
	pad.addstr(y,1,  ' ____|\\')
	pad.addstr(y+1,1,'|      \\')
	pad.addstr(y+2,1,'|____  /')
	pad.addstr(y+3,1,'     |/')

def main():
	init()

	s = Scorer()

	curses.start_color()
	y = 0
         
        key_val = -1
	notFinished = False
        restart = True
        ##keeps going until you press q or lose
	while(notFinished == False):
                
                
		hit = False
		char = s.get_row()
                pad6.clear()       
		for y in range(0,40):
                        
			pad.clear()
			pad2.clear()
			pad3.clear()
			pad4.clear()
                        
			if char == 'L':
				print_left(pad,y)
			if char == 'D':
				print_down(pad2,y)
			if char == 'U':
				print_up(pad3,y)
			if char == 'R':
				print_right(pad4,y)

			pad.addstr(25,0,"----------")
			pad2.addstr(25,0,"----------")
			pad3.addstr(25,0,"----------")
			pad4.addstr(25,0,"----------")

			pad5.addstr(0,0,"Score: " + str(s.score))
			pad5.addstr(1,0,"Lives: " + str(s.lives))
			pad5.addstr(2,0,"Level: " + str(s.level))

			pad.refresh()
			pad2.refresh()
			pad3.refresh()
			pad4.refresh()
			pad5.refresh()
			key_val = stdscr.getch()
                        sleep(0.1/s.level)
       
                        if(key_val == keys['Q']):
                            cleanexit("Thanks for playing your score is "  + str(s.score))
                            
                         
		
                        #checks if key pressed within range        
                        elif (y >= 19 and y <= 31 and key_val == keys[char] and hit == False): # down
			    s.hit()
			    hit = True
                                   
			    break
                        #quits game 
                               
			elif (y > 31):
				s.miss()
                                pad5.addstr(3,0,"YOU MISSED" )
                                pad5.addstr(4,0,str(key_val) )

				if(s.lives < 0):
				    pad6.addstr(0,0,"You Lose! Score: " + str(s.score))
                                    pad6.refresh()
                                    s = Scorer()
               			break

        

def cleanexit(text):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	print(text)
	exit()

#try:
main()
#except:
cleanexit("Fatal Error occured")
