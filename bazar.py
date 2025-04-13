import random

def sonata_hits(revealed):
     attack = revealed.count("a")
     non_attack = revealed.count("n") + revealed.count("s")
     return min(attack, non_attack)

def sample_deck(deck):
    hits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
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
            n_hits = sonata_hits(sonata)
            hits[n_hits] += 1
            for _ in range(n_hits):
                deck.remove("a")
            random.shuffle(deck)

    #if played != 3:
    #    return None
    #else:
    return hits
                
n = 10000


for j in range(1):
    file_name = f"sonata_{j}_misses.txt"
    with open(file_name, "w") as file:  # "a" mode appends to the file
        print("n=",n,file=file)
    for i in range(11):
        #miss = j
        miss = 0
        attack = 30-i
        non_attack = 30+i-miss
        sonata_size = 3

        deck = "s"*3 + "n"*(non_attack - 3) + "a"*(attack) + "m"*miss
        deck = list(deck)
        hits_per_game = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
        
        for _ in range(n):
            random.shuffle(deck)
            hits = sample_deck(deck)
            #print(hits)
            hits_per_game = { key: hits_per_game[key] + hits[key] for key in hits_per_game}
        #print(hits_per_game)

        total_games = sum(hits_per_game.values())
        percentage_hits = {key: round(value / total_games, 3) for key, value in hits_per_game.items()}
        print("attack", attack,"non-attack",non_attack)
        print(percentage_hits)
        

        #total_games = sum(hits_per_game.values())
        #percent_hits_per_game = { k: v/total_games for k, v in  hits_per_game.items() }
        #formated_percentage = {key: f"{value:.2%}" for key, value in percent_hits_per_game.items()}
        #percentage_sonata = ( hits_per_game[1] + hits_per_game[2] *2 + hits_per_game[3]*3 ) / ( total_games * 3 )
        #print("attacks:", attack, "\tnon-attacks:", non_attack,"\tmisses",miss,"\thits:",hits_per_game, "\tpercent:", formated_percentage, "hit % per sonata", f"{percentage_sonata:.2%}")
        #with open(file_name, "a") as file:  # "a" mode appends to the file
        #    print("attacks:", attack, "\tnon-attacks:", non_attack, 
        #        "\thits:", hits_per_game, "\tpercent:", formated_percentage, 
        #        "single sonata percentage", f"{percentage_sonata:.2%}", file=file)
