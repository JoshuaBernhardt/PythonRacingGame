def loadScore(score):    #load score file
    import pickle
    scoreFile=open(("scorefile.dat"),'rb')   #open
    totalScore=pickle.load(scoreFile)    #load score
    scoreFile.close()
    writeScore(totalScore,score)

def writeScore(totalScore,score):       #writes new score
    import pickle
    scoreFile=open(("scorefile.dat"),'wb')
    totalScore+=score                      #adds on current game score
    pickle.dump(totalScore, scoreFile)   #write
    scoreFile.close()
    #readScore()    #read score for testing


def gameOver(score):   #Game over splash screen
    import pygame      #import
    import random
    pygame.init()      #Initialise
    pygame.display.init()
    screen=pygame.display.set_mode((1200,1080),pygame.FULLSCREEN,0) #Set display res

    crash=pygame.mixer.music.load("car_crash.mp3")  #play sound
    pygame.mixer.music.play(0,0)
    
    pygame.display.set_caption("Game Over")   #Set caption to game
    menuFont=pygame.font.SysFont("dejavsusans", 60)    #Load font
    loadScore(score)
    
    def menuLoad():        #Load the menu
        pygame.display.init()
        from menu import mainMenu
        mainMenu()
    
    while True:
        pygame.event.pump()
        pygame.display.flip()    #Update display
        screen.fill((0,100,0))     #Fill background
        scoreEnd=str(score)
        text=menuFont.render("Your Score:  "+scoreEnd,True,(255,255,255))
        text2=menuFont.render("Press ESC to return",True,(255,255,255))
        screen.blit(text,(500,400))
        screen.blit(text2,(500,700))
        keys=pygame.key.get_pressed()    #Detection of keys
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            menuLoad()
            
        for event in pygame.event.get():   #quit via window manager
            if event.type==pygame.QUIT:
                pygame.quit()

        

