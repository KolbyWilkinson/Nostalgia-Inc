print ('Welcome back to Nostalgia Inc, #3896, return to your room immediately.')
s = input ('Respond: Y or N:')
print (s)
if s==("Y" or "y"):
    print ('Thank you for your obedience.')
    print ('After the encounter you walk to your room and enter.')
    t = input ('You decide to either to go directly to bed or watch the company TV channel. Type Bed or TV:')
    print (t)
    if t==("Bed" or "bed"):
        print ('You wake up well rested for the day.')
        print ('You eat breakfast and leave for work in the comapny building. You put in your time card and enter the factory. Due to your abundance of sleep, you make no mistakes and your supervisors congratulate you.')
        print ('You return to your room feeling confident and happy.')
        if t==("Bed" or "bed"):
            w = input ('You decide either to go out to a bar or go to bed. Type Bar or Bed:')
            print (w)
            if w==("Bed" or "bed"):
                print ('You wake up feeling refreshed.')

            if w==("Bar" or "bar"):
                print ('You are drinking alone when a woman catches your eye.')
                if w==("Bar" or "bar"):
                    x = input (' You decide either to go up to her or continue drinking. Type Meet or Drink:')
                    print (x)
                    print ('You go up to her and introduce yourself. As it turns out, she has had her eye on you.')
                    if x==("Meet" or "meet"):
                        g = input ('You talk to each other and eventually she asks you back to her room. Do you go with her or do you turn down the offer? Type Go or Deny:')
                        print (g)
                        if g==("Go" or "go"):
                            print ('You both walk back to her room and enter.')

                        if g==("Deny" or "deny"):
                            print ('Well sometimes that is for the best. You go back to your room and enter.')
                            print ('As you enter your room you find that masked men are going through your belongings.')
                            if g==("Deny" or "deny"):
                                h = input ('As you enter, do you confront them; or tip toe your way back out? Type Confront or Escape:')
                                print (h)
                                if h==("Confront" or "confront"):
                                    print ('As you confront them one of them steps out of the shadows and hits you in the back of the head with his nightstick, knocking you out.')
                                    print ('You awake in a dark room with little lighting. A man appears and tells you if you talk about what you saw that the company was going to make you disappear in the middle of the night.')
                                    print ('You agree, but inwardly you vow to get revenge for this tyranny.')
                                       
                    if x==("Drink" or "drink"):
                        print (' you continue to nurse your drink until you just decide to go back to your room.')
               
    if t==("TV" or "tv"):
        print ('You wake up with less than ideal amounts of sleep.')
        print ('You eat breakfast and leave for work in the company building. You put in your time card and enter the factory.')
        if t==("TV" or "tv"):
            v = input ('Your lack of sleep interrupts your productivity. Do you take shortcuts to produce more, or do you work at a slower rate but produce higher quality goods? Type Shortcut or Quality:')
            print (v)
            if v==("Shortcut" or "shortcut"):
                print ('As you work, one of your products further down the line explode injuring seven. Your manager tracks the failure down to you. You are put in jail for three days and are fined two weeks worth of pay.')
                print ('Once you are out of jail, one of the security bots tells you that God-Emperor Clippy wants to see you. This fills you will vast amounts of fear and dread.')                       
            if v==("Quality" or "quality"):
                print ('You produce less quantity than usual and your mananger berades you for it. You put in your time card to check out and then drudge back to your room, motivated to get more sleep tonight.')
                print ('You enter your room and head directly to bed.')
                if v==("Quality" or "quality"):
                    y = input ('As you wake up you look out the window and see a man lugging a small device. You decide to either report him or leave him to his own devices. Type Report or Leave:')
                    print (y)
                    if y==("Report" or "report"):
                        print ('You report the strange man and soon two security bots knock on your door. They tell you that God-Emperor Clippy and Emperor Bonzi Buddy want to see you.')
                        print ('The security bots escort you to the throne room. They stop and open the doors for you. You walk in and down the long hall to where the Emperors sat.')
                        print ('You bow down to God-Emperor Clippy first and then to Emperor Bonzi Buddy. You look up at them from your kneeling position.')
                        print ('They start to speak in unison,"We hereby decree in this year of 2057, the honour of Citizen of the First Magnitude; the status and privileges that honour is provide.')

                    if y==("Leave" or "leave"):
                        print ('You leave him alone. 20 minutes later you hear the alarms go off and a theft of intellectual property is reported.')
                        print ('In the ensuing days it is learned that Nostalgia Inc. would lose $10,000,000 from that single man taking that small device. This weighs heavy down upon your conscience as a loyal member to the company.')
                        print ('The next day when you are working, you are so depressed that you miss a crucial part to one of the units you made. That device doesn\'t impact your production line, but it does to the one after.')
                        print ('As the next production line was assembling a fuse, someone put it in the botched unit. this caused a chain reaction that exploded all the other ordinance in the building; thaat killed 23 people.')
                        if y==("Leave" or "leave"):
                            d = input ('After you finish your day at work you make you wat slowly to your room in shocked disbelief. You enter your room and go to a special drawer. There is a gun. You decided that you are either going to kill yourself or not. Type Suicide or Life:')
                            print (d)
                            if d==("Suicide" or "suicide"):
                                print ('As you reach into the drawer you know that there will be no other decision. As soon as you pull it out you shoot yourself.')

                            if d==("Life" or "life"):
                                print ('As you reach into the drawer and pull the gun out you think about shooting yourself, but you just never did.')
                                print ('Due to your vulnerability, an enemy spy from Sans Corp. exploits you for information. God-Emperor Clippy finds out and you are summarily executed.')
                                print ('GAME OVER')
