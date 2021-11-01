class Computer:

    screen = True

    def start(self):
        print('电脑正在开机中……')


my_computer = Computer()#Computer my_computer
print(my_computer.screen)
my_computer.start()
print(type(my_computer))
print(my_computer)#打印出这个对象的地址

#------------------------
class Chinese:
    # 用赋值语句，创建类的属性
    eye = 'black'

    # 创建实例方法时，不要漏了 self
    def eat(self):
        print('吃饭，选择用筷子。')

#-----------------------------
class Chinese:      # 创建一个类
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

wufeng = Chinese()   # 类的实例化
print(wufeng.eye)   # 实例调用类属性
wufeng.eat()  # 调用类中的方法（传参不用管self）
#----------------------------------------
#特殊参数：self
#正式揭秘特殊参数self的作用：self会接收实例化过程中传入的数据，当实例对象创建后，实例便会代替 self，在代码中运行。
#换言之，self 是所有实例的替身，“替身”是什么意思呢？我们来看一个例子。
#刚刚我们列举的类方法都只有一个self参数，实际上和一般函数一样，类的方法也可以设置多个参数：（直接运行即可 ）

class Chinese:

    name = '吴枫'  # 类属性name

    def say(self):     
        print(self.name + '是中国人')

person = Chinese()   # 创建Chinese的实例person
person.say()         # 调用实例方法

#-------------------------------------
class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):
        self.greeting() 
        print('我来自中国')

person = Chinese()
# 创建实例person
person.say()
# 调用say()方法

#----------------------------------------
#特殊方法：初始化方法
#定义初始化方法的格式是def __init__(self)，是由init加左右两边的【双】下划线组成（ initialize “初始化”的缩写）。
#初始化方法的作用在于：当每个实例对象创建时，该方法内的代码无须调用就会自动运行。
# 阅读代码后直接运行    
class Chinese:

    def __init__(self): 
        print('很高兴遇见你，我是初始化方法')

person = Chinese()

#-----------------------------------------
#除了设置固定常量，初始化方法同样可以接收其他参数，让传入的这些数据能作为属性在类的方法之间流转。我们再来看个例子：

class Chinese:

    def __init__(self, name, birth, region):
        self.name = name   # self.name = '吴枫' 
        self.birth = birth  # self.birth = '广东'
        self.region = region  # self.region = '深圳'

    def born(self):
        print(self.name + '出生在' + self.birth)

    def live(self):
        print(self.name + '居住在' + self.region)    

person = Chinese('吴枫','广东','深圳') # 传入初始化方法的参数
person.born()
person.live()


#--------------------------------------------
#用类写计算器
import math

class Project:
    
    def __init__(self):
        self.key = 1

    def input(self):
        choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
        if choice == '1':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = int(input('请输入人力数量：（请输入整数）'))
            self.time = None
        if choice == '2':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = None
            self.time = float(input('请输入工时数量：（请输入小数）'))

    def estimated(self):
        # 人力计算
        if (self.number == None) and (self.time != None):
            self.number = math.ceil(self.size * 80 / self.time)
            print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(self.size,self.time,self.number)) 
        # 工时计算
        elif (self.number != None) and (self.time == None):
            self.time = self.size * 80 / self.number
            print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(self.size,self.number,self.time))  
    
    def again(self):
        a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
        if a != 'y':
            # 如果用户不输入'y'，则把key赋值为0
            self.key = 0  

    # 主函数
    def main(self):
        print('欢迎使用工作量计算小程序！')
        while self.key == 1:
            self.input()
            self.estimated()
            self.again()
        print('感谢使用工作量计算小程序！')
        
# 创建实例
project1 = Project()
project1.main()
#------------------------------------
