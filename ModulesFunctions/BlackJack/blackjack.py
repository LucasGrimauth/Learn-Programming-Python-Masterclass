import tkinter
import random

def load_images(card_images):
  suits = ["heart", "club", "diamond", "spade"]
  face_cards = ["jack", "queen", "king"]
  extension = "png"

  # tkinter version must be equal or above 8.6 to handle png
  for suit in suits:
    for card in range(1, 11):
      name = "cards/{}_{}.{}".format(str(card), suit, extension)
      image = tkinter.PhotoImage(file=name)
      card_images.append((card, image,))

    for card in face_cards:
      name = "cards/{}_{}.{}".format(str(card), suit, extension)
      image = tkinter.PhotoImage(file=name)
      card_images.append((10, image,))

def deal_card(frame):
  card = deck.pop(0)
  deck.append(card)
  tkinter.Label(frame, image=card[1], relief="raised").pack(side="left")
  return card

def score_hand(hand):
  score = 0
  ace = False

  for card in hand:
    card_value = card[0]
    if card_value == 1 and not ace:
      ace = True
      card_value = 11
    score += card_value

    if score > 21 and ace:
      score -= 10
      ace = False

  return score

def deal_dealer():
  dealer_score = score_hand(dealer_hand)
  while 0 < dealer_score < 17:
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

  player_score = score_hand(player_hand)

  if player_score > 21:
    result_text.set("Dealer wins!")
  elif dealer_score > 21 or dealer_score < player_score:
    result_text.set("Player wins!")
  elif dealer_score > player_score:
    result_text.set("Dealer wins!")
  else:
    result_text.set("Draw!")

def deal_player():
  player_hand.append(deal_card(player_card_frame))
  player_score = score_hand(player_hand)
  
  player_score_label.set(player_score)

  if player_score > 21:
    result_text.set("Dealer wins!")

def initial_deal():
  deal_player()
  dealer_hand.append(deal_card(dealer_card_frame))
  dealer_score_label.set(score_hand(dealer_hand))
  deal_player()

def new_game():
  global dealer_card_frame
  global player_card_frame
  global dealer_hand
  global player_hand

  dealer_card_frame.destroy()
  dealer_card_frame = tkinter.Frame(card_frame, background="green")
  dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

  player_card_frame = tkinter.Frame(card_frame, background="green")
  player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

  result_text.set("")

  # Create the list to store the dealer's and player's hands
  dealer_hand = []
  player_hand = []

  initial_deal();

def shuffle():
  random.shuffle(deck)

def play():
  initial_deal();
  mainWindow.mainloop()

mainWindow = tkinter.Tk()

# Set up screen and frames
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(backgroun="forest green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# Load cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
  play()