if s==("N" or "n"):
    print ('As you resist, two security bots roll up and bludgeon you until you are unconscious.')
    print ('You wake up in the company jail surrounded by dozing drunks and winos.')
    print ('As soon as you wake up the security bots pull you out of your cell and administer a fine to your account. You are then let free.')
    print ('You walk slowly to your room and enter.')
    if s==("N" or "n"):
        u = input ('You decide either to take a bath and go to bed or watch TV. Type Bath or TV:')
        print (u)
        if u==("Bath" or "bath"):
            print ('Your wounds are healed and you wake up refreshed.')
            print ('You eat breakfast and leave for work in the comapny building. You put in your time card and enter the factory. Due to your abundance of sleep, you make no mistakes and your supervisors congratulate you.')
            print ('You return to your room feeling confident and happy.')
            if u==("Bath" or "bath"):
                z = input ('You decide either to go out to a bar or go to bed. Type Bar or Bed:')
                print (z)
                if z==("Bed" or "bed"):
                    print ('You wake up feeling refreshed.')
                    print ('You eat breakfast and go to the factory. While you punch your time card, a man is dragged away screaming by two security bots. This plants the first seeds of doubt of something.')
                    if z==("Bed" or "bed"):
                        c = input ('As he is dragged away you decide to either leave the situation be or ask your manager why he was taken away. Type Leave or Taken:')
                        print (c)
                        if c==("Taken" or "taken"):
                            print ('Your manager asks you if you want to be like the guy that was just taken away. When you respond with a firm no he says to not be nosy. This further creates doubt in the system for you.')

                        if c==("Leave" or "leave"):
                            print ('You wonder what that poor sod did.')
                if z==("Bar" or "bar"):
                    print ('You are drinking alone when a woman catches your eye.')
                    if z==("Bar" or "bar"):
                        b = input ('You decide either to go up to her or continue drinking. Type Meet or Drink:')
                        print (b)
                        if b==("Meet" or "meet"):
                            print ('You go up to her and introduce yourself. As it turns out, she has had her eye on you.')

                        if b==("Drink" or "drink"):
                            print ('You continue to nurse your drink until you just decide to go back to your room.')
                            print ('You walk back to your room.')
                            if b==("Drink" or "drink"):
                                e = input ('You decide to either go to bed or watch TV. Type Bed or TV:')
                                print (e)
                                if e==("Bed" or "bed"):
                                    print ('You wake up feeling refreshed.')
                                    
                                if e==("TV" or "tv"):
                                    print ('You wake up feeling poorly due to lack of sleep.')
                                    
        if u==("TV" or "tv"):
            print ('You ache all over and your eyes are dry due to lack of sleep.')
            print ('You eat breakfast and leave for work in the company building. You put in your time card and enter the factory.')
            if u==("TV" or "tv"):
                a = input ('Your lack of sleep interrupts your productivity. Do you take shortcuts to produce more, or do you work at a slower rate but produce higher quality goods? Type Shortcut or Quality:')
                print (a)
                if a==("Shortcut" or "shortcut"):
                    print ('As you work, one of your products further down the line explode injuring seven. Your manager tracks the failure down to you. You are put in jail for three days and are fined two weeks worth of pay.')
                    print ('Once you are out of jail, one of the security bots tells you that God-Emperor Clippy wants to see you. This fills you will vast amounts of fear and dread.')                       

                if a==("Quality" or "quality"):  
                    print ('You produce less quantity than usual and your mananger berades you for it. You put in your time card to check out and then drudge back to your room, motivated to get more sleep tonight.')
                    if a==("Quality" or "quality"):
                        f = input ('You decide to either to go to bed or watch TV.  Type Bed or TV:')
                        print (f)
                        if f==("Bed" or "bed"):
                            print ('You wake up well rested.')
                            
                        if f==("TV" or "tv"):
                            print ('You wake up poorly rested.')

