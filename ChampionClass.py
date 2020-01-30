# script to grab champ info from text file and read it into a class

# class object for a champion
class champion:
    def __init__ (self, championData_n):
        if (championData_n == None):
            self.name = ""
            self.level = 1.
            self.health = 0.
            self.healthRegen = 0.
            self.armor = 0.
            self.magicResist = 0.
            self.attackSpeed = 0.
            self.attackSpeedRatio = 0.
            self.mana = 0.
            self.manaRegen = 0.
            self.attackDamage = 0.
            self.critDamage = 0.
            self.attackRange = 0.

        else:
            self.name =	championData_n[0]
            self.level = 1
            self.health = float(championData_n[3])
            self.healthRegen = float(championData_n[4])
            self.armor = float(championData_n[5])
            self.magicResist = float(championData_n[6])
            self.attackSpeed = float(championData_n[7])
            self.attackSpeedRatio = float(championData_n[8])
            self.mana = float(championData_n[9])
            self.manaRegen = float(championData_n[10])
            self.attackDamage = float(championData_n[11])
            self.critDamage = float(championData_n[12])
            self.attackRange = float(championData_n[13])
            
