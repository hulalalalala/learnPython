# 定义一个 Animal 类
class Animal:
    def __init__(self, typeStr = "小狗", color = "红色", speak = "汪汪汪"): # 构造函数
        self.typeStr = typeStr
        self.color = color
        self.speak = speak

    # 获取这只动物的种类
    def getType (self):
        str = '这只动物的种类是:' + self.typeStr
        return str

    # 获取该动物的叫声
    def getSpeak (self):
        str = self.typeStr + '发出的声音是:' + self.speak
        return str

    # 获取该动物的颜色
    def getColor (self):
        str = self.typeStr + '的颜色是:' + self.color
        return str

    # 销毁此类 del ClassName
    def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "销毁")
      