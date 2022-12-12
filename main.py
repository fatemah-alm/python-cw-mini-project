# part 1

def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20

#######

def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200

############

def padel_balls_cost(ball_boxes):
    if ball_boxes == "1":
        return 2
    elif ball_boxes == "2":
        return 3.5
    elif ball_boxes == "3":
        return 5

############

def padel_game_cost():
    hours = input("How many hours: ")
    court_type = input("Do you want indoor or outdoor court: ")
    racket_band = input("What racket brand you want Bullpadel, Nox, or Siux: ")
    boxes = input("How many ball boxes do you want: ")
    total_cost = padel_court_cost(court_type) + rackets_cost(racket_band) +padel_balls_cost(boxes)

    print(f"for {court_type} it will cost {padel_court_cost(court_type)}")
    print(f"{racket_band} will cost {rackets_cost(racket_band)}")
    print(f"{boxes} boxes will cost {padel_balls_cost(boxes)}")
    print(f"total game cost is: {total_cost} ")
padel_game_cost()