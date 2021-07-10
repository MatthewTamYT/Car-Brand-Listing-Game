from car_brands import brand_list

guessed_cars = []

print("Let's play this car brand guessing game! There are 50 famous car brands to be chosen. If you "
      "successfully name 30, you have won.")

score = 0

play = True

while play:

    guess = True

    while guess:

        guess1 = True

        while guess1:

            car1 = input("Enter the car brand: ")
            if car1.lower().strip() in brand_list:
                guessed_cars = brand_list.pop(brand_list.index(car1.lower().strip()))
                score = score + 1
                guess1 = False
            elif car1.lower().strip() in guessed_cars:
                print("You have already said this one.")
                guess1 = False
            else:
                print("Unfortunately, your guess either not famous enough to be on the list, or is "
                      "wrong.")
                guess1 = False

        guess_after_1 = True

        while guess_after_1:

            if score >= 30:
                print("You have successfully guessed 30 car brands!")
                print("Thank you for playing.")
                placeholder = input("")
            else:
                car2 = input("Correct! Next guess (type 'n' if you don't have one): ")
                if car2.lower().strip() == 'n':
                    guess = False
                    print(f"Unfortunately, you did not guess all of the items. You guessed {score}"
                          "/30.")
                    play_again = input("If you want to play again, type x: ")
                    if play_again.strip().lower() != 'x':
                        thank_you = True
                        while thank_you:
                            enjoy = input("Did you enjoy the game? This would really help "
                                          "us make the game better! (y/n): ")
                            if enjoy.lower().strip() == 'y':
                                print("Glad you enjoyed the game.")
                                raise SystemExit
                            else:
                                print("We would be working to make this game better.")
                                raise SystemExit

                    else:
                        guess_after_1 = False
                elif car2.lower().strip() in brand_list:
                    guessed_cars = brand_list.pop(brand_list.index(car2.lower().strip()))
                    score = score + 1
                else:
                    print("You have either entered this already, made a spelling mistake, "
                          "or your entry was not famous enough.")
