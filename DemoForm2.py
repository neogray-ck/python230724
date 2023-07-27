# DemoForm2.py
# DemoForm2.ui(화면) + DemoForm2.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹서버와 통신
import requests
# 크롤링
from bs4 import BeautifulSoup

# 디자인된 문서 로딩(시그널 & 슬롯 포함)
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    # 초기화 Method
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
    
    # 슬롯 Method
    def firstClick(self):
        url = "https://www.daangn.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})

        # 파일에 저장
        f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8")

        for post in posts:
            title = post.find("h2" , attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            addr  = post.find("div", attrs={"class":"card-region-name"})
            title = title.text.replace("\n", "").strip()
            price = price.text.replace("\n", "")
            addr  = addr.text.replace("\n", "")
            print("{0:<30}, {1}, {2}".format(title, price, addr))
            f.write(f"{title}, {price}, {addr}\n")

        f.close()
        self.label.setText("당근마켓 크롤링 완료")
        print(self.pushButton.text())
    def secondClick(self):
        sender_button = self.sender() # 시그널을 보낸 Object의 handle 취득
        self.label.setText("버튼 클릭 : " + sender_button.text())
        sender_button.setText(sender_button.text() + "(Clicked)")
        # self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        sender_button = self.sender()
        self.label.setText("버튼 클릭 : " + sender_button.text())
        sender_button.setText(sender_button.text() + "(Clicked)")
        # self.label.setText("세번째 버튼 클릭")

        

# 직접 모듈을 실행했는지 체크(진입점)
# __name__은 미리 정의된 변수인데, 본 프로그램이 사용자에 의해 단독으로 실행되면
# __name__은 자동으로 __main__으로 세팅된다. 이를 확인해서 직접 실행 여부를 판단
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()