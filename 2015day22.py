import random

def oneBattle(mode = 1):
    pHP = 50
    pMP = 500
    pArm = 0
    eHP = 58
    eDam = 9

    manaSpent = 0
    turnsUntilShield = 0
    turnsUntilPoison = 0
    turnsUntilRecharge = 0

    shieldOn = False
    poisonOn = False
    rechargeOn = False

    while pHP >0 and eHP >0:
        
    #PLAYER TURN
        if mode == 2:
            pHP -= 1
            if pHP <= 0:
                return(False)
        if poisonOn == True:
            eHP -= 3
            if eHP <= 0:
                return(manaSpent)
            turnsUntilPoison -= 1
            if turnsUntilPoison == 0:
                poisonOn = False
        if shieldOn == True:
            turnsUntilShield -= 1
            if turnsUntilShield == 0:
                shieldOn = False
        if rechargeOn == True:
            pMP += 101
            turnsUntilRecharge -= 1
            if turnsUntilRecharge == 0:
                rechargeOn = False

        if pMP < 53:
            return(False)    
        validAction = False
        while validAction == False:
            pAction = random.randint(0,4)
            if pAction ==0:
                if pMP >= 53:
                    pMP -= 53
                    eHP -=4
                    manaSpent += 53
                    validAction = True
                    
                    if eHP <=0:
                        return(manaSpent)
            elif pAction == 1:
                if pMP >= 73:
                    pMP -= 73
                    pHP += 2
                    eHP -= 2
                    manaSpent += 73
                    
                    validAction = True
                    if eHP <=0:
                        return(manaSpent)
            elif pAction == 2:
                if pMP >=113 and turnsUntilShield == 0:
                    pMP -= 113
                    shieldOn = True
                    turnsUntilShield = 6
                    manaSpent += 113
                    validAction = True
                    
            elif pAction == 3:
                if pMP >= 173 and turnsUntilPoison ==0:
                    pMP -= 173
                    poisonOn = True
                    turnsUntilPoison = 6
                    manaSpent +=173
                    validAction = True
                    
            elif pAction == 4:
                if pMP>= 229 and turnsUntilRecharge == 0:
                    pMP -= 229
                    rechargeOn = True
                    turnsUntilRecharge = 5
                    manaSpent += 229
                    validAction = True
                    
                    
        #ENEMY TURN
        
        if poisonOn == True:
            eHP -= 3
            if eHP <= 0:
                return(manaSpent)
            turnsUntilPoison -= 1
            if turnsUntilPoison == 0:
                poisonOn = False
        if shieldOn == True:
            turnsUntilShield -= 1
            pArm = 7
            if turnsUntilShield == 0:
                shieldOn = False

        if rechargeOn == True:
            pMP += 101
            turnsUntilRecharge -= 1
            if turnsUntilRecharge == 0:
                rechargeOn = False

        damDealt = eDam - pArm
        if damDealt <1: 
            damDealt = 1
        pHP-=damDealt
        if pHP <=0:
            return(False)
        pArm = 0



lowest = 9999
for x in range(1000000):
    result = oneBattle(2) #the two means part 2
    if result != False:
        if result < lowest:
            lowest = result
            print(lowest)

