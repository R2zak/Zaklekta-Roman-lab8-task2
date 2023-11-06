def validate_board(board:list) -> bool:
    """
    list->bool
    Function that check game board and returns 
    True or False depending on the fulfillment of the rules of the game
    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****","    19 5 ",\
" 6  83  *","3      **","  8  2***","  2  ****"])
    False
    """
    num=["1","2","3","4","5","6","7","8","9"]
    pillars=['','','','','','','','','','']
    color_panels=[]
    for i in board:
        y=0
        while y<9:
            pillars[y]+=i[y]
            y+=1
        for j in num:
            if i.count(j)>1:
                return False
    for l in pillars:
        for j in num:
            if l.count(j)>1:
                return False