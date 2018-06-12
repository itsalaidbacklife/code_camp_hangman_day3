def setup():
    size(1000, 1000)
    global show_guy, correct_guesses, incorrect_guesses, word
    show_guy = False
    correct_guesses = []
    incorrect_guesses = []
    word = "secret" #The secret word
    
    #set up correct guesses to have blank spaces for each missing letter
    for x in range(len(word)):
        correct_guesses.append("--")
    
def draw():
    # Draw gallows
    background(150)
    fill(255)
    strokeWeight(7)
    line(200, 800, 800, 800)
    line(500, 800, 500, 200)
    line(500, 200, 300, 200)
    line(300, 200, 300, 300)
    
    # Draw guy
    if len(incorrect_guesses) > 0:
        ellipse(300, 350, 100, 100) #head
        if len(incorrect_guesses) > 1:
            line(300, 400, 300, 650) #body
            if len(incorrect_guesses) > 2:
                line(300, 500, 200, 350)#left arm
                if len(incorrect_guesses) > 3:
                    line(300, 500, 400, 350) #right arm
                    if len(incorrect_guesses) > 4:
                        line(300, 650, 200, 750)#left leg
                        if len(incorrect_guesses) > 5:
                            line(300, 650, 400, 750) #right leg
                            if len(incorrect_guesses) > 6:
                                # Frowny Face
                                noFill()
                                arc(300, 400, 50, 50, PI+PI/6, 2*PI - PI/6)
                                ellipse(280, 340, 20, 20)
                                ellipse(320, 340, 20, 20)
        
    # Display guessed letters
    textSize(18)
        # Wrong guesses
    text("Wrong Guesses:", 0, 50)
    for index, letter in enumerate(incorrect_guesses):
        text(letter, index*25, 100)
        # Right guesses
    for index, letter in enumerate(correct_guesses):
        text("Secret Word", 0, 700)
        text(letter, index*25, 800)
    
def mousePressed():
    global show_guy
    show_guy = not show_guy
    
def keyPressed():
    global guesses
    guess(key)
    
def guess(letter):
    global correct_guesses, incorrect_guesses, word
    in_word = False
    for index, x in enumerate(word):
        if letter == x:
            correct_guesses[index] = letter
            in_word = True
    if not in_word:
        incorrect_guesses.append(letter)