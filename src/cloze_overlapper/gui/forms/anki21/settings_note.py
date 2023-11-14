# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'build/dist/designer/settings_note.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError:
    from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 217)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_1 = QtWidgets.QGridLayout()
        self.gridLayout_1.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_1.addWidget(self.label_4, 1, 2, 1, 1)
        self.sb_before = QtWidgets.QSpinBox(Dialog)
        self.sb_before.setMinimum(-1)
        self.sb_before.setObjectName("sb_before")
        self.gridLayout_1.addWidget(self.sb_before, 2, 0, 1, 1)
        self.sb_cloze = QtWidgets.QSpinBox(Dialog)
        self.sb_cloze.setMinimum(1)
        self.sb_cloze.setObjectName("sb_cloze")
        self.gridLayout_1.addWidget(self.sb_cloze, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_1.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_1.addWidget(self.label_3, 1, 1, 1, 1)
        self.sb_after = QtWidgets.QSpinBox(Dialog)
        self.sb_after.setMinimum(-1)
        self.sb_after.setObjectName("sb_after")
        self.gridLayout_1.addWidget(self.sb_after, 2, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout_1.addWidget(self.label_1, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb_ncf = QtWidgets.QCheckBox(Dialog)
        self.cb_ncf.setObjectName("cb_ncf")
        self.gridLayout_2.addWidget(self.cb_ncf, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 2)
        self.cb_ncl = QtWidgets.QCheckBox(Dialog)
        self.cb_ncl.setObjectName("cb_ncl")
        self.gridLayout_2.addWidget(self.cb_ncl, 2, 0, 1, 1)
        self.cb_incr = QtWidgets.QCheckBox(Dialog)
        self.cb_incr.setObjectName("cb_incr")
        self.gridLayout_2.addWidget(self.cb_incr, 1, 1, 1, 1)
        self.cb_gfc = QtWidgets.QCheckBox(Dialog)
        self.cb_gfc.setObjectName("cb_gfc")
        self.gridLayout_2.addWidget(self.cb_gfc, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.sb_before, self.sb_cloze)
        Dialog.setTabOrder(self.sb_cloze, self.sb_after)
        Dialog.setTabOrder(self.sb_after, self.cb_ncf)
        Dialog.setTabOrder(self.cb_ncf, self.cb_ncl)
        Dialog.setTabOrder(self.cb_ncl, self.cb_incr)
        Dialog.setTabOrder(self.cb_incr, self.cb_gfc)
        Dialog.setTabOrder(self.cb_gfc, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Overlapping Cloze Note Settings"))
        self.label_4.setText(_translate("Dialog", "Context After"))
        self.sb_before.setToolTip(_translate("Dialog", "Number of context cues before the prompt.<br>Set to -1/\'all\' to show all previous items as context"))
        self.sb_before.setSpecialValueText(_translate("Dialog", "all"))
        self.sb_cloze.setToolTip(_translate("Dialog", "Number of items to prompt for per card"))
        self.label_2.setText(_translate("Dialog", "Context Before"))
        self.label_3.setText(_translate("Dialog", "Cloze Prompts"))
        self.sb_after.setToolTip(_translate("Dialog", "Number of context cues after the prompt.<br>Set to -1/\'all\' to show all following items as context"))
        self.sb_after.setSpecialValueText(_translate("Dialog", "all"))
        self.label_1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Context Cues and Prompts</span></p></body></html>"))
        self.cb_ncf.setToolTip(_translate("Dialog", "Don\'t provide any context cues for first cloze item"))
        self.cb_ncf.setText(_translate("Dialog", "No cues for first item"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Other Cloze Generation Options</span></p></body></html>"))
        self.cb_ncl.setToolTip(_translate("Dialog", "Don\'t provide any context cues for last cloze item"))
        self.cb_ncl.setText(_translate("Dialog", "No cues for last item"))
        self.cb_incr.setToolTip(_translate("Dialog", "For notes that have multiple clozes revealed per card,<br>gradually build up to full reveal count at the start,<br>and vice-versa in the end"))
        self.cb_incr.setText(_translate("Dialog", "Gradual build-up/-down"))
        self.cb_gfc.setToolTip(_translate("Dialog", "Disable cards that prompt you for all items at once"))
        self.cb_gfc.setText(_translate("Dialog", "Don\'t generate full cloze"))
