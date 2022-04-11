#
# This file is part of KDDockWidgets.
#
# SPDX-FileCopyrightText: 2020-2022 Klarälvdalens Datakonsult AB, a KDAB Group company <info@kdab.com>
# Author: Renato Araujo Oliveira Filho <renato.araujo@kdab.com>
#
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only
#
# Contact KDAB at <info@kdab.com> for commercial licensing options.
#

from PyKDDockWidgetsQt6 import KDDockWidgets

from PySide6 import QtCore, QtWidgets, QtGui

from MyWidget1 import MyWidget1
from MyWidget2 import MyWidget2
from MyWidget3 import MyWidget3


def newMyWidget(parent=None):  # MyWidget1,2,3からランダムに選ぶ
    randomNumber = QtCore.QRandomGenerator.global_().bounded(0, 100) + 1
    if (randomNumber < 50):
        if (randomNumber < 33):
            return MyWidget1(parent)
        else:
            return MyWidget3(parent)
    else:
        return MyWidget2(parent)


class MyMainWindow(KDDockWidgets.MainWindow):
    s_count = 0
    s_menuCount = 0

    def __init__(self, uniqueName, options=KDDockWidgets.MainWindowOption_None, restoreIsRelative=False, affinityName="", parent=None):
        super().__init__(uniqueName, options, parent)
        self.m_restoreIsRelative = restoreIsRelative
        self.m_dockwidgets = []  # 全てのドックウィジェットを格納

        # ----------------------------------- メニュー ----------------------------------- #
        menubar = self.menuBar()
        fileMenu = QtWidgets.QMenu("File")
        self.m_toggleMenu = QtWidgets.QMenu("Toggle")
        menubar.addMenu(fileMenu)
        menubar.addMenu(self.m_toggleMenu)

        newAction = fileMenu.addAction("New DockWidget")
        newAction.triggered.connect(self._newDockWidget)

        saveLayoutAction = fileMenu.addAction("Save Layout")
        saveLayoutAction.triggered.connect(self._saveLayout)

        restoreLayoutAction = fileMenu.addAction("Restore Layout")
        restoreLayoutAction.triggered.connect(self._restoreLayout)

        closeAllAction = fileMenu.addAction("Close All")
        closeAllAction.triggered.connect(self._closeAll)

        layoutEqually = fileMenu.addAction("Layout Equally")  # 全てのサイズを均等に
        layoutEqually.triggered.connect(self.layoutEqually)

        quitAction = fileMenu.addAction("Quit")
        quitAction.triggered.connect(QtWidgets.QApplication.instance().quit)

        self.setAffinities([affinityName])
        self.createDockWidgets()
        # ---------------------------------------------------------------------------- #

    # ---------------------------------- メニュー用関数 --------------------------------- #

    def _newDockWidget(self):
        MyMainWindow.s_menuCount += 1
        w = newMyWidget(self)
        w.setGeometry(100, 100, 400, 400)
        dock = KDDockWidgets.DockWidget(
            "new dock %d" % (MyMainWindow.s_menuCount))
        dock.setWidget(w)
        dock.resize(600, 600)
        dock.show()
        self.m_dockwidgets.append(dock)

    def _saveLayout(self):
        #saver = KDDockWidgets.LayoutSaver()
        #result = saver.saveToFile("mylayout.json")
        #print("Saving layout to disk. Result=", result)
        print("Not available")

    def _restoreLayout(self):
        #options = KDDockWidgets.RestoreOption_None
        # if self.m_restoreIsRelative:
        #    options |= KDDockWidgets.RestoreOption_RelativeToMainWindow
        #saver = KDDockWidgets.LayoutSaver(options)
        # saver.restoreFromFile("mylayout.json")
        print("Not available")

    def _closeAll(self):
        for dw in self.m_dockwidgets:
            dw.close()
    # ---------------------------------------------------------------------------- #

    def createDockWidgets(self):  # 初期化

        # ---------------------------- newDockWidget loop ---------------------------- #
        for i in range(10):  # 10個作成
            if(i == 0):  # 0は閉じれない
                self.m_dockwidgets.append(
                    self.newDockWidget(nonColoseable=True))
            elif(i == 8):  # 8は最大サイズ指定
                self.m_dockwidgets.append(
                    self.newDockWidget(maxSize=(200, 200)))
            elif(i == 9):  # 9はドッキングできない
                self.m_dockwidgets.append(self.newDockWidget(nonDockable=True))
            else:
                self.m_dockwidgets.append(self.newDockWidget())
        # ---------------------------------------------------------------------------- #

        # addDockWidget() で メインウィンドウにアタッチ
        # ------------------------------------ 0番目 ----------------------------------- #
        # 初期状態を設定することも可 (initialOpts)
        initialOpts = KDDockWidgets.InitialOption(
            KDDockWidgets.InitialVisibilityOption.StartHidden, QtCore.QSize(500, 500))  # 初期状態非表示
        self.addDockWidget(
            self.m_dockwidgets[0], KDDockWidgets.Location_OnBottom, None, initialOpts)
        # ---------------------------------------------------------------------------- #

        self.addDockWidget(
            self.m_dockwidgets[1], KDDockWidgets.Location_OnRight, self.m_dockwidgets[0])  # 0番目の右に追加

        self.addDockWidget(
            self.m_dockwidgets[2], KDDockWidgets.Location_OnLeft)  # 左に追加
        self.addDockWidget(
            self.m_dockwidgets[3], KDDockWidgets.Location_OnBottom)  # 下に追加
        self.addDockWidget(
            self.m_dockwidgets[4], KDDockWidgets.Location_OnBottom)  # 下に追加

        # ------------------------------------ タブ ------------------------------------ #
        self.m_dockwidgets[3].addDockWidgetAsTab(
            self.m_dockwidgets[5])  # 5を3とタブ化

        # 6番目はaddDockWidget()してないのでメインウィンドウとは別ウィンドウになる
        self.m_dockwidgets[6].addDockWidgetAsTab(
            self.m_dockwidgets[7])  # 7を6とタブ化
        # ---------------------------------------------------------------------------- #

        # addDockWidgetToContainingWindow()で6があるウィンドウに追加
        self.m_dockwidgets[6].addDockWidgetToContainingWindow(
            self.m_dockwidgets[8], KDDockWidgets.Location_OnBottom)  # 下に追加

        floatingWindow = self.m_dockwidgets[6].window()  # 6のウィンドウを作成
        floatingWindow.move(100, 100)

    # ドックウィジェット作成
    def newDockWidget(self, nonColoseable: bool = False, nonDockable: bool = False, maxSize: tuple[int, int] = (0, 0)):
        now_num = len(self.m_dockwidgets)
        # ---------------------------------------------------------------------------- #
        # ----------------------------------- オプション ------------------------------ #
        options = KDDockWidgets.DockWidget.Option_None

        if nonColoseable:
            options |= KDDockWidgets.DockWidget.Option_NotClosable
        if nonDockable:
            options |= KDDockWidgets.DockWidget.Option_NotDockable

        dock = KDDockWidgets.DockWidget(
            "DockWidget #%d" % (now_num), options)  # DockWidget作成
        # ---------------------------------------------------------------------------- #

        # optional, just to show the feature. Pass -mi to the example to see incompatible dock widgets
        dock.setAffinities(self.affinities())

        if MyMainWindow.s_count == 1:
            dock.setIcon(QtGui.QIcon.fromTheme("mail-message"))

        # ---------------------------------------------------------------------------- #
        # -------------------------- DockWidgetに格納するWidget作成 ------------------- #
        myWidget = newMyWidget(self)
        if maxSize[0]*maxSize[0]:  # if not set
            myWidget.setMaximumSize(maxSize[0], maxSize[1])
        dock.setWidget(myWidget)
        # ---------------------------------------------------------------------------- #

        if dock.options() & KDDockWidgets.DockWidget.Option_NotDockable:
            dock.setTitle("DockWidget #%d (%s)" % (now_num, "non dockable"))
        else:
            dock.setTitle("DockWidget #%d" % (now_num))

        dock.resize(600, 600)
        self.m_toggleMenu.addAction(dock.toggleAction())
        MyMainWindow.s_count += 1
        return dock
