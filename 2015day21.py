def battle(pHp, pDam, pArm, eHp, eDam, eArm):
    playerHP = pHp
    enemyHP = eHp
    pDamDealt = pDam - eArm
    if pDamDealt <= 1:
        pDamDealt = 1
    eDamDealt = eDam - pArm
    if eDamDealt <= 1:
        eDamDealt = 1
    while playerHP > 0 and enemyHP >0:
        enemyHP -= pDamDealt
        if enemyHP <= 0:
            return(True)
        playerHP -= eDamDealt
        if playerHP <=0:
            return(False)

weaponDict = {'Dagger':[8,4,0], 'Shortsword':[10,5,0], 'Warhammer':[25,6,0], 'Longsword':[40,7,0], 'Greataxe':[74,8,0]}
armorDict = {'None':[0,0,0], 'Leather':[13,0,1], 'Chainmail':[31,0,2], 'Splintmail':[53,0,3], 'Bandedmail':[75,0,4], 'Platemail':[102,0,5]}
ringDict = {'None1':[0,0,0], 'None2':[0,0,0], 'Dam1':[25,1,0], 'Dam2':[50,2,0], 'Dam3':[100,3,0], 'Def1':[20,0,1], 'Def2':[40,0,2], 'Def3':[80,0,3]}

eHp = 109
eDam = 8
eArm = 2
pHp = 100
pDam = 0
pArm = 0

def lowestWinCost(weaponDict, armorDict, ringDict, eHp, eDam, eArm, pHp, pDam, pArm):
    lowestWinCost = 99999999999
    for weapon in weaponDict:
        for armor in armorDict:
            for ring1 in ringDict:
                for ring2 in ringDict:
                    if ring1 != ring2:
                        if battle(pHp, pDam+weaponDict[weapon][1]+ringDict[ring1][1]+ringDict[ring2][1], pArm+armorDict[armor][2]+ringDict[ring1][2]+ringDict[ring2][2], eHp, eDam, eArm) == True:
                            cost = weaponDict[weapon][0]+armorDict[armor][0]+ringDict[ring1][0]+ringDict[ring2][0]
                            if cost < lowestWinCost:
                                lowestWinCost = cost
    return(lowestWinCost)

def highestLossCost(weaponDict, armorDict, ringDict, eHp, eDam, eArm, pHp, pDam, pArm):
    highestLossCost = 0
    for weapon in weaponDict:
        for armor in armorDict:
            for ring1 in ringDict:
                for ring2 in ringDict:
                    if ring1 != ring2:
                        if battle(pHp, pDam+weaponDict[weapon][1]+ringDict[ring1][1]+ringDict[ring2][1], pArm+armorDict[armor][2]+ringDict[ring1][2]+ringDict[ring2][2], eHp, eDam, eArm) == False:
                            cost = weaponDict[weapon][0]+armorDict[armor][0]+ringDict[ring1][0]+ringDict[ring2][0]
                            if cost > highestLossCost:
                                highestLossCost = cost
    return(highestLossCost)


print("Part 1:", lowestWinCost(weaponDict, armorDict, ringDict, eHp, eDam, eArm, pHp, pDam, pArm))
print("Part 2:", highestLossCost(weaponDict, armorDict, ringDict, eHp, eDam, eArm, pHp, pDam, pArm))