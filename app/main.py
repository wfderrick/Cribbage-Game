import tools
import structs
import round


def main():
    print("Welcome to my homemade Cribbage game!")
    print("I hope you enjoy!")
    play = input("Press any button" " to start: ")
    round_num = 1
    player1_hand = []
    player2_hand = []
    cut_card = 0
    player1_score = 0
    player2_score = 0
    crib = []
    crib_track = 0
    # print("|----------------------------------------------------|\n| Your Score: 0                   Opponent's Score: 0|\n|                                                    |\n|                                                    |\n|                                                    |\n|----------------------------------------------------|")

    round.round(
        player1_hand,
        player2_hand,
        cut_card,
        round_num,
        player1_score,
        player2_score,
        crib,
    )


if __name__ == "__main__":
    main()
