
def guess_gamme():
    score = 0
    Questions = {
        "when was the first known use of the word 'quiz'?" : ['0) 1771', '1) 1781', '2) 1871', '3) 1881'],
        "which built_in function can get information from the user?": ['get', 'input', 'print', 'write'],
        "which keyboard do you use to loop over a given list of elements?":['To combine several strings into one',
        'To compress several files into one archive', 'To get information from the user', 'To iterate over two or more sequences at the same time.']
}
    # user_response = int(input('enter the correct option'))
    for questions, options in Questions.items():
        print (questions)
        print(*options ,  sep = "\n")
        user_response =(input('enter your options: '))
        if user_response.lower() == options[0].lower():
            score+=1
            print("correct!!!")
        
        elif user_response.lower() == options[1].lower():
            score+=1
            print("1, correct!")
        
        elif user_response.lower() == options[2].lower():
            score+=1
            print("2, correct!")
        else:
            print("Not correct!!!")

    print(f"Your total score is {score}")
       
guess_gamme()