def gameStart():


    import pygame      #import
    import random
    pygame.init()      #Initialise
    gameRunning=True   #gameRunning
    pygame.display.init()
    gameContinue=True

    
    
    def menuLoad():
        from menu import mainMenu   #load main menu
        
        mainMenu()

    screen=pygame.display.set_mode((1200,1080),pygame.FULLSCREEN,0) #Set display res
    pygame.display.set_caption("Game")   #Set caption to game

    
    car=pygame.image.load("Car.png")     #Load assets

        #car=pygame.image.load("Black_viper.png")
    
    traffic=pygame.image.load("Van.png")
    road=pygame.image.load("roadbig.jpg")   
    traffic2=pygame.image.load("taxi.png")



    grass=pygame.image.load("grassL.jpg")

    #else:
        #grass=pygame.image.load("snow.jpg")
    
 
    
    
    
    screenWidth=screen.get_rect().width     #Get width of screen
    screenHeight=screen.get_rect().height   #Get height
    clock=pygame.time.Clock()               #Set up clock

    carRunning=pygame.mixer.music.load("Car Driving-SoundBible.com-923766101.mp3")
    pygame.mixer.music.play(1,0)
    
    
    
    menuFont=pygame.font.SysFont("dejavsusans", 60)    #Load font
    font2=pygame.font.SysFont("dejavsusans", 30)

    x1car=500          #Initial car coordinate
    y1road=(-2400)      #Initial y coords
    yGrass=(-2400)

    x1traffic=330   #x coords of traffic

    x2traffic=470

    speed=3          #Initial speed
    score=0          #Initial score
    
    y1traffic=(-200)

    y2traffic=(-800)
    
    def randomise(x1traffic):           #Randomising position of traffic1
        randomPos=random.randint(0,3)
        
        
        if randomPos==0:                
            x1traffic=330
            
            
        if randomPos==1:
            x1traffic=460
            
            
        if randomPos==2:
            x1traffic=620
            
            
        if randomPos==3:
            x1traffic=740
            
            
        
        return x1traffic
    
    def randomise2(x1traffic):              #Randomising position of traffic2
        randomPos=random.randint(0,3)
        
        if randomPos==0:
            x2traffic=360
            
            
        if randomPos==1:
            x2traffic=470
            
            
        if randomPos==2:
            x2traffic=620
            
            
            
        if randomPos==3:
            x2traffic=740
            
            
        
        return x2traffic
    
    while gameRunning==True:             #Keep running
        pygame.event.pump()
        pygame.display.flip()    #Update display
        screen.fill((0,200,0))     #Fill background
        screen.blit(grass,(0,yGrass))      
        screen.blit(grass,(1010,yGrass))      #Blit images
        screen.blit(road,(300,y1road))
        
        
        
        speed+=0.03         #Increasing speed over time
        
        scoreText1=str(score)                                #Display score on screen
        text=menuFont.render(scoreText1,True,(255,255,255))
        scoreText=menuFont.render("Score: ",True,(255,255,255))
        controls=font2.render("Movement = Arrow Keys",True,(255,255,255))
        controls2=font2.render("Escape Key = Exit",True,(255,255,255))
        tutorial=font2.render("Try to dodge the cars",True,(220,220,255))
        screen.blit(scoreText,(910,398))
        screen.blit(text,(1050,400))
        screen.blit(controls,(910,800))
        screen.blit(controls2,(910,700))
        screen.blit(tutorial,(910,900))
        
        
        if y1road>=(-33):      #Scrolling logic
            y1road=(-2400)
            yGrass=(-2400)
            
        else:
            y1road+=(speed)
            yGrass+=(speed)
            

        
            

        screen.blit(car,(x1car,845))   #BLIT player car
        
        if y1traffic<=1000:       #Placing traffic and adjusting positions
            y1traffic+=(speed)
        else:
            y1traffic=(-200)
            score+=1
            x1traffic=randomise(x1traffic)

        if y1traffic<=1000:
            y1traffic+=(speed)
        else:
            y1traffic=(-200)
            score+=1
            x1traffic=randomise(x1traffic)

        if y2traffic<=1000:
            y2traffic+=(speed)
        else:
            y2traffic=(-200)
            score+=1
            x2traffic=randomise2(x2traffic)

        if y2traffic<=1000:
            y2traffic+=(speed)
        else:
            y2traffic=(-200)
            score+=1
            x2traffic=randomise2(x2traffic)

        
        
            
        screen.blit(traffic2,(x2traffic,y2traffic))  #Display traffic

        screen.blit(traffic,(x1traffic,y1traffic))

        

        pygame.display.flip()
        keys=pygame.key.get_pressed()    #Detection of keys


        #Player Car Controls

        if keys[pygame.K_LEFT]:    #If left arrow pressed
            if x1car<300:          #If car reaches edge of road
                None
                
            else:               #Otherwise:
                
                x1car-=35      #Move car left with update x coord
                
        if keys[pygame.K_RIGHT]:    #Right arrow
            if x1car>800:           #Edge of right side of road
                None
            else:
                
                x1car+=35

        
                
                           #Move car right, updated x coord
               

    ##################

        carWidth=car.get_width()
        carHeight=car.get_height()
        carRect=pygame.Rect(x1car,845,carWidth,carHeight)
        
        traffic1Width=traffic.get_width()
        traffic1Height=traffic.get_height()
        
        traffic2Width=traffic2.get_width()
        traffic2Height=traffic2.get_height()
        
        trafficRect=pygame.Rect(x1traffic+20,y1traffic-20,traffic1Width-30,traffic1Height-40)
        traffic2Rect=pygame.Rect(x2traffic+20,y2traffic-20,traffic2Width-30,traffic2Height-40)
        
        if carRect.colliderect(trafficRect):
            pygame.mixer.music.stop()
            gameOver(score) 
        if carRect.colliderect(traffic2Rect):
            pygame.mixer.music.stop()
            gameOver(score)
        
        


        pygame.display.flip()       #Update display
                    #Clock speed


        #Exit on window exit

        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            menuLoad()

        for event in pygame.event.get():
            pygame.display.init()
            if event.type==pygame.QUIT:
                
                gameRunning=False
                pygame.quit()
               

        #start the game

