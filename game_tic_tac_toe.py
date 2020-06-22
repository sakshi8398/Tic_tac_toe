# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Display the tic tac toe board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print()

#taking name of players
def name_of_player():
    name1=input("Enter the name of player1 : ")
    name2=input("Enter the name of player2 : ")
    return (name1,name2)

#for selecting which player is going to play first
def toss(name1,name2):
    from random import randint
    player=randint(0,1)
    if player==1:
        print("Congratulations, "+ name2+" you Win the toss!!!")
        return (name2,name1)
    else:
        print("Congratulations, "+ name1+" you Win the toss!!!")
        return (name1,name2)

#definig markers for players
def user_input(name1,name2):
    marker=" "
    while marker!='X' and marker!='O':
    
        marker=input("Enter the marker for "+name1+" (O/X):").upper()
        if marker!='X' and marker!='O':
            print ("sorry invalid marker choice, choose either O or X")
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

#Taking position where player wants to insert it's marker
def position_choice():
    position = 0
    while position not in range(1,10):
        position=int(input("Enter the position between (1-9): "))
        if position not in range(1,10):
            print("Sorry! Invalid position choose between 1 to 9")
    return position;

#checking the position selected by user is empty or not
def valid_position(pos,board):
    if board[pos]=='O' or board[pos]=='X':
        print ("Sorry! Try empty position this position is occupied. ")
        return False
    return True

#Checking for win condition of game
def win_condition(board,marker):
    if board[1]==board[2]==board[3] == marker:
        return True
    elif board[4]==board[5]==board[6] == marker:
        return True
    elif board[7]==board[8]==board[9] == marker:
        return True
    elif board[1]==board[4]==board[7] == marker:
        return True
    elif board[2]==board[5]==board[8] == marker:
        return True
    elif board[3]==board[6]==board[9] == marker:
        return True
    elif board[1]==board[5]==board[9] == marker:
        return True
    elif board[3]==board[5]==board[7] == marker:
        return True
    else:
        return False
    
#checking tie condition of the game 
def tie_condition(board):
    for i in range(1,10):
        if board[i] not in ['X','O'] :
            return False 
    return True

#if user wants to play again
def replay_match():
    rematch=" "
    while rematch!="Y" and rematch!="N":
        rematch=input("Do you want to play Again? Enter y/n : ").upper()
        if rematch!="Y" and rematch!="N":
            print("Sorry! Invalid option try again")
    if rematch=="Y":
        return True
    else :
        return False


#tic_tac_toe main code putting all functions together
def tic_tac_toe():
    print("Welcome to TIC TAC TOE game !!!")
    game_on=True
    p1,p2=name_of_player()
    while game_on:
        name1,name2=toss(p1,p2)
        board=[' ']*10
        counter=1
        player1,player2=user_input(name1,name2)
        win=False
        tie=False
        marker=" "
        while win==False and tie==False:
            if counter%2==1:
                print(name1+" your chance!!!")
                marker=player1
            else :
                print(name2+" your chance!!!")
                marker=player2
            choice=False
            while choice == False:
                pos=position_choice()
                choice=valid_position(pos,board)
            board[pos]=marker
            display_board(board)
            counter=counter+1
            win=win_condition(board,marker)
            tie=tie_condition(board)
        if win==True:
            if marker==player1:
                print("Congratulations, "+ name1+" you Win!!!")
            else :
                print("Congratulations, "+ name2+" you Win!!!")
        elif tie==True:
            print("Game is tie !!!")
        print("Game Over !!!")
        game_on=replay_match()
    if game_on==False:
        print("Thank You for playing game !!!")
        

tic_tac_toe()