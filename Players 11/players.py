
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox, QInputDialog, QComboBox
from utilities import *
from validations import *
from instructions import Ui_Dialog
from evaluation import Ui_Dialog_2
from scores import Ui_Dialog_3
from num2words import num2words

class Ui_MainWindow(QtWidgets.QWidget):        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 39, 741, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batsmen_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsmen_label.setObjectName("batsmen_label")
        self.horizontalLayout.addWidget(self.batsmen_label)
        self.batsmen_num = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsmen_num.setObjectName("batsmen_num")
        self.horizontalLayout.addWidget(self.batsmen_num)
        self.bowlers_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bowlers_label.setObjectName("bowlers_label")
        self.horizontalLayout.addWidget(self.bowlers_label)
        self.bowlers_num = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bowlers_num.setObjectName("bowlers_num")
        self.horizontalLayout.addWidget(self.bowlers_num)
        self.allrounders_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.allrounders_label.setObjectName("allrounders_label")
        self.horizontalLayout.addWidget(self.allrounders_label)
        self.allrounders_num = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.allrounders_num.setObjectName("allrounders_num")
        self.horizontalLayout.addWidget(self.allrounders_num)
        self.wicketkeepers_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicketkeepers_label.setObjectName("wicketkeepers_label")
        self.horizontalLayout.addWidget(self.wicketkeepers_label)
        self.wicketkeepers_num = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicketkeepers_num.setObjectName("wicketkeepers_num")
        self.horizontalLayout.addWidget(self.wicketkeepers_num)
        self.selections_label = QtWidgets.QLabel(self.centralwidget)
        self.selections_label.setGeometry(QtCore.QRect(30, 19, 91, 21))
        self.selections_label.setObjectName("selections_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.batsmen_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.batsmen_button.setObjectName("batsmen_button")
        self.horizontalLayout_2.addWidget(self.batsmen_button)
        self.batsmen_button.clicked.connect(self.display_batsmen)
        self.batsmen_button.setEnabled(False)
        self.bowlers_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.bowlers_button.setObjectName("bowlers_button")
        self.horizontalLayout_2.addWidget(self.bowlers_button)
        self.bowlers_button.clicked.connect(self.display_bowlers)
        self.bowlers_button.setEnabled(False)
        self.allrounders_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.allrounders_button.setObjectName("allrounders_button")
        self.horizontalLayout_2.addWidget(self.allrounders_button)
        self.allrounders_button.clicked.connect(self.display_allrounders)
        self.allrounders_button.setEnabled(False)
        self.wicketkeepers_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.wicketkeepers_button.setObjectName("wicketkeepers_button")
        self.horizontalLayout_2.addWidget(self.wicketkeepers_button)
        self.wicketkeepers_button.clicked.connect(self.display_wicketkeepers)
        self.wicketkeepers_button.setEnabled(False)
        self.points_available_label = QtWidgets.QLabel(self.centralwidget)
        self.points_available_label.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.points_available_label.setObjectName("points_available_label")
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(146, 100, 41, 16))
        self.points_available.setObjectName("points_available")
        self.points_used_label = QtWidgets.QLabel(self.centralwidget)
        self.points_used_label.setGeometry(QtCore.QRect(410, 99, 71, 20))
        self.points_used_label.setObjectName("points_used_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 169, 361, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.team_1_Label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.team_1_Label.setObjectName("team_1_Label")
        self.verticalLayout.addWidget(self.team_1_Label)
        list_font = QtGui.QFont("Roboto Mono")
        self.team_1_listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.team_1_listWidget.setObjectName("team_1_listWidget")
        self.team_1_listWidget.setFont(list_font)
        self.team_1_listWidget.itemDoubleClicked.connect(self.remove_players)
        self.verticalLayout.addWidget(self.team_1_listWidget)
        self.team_2_Label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.team_2_Label.setObjectName("team_2_Label")
        self.verticalLayout.addWidget(self.team_2_Label)
        self.team_2_listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.team_2_listWidget.setObjectName("team_2_listWidget")
        self.team_2_listWidget.setFont(list_font)
        self.team_2_listWidget.itemDoubleClicked.connect(self.remove_players)
        self.verticalLayout.addWidget(self.team_2_listWidget)
        self.team_name_label = QtWidgets.QLabel(self.centralwidget)
        self.team_name_label.setGeometry(QtCore.QRect(500, 136, 101, 20))
        self.team_name_label.setObjectName("team_name_label")
        self.my_team_name = QtWidgets.QLabel(self.centralwidget)
        self.my_team_name.setGeometry(QtCore.QRect(610, 136, 161, 20))
        self.my_team_name.setObjectName("my_team_name")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(409, 169, 361, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.my_team_listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2) 
        self.my_team_listWidget.setObjectName("my_team_listWidget")
        self.my_team_listWidget.setFont(list_font)
        self.my_team_listWidget.itemDoubleClicked.connect(self.remove_players_chosen)
        self.verticalLayout_2.addWidget(self.my_team_listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.team_1_numLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.team_1_numLabel.setObjectName("team_1_numLabel")
        self.horizontalLayout_3.addWidget(self.team_1_numLabel)
        self.team_1_playersNum = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.team_1_playersNum.setObjectName("team_1_playersNum")
        self.horizontalLayout_3.addWidget(self.team_1_playersNum)
        self.team_2_numLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.team_2_numLabel.setObjectName("team_2_numLabel")
        self.horizontalLayout_3.addWidget(self.team_2_numLabel)
        self.team_2_playersNum = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.team_2_playersNum.setObjectName("team_2_playersNum")
        self.horizontalLayout_3.addWidget(self.team_2_playersNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(769, 10, 16, 81))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(17, -5, 761, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(9, 10, 16, 81))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(17, 75, 761, 31))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 120, 16, 431))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.line_5.setFont(font)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(767, 120, 20, 431))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(17, 110, 761, 20))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(17, 540, 761, 20))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(390, 120, 20, 431))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(17, 150, 761, 20))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.match_chosen_label = QtWidgets.QLabel(self.centralwidget)
        self.match_chosen_label.setGeometry(QtCore.QRect(420, 19, 91, 21))
        self.match_chosen_label.setObjectName("match_chosen_label")
        self.match_chosen = QtWidgets.QLabel(self.centralwidget)
        self.match_chosen.setGeometry(QtCore.QRect(510, 19, 131, 20))
        self.match_chosen.setObjectName("match_chosen")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(496, 99, 61, 21))
        self.points_used.setObjectName("points_used")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionVIEW_Scores = QtWidgets.QAction(MainWindow)
        self.actionVIEW_Scores.setObjectName("actionVIEW_Scores")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addAction(self.actionVIEW_Scores)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu_choices)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.batsmen_label.setText(_translate("MainWindow", "Batsmen(BAT) :"))
        self.batsmen_num.setText(_translate("MainWindow", "##"))
        self.bowlers_label.setText(_translate("MainWindow", "Bowlers(BWL) :"))
        self.bowlers_num.setText(_translate("MainWindow", "##"))
        self.allrounders_label.setText(_translate("MainWindow", "All-Rounders(AR) :"))
        self.allrounders_num.setText(_translate("MainWindow", "##"))
        self.wicketkeepers_label.setText(_translate("MainWindow", "Wicket-keeper(WK) :"))
        self.wicketkeepers_num.setText(_translate("MainWindow", "##"))
        self.selections_label.setText(_translate("MainWindow", "Your Selections"))
        self.batsmen_button.setText(_translate("MainWindow", "BAT"))
        self.bowlers_button.setText(_translate("MainWindow", "BWL"))
        self.allrounders_button.setText(_translate("MainWindow", "AR"))
        self.wicketkeepers_button.setText(_translate("MainWindow", "WK"))
        self.points_available_label.setText(_translate("MainWindow", "Points Available :"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.points_used_label.setText(_translate("MainWindow", "Points Used :"))
        self.team_1_Label.setText(_translate("MainWindow", "#Team 1#"))
        self.team_2_Label.setText(_translate("MainWindow", "#Team 2#"))
        self.team_name_label.setText(_translate("MainWindow", "Your Team Name"))
        self.my_team_name.setText(_translate("MainWindow", "#########"))
        self.team_1_numLabel.setText(_translate("MainWindow", "#Team 1#"))
        self.team_1_playersNum.setText(_translate("MainWindow", "##"))
        self.team_2_numLabel.setText(_translate("MainWindow", "#Team 2#"))
        self.team_2_playersNum.setText(_translate("MainWindow", "##"))
        self.match_chosen_label.setText(_translate("MainWindow", "Match chosen : "))
        self.match_chosen.setText(_translate("MainWindow", " ##########################"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionVIEW_Scores.setText(_translate("MainWindow", "VIEW Scores"))

    def display_batsmen(self):
        self.display_helper('BAT')

    def display_bowlers(self):
        self.display_helper('BWL')

    def display_allrounders(self):
        self.display_helper('AR')

    def display_wicketkeepers(self):
        self.display_helper('WK')
    
    def display_helper(self, role):
        team_1, team_2 = self.team_1_numLabel.text(), self.team_2_numLabel.text()
        list_player_ids_1, list_player_ids_2 = [item[0] for item in get_list_players(team_1, role)], [item[0] for item in get_list_players(team_2, role)]
        self.team_1_listWidget.clear()
        self.team_2_listWidget.clear()
        self.generic_display_function(list_player_ids_1, self.my_team_listWidget.count(), team_1, self.team_1_listWidget)
        self.generic_display_function(list_player_ids_2, self.my_team_listWidget.count(), team_2, self.team_2_listWidget)

    def generic_display_function(self, player_ids, chosen_players_count, team_code, list_widget):
        list_widget.setSortingEnabled(False)
        for player_id in player_ids:
            flag = 0
            for j in range(chosen_players_count):
                if self.my_team_listWidget.item(j).data(QtCore.Qt.UserRole) == int(player_id):
                    flag = 1
                    break
            if flag == 1:
                continue
            player_details = get_player_details(player_id)
            player_text = self.build_player_text_left(player_details)
            item = QListWidgetItem()
            item.setText(player_text)
            item.setData(QtCore.Qt.UserRole, player_id)
            list_widget.addItem(item)
        list_widget.sortItems()

    def display_players(self):
        if self.batsmen_button.isChecked():
            self.display_helper('BAT')
        elif self.bowlers_button.isChecked():
            self.display_helper('BWL')
        elif self.allrounders_button.isChecked():
            self.display_helper('AR')
        elif self.wicketkeepers_button.isChecked():
            self.display_helper('WK')

    def enable_disable_buttons(self, value):
        self.batsmen_button.setEnabled(value)
        self.bowlers_button.setEnabled(value)
        self.allrounders_button.setEnabled(value)
        self.wicketkeepers_button.setEnabled(value)

    def uncheck_buttons(self):
        self.batsmen_button.setChecked(False)
        self.bowlers_button.setChecked(False)
        self.allrounders_button.setChecked(False)
        self.wicketkeepers_button.setChecked(False)

    def button_checked_status(self):
        return [self.batsmen_button.isChecked(), self.bowlers_button.isChecked(), self.allrounders_button.isChecked(), self.wicketkeepers_button.isChecked()]

    def set_fields(self, match, team_name, num_batsmen, num_bowlers, num_allrounders, num_wicketkeepers, available_points, used_points, team_1_fullname, team_2_fullname, team_1_code, playersNum_team_1, team_2_code, playersNum_team_2):
        self.match_chosen.setText(match)
        self.my_team_name.setText(team_name)
        self.batsmen_num.setText(num_batsmen)
        self.bowlers_num.setText(num_bowlers)
        self.allrounders_num.setText(num_allrounders)
        self.wicketkeepers_num.setText(num_wicketkeepers)
        self.points_available.setText(available_points)
        self.points_used.setText(used_points)
        self.team_1_Label.setText(team_1_fullname)
        self.team_2_Label.setText(team_2_fullname)
        self.team_1_numLabel.setText(team_1_code)
        self.team_1_playersNum.setText(playersNum_team_1)
        self.team_2_numLabel.setText(team_2_code)
        self.team_2_playersNum.setText(playersNum_team_2)

    def build_player_text_right(self, player_details):
        player_name, player_team_code, player_role, player_value = player_details
        num_spaces = 41 - (len(player_name) + len(player_team_code))
        player_text = player_name + "(" + player_team_code + ")" + ' '*num_spaces
        player_text += player_role if len(player_role) == 3 else player_role + ' '
        player_text += ' ' + str(player_value) if len(str(player_value)) == 3 else '  ' +  str(player_value)
        return player_text

    def build_player_text_left(self, player_details):
        player_name, player_value = str(player_details[0]), str(player_details[3])
        num_spaces = 50 - (len(player_name) + len(player_value))
        player_text = player_name + ' '*num_spaces + player_value
        return player_text
        
    def remove_players(self, item):
        list_widget_name = item.listWidget().objectName()
        player_value = int(item.text().split(" ")[-1])
        btn_1, btn_2, btn_3, btn_4 = self.button_checked_status()
        available_points = int(self.points_available.text()) - player_value
        selection_condition_batsmen_num = int(self.batsmen_num.text()) < 4
        selection_condition_bowlers_num = int(self.bowlers_num.text()) < 3
        selection_condition_allrounders_num = int(self.allrounders_num.text()) < 3
        selection_condition_wicketkeepers_num = int(self.wicketkeepers_num.text()) < 1
        selection_condition_available_points = available_points >= 0
        selection_condition_team_1_limit = int(self.team_1_playersNum.text()) <= 6
        selection_condition_team_2_limit = int(self.team_2_playersNum.text()) <= 6
        selection_condition_team_limit = selection_condition_team_1_limit if list_widget_name == 'team_1_listWidget' else selection_condition_team_2_limit

        if btn_1:
            if selection_condition_batsmen_num and selection_condition_available_points and selection_condition_team_limit:#atmost four batsmen are allowed
                self.batsmen_num.setText(str(int(self.batsmen_num.text()) + 1))
                self.select_player(item, available_points)
            else:
                self.selection_error("Warning", selection_condition_available_points, ["selection_condition_batsmen", selection_condition_batsmen_num, "four"], selection_condition_team_limit)
                    
        elif btn_2:
            if selection_condition_bowlers_num and selection_condition_available_points and selection_condition_team_limit:#atmost three bowlers are allowed
                self.bowlers_num.setText(str(int(self.bowlers_num.text()) + 1))
                self.select_player(item, available_points)
            else:
                self.selection_error("Warning", selection_condition_available_points, ["selection_condition_bowlers", selection_condition_bowlers_num, "three"], selection_condition_team_limit)
                    
        elif btn_3:
            if selection_condition_allrounders_num and selection_condition_available_points and selection_condition_team_limit:#atmost three allrounders are allowed
                self.allrounders_num.setText(str(int(self.allrounders_num.text()) + 1))
                self.select_player(item, available_points)
            else:
                self.selection_error("Warning", selection_condition_available_points, ["selection_condition_allrounders", selection_condition_allrounders_num, "three"], selection_condition_team_limit)
                    
        else:
            if selection_condition_wicketkeepers_num and selection_condition_available_points and selection_condition_team_limit:#atmost one wicketkeeper is allowed
                self.wicketkeepers_num.setText(str(int(self.wicketkeepers_num.text()) + 1))
                self.select_player(item, available_points)
            else:
                self.selection_error("Warning", selection_condition_available_points, ["selection_condition_wicketkeeper", selection_condition_wicketkeepers_num, "one"], selection_condition_team_limit)
        item.listWidget().sortItems()
                
    def remove_players_chosen(self, item):
        player_id = item.data(QtCore.Qt.UserRole)
        player_details = get_player_details(player_id)
        player_team_code, player_role, player_value = str(player_details[1]), str(player_details[2]), str(player_details[3])
        btn_1, btn_2, btn_3, btn_4 = self.button_checked_status()
        if (player_role == 'BAT' and btn_1) or (player_role == 'BWL' and btn_2) or (player_role == 'AR' and btn_3) or (player_role == 'WK' and btn_4):
            if btn_1:
                self.batsmen_num.setText(str(int(self.batsmen_num.text()) - 1))
            elif btn_2:
                self.bowlers_num.setText(str(int(self.bowlers_num.text()) - 1))
            elif btn_3:
                self.allrounders_num.setText(str(int(self.allrounders_num.text()) - 1))
            else:
                self.wicketkeepers_num.setText(str(int(self.wicketkeepers_num.text()) - 1))
            self.points_available.setText(str(int(self.points_available.text()) + int(player_value)))
            self.points_used.setText(str(int(self.points_used.text()) - int(player_value)))
            self.my_team_listWidget.takeItem(self.my_team_listWidget.row(item))
            player_text = self.build_player_text_left(player_details)
            item.setText(player_text)  
            if self.team_1_numLabel.text() == player_team_code:
                self.team_1_playersNum.setText(str(int(self.team_1_playersNum.text()) - 1))
                list_widget = self.team_1_listWidget
            else:
                self.team_2_playersNum.setText(str(int(self.team_2_playersNum.text()) - 1))
                list_widget = self.team_2_listWidget
            list_widget.addItem(item)
            self.my_team_listWidget.sortItems()
            self.team_1_listWidget.sortItems()
            self.team_2_listWidget.sortItems()

    def select_player(self, item, available_points):
        player_id = item.data(QtCore.Qt.UserRole)
        player_details = get_player_details(player_id)
        player_team_code = player_details[1]
        player_text = self.build_player_text_right(player_details)
        self.points_available.setText(str(available_points))
        self.points_used.setText(str(1000 - available_points))
        if player_team_code == self.team_1_numLabel.text():
            self.team_1_playersNum.setText(str(int(self.team_1_playersNum.text()) + 1))
            list_widget = self.team_1_listWidget
        else:
            self.team_2_playersNum.setText(str(int(self.team_2_playersNum.text()) + 1))
            list_widget = self.team_2_listWidget
        list_widget.takeItem(list_widget.row(item))
        item.setText(player_text) 
        self.my_team_listWidget.addItem(item)
        self.my_team_listWidget.sortItems()
        
    def selection_error(self, display_icon, selection_condition_available_points, selection_condition_num_players, selection_condition_team_limit):
        selection_condition_role = selection_condition_num_players[0]
        boolean_result_selection_condition = selection_condition_num_players[1]
        players_role_limit = selection_condition_num_players[2]
        if not selection_condition_available_points:
            message = "You have exceeded the 1000 points available to you!"
        elif not boolean_result_selection_condition:
            message = "You can only select " + players_role_limit + " " + selection_condition_role.split("_")[2] + " in your fantasy team!"
        elif not selection_condition_team_limit:
            message = "Only seven players from a team can be chosen into your fantasy team!"
        self.show_message_box(" ", message, display_icon, False, False)
         
    def show_message_box(self, title, message, display_icon, retry_ignore, ok_cancel):#used to show info, warnings, critical errors in the form of a message box
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        if display_icon == 'Question':
            message_box.setIcon(QMessageBox.Question)
        elif display_icon == 'Information':
            message_box.setIcon(QMessageBox.Information)
        elif display_icon == 'Warning':
            message_box.setIcon(QMessageBox.Warning)
        elif display_icon == 'Critical':
            message_box.setIcon(QMessageBox.Critical)
        if retry_ignore:
            message_box.setStandardButtons(QMessageBox.Retry | QMessageBox.Ignore)
        if ok_cancel:
            message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = message_box.exec_()
        return x

    def menu_choices(self, action):
        choice = action.text()
        if choice == 'NEW Team':
            self.new_team()
        elif choice == 'OPEN Team':
            self.open_team()
        elif choice == 'SAVE Team':
            self.save_team()
        elif choice == 'EVALUATE Team':
            self.evaluate_team()
        else:
            self.view_scores()

    def new_team(self):
        matches = tuple(["Match " + str(i[0]) + " - " + str(i[1]) for i in get_matches()])
        match, match_confirmation = QInputDialog.getItem(self, "Match Selection", "Select a match : ", matches, 0, False)
        if match_confirmation:
            self.new_team_helper(match)

    def new_team_helper(self, match):
        team_name, name_confirmation = QInputDialog.getText(self, "Your Team Name", "Enter your team name : ")
        if name_confirmation:
            validity, error_message = validate_teamname(team_name)
            if validity:
                match_number = match.split(" ")[1]
                team_1_code,_,team_2_code = str(get_versus(match_number)[0]).split(" ")
                team_1_fullname, team_2_fullname = str(get_full_teamname(team_1_code)[0]), str(get_full_teamname(team_2_code)[0])
                self.set_fields(match, team_name, "0", "0", "0", "0", "1000", "0", team_1_fullname, team_2_fullname, team_1_code, "0", team_2_code, "0")
                self.enable_disable_buttons(True)
                self.my_team_listWidget.clear()
                self.display_players()
            else:
                x = self.show_message_box(" ", error_message, "Critical", True, False)
                if x == 524288:
                    self.new_team_helper(match)

    def open_team(self):
        self.open_evaluate_team_helper("open")

    def open_evaluate_team_helper(self, operation):
        matches = tuple(["Match " + str(i[0]) + " - " + str(i[1]) for i in get_matches()])
        match, match_confirmation = QInputDialog.getItem(self, "Match Selection", "Select a match : ", matches, 0, False)
        if match_confirmation:
            match_number  = match.split(" ")[1]
            user_teamnames = tuple([user_teamname[0] for user_teamname in get_user_teamnames(match_number)])
            if user_teamnames != ():
                user_teamname, team_confirmation = QInputDialog.getItem(self, "Team Selection", "Select a team : ", user_teamnames, 0, False)
                if team_confirmation:
                    if operation == "open":
                        self.open_team_helper(user_teamname, match_number)
                    else:
                        self.evaluate_team_helper(user_teamname, match_number)
            else:
                error_message = "No teams have been created for " + match + ". Select another match or create a new team for this match!"
                x = self.show_message_box(" ", error_message, "Information", True, False)
                if x == 524288:
                    if operation == "open":
                        self.open_evaluate_team_helper("open")
                    else:
                        self.open_evaluate_team_helper("evaluate")

    def open_team_helper(self, user_teamname, match_number):
        self.my_team_listWidget.clear()
        userteam_details = get_userteam_details(user_teamname, match_number)
        used_points = userteam_details[0]
        player_ids = list(int(player_id) for player_id in userteam_details[2][1:-1].split(", "))
        available_points = 1000 - used_points
        team_1_code,_,team_2_code = str(get_versus(match_number)[0]).split(" ")
        team_1_fullname, team_2_fullname = str(get_full_teamname(team_1_code)[0]), str(get_full_teamname(team_2_code)[0])
        num_batsmen, num_bowlers, num_allrounders, num_wicketkeepers, playersNum_team_1, playersNum_team_2 = 0, 0, 0, 0, 0, 0
        for player_id in player_ids:
            player_details = get_player_details(player_id)
            player_text = self.build_player_text_right(player_details)
            player_team_code, player_role = str(player_details[1]), str(player_details[2])
            if player_team_code == team_1_code:
                playersNum_team_1 = playersNum_team_1 + 1
            else:
                playersNum_team_2 = playersNum_team_2 + 1
            if player_role == 'BAT':
                num_batsmen = num_batsmen + 1
            elif player_role == 'BWL':
                num_bowlers = num_bowlers + 1
            elif player_role == 'AR':
                num_allrounders = num_allrounders + 1
            elif player_role == 'WK':
                num_wicketkeepers = num_wicketkeepers + 1
            item = QListWidgetItem()
            item.setText(str(player_text))
            item.setData(QtCore.Qt.UserRole, player_id)
            self.my_team_listWidget.addItem(item)
        self.set_fields("Match " + match_number, user_teamname, str(num_batsmen), str(num_bowlers), str(num_allrounders), str(num_wicketkeepers), str(available_points), str(used_points), team_1_fullname, team_2_fullname, team_1_code, str(playersNum_team_1), team_2_code, str(playersNum_team_2))
        self.enable_disable_buttons(True)
        self.my_team_listWidget.sortItems()
        self.display_players()
        
    def save_team(self):
        save_error = False
        if self.my_team_name.text() == '#########':
            error_message =  "Create a team before saving it!"
            x = self.show_message_box(" ", error_message, "Critical", True, False)
            if x == 524288:
                self.new_team()
                return
            else:
                return
        if self.my_team_listWidget.count() >= 0 and self.my_team_listWidget.count() < 11:
            team_size = self.my_team_listWidget.count()
            placeholder_1, placeholder_3 = "is" if team_size == 1 else "are", "player" if team_size == 1 else "players"
            error_message =  "There {} only {} {} in your team. There need to be eleven!".format(placeholder_1, team_size, placeholder_3)
            x = self.show_message_box(" ", error_message, "Critical", True, False)
            if x != 524288:
                save_error = True
        if save_error:
            self.uncheck_buttons()
            self.enable_disable_buttons(False)
            
        if not save_error:
            user_team_name = self.my_team_name.text()
            match_chosen = int(self.match_chosen.text().split(" ")[1])
            points_used = int(self.points_used.text())
            team_performance = 0
            player_ids = []

            if (int(self.batsmen_num.text()) + int(self.bowlers_num.text()) + int(self.allrounders_num.text()) + int(self.wicketkeepers_num.text()) == 11) and (int(self.team_1_playersNum.text()) + int(self.team_2_playersNum.text()) == 11):
                for i in range(11):
                    player_id = self.my_team_listWidget.item(i).data(QtCore.Qt.UserRole)
                    player_ids.append(player_id)
                team_performance_score, player_performance_scores = self.calculate_team_performance(match_chosen, player_ids)
                squad_info = [user_team_name, match_chosen, points_used, team_performance_score, player_ids, player_performance_scores]
                insert_success, integrity_error = insert_usersquad(squad_info, False)
                list_user_teamnames = list(str(team_name[0]) for team_name in get_user_teamnames(match_chosen))
                if not insert_success and integrity_error:
                    if user_team_name in list_user_teamnames:
                        same_composition = save_team_validation(player_ids, user_team_name, match_chosen)
                        if same_composition:
                            self.show_message_box(" ", "This team already exists!", "Critical", False, False)
                        else:
                            y = self.show_message_box(" ", "Do you want to overwrite the existing team " + "\"" + str(user_team_name) + "\"" + " with this team?", "Warning", False, True)
                            if y == 1024:
                                delete_usersquad(user_team_name)
                                self.save_team()
                                
                elif (not insert_success and not integrity_error):
                    self.show_message_box(" ", "Unable to save team {}!!".format("\"" + user_team_name + "\""), "Critical", False, False)
                elif insert_success:
                    same_composition = False
                    for team_name in list_user_teamnames:
                        same_composition = save_team_validation(player_ids, team_name, match_chosen)
                        if same_composition:
                            break
                    if same_composition:
                        y = self.show_message_box(" ", "There is another team " + "\"" + str(team_name) + "\"" + "with the same composition as this! Do you still want to save this team?", "Question", False, False)
                        if y == 1024:
                            insert_usersquad(squad_info, True)
                            self.show_message_box(" ", "Team {} saved successfully!".format("\"" + user_team_name + "\""), "Information", False, False)
                    else:
                        insert_success_2, integrity_error_2 = insert_usersquad(squad_info, True)
                        if insert_success_2:
                            self.show_message_box(" ", "Team {} saved successfully!".format("\"" + user_team_name + "\""), "Information", False, False)

    def evaluate_team(self):
        self.open_evaluate_team_helper("evaluate")
                
    def evaluate_team_helper(self, user_teamname, match_number):
        versus = get_versus(match_number)[0]
        input_userteam_details = get_userteam_details(user_teamname, match_number)
        user_teamnames = get_user_teamnames(match_number)
        team_score = 0
        userteams_list = []
        for i in user_teamnames:
            userteam_details = get_userteam_details(i[0], match_number)
            score = float(userteam_details[1])
            userteams_list.append((i[0], score))
        userteams_list.sort(key = lambda x: x[1], reverse = True)
        winning_team, winning_score = userteams_list[0]
        userteam_standing = userteams_list.index([item for item in userteams_list if item[0] == user_teamname][0]) + 1
        if userteam_standing == 1:
            display_message = "Congratulations! You have finished first."
        else:
            display_message = "You have finished {}. Team {} with {} points is the winner!".format(num2words(userteam_standing, to='ordinal', lang='en'), winning_team, winning_score)
        player_ids = list(int(player_id) for player_id in input_userteam_details[2][1:-1].split(", "))
        userteam_details_2 = []
        _, player_performance_scores = self.calculate_team_performance(match_number, player_ids)
        for i in player_performance_scores[1:-1].split(","):
            player_id, player_score = i.split(":")
            team_score = team_score + float(player_score)
            player_name = get_player_details(player_id)[0]
            userteam_details_2.append((player_name, str(float(player_score))))
        userteam_info = ["Match " + match_number + " - " + versus, user_teamname, userteam_details_2, team_score, display_message]
        evaluation = QtWidgets.QDialog()
        evaluation.setStyleSheet("""
        QLabel#label_4, #label_12, #label_5, #label_6, #label_9, #label_8, #label_13, #label_10, #label_11, #label_7, #label_3, #label_15, #label_20, #label_16, #label_17, #label_24, #label_21, #label_18, #label_22, #label_19, #label_23, #label_14 {
            font: Arial;
            font-weight : bold;
            background-color : rgb(31, 31, 46);
            color : white;
            qproperty-alignment : AlignCenter;
            }
        QLabel#label_28, #label_2, #label_26, #label_27 {
            font : Comic Sans MS;
            font-weight : bold;
            color : black;
            qproperty-alignment : AlignCenter;
            }
        QLabel#label_25 {
            font: Arial;
            font-weight : bold;
            background-color : rgb(15, 0, 83);
            color : white;
            qproperty-alignment : AlignCenter;
            }
        QDialog {
            background-color: rgb(252, 252, 252);
            }
        """)
        ui_3 = Ui_Dialog_2()
        ui_3.setupUi(evaluation, userteam_info)
        evaluation.exec_()
        
    def calculate_team_performance(self, match_chosen, player_ids):
        match_details = get_match_details(match_chosen)
        match_player_ids_list = list(int(match_player_id) for match_player_id in match_details[0][1:-1].split(", "))
        team_performance_score = 0
        player_performance_scores = "{"
        for player_id in player_ids:
            if int(player_id) in match_player_ids_list:
                player_performance_values = []
                player_id_index = match_player_ids_list.index(int(player_id))
                for i in range(1, 11):
                    player_performance_value = list(int(match_detail) for match_detail in match_details[i][1:-1].split(", "))[player_id_index]
                    player_performance_values.append(player_performance_value)
                player_performance_score = self.calculate_player_performance(player_performance_values)
                player_performance_scores = player_performance_scores + str(player_id) + ":" + str(player_performance_score) + ","
                team_performance_score = team_performance_score + player_performance_score
            else:
                player_performance_scores = player_performance_scores + str(player_id) + ":" + "0" + ","
                continue
        player_performance_scores = player_performance_scores[:-1] + "}"
        return [team_performance_score, player_performance_scores]
                            
    def calculate_player_performance(self, player_performance_values):
        player_performance_score = 0
        runs_scored, balls_faced, fours_hit, sixes_hit, balls_bowled, runs_given, wickets_taken, catches_taken, stumpings_effected, runouts_effected = player_performance_values

        if balls_faced != 0 and runs_scored != 0:
            player_performance_score = player_performance_score + runs_scored/2.0
            strike_rate = 100*runs_scored/float(balls_faced)
            if strike_rate >= 80:
                if strike_rate >= 100:
                    player_performance_score = player_performance_score + 6
                else:
                    player_performance_score = player_performance_score + 2

            if runs_scored >= 50 and runs_scored < 100:
                player_performance_score = player_performance_score + 5
            elif runs_scored >= 100:
                if runs_scored >= 200:
                    player_performance_score = player_performance_score + 30
                else:
                    player_performance_score = player_performance_score + 10

        if balls_bowled != 0:
            economy_rate = runs_given/(balls_bowled/6.0)
            if economy_rate <= 2:
                player_performance_score = player_performance_score + 10
            elif economy_rate > 2 and economy_rate <= 3.5:
                player_performance_score = player_performance_score + 7
            elif economy_rate > 3.5 and economy_rate <=4.5:
                player_performance_score = player_performance_score + 4

        if wickets_taken == 3 or wickets_taken == 4:
            player_performance_score = player_performance_score + 5
        elif wickets_taken >= 5:
            player_performance_score = player_performance_score + 10

        player_performance_score = player_performance_score + 10*(wickets_taken + catches_taken + stumpings_effected + runouts_effected)
        return player_performance_score

    def view_scores(self):
        scores = QtWidgets.QDialog()
        scores.setStyleSheet("""
        QDialog {
            background-color : rgb(250, 250, 250);
        }
        QLabel#match_1_link, #match_2_link, #match_3_link, #match_4_link {
            background-color : white;
        }
        """)
        ui_4 = Ui_Dialog_3()
        ui_4.setupUi(scores)
        scores.exec_()
                                   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet("""
        QRadioButton:checked {
            background-color : rgb(134, 134, 172);
        }
        QLabel {
            font : Arial;
            font-weight : bold;
            color : rgb(0, 0, 51);
        }
        #line, #line_2, #line_3, #line_4, #line_5, #line_6, #line_7, #line_8, #line_9, #line_10 {
            color : rgb(0, 0, 51);
        }
        QListWidget::item {
            background-color : black;
            color : white;
        }
        QMainWindow {
            background-color : rgb(250, 250, 250);
        }
        """)
    ui_1 = Ui_MainWindow()
    ui_1.setupUi(MainWindow)
    instructions = QtWidgets.QDialog()
    ui_2 = Ui_Dialog()
    ui_2.setupUi(instructions)
    p = instructions.exec_()
    if p == 1:
        MainWindow.show()
    else:
        sys.exit(1)
    sys.exit(app.exec_())
