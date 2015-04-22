from player import Player, Bot

class Table():
  '''
    This enforces all rules, controlls turns, etc.
  '''
  def __init__(self, user_player_obj):
    self.player_list = [user_player_obj]
    while len(self.player_list) < 4:
      self.player_list.append(player.Bot())
  def bet():
    '''
      Options:
        Raise,
          --I consider the initial bet a raise from 0--
        Call,
          --check is call of 0--
        Fold.
    '''
    match_value = 0
    player_investments = [0]*4
    
    for i in range(3):
      if player_list[i]!=false:
        response = player_list[i].bet()
        if response == false:
          fold(player_list[i])
        else:#all other responses are number values for bets
          if response+player_investments[i] < match_value and self.player_list[i].value > 0:
            print("Cheater!")
            fold(i)
          elif(response > match_value):
            match_value = response
            player_investments[i]+=response
          else:
            player_investments[i]+=response

  def full_game():
    '''
      A game consists of: 
        draw 2 cards;
        bet;
        draw more cards;
        bet;
        conclusion.
    '''
  def fold(player_number):
    
