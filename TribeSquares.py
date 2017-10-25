import sys
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

# Be sure to put your (corrected) Score class in the same directory.
from Score import Score
P1=input("Enter Player 1 name: ")
P2=input("Enter Player 2 name: ")
Player_1=Score(P1)
Player_2=Score(P2)


# This would be a good place to define some numeric constants for
# sizes and positions.

class TribeSquares(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(400, 400, 450, 400)
    self.setWindowTitle('Tribe Squares')
    self.count=0
    self.list_1=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    self.outofscope=False
    self.overwritegrids=False
    self.sum=0
    
    
          
        
    self.show()
    # TODO add your implementation.
    # the constructor should initialize attributes and
    # display the game window.

  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    qp.setPen(QColor(17,87,64))
    qp.drawText(10,350,P1)
    qp.setPen(QColor(185,151,91))
    qp.drawText(10,370,P2)
    qp.setPen(Qt.black)
    qp.drawRect(300,360,80,20)
    qp.drawText(310,375,"Rematch!")
    for a in range(9):
      qp.drawLine(10,10+40*a,330,10+40*a)
      qp.drawLine(10+40*a,10,10+40*a,330)
    for b in range(8):
      for c in range(8):
        if self.list_1[b][c]==1:
          qp.fillRect(15+40*c+1,15+40*b+1,30,30,QBrush(QColor(17,87,64)))
        elif self.list_1[b][c]==2:
          qp.fillRect(15+40*c+1,15+40*b+1,30,30,QBrush(QColor(185,151,91)))
    if self.count%2==0:
      qp.setPen(QColor(17,87,64))
      qp.drawText(200,350,"Your Turn")
    elif self.count%2==1:
      qp.setPen(QColor(185,151,91))
      qp.drawText(200,370,"Your Turn")
    
    for row in range(8):
      for col in range(8):
        if row>col:
          for length in range(1,(8-row)):
            if self.list_1[row][col]==1 and self.list_1[row+length][col]==1 and self.list_1[row][col+length]==1 and self.list_1[row+length][col+length]==1:
              qp.setPen(QColor(17,87,64))
              qp.drawRect(30+col*40,30+row*40,length*40,length*40)
              
            elif self.list_1[row][col]==2 and self.list_1[row+length][col]==2 and self.list_1[row][col+length]==2 and self.list_1[row+length][col+length]==2:
              qp.setPen(QColor(185,151,91))
              qp.drawRect(30+col*40,30+row*40,length*40,length*40)
              
        elif col>=row:
          for length in range(1,(8-col)):
            if self.list_1[row][col]==1 and self.list_1[row+length][col]==1 and self.list_1[row][col+length]==1 and self.list_1[row+length][col+length]==1:
              qp.setPen(QColor(17,87,64))
              qp.drawRect(30+col*40,30+row*40,length*40,length*40)
              
            elif self.list_1[row][col]==2 and self.list_1[row+length][col]==2 and self.list_1[row][col+length]==2 and self.list_1[row+length][col+length]==2:
              qp.setPen(QColor(185,151,91))
              qp.drawRect(30+col*40,30+row*40,length*40,length*40)
    for row in range(8):
      for col in range(8):
        for subrow in range(row+1,8):
          for subcol in range(col+1,8):
            if (subcol-(subrow-row))>=0 and (subrow+(subcol-col))<8 and (row+(subcol-col))<8 and (col-(subrow-row))>=0:
              if self.list_1[row][col]==1 and self.list_1[subrow][subcol]==1 and self.list_1[subrow+(subcol-col)][subcol-(subrow-row)]==1 and self.list_1[row+(subcol-col)][col-(subrow-row)]==1:
                qp.setPen(QColor(17,87,64))
                qp.drawLine(30+col*40,30+row*40,30+subcol*40,30+subrow*40)
                qp.drawLine(30+col*40,30+row*40,30+(col-subrow+row)*40,30+(row+subcol-col)*40)
                qp.drawLine(30+(subcol-subrow+row)*40,30+(subrow+subcol-col)*40,30+subcol*40,30+subrow*40)
                qp.drawLine(30+(subcol-subrow+row)*40,30+(subrow+subcol-col)*40,30+(col-subrow+row)*40,30+(row+subcol-col)*40)
               
              elif self.list_1[row][col]==2 and self.list_1[subrow][subcol]==2 and self.list_1[subrow+(subcol-col)][subcol-(subrow-row)]==2 and self.list_1[row+(subcol-col)][col-(subrow-row)]==2:
                qp.setPen(QColor(185,151,91))
                qp.drawLine(30+col*40,30+row*40,30+subcol*40,30+subrow*40)
                qp.drawLine(30+col*40,30+row*40,30+(col-subrow+row)*40,30+(row+subcol-col)*40)
                qp.drawLine(30+(subcol-subrow+row)*40,30+(subrow+subcol-col)*40,30+subcol*40,30+subrow*40)
                qp.drawLine(30+(subcol-subrow+row)*40,30+(subrow+subcol-col)*40,30+(col-subrow+row)*40,30+(row+subcol-col)*40)
                
              
    qp.setPen(QColor(17,87,64))
    qp.drawText(70,350,str(Player_1.get_score()))
    qp.drawText(130,350,"*"+str(Player_1.get_multiplier()))
    qp.setPen(QColor(185,151,91))
    qp.drawText(70,370,str(Player_2.get_score()))
    qp.drawText(130,370,"*"+str(Player_2.get_multiplier()))
    if self.outofscope==True:
      qp.setPen(Qt.black)
      qp.drawText(20,390,"Error! Please click in the grids!")
    if self.overwritegrids==True:
      qp.setPen(Qt.black)
      qp.drawText(20,390,"Error! You cannot overwrite grids!")
   
    self.sum=0
    for k in self.list_1:
      for i in k:
        self.sum+=i
        if self.sum==96:
          
          if Player_1.get_score()>Player_2.get_score():
            qp.setPen(QColor(17,87,64))
            qp.drawText(340,80,"Game Over!")
            qp.drawText(340,100,P1+" won!")
          elif Player_1.get_score()<Player_2.get_score():
            qp.setPen(QColor(185,151,91))
            qp.drawText(340,80,"Game Over!")
            qp.drawText(340,100,P2+" won!")
          else:
            qp.setPen(Qt.black)
            qp.drawText(340,80,"Game Over!")
            qp.drawText(340,100,"Draw!")

    # TODO draw the playing field, including all moves so far and resulting
    # squares. Also dray score information for both players and display
    # whose turn it is.

    qp.end()

  # TODO We sugguest the following private method, which takes the indices of
  # a player's move and updates that player's score object so that it is
  # displayed correctly on the next update. THis method is not required, and if
  # you choose to use it, you are free to change its parameters.
  #def __move(self, x, y):
  

  def mousePressEvent(self, event):
    x=event.x()
    y=event.y()
    square_count=0
    self.outofscope=False
    self.overwritegrids=False
    

    if 10<=x<330 and 10<=y<330:
        col1=(x-10)//40
        row1=(y-10)//40
        if self.list_1[row1][col1]!=0:
          self.overwritegrids=True
        else:
          if self.count%2==0:
            self.list_1[row1][col1]=1
            self.count+=1
            for length in range(-min(row1,col1),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1+length][col1]==1 and self.list_1[row1][col1+length]==1 and self.list_1[row1+length][col1+length]==1:
                square_count+=1
            for length in range(-min(row1,(7-col1)),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1+length][col1]==1 and self.list_1[row1][col1-length]==1 and self.list_1[row1+length][col1-length]==1:
                square_count+=1
            for length in range(-min((7-row1),col1),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1-length][col1]==1 and self.list_1[row1][col1+length]==1 and self.list_1[row1-length][col1+length]==1:
                square_count+=1
            for length in range(-min((7-row1),(7-col1)),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1-length][col1]==1 and self.list_1[row1][col1-length]==1 and self.list_1[row1-length][col1-length]==1:
                square_count+=1
          
          
            for subrow1 in range(row1+1,8):
              for subcol1 in range(col1+1,8):
                if (subcol1-(subrow1-row1))>=0 and (subrow1+(subcol1-col1))<8 and (row1+(subcol1-col1))<8 and (col1-(subrow1-row1))>=0:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow1][subcol1]==1 and self.list_1[subrow1+(subcol1-col1)][subcol1-(subrow1-row1)]==1 and self.list_1[row1+(subcol1-col1)][col1-(subrow1-row1)]==1:
                    square_count+=1
                if (row1-(subcol1-col1))>=0 and (col1+(subrow1-row1))<8 and (subrow1-(subcol1-col1))>=0 and (subcol1+(subrow1-row1))<8:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow1][subcol1]==1 and self.list_1[subrow1-(subcol1-col1)][subcol1+(subrow1-row1)]==1 and self.list_1[row1-(subcol1-col1)][col1+(subrow1-row1)]==1:
                    square_count+=1
          
            for subrow2 in range(0,row1):
              for subcol2 in range(0,col1):
                if (subrow2-(col1-subcol2))>=0 and (subcol2+(row1-subrow2))<8 and (row1-(col1-subcol2))>=0 and (col1+(row1-subrow2))<8:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow2][subcol2]==1 and self.list_1[subrow2-(col1-subcol2)][subcol2+(row1-subrow2)]==1 and self.list_1[row1-(col1-subcol2)][col1+(row1-subrow2)]==1:
                    square_count+=1
                if (row1+(col1-subcol2))<8 and (col1-(row1-subrow2))>=0 and (subrow2+(col1-subcol2))<8 and (subcol2-(row1-subrow2))>=0:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow2][subcol2]==1 and self.list_1[subrow2+(col1-subcol2)][subcol2-(row1-subrow2)]==1 and self.list_1[row1+(col1-subcol2)][col1-(row1-subrow2)]==1:
                    square_count+=1
          
              
            if square_count>=1:
              Player_1.set_multiplier(square_count)
            else:
              Player_1.set_multiplier(1)
          
            for length in range(-min(row1,col1),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1+length][col1]==1 and self.list_1[row1][col1+length]==1 and self.list_1[row1+length][col1+length]==1:
                Player_1.add_points((length-1)**2)
            for length in range(-min(row1,(7-col1)),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1+length][col1]==1 and self.list_1[row1][col1-length]==1 and self.list_1[row1+length][col1-length]==1:
                Player_1.add_points((length-1)**2)
            for length in range(-min((7-row1),col1),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1-length][col1]==1 and self.list_1[row1][col1+length]==1 and self.list_1[row1-length][col1+length]==1:
                Player_1.add_points((length-1)**2)
            for length in range(-min((7-row1),(7-col1)),0):
              if self.list_1[row1][col1]==1 and self.list_1[row1-length][col1]==1 and self.list_1[row1][col1-length]==1 and self.list_1[row1-length][col1-length]==1:
                Player_1.add_points((length-1)**2)
            
            for subrow1 in range(row1+1,8):
              for subcol1 in range(col1+1,8):
                if (subcol1-(subrow1-row1))>=0 and (subrow1+(subcol1-col1))<8 and (row1+(subcol1-col1))<8 and (col1-(subrow1-row1))>=0:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow1][subcol1]==1 and self.list_1[subrow1+(subcol1-col1)][subcol1-(subrow1-row1)]==1 and self.list_1[row1+(subcol1-col1)][col1-(subrow1-row1)]==1:
                    Player_1.add_points((subrow1-row1+0.5)**2+(subcol1-col1+0.5)**2)
                if (row1-(subcol1-col1))>=0 and (col1+(subrow1-row1))<8 and (subrow1-(subcol1-col1))>=0 and (subcol1+(subrow1-row1))<8:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow1][subcol1]==1 and self.list_1[subrow1-(subcol1-col1)][subcol1+(subrow1-row1)]==1 and self.list_1[row1-(subcol1-col1)][col1+(subrow1-row1)]==1:
                    Player_1.add_points((subrow1-row1+0.5)**2+(subcol1-col1+0.5)**2)
          
            for subrow2 in range(0,row1):
              for subcol2 in range(0,col1):
                if (subrow2-(col1-subcol2))>=0 and (subcol2+(row1-subrow2))<8 and (row1-(col1-subcol2))>=0 and (col1+(row1-subrow2))<8:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow2][subcol2]==1 and self.list_1[subrow2-(col1-subcol2)][subcol2+(row1-subrow2)]==1 and self.list_1[row1-(col1-subcol2)][col1+(row1-subrow2)]==1:
                    Player_1.add_points((subrow2-row1-0.5)**2+(subcol2-col1-0.5)**2)
                if (row1+(col1-subcol2))<8 and (col1-(row1-subrow2))>=0 and (subrow2+(col1-subcol2))<8 and (subcol2-(row1-subrow2))>=0:
                  if self.list_1[row1][col1]==1 and self.list_1[subrow2][subcol2]==1 and self.list_1[subrow2+(col1-subcol2)][subcol2-(row1-subrow2)]==1 and self.list_1[row1+(col1-subcol2)][col1-(row1-subrow2)]==1:
                    Player_1.add_points((subrow2-row1-0.5)**2+(subcol2-col1-0.5)**2)
           
            
          else:
            self.list_1[row1][col1]=2
            self.count+=1
            for length in range(-min(row1,col1),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1+length][col1]==2 and self.list_1[row1][col1+length]==2 and self.list_1[row1+length][col1+length]==2:
                square_count+=1
            for length in range(-min(row1,(7-col1)),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1+length][col1]==2 and self.list_1[row1][col1-length]==2 and self.list_1[row1+length][col1-length]==2:
                square_count+=1
            for length in range(-min((7-row1),col1),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1-length][col1]==2 and self.list_1[row1][col1+length]==2 and self.list_1[row1-length][col1+length]==2:
                square_count+=1
            for length in range(-min((7-row1),(7-col1)),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1-length][col1]==2 and self.list_1[row1][col1-length]==2 and self.list_1[row1-length][col1-length]==2:
                square_count+=1
          
            for subrow1 in range(row1+1,8):
              for subcol1 in range(col1+1,8):
                if (subcol1-(subrow1-row1))>=0 and (subrow1+(subcol1-col1))<8 and (row1+(subcol1-col1))<8 and (col1-(subrow1-row1))>=0:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow1][subcol1]==2 and self.list_1[subrow1+(subcol1-col1)][subcol1-(subrow1-row1)]==2 and self.list_1[row1+(subcol1-col1)][col1-(subrow1-row1)]==2:
                    square_count+=1
                if (row1-(subcol1-col1))>=0 and (col1+(subrow1-row1))<8 and (subrow1-(subcol1-col1))>=0 and (subcol1+(subrow1-row1))<8:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow1][subcol1]==2 and self.list_1[subrow1-(subcol1-col1)][subcol1+(subrow1-row1)]==2 and self.list_1[row1-(subcol1-col1)][col1+(subrow1-row1)]==2:
                    square_count+=1
                  
            for subrow2 in range(0,row1):
              for subcol2 in range(0,col1):
                if (subrow2-(col1-subcol2))>=0 and (subcol2+(row1-subrow2))<8 and (row1-(col1-subcol2))>=0 and (col1+(row1-subrow2))<8:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow2][subcol2]==2 and self.list_1[subrow2-(col1-subcol2)][subcol2+(row1-subrow2)]==2 and self.list_1[row1-(col1-subcol2)][col1+(row1-subrow2)]==2:
                    square_count+=1
                if (row1+(col1-subcol2))<8 and (col1-(row1-subrow2))>=0 and (subrow2+(col1-subcol2))<8 and (subcol2-(row1-subrow2))>=0:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow2][subcol2]==2 and self.list_1[subrow2+(col1-subcol2)][subcol2-(row1-subrow2)]==2 and self.list_1[row1+(col1-subcol2)][col1-(row1-subrow2)]==2:
                    square_count+=1
              
            if square_count>=1:
              Player_2.set_multiplier(square_count)
            else:
              Player_2.set_multiplier(1)
          
            for length in range(-min(row1,col1),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1+length][col1]==2 and self.list_1[row1][col1+length]==2 and self.list_1[row1+length][col1+length]==2:
                Player_2.add_points((length-1)**2)
            for length in range(-min(row1,(7-col1)),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1+length][col1]==2 and self.list_1[row1][col1-length]==2 and self.list_1[row1+length][col1-length]==2:
                Player_2.add_points((length-1)**2)
            for length in range(-min((7-row1),col1),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1-length][col1]==2 and self.list_1[row1][col1+length]==2 and self.list_1[row1-length][col1+length]==2:
                Player_2.add_points((length-1)**2)
            for length in range(-min((7-row1),(7-col1)),0):
              if self.list_1[row1][col1]==2 and self.list_1[row1-length][col1]==2 and self.list_1[row1][col1-length]==2 and self.list_1[row1-length][col1-length]==2:
                Player_2.add_points((length-1)**2)
          
            for subrow1 in range(row1+1,8):
              for subcol1 in range(col1+1,8):
                if (subcol1-(subrow1-row1))>=0 and (subrow1+(subcol1-col1))<8 and (row1+(subcol1-col1))<8 and (col1-(subrow1-row1))>=0:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow1][subcol1]==2 and self.list_1[subrow1+(subcol1-col1)][subcol1-(subrow1-row1)]==2 and self.list_1[row1+(subcol1-col1)][col1-(subrow1-row1)]==2:
                    Player_2.add_points((subrow1-row1+0.5)**2+(subcol1-col1+0.5)**2)
                if (row1-(subcol1-col1))>=0 and (col1+(subrow1-row1))<8 and (subrow1-(subcol1-col1))>=0 and (subcol1+(subrow1-row1))<8:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow1][subcol1]==2 and self.list_1[subrow1-(subcol1-col1)][subcol1+(subrow1-row1)]==2 and self.list_1[row1-(subcol1-col1)][col1+(subrow1-row1)]==2:
                    Player_2.add_points((subrow1-row1+0.5)**2+(subcol1-col1+0.5)**2)
          
            for subrow2 in range(0,row1):
              for subcol2 in range(0,col1):
                if (subrow2-(col1-subcol2))>=0 and (subcol2+(row1-subrow2))<8 and (row1-(col1-subcol2))>=0 and (col1+(row1-subrow2))<8:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow2][subcol2]==2 and self.list_1[subrow2-(col1-subcol2)][subcol2+(row1-subrow2)]==2 and self.list_1[row1-(col1-subcol2)][col1+(row1-subrow2)]==2:
                    Player_2.add_points((subrow2-row1-0.5)**2+(subcol2-col1-0.5)**2)
                if (row1+(col1-subcol2))<8 and (col1-(row1-subrow2))>=0 and (subrow2+(col1-subcol2))<8 and (subcol2-(row1-subrow2))>=0:
                  if self.list_1[row1][col1]==2 and self.list_1[subrow2][subcol2]==2 and self.list_1[subrow2+(col1-subcol2)][subcol2-(row1-subrow2)]==2 and self.list_1[row1+(col1-subcol2)][col1-(row1-subrow2)]==2:
                    Player_2.add_points((subrow2-row1-0.5)**2+(subcol2-col1-0.5)**2)

    #for l in self.list_1:
      #print (l)    
    #print (" ")
    elif 300<=x<380 and 360<=y<=380:
      self.count=0
      self.list_1=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
      Player_1.reset_score()
      Player_2.reset_score()
      Player_1.reset_multiplier()
      Player_2.reset_multiplier()
      
    else:
      self.outofscope=True
      
    

    self.update()
      
    # TODO replace pass with your implementation
    # Here, the player clicked on the window. If she clicked on a valiud
    # space, process her score changes, if any. Be sure to update the attributes
    # needed to draw the resulting game board.
    

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeSquares()
  sys.exit(app.exec_())
  
