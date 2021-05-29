from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_ui_design import Ui_MainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView


import sys, threading

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.appSettings() # Contains all button functionality and window settings
        # self.setGeometry(670, 115, 325, 588)
        
        self.show()
        
        # while True:
        #     QApplication.processEvents()
        #     print('Geometry is :"',self.geometry())

        self.windowAnimation()


##_______________________________________________________________
## Defining all the settings in a function to make the code more neat and clean
    def appSettings(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.reverse_opacity = 1
        self.opacity = 0
        self.logoFrameopacity = 0
        
        ## Hiding the size grip for the Login Screen
        self.ui.SizeGrip_upper_right.hide()
        self.ui.SizeGrip_bottom_right.hide()
        # self.ui.stackedContentBase.hide()

        self.screenGeo = QApplication.desktop().screenGeometry()
        self.default_geometry = self.geometry() # Starting position of the window Note - no use for maxi button
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page1)
        
        self.ui.Home_search_button.clicked.connect(self.searcher)
        self.ui.hm_searchBox.returnPressed.connect(self.searcher)
        
        self.ui.Account_button.clicked.connect(lambda :self.ui.stackedWidget_2.setCurrentWidget(self.ui.GoogleMapsPage))
        self.ui.Home_button.clicked.connect(lambda : self.ui.stackedWidget_2.setCurrentWidget(self.ui.Home))
        self.ui.Contact_button.clicked.connect(self.email_search)
        
        self.searchProgress(0)
        

        self.ui.HomeBrowser.setUrl(QUrl('https://www.google.com'))

        # Making Home Page as default page
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.Home)
        
        self.ui.leftMenuFrame.resize(41,self.ui.stackedWidget_2.geometry().height())
        
        self.ui.CloseButton.clicked.connect(self.closer)
        self.ui.Minimizebtn.clicked.connect(self.mini_button)
        self.ui.Maximizebtn.clicked.connect(self.maxi_button)
        self.ui.LoginButton.clicked.connect(self.loginer)
        self.ui.searchMap_button.clicked.connect(self.Map_search)
        
        # self.ui.HomeBrowser.loadStarted.connect(self.searchStart)
        self.ui.HomeBrowser.loadProgress.connect(self.searchProgress)
        self.ui.HomeBrowser.loadFinished.connect(self.searchProgress)
        
        self.ui.mapWidget.loadProgress.connect(self.searchProgress)
        self.ui.mapWidget.loadFinished.connect(self.searchProgress)
        
        self.ui.HomeBrowser.loadStarted.connect(self.searchBox_tex_change)
        
        
        
        QSizeGrip(self.ui.SizeGrip_bottom_right) ## Defining size GRip for upper right corner
        QSizeGrip(self.ui.SizeGrip_upper_right) ## Defining size GRip for bottom right corner
        
        self.ui.Men_button.clicked.connect(self.leftMenuOpner)
        self.resize(303,565)
        
        
  
        
      
        def moveWindow(e):
            FRAME = QApplication.desktop().screenGeometry()
            if not (FRAME == self.geometry()):
                if e.buttons() == Qt.LeftButton:
                    if not (self.geometry() == self.screenGeo):
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
                    else:
                        self.setGeometry(self.default_geometry)

        self.ui.util_buttons.mouseMoveEvent = moveWindow
        self.ui.upper_drag.mouseMoveEvent = moveWindow
        self.ui.bottom_drag.mouseMoveEvent = moveWindow
      
    
