# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(872, 673)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 183, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 183, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 183, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.png.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lblMonero = QtWidgets.QLabel(self.centralWidget)
        self.lblMonero.setGeometry(QtCore.QRect(40, 603, 53, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblMonero.setFont(font)
        self.lblMonero.setObjectName("lblMonero")
        self.lblMoneroinclO = QtWidgets.QLabel(self.centralWidget)
        self.lblMoneroinclO.setGeometry(QtCore.QRect(200, 603, 164, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblMoneroinclO.setFont(font)
        self.lblMoneroinclO.setObjectName("lblMoneroinclO")
        self.lblBitcoin = QtWidgets.QLabel(self.centralWidget)
        self.lblBitcoin.setGeometry(QtCore.QRect(680, 603, 47, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblBitcoin.setFont(font)
        self.lblBitcoin.setObjectName("lblBitcoin")
        self.lblEthereum = QtWidgets.QLabel(self.centralWidget)
        self.lblEthereum.setGeometry(QtCore.QRect(360, 603, 65, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblEthereum.setFont(font)
        self.lblEthereum.setObjectName("lblEthereum")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 220, 791, 371))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 118, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.OpenOrders = QtWidgets.QWidget()
        self.OpenOrders.setMinimumSize(QtCore.QSize(858, 0))
        self.OpenOrders.setMaximumSize(QtCore.QSize(600, 16777215))
        self.OpenOrders.setBaseSize(QtCore.QSize(0, 0))
        self.OpenOrders.setObjectName("OpenOrders")
        self.tabOO = QtWidgets.QTabWidget(self.OpenOrders)
        self.tabOO.setGeometry(QtCore.QRect(-1, -2, 791, 361))
        self.tabOO.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 0px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 12ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabOO.setObjectName("tabOO")
        self.tabXMR = QtWidgets.QWidget()
        self.tabXMR.setObjectName("tabXMR")
        self.OpenOrdersWidgetXMR = QtWidgets.QTableWidget(self.tabXMR)
        self.OpenOrdersWidgetXMR.setGeometry(QtCore.QRect(-1, -1, 791, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenOrdersWidgetXMR.sizePolicy().hasHeightForWidth())
        self.OpenOrdersWidgetXMR.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.OpenOrdersWidgetXMR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.OpenOrdersWidgetXMR.setFont(font)
        self.OpenOrdersWidgetXMR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OpenOrdersWidgetXMR.setAutoFillBackground(True)
        self.OpenOrdersWidgetXMR.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}")
        self.OpenOrdersWidgetXMR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OpenOrdersWidgetXMR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OpenOrdersWidgetXMR.setLineWidth(1)
        self.OpenOrdersWidgetXMR.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.OpenOrdersWidgetXMR.setAlternatingRowColors(False)
        self.OpenOrdersWidgetXMR.setTextElideMode(QtCore.Qt.ElideLeft)
        self.OpenOrdersWidgetXMR.setShowGrid(True)
        self.OpenOrdersWidgetXMR.setGridStyle(QtCore.Qt.DashLine)
        self.OpenOrdersWidgetXMR.setCornerButtonEnabled(False)
        self.OpenOrdersWidgetXMR.setRowCount(0)
        self.OpenOrdersWidgetXMR.setObjectName("OpenOrdersWidgetXMR")
        self.OpenOrdersWidgetXMR.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetXMR.setHorizontalHeaderItem(4, item)
        self.OpenOrdersWidgetXMR.horizontalHeader().setDefaultSectionSize(151)
        self.OpenOrdersWidgetXMR.horizontalHeader().setStretchLastSection(True)
        self.OpenOrdersWidgetXMR.verticalHeader().setVisible(False)
        self.OpenOrdersWidgetXMR.verticalHeader().setStretchLastSection(False)
        self.tabOO.addTab(self.tabXMR, "")
        self.tabETH = QtWidgets.QWidget()
        self.tabETH.setObjectName("tabETH")
        self.OpenOrdersWidgetETH = QtWidgets.QTableWidget(self.tabETH)
        self.OpenOrdersWidgetETH.setGeometry(QtCore.QRect(-1, -1, 790, 333))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenOrdersWidgetETH.sizePolicy().hasHeightForWidth())
        self.OpenOrdersWidgetETH.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 101, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.OpenOrdersWidgetETH.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.OpenOrdersWidgetETH.setFont(font)
        self.OpenOrdersWidgetETH.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OpenOrdersWidgetETH.setAutoFillBackground(False)
        self.OpenOrdersWidgetETH.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}")
        self.OpenOrdersWidgetETH.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OpenOrdersWidgetETH.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OpenOrdersWidgetETH.setLineWidth(1)
        self.OpenOrdersWidgetETH.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.OpenOrdersWidgetETH.setAlternatingRowColors(False)
        self.OpenOrdersWidgetETH.setTextElideMode(QtCore.Qt.ElideLeft)
        self.OpenOrdersWidgetETH.setShowGrid(True)
        self.OpenOrdersWidgetETH.setGridStyle(QtCore.Qt.DashLine)
        self.OpenOrdersWidgetETH.setCornerButtonEnabled(False)
        self.OpenOrdersWidgetETH.setRowCount(0)
        self.OpenOrdersWidgetETH.setObjectName("OpenOrdersWidgetETH")
        self.OpenOrdersWidgetETH.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetETH.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetETH.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetETH.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetETH.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.OpenOrdersWidgetETH.setHorizontalHeaderItem(4, item)
        self.OpenOrdersWidgetETH.horizontalHeader().setDefaultSectionSize(151)
        self.OpenOrdersWidgetETH.horizontalHeader().setStretchLastSection(True)
        self.OpenOrdersWidgetETH.verticalHeader().setVisible(False)
        self.tabOO.addTab(self.tabETH, "")
        self.tabWidget.addTab(self.OpenOrders, "")
        self.History = QtWidgets.QWidget()
        self.History.setObjectName("History")
        self.tabHistory = QtWidgets.QTabWidget(self.History)
        self.tabHistory.setGeometry(QtCore.QRect(-1, -2, 790, 361))
        self.tabHistory.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 0px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 12ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabHistory.setObjectName("tabHistory")
        self.tabXMR1 = QtWidgets.QWidget()
        self.tabXMR1.setObjectName("tabXMR1")
        self.HistoryWidgetXMR = QtWidgets.QTableWidget(self.tabXMR1)
        self.HistoryWidgetXMR.setGeometry(QtCore.QRect(-1, -1, 791, 333))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HistoryWidgetXMR.sizePolicy().hasHeightForWidth())
        self.HistoryWidgetXMR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.HistoryWidgetXMR.setFont(font)
        self.HistoryWidgetXMR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HistoryWidgetXMR.setAutoFillBackground(False)
        self.HistoryWidgetXMR.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}\n"
"\n"
"")
        self.HistoryWidgetXMR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HistoryWidgetXMR.setLineWidth(1)
        self.HistoryWidgetXMR.setShowGrid(True)
        self.HistoryWidgetXMR.setGridStyle(QtCore.Qt.DashLine)
        self.HistoryWidgetXMR.setCornerButtonEnabled(True)
        self.HistoryWidgetXMR.setRowCount(0)
        self.HistoryWidgetXMR.setObjectName("HistoryWidgetXMR")
        self.HistoryWidgetXMR.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetXMR.setHorizontalHeaderItem(4, item)
        self.HistoryWidgetXMR.horizontalHeader().setDefaultSectionSize(151)
        self.HistoryWidgetXMR.horizontalHeader().setSortIndicatorShown(True)
        self.HistoryWidgetXMR.horizontalHeader().setStretchLastSection(True)
        self.HistoryWidgetXMR.verticalHeader().setVisible(False)
        self.tabHistory.addTab(self.tabXMR1, "")
        self.tabETH1 = QtWidgets.QWidget()
        self.tabETH1.setObjectName("tabETH1")
        self.HistoryWidgetETH = QtWidgets.QTableWidget(self.tabETH1)
        self.HistoryWidgetETH.setGeometry(QtCore.QRect(-1, -1, 790, 333))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HistoryWidgetETH.sizePolicy().hasHeightForWidth())
        self.HistoryWidgetETH.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.HistoryWidgetETH.setFont(font)
        self.HistoryWidgetETH.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HistoryWidgetETH.setAutoFillBackground(False)
        self.HistoryWidgetETH.setStyleSheet("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-left-width:1 px;\n"
"     border-right-width: 1px ;\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QTableWidget {\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"}")
        self.HistoryWidgetETH.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HistoryWidgetETH.setLineWidth(1)
        self.HistoryWidgetETH.setShowGrid(True)
        self.HistoryWidgetETH.setGridStyle(QtCore.Qt.DashLine)
        self.HistoryWidgetETH.setCornerButtonEnabled(True)
        self.HistoryWidgetETH.setRowCount(0)
        self.HistoryWidgetETH.setObjectName("HistoryWidgetETH")
        self.HistoryWidgetETH.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetETH.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetETH.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetETH.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetETH.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        item.setFont(font)
        self.HistoryWidgetETH.setHorizontalHeaderItem(4, item)
        self.HistoryWidgetETH.horizontalHeader().setDefaultSectionSize(151)
        self.HistoryWidgetETH.horizontalHeader().setSortIndicatorShown(True)
        self.HistoryWidgetETH.horizontalHeader().setStretchLastSection(True)
        self.HistoryWidgetETH.verticalHeader().setVisible(False)
        self.tabHistory.addTab(self.tabETH1, "")
        self.tabWidget.addTab(self.History, "")
        self.Trading = QtWidgets.QWidget()
        self.Trading.setObjectName("Trading")
        self.tabTrading = QtWidgets.QTabWidget(self.Trading)
        self.tabTrading.setGeometry(QtCore.QRect(-1, -2, 791, 361))
        self.tabTrading.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 0px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 12ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabTrading.setObjectName("tabTrading")
        self.tabXMR2 = QtWidgets.QWidget()
        self.tabXMR2.setObjectName("tabXMR2")
        self.sellButton = QtWidgets.QPushButton(self.tabXMR2)
        self.sellButton.setGeometry(QtCore.QRect(540, 150, 93, 28))
        self.sellButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.sellButton.setObjectName("sellButton")
        self.layoutWidget = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 30, 101, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblBuy = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblBuy.setFont(font)
        self.lblBuy.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuy.setObjectName("lblBuy")
        self.verticalLayout_3.addWidget(self.lblBuy)
        self.lblBuyPrice = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyPrice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyPrice.setObjectName("lblBuyPrice")
        self.verticalLayout_3.addWidget(self.lblBuyPrice)
        self.lblBuyAmount = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyAmount.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyAmount.setObjectName("lblBuyAmount")
        self.verticalLayout_3.addWidget(self.lblBuyAmount)
        self.lblBuyTotal = QtWidgets.QLabel(self.layoutWidget)
        self.lblBuyTotal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyTotal.setObjectName("lblBuyTotal")
        self.verticalLayout_3.addWidget(self.lblBuyTotal)
        self.layoutWidget1 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget1.setGeometry(QtCore.QRect(142, 52, 139, 85))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lnBuyPrice = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyPrice.setClearButtonEnabled(False)
        self.lnBuyPrice.setObjectName("lnBuyPrice")
        self.verticalLayout_6.addWidget(self.lnBuyPrice)
        self.lnBuyAmount = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyAmount.setObjectName("lnBuyAmount")
        self.verticalLayout_6.addWidget(self.lnBuyAmount)
        self.lnBuyTotal = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnBuyTotal.setObjectName("lnBuyTotal")
        self.verticalLayout_6.addWidget(self.lnBuyTotal)
        self.layoutWidget2 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget2.setGeometry(QtCore.QRect(382, 30, 101, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblSell = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSell.setFont(font)
        self.lblSell.setObjectName("lblSell")
        self.verticalLayout_5.addWidget(self.lblSell)
        self.lblSellPrice = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellPrice.setObjectName("lblSellPrice")
        self.verticalLayout_5.addWidget(self.lblSellPrice)
        self.lblSellAmount = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellAmount.setObjectName("lblSellAmount")
        self.verticalLayout_5.addWidget(self.lblSellAmount)
        self.lblSellTotal = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSellTotal.setObjectName("lblSellTotal")
        self.verticalLayout_5.addWidget(self.lblSellTotal)
        self.layoutWidget3 = QtWidgets.QWidget(self.tabXMR2)
        self.layoutWidget3.setGeometry(QtCore.QRect(492, 52, 139, 85))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lnSellPrice = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellPrice.setObjectName("lnSellPrice")
        self.verticalLayout_7.addWidget(self.lnSellPrice)
        self.lnSellAmount = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellAmount.setObjectName("lnSellAmount")
        self.verticalLayout_7.addWidget(self.lnSellAmount)
        self.lnSellTotal = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnSellTotal.setObjectName("lnSellTotal")
        self.verticalLayout_7.addWidget(self.lnSellTotal)
        self.btnSellGetBTCPrice = QtWidgets.QPushButton(self.tabXMR2)
        self.btnSellGetBTCPrice.setGeometry(QtCore.QRect(642, 55, 21, 21))
        self.btnSellGetBTCPrice.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.btnSellGetBTCPrice.setFlat(False)
        self.btnSellGetBTCPrice.setObjectName("btnSellGetBTCPrice")
        self.btnBuyGetBTCTotal = QtWidgets.QPushButton(self.tabXMR2)
        self.btnBuyGetBTCTotal.setGeometry(QtCore.QRect(292, 115, 21, 21))
        self.btnBuyGetBTCTotal.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.btnBuyGetBTCTotal.setObjectName("btnBuyGetBTCTotal")
        self.buyButton = QtWidgets.QPushButton(self.tabXMR2)
        self.buyButton.setGeometry(QtCore.QRect(190, 150, 93, 28))
        self.buyButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.buyButton.setObjectName("buyButton")
        self.tabTrading.addTab(self.tabXMR2, "")
        self.tabETH2 = QtWidgets.QWidget()
        self.tabETH2.setObjectName("tabETH2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabETH2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(32, 30, 101, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lblBuy_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblBuy_2.setFont(font)
        self.lblBuy_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuy_2.setObjectName("lblBuy_2")
        self.verticalLayout_10.addWidget(self.lblBuy_2)
        self.lblBuyPrice_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblBuyPrice_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyPrice_2.setObjectName("lblBuyPrice_2")
        self.verticalLayout_10.addWidget(self.lblBuyPrice_2)
        self.lblBuyAmount_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblBuyAmount_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyAmount_2.setObjectName("lblBuyAmount_2")
        self.verticalLayout_10.addWidget(self.lblBuyAmount_2)
        self.lblBuyTotal_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblBuyTotal_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblBuyTotal_2.setObjectName("lblBuyTotal_2")
        self.verticalLayout_10.addWidget(self.lblBuyTotal_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tabETH2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(142, 52, 139, 85))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lnETHBuyPrice = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lnETHBuyPrice.setClearButtonEnabled(False)
        self.lnETHBuyPrice.setObjectName("lnETHBuyPrice")
        self.verticalLayout_11.addWidget(self.lnETHBuyPrice)
        self.lnETHBuyAmount = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lnETHBuyAmount.setObjectName("lnETHBuyAmount")
        self.verticalLayout_11.addWidget(self.lnETHBuyAmount)
        self.lnETHBuyTotal = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lnETHBuyTotal.setObjectName("lnETHBuyTotal")
        self.verticalLayout_11.addWidget(self.lnETHBuyTotal)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tabETH2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(382, 30, 101, 101))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lblSell_2 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSell_2.setFont(font)
        self.lblSell_2.setObjectName("lblSell_2")
        self.verticalLayout_12.addWidget(self.lblSell_2)
        self.lblSellPrice_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.lblSellPrice_2.setObjectName("lblSellPrice_2")
        self.verticalLayout_12.addWidget(self.lblSellPrice_2)
        self.lblSellAmount_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.lblSellAmount_2.setObjectName("lblSellAmount_2")
        self.verticalLayout_12.addWidget(self.lblSellAmount_2)
        self.lblSellTotal_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.lblSellTotal_2.setObjectName("lblSellTotal_2")
        self.verticalLayout_12.addWidget(self.lblSellTotal_2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tabETH2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(492, 52, 139, 85))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lnETHSellPrice = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lnETHSellPrice.setObjectName("lnETHSellPrice")
        self.verticalLayout_13.addWidget(self.lnETHSellPrice)
        self.lnETHSellAmount = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lnETHSellAmount.setObjectName("lnETHSellAmount")
        self.verticalLayout_13.addWidget(self.lnETHSellAmount)
        self.lnETHSellTotal = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lnETHSellTotal.setObjectName("lnETHSellTotal")
        self.verticalLayout_13.addWidget(self.lnETHSellTotal)
        self.btnETHSellGetBTCPrice = QtWidgets.QPushButton(self.tabETH2)
        self.btnETHSellGetBTCPrice.setGeometry(QtCore.QRect(642, 55, 21, 21))
        self.btnETHSellGetBTCPrice.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.btnETHSellGetBTCPrice.setFlat(False)
        self.btnETHSellGetBTCPrice.setObjectName("btnETHSellGetBTCPrice")
        self.sellETHButton = QtWidgets.QPushButton(self.tabETH2)
        self.sellETHButton.setGeometry(QtCore.QRect(540, 150, 93, 28))
        self.sellETHButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.sellETHButton.setObjectName("sellETHButton")
        self.buyETHButton = QtWidgets.QPushButton(self.tabETH2)
        self.buyETHButton.setGeometry(QtCore.QRect(190, 150, 93, 28))
        self.buyETHButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.buyETHButton.setObjectName("buyETHButton")
        self.btnETHBuyGetBTCTotal = QtWidgets.QPushButton(self.tabETH2)
        self.btnETHBuyGetBTCTotal.setGeometry(QtCore.QRect(292, 115, 21, 21))
        self.btnETHBuyGetBTCTotal.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.btnETHBuyGetBTCTotal.setObjectName("btnETHBuyGetBTCTotal")
        self.tabTrading.addTab(self.tabETH2, "")
        self.tabWidget.addTab(self.Trading, "")
        self.tabConfiguration = QtWidgets.QWidget()
        self.tabConfiguration.setObjectName("tabConfiguration")
        self.saveButton = QtWidgets.QPushButton(self.tabConfiguration)
        self.saveButton.setGeometry(QtCore.QRect(590, 120, 93, 28))
        self.saveButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(False)
        self.saveButton.setObjectName("saveButton")
        self.layoutWidget4 = QtWidgets.QWidget(self.tabConfiguration)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 30, 91, 66))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblPoloniex = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPoloniex.setFont(font)
        self.lblPoloniex.setObjectName("lblPoloniex")
        self.verticalLayout_8.addWidget(self.lblPoloniex)
        self.lblPublicKey = QtWidgets.QLabel(self.layoutWidget4)
        self.lblPublicKey.setObjectName("lblPublicKey")
        self.verticalLayout_8.addWidget(self.lblPublicKey)
        self.lblSecretKey = QtWidgets.QLabel(self.layoutWidget4)
        self.lblSecretKey.setObjectName("lblSecretKey")
        self.verticalLayout_8.addWidget(self.lblSecretKey)
        self.layoutWidget5 = QtWidgets.QWidget(self.tabConfiguration)
        self.layoutWidget5.setGeometry(QtCore.QRect(150, 50, 531, 55))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lnPublicKey = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lnPublicKey.setObjectName("lnPublicKey")
        self.verticalLayout_9.addWidget(self.lnPublicKey)
        self.lnSecretKey = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lnSecretKey.setObjectName("lnSecretKey")
        self.verticalLayout_9.addWidget(self.lnSecretKey)
        self.lblrestartkey = QtWidgets.QLabel(self.tabConfiguration)
        self.lblrestartkey.setGeometry(QtCore.QRect(30, 160, 501, 16))
        self.lblrestartkey.setObjectName("lblrestartkey")
        self.tabWidget.addTab(self.tabConfiguration, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tabLog)
        self.plainTextEdit.setGeometry(QtCore.QRect(-1, -1, 791, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")
        icon = QtGui.QIcon.fromTheme("test")
        self.tabWidget.addTab(self.tabLog, icon, "")
        self.layoutWidget6 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 39, 95, 141))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.layoutWidget6.setFont(font)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPriceBTC = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblPriceBTC.setFont(font)
        self.lblPriceBTC.setObjectName("lblPriceBTC")
        self.verticalLayout.addWidget(self.lblPriceBTC)
        self.lblPriceUSD = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblPriceUSD.setFont(font)
        self.lblPriceUSD.setObjectName("lblPriceUSD")
        self.verticalLayout.addWidget(self.lblPriceUSD)
        self.lblHigh = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblHigh.setFont(font)
        self.lblHigh.setObjectName("lblHigh")
        self.verticalLayout.addWidget(self.lblHigh)
        self.lblLow = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblLow.setFont(font)
        self.lblLow.setObjectName("lblLow")
        self.verticalLayout.addWidget(self.lblLow)
        self.lblChange = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblChange.setFont(font)
        self.lblChange.setScaledContents(True)
        self.lblChange.setObjectName("lblChange")
        self.verticalLayout.addWidget(self.lblChange)
        self.lblEthereuminclO = QtWidgets.QLabel(self.centralWidget)
        self.lblEthereuminclO.setGeometry(QtCore.QRect(520, 603, 176, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.lblEthereuminclO.setFont(font)
        self.lblEthereuminclO.setObjectName("lblEthereuminclO")
        self.lblCancelOrderInfo = QtWidgets.QLabel(self.centralWidget)
        self.lblCancelOrderInfo.setGeometry(QtCore.QRect(39, 196, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setItalic(True)
        self.lblCancelOrderInfo.setFont(font)
        self.lblCancelOrderInfo.setObjectName("lblCancelOrderInfo")
        self.lblMonerox = QtWidgets.QLabel(self.centralWidget)
        self.lblMonerox.setGeometry(QtCore.QRect(140, 17, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 132, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblMonerox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblMonerox.setFont(font)
        self.lblMonerox.setAutoFillBackground(False)
        self.lblMonerox.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(239, 132, 45);\n"
"}")
        self.lblMonerox.setTextFormat(QtCore.Qt.AutoText)
        self.lblMonerox.setScaledContents(False)
        self.lblMonerox.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMonerox.setObjectName("lblMonerox")
        self.lblEthereumx = QtWidgets.QLabel(self.centralWidget)
        self.lblEthereumx.setGeometry(QtCore.QRect(249, 17, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblEthereumx.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblEthereumx.setFont(font)
        self.lblEthereumx.setAutoFillBackground(False)
        self.lblEthereumx.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: black;\n"
"}")
        self.lblEthereumx.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEthereumx.setWordWrap(False)
        self.lblEthereumx.setContentsMargins(0, 0, 0, 0)
        self.lblEthereumx.setObjectName("lblEthereumx")
        self.layoutWidget7 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(140, 40, 91, 140))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lnPriceXMR = QtWidgets.QLineEdit(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lnPriceXMR.setFont(font)
        self.lnPriceXMR.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnPriceXMR.setFrame(False)
        self.lnPriceXMR.setClearButtonEnabled(False)
        self.lnPriceXMR.setObjectName("lnPriceXMR")
        self.verticalLayout_2.addWidget(self.lnPriceXMR)
        self.lnPriceUSD = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lnPriceUSD.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnPriceUSD.setFrame(False)
        self.lnPriceUSD.setObjectName("lnPriceUSD")
        self.verticalLayout_2.addWidget(self.lnPriceUSD)
        self.lnHigh = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lnHigh.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnHigh.setFrame(False)
        self.lnHigh.setObjectName("lnHigh")
        self.verticalLayout_2.addWidget(self.lnHigh)
        self.lnLow = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lnLow.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnLow.setFrame(False)
        self.lnLow.setObjectName("lnLow")
        self.verticalLayout_2.addWidget(self.lnLow)
        self.lnChange = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lnChange.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnChange.setFrame(False)
        self.lnChange.setObjectName("lnChange")
        self.verticalLayout_2.addWidget(self.lnChange)
        self.layoutWidget8 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(249, 40, 91, 140))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lnPriceETH = QtWidgets.QLineEdit(self.layoutWidget8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lnPriceETH.setFont(font)
        self.lnPriceETH.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnPriceETH.setFrame(False)
        self.lnPriceETH.setObjectName("lnPriceETH")
        self.verticalLayout_4.addWidget(self.lnPriceETH)
        self.lnETHPriceUSD = QtWidgets.QLineEdit(self.layoutWidget8)
        self.lnETHPriceUSD.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnETHPriceUSD.setFrame(False)
        self.lnETHPriceUSD.setObjectName("lnETHPriceUSD")
        self.verticalLayout_4.addWidget(self.lnETHPriceUSD)
        self.lnETHHigh = QtWidgets.QLineEdit(self.layoutWidget8)
        self.lnETHHigh.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnETHHigh.setFrame(False)
        self.lnETHHigh.setObjectName("lnETHHigh")
        self.verticalLayout_4.addWidget(self.lnETHHigh)
        self.lnETHLow = QtWidgets.QLineEdit(self.layoutWidget8)
        self.lnETHLow.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnETHLow.setFrame(False)
        self.lnETHLow.setObjectName("lnETHLow")
        self.verticalLayout_4.addWidget(self.lnETHLow)
        self.lnETHChange = QtWidgets.QLineEdit(self.layoutWidget8)
        self.lnETHChange.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnETHChange.setFrame(False)
        self.lnETHChange.setObjectName("lnETHChange")
        self.verticalLayout_4.addWidget(self.lnETHChange)
        self.lcdEthereum = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdEthereum.setGeometry(QtCore.QRect(360, 620, 141, 21))
        self.lcdEthereum.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdEthereum.setPalette(palette)
        self.lcdEthereum.setAutoFillBackground(True)
        self.lcdEthereum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdEthereum.setDigitCount(15)
        self.lcdEthereum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdEthereum.setObjectName("lcdEthereum")
        self.lcdMonero = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdMonero.setGeometry(QtCore.QRect(40, 620, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 181, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 181, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 27, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lcdMonero.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lcdMonero.setFont(font)
        self.lcdMonero.setAutoFillBackground(True)
        self.lcdMonero.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdMonero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdMonero.setLineWidth(1)
        self.lcdMonero.setSmallDecimalPoint(False)
        self.lcdMonero.setDigitCount(15)
        self.lcdMonero.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdMonero.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMonero.setObjectName("lcdMonero")
        self.lcdEthereuminclO = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdEthereuminclO.setGeometry(QtCore.QRect(520, 620, 141, 21))
        self.lcdEthereuminclO.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdEthereuminclO.setPalette(palette)
        self.lcdEthereuminclO.setAutoFillBackground(True)
        self.lcdEthereuminclO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdEthereuminclO.setDigitCount(15)
        self.lcdEthereuminclO.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdEthereuminclO.setObjectName("lcdEthereuminclO")
        self.lcdBitcoin = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdBitcoin.setGeometry(QtCore.QRect(680, 620, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdBitcoin.setPalette(palette)
        self.lcdBitcoin.setAutoFillBackground(True)
        self.lcdBitcoin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdBitcoin.setDigitCount(15)
        self.lcdBitcoin.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdBitcoin.setObjectName("lcdBitcoin")
        self.lcdMoneroinclO = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdMoneroinclO.setGeometry(QtCore.QRect(200, 620, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 57, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 27, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 14, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdMoneroinclO.setPalette(palette)
        self.lcdMoneroinclO.setAutoFillBackground(True)
        self.lcdMoneroinclO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdMoneroinclO.setDigitCount(15)
        self.lcdMoneroinclO.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMoneroinclO.setObjectName("lcdMoneroinclO")
        self.layoutWidget9 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget9.setGeometry(QtCore.QRect(664, 20, 102, 43))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lblAppStatus = QtWidgets.QLabel(self.layoutWidget9)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(147, 49, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 49, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblAppStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblAppStatus.setFont(font)
        self.lblAppStatus.setAutoFillBackground(True)
        self.lblAppStatus.setObjectName("lblAppStatus")
        self.verticalLayout_14.addWidget(self.lblAppStatus)
        self.lblNetworkStatus = QtWidgets.QLabel(self.layoutWidget9)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(165, 16, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 16, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblNetworkStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblNetworkStatus.setFont(font)
        self.lblNetworkStatus.setAutoFillBackground(True)
        self.lblNetworkStatus.setObjectName("lblNetworkStatus")
        self.verticalLayout_14.addWidget(self.lblNetworkStatus)
        self.layoutWidget10 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget10.setGeometry(QtCore.QRect(774, 20, 61, 43))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lblAppStatusResult = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lblAppStatusResult.setFont(font)
        self.lblAppStatusResult.setText("")
        self.lblAppStatusResult.setObjectName("lblAppStatusResult")
        self.verticalLayout_15.addWidget(self.lblAppStatusResult)
        self.lblNetworkStatusResult = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lblNetworkStatusResult.setFont(font)
        self.lblNetworkStatusResult.setText("")
        self.lblNetworkStatusResult.setObjectName("lblNetworkStatusResult")
        self.verticalLayout_15.addWidget(self.lblNetworkStatusResult)
        self.lblBitcoinx = QtWidgets.QLabel(self.centralWidget)
        self.lblBitcoinx.setGeometry(QtCore.QRect(360, 17, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lblBitcoinx.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblBitcoinx.setFont(font)
        self.lblBitcoinx.setAutoFillBackground(False)
        self.lblBitcoinx.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: gold;\n"
"}")
        self.lblBitcoinx.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBitcoinx.setWordWrap(False)
        self.lblBitcoinx.setContentsMargins(0, 0, 0, 0)
        self.lblBitcoinx.setObjectName("lblBitcoinx")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(361, 55, 91, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lnBTCPriceUSD = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lnBTCPriceUSD.setFont(font)
        self.lnBTCPriceUSD.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lnBTCPriceUSD.setFrame(False)
        self.lnBTCPriceUSD.setObjectName("lnBTCPriceUSD")
        self.verticalLayout_16.addWidget(self.lnBTCPriceUSD)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabOO.setCurrentIndex(1)
        self.tabHistory.setCurrentIndex(0)
        self.tabTrading.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblMonero.setText(_translate("MainWindow", "Monero"))
        self.lblMoneroinclO.setText(_translate("MainWindow", "Monero incl. OO"))
        self.lblBitcoin.setText(_translate("MainWindow", "Bitcoin"))
        self.lblEthereum.setText(_translate("MainWindow", "Ethereum"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order Number"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price (BTC)"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SAmount (XMR)"))
        item = self.OpenOrdersWidgetXMR.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount (XMR)"))
        self.tabOO.setTabText(self.tabOO.indexOf(self.tabXMR), _translate("MainWindow", "XMR"))
        item = self.OpenOrdersWidgetETH.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order Number"))
        item = self.OpenOrdersWidgetETH.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.OpenOrdersWidgetETH.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price (BTC)"))
        item = self.OpenOrdersWidgetETH.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SAmount (ETH)"))
        item = self.OpenOrdersWidgetETH.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount (ETH)"))
        self.tabOO.setTabText(self.tabOO.indexOf(self.tabETH), _translate("MainWindow", "ETH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OpenOrders), _translate("MainWindow", "Open Orders"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.HistoryWidgetXMR.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.tabHistory.setTabText(self.tabHistory.indexOf(self.tabXMR1), _translate("MainWindow", "XMR"))
        item = self.HistoryWidgetETH.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.HistoryWidgetETH.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.HistoryWidgetETH.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.HistoryWidgetETH.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.HistoryWidgetETH.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.tabHistory.setTabText(self.tabHistory.indexOf(self.tabETH1), _translate("MainWindow", "ETH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.History), _translate("MainWindow", "History"))
        self.sellButton.setText(_translate("MainWindow", "Sell"))
        self.lblBuy.setText(_translate("MainWindow", "Buy"))
        self.lblBuyPrice.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblBuyAmount.setText(_translate("MainWindow", "Amount (XMR):"))
        self.lblBuyTotal.setText(_translate("MainWindow", "Total (BTC)"))
        self.lblSell.setText(_translate("MainWindow", "Sell"))
        self.lblSellPrice.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblSellAmount.setText(_translate("MainWindow", "Amount (XMR):"))
        self.lblSellTotal.setText(_translate("MainWindow", "Total (BTC):"))
        self.btnSellGetBTCPrice.setText(_translate("MainWindow", "A"))
        self.btnBuyGetBTCTotal.setText(_translate("MainWindow", "A"))
        self.buyButton.setText(_translate("MainWindow", "Buy"))
        self.tabTrading.setTabText(self.tabTrading.indexOf(self.tabXMR2), _translate("MainWindow", "XMR"))
        self.lblBuy_2.setText(_translate("MainWindow", "Buy"))
        self.lblBuyPrice_2.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblBuyAmount_2.setText(_translate("MainWindow", "Amount (ETH):"))
        self.lblBuyTotal_2.setText(_translate("MainWindow", "Total (BTC)"))
        self.lblSell_2.setText(_translate("MainWindow", "Sell"))
        self.lblSellPrice_2.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblSellAmount_2.setText(_translate("MainWindow", "Amount (ETH):"))
        self.lblSellTotal_2.setText(_translate("MainWindow", "Total (BTC):"))
        self.btnETHSellGetBTCPrice.setText(_translate("MainWindow", "A"))
        self.sellETHButton.setText(_translate("MainWindow", "Sell"))
        self.buyETHButton.setText(_translate("MainWindow", "Buy"))
        self.btnETHBuyGetBTCTotal.setText(_translate("MainWindow", "A"))
        self.tabTrading.setTabText(self.tabTrading.indexOf(self.tabETH2), _translate("MainWindow", "ETH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Trading), _translate("MainWindow", "Trading"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.lblPoloniex.setText(_translate("MainWindow", "Poloniex"))
        self.lblPublicKey.setText(_translate("MainWindow", "Public Key:"))
        self.lblSecretKey.setText(_translate("MainWindow", "Secret Key:"))
        self.lblrestartkey.setText(_translate("MainWindow", "Restart the application to activate the saved keys."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguration), _translate("MainWindow", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), _translate("MainWindow", "Log"))
        self.lblPriceBTC.setText(_translate("MainWindow", "Price (BTC):"))
        self.lblPriceUSD.setText(_translate("MainWindow", "Price (USD):"))
        self.lblHigh.setText(_translate("MainWindow", "24h High:"))
        self.lblLow.setText(_translate("MainWindow", "24h Low:"))
        self.lblChange.setText(_translate("MainWindow", "24h Change:"))
        self.lblEthereuminclO.setText(_translate("MainWindow", "Ethereum incl. OO"))
        self.lblCancelOrderInfo.setText(_translate("MainWindow", "To cancel an order double click the cell with the order number."))
        self.lblMonerox.setText(_translate("MainWindow", "Monero"))
        self.lblEthereumx.setText(_translate("MainWindow", "Ethereum"))
        self.lblAppStatus.setText(_translate("MainWindow", "App status: "))
        self.lblNetworkStatus.setText(_translate("MainWindow", "Connection:"))
        self.lblBitcoinx.setText(_translate("MainWindow", "Bitcoin"))

