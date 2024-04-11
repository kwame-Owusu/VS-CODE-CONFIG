#include <iostream>
#include <ctime>
using namespace std;


void draw_board(char *spaces);
void player_move(char *spaces, char player);
void computer_move(char *spaces, char computer);
bool check_winner(char *spaces, char player);
bool check_tie(char *spaces);
void check_occupied(char *spaces, char player, char computer);







int main(){
  char spaces[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
  char player = 'X';
  char computer = 'O';
  bool running = true;

  draw_board(spaces);

  while (running)
  {
    player_move(spaces, player);
    draw_board(spaces);
    if (check_winner(spaces, player))
    {
      running = false;
      break;
    }
    else if (check_tie(spaces))
    {
      running = false;
      break;
    }
    
    
    computer_move(spaces,computer);
    draw_board(spaces);
   
     if (check_winner(spaces, player))
    {
      running = false;
      break;
     
    }
     else if (check_tie(spaces))
    {
      running = false;
      break;
    }

    
  }
  
  cout <<"Thanks For Playing"<<endl;
    


  return 0;
}



void draw_board(char *spaces){
  cout<<"\n";
  cout << "     |     |     "<<endl;
  cout << "  "<<spaces[0]<<"  |  "<<spaces[1]<<"  |   "<<spaces[2]<<"  "<<endl;
  cout << "_____|_____|_____"<<endl;
  cout << "     |     |     "<<endl;
  cout << "  "<<spaces[3]<<"  |  "<<spaces[4]<<"  |   "<<spaces[5]<<"  "<<endl;
  cout << "_____|_____|_____"<<endl;
  cout << "     |     |"<<endl;
  cout << "  "<<spaces[6]<<"  |  "<<spaces[7]<<"  |   "<<spaces[8]<<"  "<<endl;
  cout << "     |     |     "<<endl;
  cout<<"\n";

}
void player_move(char *spaces, char player){
  int number;
  do
  {
    cout<<"Enter a spot to place a marker (1-9)"<<endl;
    cin>>number;
    number--;
    if (spaces[number] == ' ')
    {
      spaces[number] = player;
      break;
    }
    

  } while (!number > 0 || !number < 8);
  
}
void computer_move(char *spaces, char computer){
  int number;
  // to create a random number
  srand(time(0));

  while (true)
  {
  // creates a random number between 0 and 9
    number = rand() % 9;
    if (spaces[number] ==  ' ')
    {
      spaces[number] = computer;
      break;
    
    }

  }
  
}
// what i used before making the winning condition better
bool checkWin(char *spaces,char player){
  // conditions to check for all vertical, horizontal and diagonal winning conditions.

  // row check
  if ((spaces[0] != ' ')&& (spaces[0] == spaces[1]) && (spaces[1] == spaces[2])){
    spaces[0] == player ? cout<<"You win \n" : cout<<"You lose\n";
  }
  else if ((spaces[3] != ' ')&& (spaces[3] == spaces[4]) && (spaces[4] == spaces[5])){
    spaces[3] == player ? cout<<"You win! \n" : cout<<"You lose\n";
  }
  else if ((spaces[6] != ' ')&& (spaces[6] == spaces[7]) && (spaces[7] == spaces[8])){
    spaces[6] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  // column check
  else if ((spaces[0] != ' ')&& (spaces[0] == spaces[3]) && (spaces[3] == spaces[6])){
    spaces[0] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  else if ((spaces[1] != ' ')&& (spaces[1] == spaces[4]) && (spaces[4] == spaces[7])){
    spaces[1] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  else if ((spaces[2] != ' ')&& (spaces[2] == spaces[5]) && (spaces[5] == spaces[8])){
    spaces[2] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  // diagonal check
  else if ((spaces[0] != ' ')&& (spaces[0] == spaces[4]) && (spaces[4] == spaces[8])){
    spaces[0] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  else if ((spaces[2] != ' ')&& (spaces[2] == spaces[4]) && (spaces[4] == spaces[6])){
    spaces[2] == player ? cout<<"You win \n" : cout<<"You lose\n";
  
  }
  else{
    return false; 
  }

  return true;
}

bool check_tie(char *spaces){
  for (int i = 0; i < 9; i++)
  {
    if (spaces[i] == ' ')
    {
      return false;
    }
    
  }
  cout <<"its a tie \n";
  return true;
}

bool check_winner(char spaces[], char player) {
    // Winning conditions: rows, columns, diagonals
    int winningConditions[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // rows
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // columns
        {0, 4, 8}, {2, 4, 6}              // diagonals
    };

    // Check all winning conditions
    for (int i = 0; i < 8; ++i) {
        int row = winningConditions[i][0];
        int col = winningConditions[i][1];
        int diag = winningConditions[i][2];

        if (spaces[row] != ' ' && spaces[row] == spaces[col] && spaces[col] == spaces[diag]) {
            spaces[row] == player ? cout<<"You win \n" : cout<<"You lose\n";
            return true;
        }
    }

    return false; // No winning condition found
}


void check_occupied(char *spaces, char player, char computer){
  for (int i = 0; i < 9; i++)
  {
    if (spaces[i] == player || computer)
    {
     cout <<"Space occupied, try different space"<<endl;
    }
    
  }
   
}
