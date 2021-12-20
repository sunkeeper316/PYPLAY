

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