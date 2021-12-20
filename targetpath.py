

class TargetPath :
    def __init__(self , target , postion , checkpostion ,direction = "") :
        self.target = target
        self.direction = direction
        self.postion = postion
        self.checkpostion = checkpostion

    @staticmethod
    def a5_redDoorPaths():
        t1 = TargetPath("assets/templates/a5_town/a5_town_4.png","goLeftDown")
        t2 = TargetPath("assets/templates/a5_town/a5_town_12.png","goLeftDown")
        t3 = TargetPath("assets/templates/a5_town/a5_town_7.png","goLeft")

        return [t1 , t2 , t3]