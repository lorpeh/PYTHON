
def quizz_game():
    Initial_point = 0
    Questions = {
        "What is the first name of Iron man":"Tony",
        "Who is called the god of ligthening in avengers": "Thor",
        "Who carried a shield of American flag theme in avengers": "Captain America",
        "Which avenger is green in color": "Hulk",
        "Which avenger can change it size": "Ant-man",
        "Which avenger is red in color and ha mind-stone": "vision"
    }
    player_name = input("enter your name: ")
    for question, answer in Questions.items():
        attempts = 3
        while attempts > 0:
            print(question)
            user_input = input("enter your answer: ")
            if Questions[question].lower()== user_input.lower():
                print('correct answer!!!')
                Initial_point += 1
                break
            
            attempts -= 1
            print(f"incorrect answer, you have {attempts} left")
            # user_input = input("enter your answer: ")
    total_points = Initial_point
    if total_points < 4:
        print("game is over, you failed")
    else:
        print("game is over, you passed")
    print(f"total_points is: {total_points}")
    print(f"thanks for playing: {player_name}")
    
quizz_game()



# def quiz_game():
#     Question = {
#     "What is the first name of Iron man":"Tony",
#     "Who is called the god of ligthening in avengers": "Thor",
#     "Who carried a shield of American flag theme in avengers": "Captain America",
#     "Which avenger is green in color": "Hulk",
#     "Which avenger can change it size": "Ant-man",
#     "Which avenger is red in color and ha mind-stone": "vision"
#     }

#     intial_point = 0
#     attempt = 3
#     for question in Question:
#         while attempt > 0:
#             print(question)
#             user_input = input("Enter your answer: ")
#             if Question[question].lower() == user_input.lower():
#                 print(attempt)
#                 intial_point +=1
#                 break
#             elif Question[question].lower() != user_input.lower():
#                 attempt -=1
#                 print(f"incorrect answer, you have {attempt} left. Try again!")
#                 user_input = input("Enter your answer: ")
#     total_points = intial_point
#     print(f"Your total point is: {total_points}")
# quiz_game()
