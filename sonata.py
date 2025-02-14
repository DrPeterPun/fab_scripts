
import random
def sonata_hits(revealed):
     attack = revealed.count("a")
     non_attack = revealed.count("n")
     return min(attack, non_attack)

def sample_deck(deck):
    hits = 0
    played = 0
    while len(deck) >= 4+sonata_size:
        # draw for the turn
        hand = deck[:4]
        deck = deck[4:]

        # cast each sonata
        for _ in range(hand.count("s")):
            played += 1
            #reveal top n
            sonata =  deck[:sonata_size]
            #remove attacks for each sonata hit
            for _ in range(sonata_hits(sonata)):
                deck.remove("a")
                hits += 1
            deck.shuffle()

    if played != 3:
        return None
    else:
        hits
                

for i in range(10):
    attack = 30-i
    non_attack = 30+i
    sonata_size = 3

    deck = "s"*3 + "n"*(non_attack - 3) + "a"*(attack)
    deck = list(deck)
    hits_per_game = {0:0, 1:0, 2:0, 3:0}
    for i in range(1000):
        deck.shuffle()
        hits = sample_deck(deck)
        if hits != None:
            hits_per_game[hits] += 1
    total_games = sum(hits_per_game.values())
    percent_hits_per_game = { k: v/total_games for k, v in  hits_per_game.items() }
    print("attacks:", attack, "\tnon-attacks:", attack,"\thits:",hits_per_game, "\tpercent:", percent_hits_per_game)