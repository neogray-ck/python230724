str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #print(str)
        print(self.str)

g = GString()
g.set("First Message")
g.print()

print(g.str)