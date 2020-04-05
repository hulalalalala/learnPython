from package_class.Animal import Animal
class Cat(Animal): # 定义Cat类继承 Animal类
    def __init__(self, name = '小叮当'):
        self.name = name
        self.typeStr = '猫咪'

    def getName (self):
        return self.getType() + '名叫' + self.name