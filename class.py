class BSSM:
    def __init__(self, task, age , name):
        self.team = "부소마" #BSSM 클래스로 찍어낸 객체들은 모두 team 변수에 '부소마'가 들어가도록 만듦
        self.task = task
        self.age = age
        self.name = name
    
    def intro(self):
        print("안녕하세요, %s에서 %s를 담당하고 있는 %d살 %s입니다." %(self.team, self.task, \
                                                    self.age, self.name))
        

Ian = BSSM('AI', 17, 'Ian')
Ian.intro()

