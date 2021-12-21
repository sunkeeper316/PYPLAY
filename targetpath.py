
class TargetProcess :
    def __init__(self ,start_target , poslist , end_target) :
        self.start_target = start_target
        self.poslist = poslist
        self.end_target = end_target
    
    @staticmethod
    def a5_redDoor():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = [(-475 , 340),(0 , 225),(-500 , 330),(0 , 210) , (0 , 50),(-500 , -90)]
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)

class TargetPath :
    def __init__(self , target , postion , checkpostion = "" ,direction = "") :
        self.target = target
        self.direction = direction
        self.postion = postion
        self.checkpostion = checkpostion

    @staticmethod
    def a5_redDoorPaths():
        t1 = TargetPath("assets/templates/a5_town/a5_town_4.png",postion = (-475 , 340))
        t2 = TargetPath("assets/templates/a5_town/a5_town_12.png",postion = (0 , 225))
        t3 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (-500 , 330))
        t4 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (0 , 210))
        t5 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (0 , 50))
        t6 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (-500 , -90))

        return [t1 , t2 , t3 , t4 , t5 , t6]

    @staticmethod
    def a5_malah():
        t1 = TargetPath("assets/templates/a5_town/a5_town_4.png",postion = (-580 , -160))
        t2 = TargetPath("assets/templates/a5_town/a5_town_12.png",postion = (260 , -200))
        t3 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (-260 , 200))
        t4 = TargetPath("assets/templates/a5_town/a5_town_7.png",postion = (580 , 160))
        return [t1 , t2 , t3 , t4 ]

class TargetPos :
#找尋目標而且確認目標應該距離當前位子座標
    def __init__(self , target , postion) :
        self.target = target
        self.postion = postion

    @staticmethod

    def a5_town_0() :
        return TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))

    
        
    