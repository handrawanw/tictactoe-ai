from string import Template
from random import randint

pattern=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
map_board=[[0,1,2],[3,4,5],[6,7,8]]
number_board=[['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
string_board = """(0?0),(0?1),(0?2):(1?3),(1?4),(1?5):(2?6),(2?7),(2?8)""" 

def reset_value():
	return [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']];
	
def wins(symbol):
	count=0
	for pnum in pattern:
		for num in pnum:
			cordsXY=positionY(num)
			if number_board[int(cordsXY['y'])][int(cordsXY['x'])] == symbol:
				count+=1
			# end if
		if count == 3:
			return True
		count=0
	return None
     

def defeat_human():
	symbol="O"
	human_xy=None
	count=0
	for pnum in pattern:
		for num in pnum:
			cordsXY=positionY(num)
			if number_board[int(cordsXY['y'])][int(cordsXY['x'])] == symbol:
				count+=1
			else:
				human_xy=positionY(num)
			# end if
		# end for
		if count == 2:
			if number_board[int(human_xy['y'])][int(human_xy['x'])] != "X":
				number_board[int(human_xy['y'])][int(human_xy['x'])]="X"
				return True
		count=0
		human_xy=None
	#end for
	return None
	

def detect_human():
	symbol="O"
	count=0
	for pnum in pattern:
		for num in pnum:
			cordsXY=positionY(num)
			if number_board[int(cordsXY['y'])][int(cordsXY['x'])] == symbol:
				count+=1
			# end if
		# end for
		if count == 2:
			return True
		count=0
	#end for
	return None
	

	
def positionEmpty():
    for i in range(3):
        for j in range(3):
            if number_board[i][j] == "N":
                return {"x":j,"y":i}
    return None

def positionY(val):
    try:
        template=Template("?$value)")
        template=template.substitute(value=val)
        posY=int(string_board[string_board.index(template)-1])
        posX=map_board[posY].index(val)
        return {"x":posX,"y":posY};
    except ValueError:
        return None

def make_board():
    info="""------------"""
    print("TicTacToe")
    print(info)
    for index in range(3):
        template=Template(" $value_one | $value_two | $value_three ")
        template=template.substitute(value_one=number_board[index][0],value_two=number_board[index][1],value_three=number_board[index][2])
        print(template)
    print(info)
make_board()

def human_player(val):
    posXY=positionY(val)
    if posXY == None:
        print("Invalid position")
    else:    
        if number_board[int(posXY['y'])][int(posXY['x'])] == "N":
            number_board[int(posXY['y'])][int(posXY['x'])]="O"
        else:
            make_board()
            human_player(int(input("Input telah ada\nMasukan position baru tictactoe(0:8)\n")))
            
        
def computer_player():
	detect_human_error=detect_human()
	if detect_human_error is True:
		defeat_human()
	else:
		posXY=positionY(randint(0,8))
		posEmpty=positionEmpty()
		if number_board[int(posXY['y'])][int(posXY['x'])] == "N":
			number_board[int(posXY['y'])][int(posXY['x'])]="X"
		else:
			if posEmpty is None:
				print("Finished")
			else:
				computer_player()

while True:
    cordinateXY=int(input("Masukan position tictactoe (0:8) \n"))
    if cordinateXY > 8:
        break
    else:
        human_player(cordinateXY);
        human_win=wins("O")
        # defeat_human()
        computer_player()
        computer_win=wins("X")
        make_board()
        posEmp=positionEmpty()
        if human_win is True or computer_win is True or posEmp is None:
            break
        if human_win is True:
        	print("Human Win");
        if computer_win is True:
            print("Computer Win");
    #end else
#end def

        
    
    
         
        