##_________________________________________________________________________________________________________________________
## Defining Animation for different widgets
     
     ## Defining Browser functions and actions
    
    

    def email_search(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.Home)
        self.ui.HomeBrowser.setUrl(QUrl('https://gmail.com/'))
    
    
    
    def Map_search(self):
        Longitude = self.ui.Longitude.text().rstrip()
        Latitude = self.ui.Latitude.text().lstrip()
        
        condition_check = Longitude != '' and Latitude != ''
        if condition_check:
            # URL="https://www.google.com/maps/@"+
            # Latitude+","
            # +Longitude+",9z"
            #https://www.google.com/maps/place/23%C2%B010'24.4%22N+81%C2%B056'10.2%22E/@23.1734515,81.9339634
            Url = QUrl(f'https://www.google.com/maps/@{Latitude},{Longitude},17z')
            print("url is :",Url)
            browser = self.ui.mapWidget
            browser.load(Url)
    
    def searchBox_tex_change(self):
        goingUrl = self.ui.HomeBrowser.url().toString()
        if goingUrl == 'https://www.google.com' : goingUrl = ''
        
        self.ui.hm_searchBox.setText(goingUrl)
        # self.ui.hm_searchBox.
        
        
    def searchFinished(self,val):
        print("load Finished Val :",val)
        self.ui.search_progress.setValue(0) 
        
    def searchStart(self,val):
        print("load Syart Val :",val)
        self.ui.search_progress.setValue(0) 
    
    
    def searchProgress(self,value):
        if value == True :
            value = self.ui.search_progress.setValue(0)
        else:
            # loop = QEventLoop()
            # QTimer.singleShot(200,loop.quit)
            # loop.exec_()
            self.ui.search_progress.setValue(value)
        if self.ui.search_progress.value() == 100:
            self.ui.search_progress.setValue(0)
      
    
    def searcher(self):
        url = QUrl(self.ui.hm_searchBox.text().rstrip().lstrip())
        print("is it a valid url ? :",url.isValid())
        
        if not ("https://www." in url.toString() and ".com" in url.toString() and len(url.toString().split(" ")) == 1):
            if not ( ('https://' in url.toString() and len( url.toString().split(' ') )== 1)  and '.com' in url.toString() and len( url.toString().split(' ') )== 1 ) :
                
                to_search = "+".join( url.toString().split(" ") )
                # url = QUrl("https://www.google.com/search?q="+self.ui.hm_searchBox.text().rstrip().lstrip())
                url = QUrl(f"https://www.google.com/search?q={to_search}")
            
            else:
                if 'https://' in url.toString() and 'https://www.' not in url.toString() : url = QUrl( url.toString().replace('https://',"https://www.") )
                else:
                    url = QUrl(f"https://www.{url.toString()}")
        
        print("Url to be searched is :" ,url)
        browser = self.ui.HomeBrowser
        
        
        browser.setUrl(url)
        self.ui.hm_searchBox.setText(url.toString())
        
        # browser.loadStarted.connect(self.searchProgress)
        
        # browse.loadFinished.connect(lambda : self.searchProgress(0))
        
        
        
        
    
    def home(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.Home)
        browser = self.ui.HomeBrowser
        self.ui.hm_brow_reload_btn.clicked.connect(browser.reload)
        
        url = QUrl(self.ui.hm_searchBox.text().rstrip().lstrip())
        
        

        
        if browser.history().canGoBack :
            iconBack= self.ui.hm_brow_back_btn.icon()
            self.ui.hm_brow_back_btn.setIcon(iconBack)
            self.ui.hm_brow_back_btn.clicked.connect(browser.back)
        else:
            # self.ui.hm_brow_back_btn.setEnabled(False)
            self.ui.hm_brow_back_btn.setIcon(None)
            
            
        
        if browser.history().canGoForward:
            iconForward = self.ui.hm_brow_foward_btn.icon()
            self.ui.hm_brow_foward_btn.setIcon(iconForward)
            self.ui.hm_brow_foward_btn.clicked.connect(browser.forward)
        else:
            self.ui.hm_brow_foward_btn.setIcon(None)
                                                   
        # if browser.history().canGoForward :
        #     self.ui.hm_brow_forward_btn.setEnabled(True)
        #     self.ui.hm_brow_foward_btn.clicked.connect(browser.forward)
        # else:
        #     self.ui.hm_brow_forward_btn.setEnabled(False)
        
        
        
        
        
        
        
    
    
    
    def windowOpacityAnimation(self,element):
        self.setWindowOpacity(0)
        self.ui.stackedWidget.setCurrentWidget(element)
        while self.opacity!=1:
            QApplication.processEvents()
            loop = QEventLoop()
            QTimer.singleShot(250,loop.quit)
            loop.exec_()
            self.setWindowOpacity(self.opacity)
            self.opacity +=0.05
        
        
    
    def leftMenuOpner(self):
        print('Printer Menu Button is clicked...')
        
        
        
        buttons = [self.ui.Home_button,self.ui.Account_button,self.ui.Settings_button,self.ui.Contact_button]
        
        newButtonStyle = '''
        QPushButton{
	color: rgb(255, 255, 255);
	background-color: rgb(39, 0, 58);
    border-radius:7px;
	border-width:1px;
	border-style:Inset;
	background-image: url(:/newPrefix/user2.png);
	border-color: rgb(29, 29, 29);
	border-bottom-color: rgb(163, 0, 0);

}


QPushButton::hover{
	background-color: rgb(85, 85, 85);
	background-image: url(:/newPrefix/user2.png);
	border-width:2px;
	border-style:Inset;
	border-color: rgb(29, 29, 29);
	border-bottom-color: rgb(0, 255, 0);
}
        '''
        
        
        
 
        duration = 250
        startVal = 41
        endVal = 111
        expand = True
        
        print("LeftMenu Frame widht is :",self.ui.leftMenuFrame.width())
        if self.ui.leftMenuFrame.width() != 32:
            startVal = 140
            endVal = 32
            expand = False
        else : 
            startVal = 32
            endVal = 140
        print("Do I need to expand??: ",expand)
        
        
            
            
        
        
        self.winanim = QPropertyAnimation(self.ui.leftMenuFrame,b'maximumWidth')
        self.winanim.setStartValue(startVal)
        self.winanim.setEasingCurve(QEasingCurve.InQuad)
        self.winanim.setEndValue(endVal)
        self.winanim.setDuration(duration)
        self.winanim.start()
        
        loop = QEventLoop()
        QTimer.singleShot(1000,loop.quit)
        loop.exec_()
        
        
        
        # if expand :
        #     self.prevStyle = self.ui.Home_button.styleSheet()
        #     # _ = list(map(lambda x: x.setStyleSheet(newButtonStyle),buttons) )
        #     # _ = list(map(lambda x: self.change_button_color(x,"background-color: rgb(39, 0, 58);"), buttons ))
        # else:
        #     _ = list(map(lambda x: x.setStyleSheet(self.prevStyle),buttons) )
    
    
    def change_button_color(self,button, color):
        """change_button_color

            Change a button's color
        :param button: target button
        :type button: QPushButton
        :param color: new color (any format)
        :type color: str
        :return: None
        """
        style_sheet = button.styleSheet()
        pairs = [pair.replace(' ', '') for pair in style_sheet.split(';') if pair]

        style_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            style_dict[key] = value

        style_dict['background-color'] = color
        style_sheet = '{}'.format(style_dict)

        chars_to_remove = ('{', '}', '\'')
        for char in chars_to_remove:
            style_sheet = style_sheet.replace(char, '')
        style_sheet = style_sheet.replace(',', ';')

        button.setStyleSheet(style_sheet)
    
    
    
    def ViewChanger_windowAnimation_width(self,Property=b'geometry',act_object=None,change_page=False,change_page_object=None,startVal=None,
                                    tarWidth=900,duration=500,easingCurve = QEasingCurve.InQuad):
        if change_page:
            self.ui.stackedWidget.setCurrentWidget(change_page_object)
        self.home()
        
        endVal = QRect( self.geometry().x()- (tarWidth*(40/100)//1), self.geometry().y() , tarWidth, self.geometry().height()  )
        
        ## Checking Condition for left Menue Frame 
        if act_object == self.ui.leftMenuFrame:
            if self.ui.leftMenuFrame.width() == 111:
                endVal =  41
            else :
                endVal = 111
        
                 
        
        width = self.geometry().width()
        print( "width change condition is :",width != tarWidth)
        
        print("10% of the tarwidht is :",( tarWidth*(10//tarWidth) )//1)
        
        
        self.winanim = QPropertyAnimation(act_object,Property)
        self.winanim.setStartValue(startVal)
        self.winanim.setEasingCurve(easingCurve)
        self.winanim.setEndValue(endVal)
        self.winanim.setDuration(duration)
        self.winanim.start()
        
        self.ui.SizeGrip_bottom_right.show()
        self.ui.SizeGrip_upper_right.show()
        
    
    def windowAnimation(self):
        self.anim = QPropertyAnimation(self.ui.BaseFrame, b"geometry")
        self.anim.setDuration(500)

        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setStartValue(QRect(12, 12, 200, 100))
        self.anim.setEndValue(QRect(0,0,307,600))
        self.anim.start()
        
##___________________________________________________________________
##_______________________________________________________________
## MousePressEvent for making the dragabe frameless window
    def mousePressEvent(self, event) -> None:
        self.clickPosition = event.globalPos()
##_____________________________________________________________________________
## Defining Functionality for different Buttons
        
    def closer(self):
        self.close()
        quit()

    def mini_button(self):
        if self.isMinimized():
            self.setGeometry(self.default_geometry)
        else:
            self.showMinimized()

    def maxi_button(self):
        x = self.geometry()
        fullscreen = self.screenGeo == self.geometry()
        # print("is it in full screen ?:",fullscreen)
        # print("screen geometry is ",self.screenGeo)
        if fullscreen:
            self.setGeometry(self.value_before_maxi_x, self.value_before_maxi_y,
                             self.value_before_maxi_geo.width(), self.value_before_maxi_geo.height())
        elif not fullscreen:
            self.value_before_maxi_x = x.x()
            self.value_before_maxi_y = x.y()
            self.value_before_maxi_geo = self.geometry()
            self.setGeometry(self.screenGeo)

    def loginer(self):
        name = self.ui.Box_name.text()
        email = self.ui.Box_email.text().lstrip().rstrip()
        password = self.ui.Box_password.text()

        realpass = ' '
        # realpass = 'KaladharGopal'
        password_check = password == realpass
        print("Checking Password: ",password_check)
        email_check = False

        if name.lstrip().rstrip() == '':
            name_check = False
            self.error(self.ui.Box_name)


        elif email[-10:] == '@gmail.com' and (len(email.split(' ')) == 1) :
            email_check = True

        elif email[-10:] != '@gmail.com' or (len(email.split(' ')) != 1):
            self.error(self.ui.Box_email)
            email_check = False

        if email_check: 
            if password_check:
                self.ui.LoginButton.setText("Login ✔️")
                loop = QEventLoop()
                QTimer.singleShot(500,loop.quit)
                loop.exec_()
                
                newWinGeo = QRect(self.geometry().x(), self.geometry().y(),900,self.geometry().height() )
                print("NEw window geometry is :",newWinGeo)
                print("Current Geometry is :",self.geometry())
                self.ViewChanger_windowAnimation_width(change_page=True,change_page_object=self.ui.page_2,startVal=self.geometry(),
                                                       tarWidth=1000,act_object=self)
                
                
                         
            else :
                self.error(self.ui.Box_password)
        
        



##_______________________________________________________________
## Defining Error Handler
    def error(self,obj):
        self.ui.LoginButton.hide()
        placeholder = obj.text()
        self.anim = QPropertyAnimation(self.ui.BaseFrame, b"geometry")
        self.anim.setDuration(500)

        obj.setText('❌')
        obj.setEchoMode(QLineEdit.Normal)

        self.anim.setEasingCurve(QEasingCurve.InOutBounce)
        # self.anim.setStartValue(QRect(12, 12, 330, 580))
        self.resize(307,565)
        self.anim.setStartValue(QRect(0,0,307 , self.ui.BaseFrame.height()-100 ))
        self.anim.setEndValue(QRect(0,0,307 ,self.height() ))
        self.anim.start()

        obj.setStyleSheet('''

         QLineEdit{
        color: rgb(255, 255, 255);
        background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, 
        stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));
        border-radius:11px;
        margin-top:20px;
        text-align:left;}''')

        loop = QEventLoop()
        QTimer.singleShot(500,loop.quit)
        loop.exec_()
        
        obj.setStyleSheet('''

        QLineEdit{
        color: rgb(255, 255, 255);
        background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, 
        stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));
        border-radius:11px;
        margin-top:20px;
        text-align:left;}
        QLineEdit::hover{
         background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, 
        stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));
        color: rgb(241, 241, 241); } ''')
        obj.setText(placeholder)

        self.ui.LoginButton.show()
        if obj == self.ui.Box_password:
            print("Wrong Password is :",obj.text())
            obj.setEchoMode(QLineEdit.Password)
            obj.clear()




    


if __name__ == '__main__':
    app = QApplication()
    window = MainApp()
    sys.exit(app.exec_())
