
class TargetProcess :
    def __init__(self ,start_target , poslist , end_target , search = None) :
        self.start_target = start_target
        self.poslist = poslist
        self.end_target = end_target
        self.search = search
    
    @staticmethod
    def a5_start_to_redDoor():
        start_target = TargetPos("assets/templates/a5_town/a5_town_1.png" , (51,135))
        poslist = [(-475 , 340),(0 , 225),(-500 , 330),(0 , 210) , (0 , 120),(-500 , -90)]
        end_target = TargetPos("assets/templates/a5_town/a5_town_7.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target , "assets/templates/a5_red_portal_text.png")
    @staticmethod
    def a5_start_to_malah():
        start_target = TargetPos("assets/templates/a5_town/a5_town_1.png" , (51,135))
        poslist = [(-580,-150),(250,-200)]
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (291,88))
        return TargetProcess(start_target , poslist , end_target , "assets/npc/malah/malah_name_tag_white.png")
    @staticmethod
    def a5_malah_to_start():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (291,88))
        poslist = [(-250,200),(580,150)]
        end_target = TargetPos("assets/templates/a5_town/a5_town_1.png" , (51,135))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_start_to_store():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_store_to_redDoor():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_store_to_fix():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_fix_to_store():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_malah_to_qual_kehk():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
        end_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        return TargetProcess(start_target , poslist , end_target)
    @staticmethod
    def a5_qual_kehk_to_store():
        start_target = TargetPos("assets/templates/a5_town/a5_town_0.png" , (0,0))
        poslist = []
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

    
        
    