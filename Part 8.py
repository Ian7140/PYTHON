# Class
# Marine : Solider , Gun usage available
# name = "Marine"
# hp = 40
# damage = 5

# print("{} unit created.".format(name))
# print("HP : {} / DAMAGE = {}".format(hp,damage))

# Tank : Attack , Tank , Normal/Seize
# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("{} unit created.".format(tank_name))
# print("HP : {} / DAMAGE = {}".format(tank_hp,tank_damage))

# tank2_name = "Tank"
# tank2_hp = 150
# tank2_damage = 35

# def attack(name, location, damage):
#     print("{} : {} Attacking [ATTACK : {}]".format(\
#         name, location, damage) )

# attack(name , "1 o'clock", damage)
# attack(tank_name,"1 o'clock",tank_damage)
# attack(tank2_name,"1 o'clock",tank2_damage)

class Unit :
    def __init__(self,name,hp):
        self.name = name #멤버변수 : 클래스안에서 생성된 변수
        self.hp = hp
        
# # Wraith : Cloaked Aerospace Strike Fighter
# wraith1 = Unit("Wraith" , 80,5)
# print("NAME : {} / DAMAGE : {}".format(wraith1.name,wraith1.damage))


# #Mind Control : 상대방 유닛 빼앗기
# wraith2 = Unit("Taken Wraith" ,80,5)
# wraith2.clocking = True 
# #외부에서 멤버변수를 만들어서 사용가능 (wraith2에는 있지만 wraith1에는 없음)
# if wraith2.clocking == True : 
#     print("{} is Clocking".format(wraith2.name))

# # Method

class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp) #상속
        self.damage = damage

    def attack(self, location):
        print("{} : {} is attacking [ATTACK : {}]"\
              .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{} : -{} hp.".format(self.name, damage))
        self.hp -= damage
        print("{} : Current HP is {}.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{} unit is deleted.".format(self.name))

#Firebat : Attack, Fire attack
firebat1 = AttackUnit("Firebat",50,16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)






