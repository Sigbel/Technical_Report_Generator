# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avaliations.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Avaliations(object):
    def setupUi(self, Avaliations):
        Avaliations.setObjectName("Avaliations")
        Avaliations.resize(383, 615)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Avaliations.sizePolicy().hasHeightForWidth())
        Avaliations.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Avaliations)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.line_dim_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_dim_ava.setObjectName("line_dim_ava")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_dim_ava)
        self.line_act_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_act_ava.setObjectName("line_act_ava")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_act_ava)
        self.line_name_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_name_ava.setObjectName("line_name_ava")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_name_ava)
        self.line_func_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_func_ava.setObjectName("line_func_ava")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_func_ava)
        self.line_ref_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ref_ava.setObjectName("line_ref_ava")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_ref_ava)
        self.line_luxe_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_luxe_ava.setObjectName("line_luxe_ava")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.line_luxe_ava)
        self.line_luxa_ava = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_luxa_ava.sizePolicy().hasHeightForWidth())
        self.line_luxa_ava.setSizePolicy(sizePolicy)
        self.line_luxa_ava.setObjectName("line_luxa_ava")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.line_luxa_ava)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.line_amb_ava = QtWidgets.QLineEdit(self.centralwidget)
        self.line_amb_ava.setObjectName("line_amb_ava")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_amb_ava)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.text_obs_ava = QtWidgets.QTextEdit(self.centralwidget)
        self.text_obs_ava.setObjectName("text_obs_ava")
        self.verticalLayout_2.addWidget(self.text_obs_ava)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_att_ava = QtWidgets.QPushButton(self.centralwidget)
        self.btn_att_ava.setObjectName("btn_att_ava")
        self.horizontalLayout.addWidget(self.btn_att_ava)
        self.btn_add_ava = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_ava.setObjectName("btn_add_ava")
        self.horizontalLayout.addWidget(self.btn_add_ava)
        self.btn_cancel_ava = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel_ava.setObjectName("btn_cancel_ava")
        self.horizontalLayout.addWidget(self.btn_cancel_ava)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 50)
        self.verticalLayout.setStretch(2, 40)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        Avaliations.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Avaliations)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menubar.setObjectName("menubar")
        Avaliations.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Avaliations)
        self.statusbar.setObjectName("statusbar")
        Avaliations.setStatusBar(self.statusbar)

        self.retranslateUi(Avaliations)
        QtCore.QMetaObject.connectSlotsByName(Avaliations)
        Avaliations.setTabOrder(self.line_dim_ava, self.line_act_ava)
        Avaliations.setTabOrder(self.line_act_ava, self.line_name_ava)
        Avaliations.setTabOrder(self.line_name_ava, self.line_func_ava)
        Avaliations.setTabOrder(self.line_func_ava, self.line_amb_ava)
        Avaliations.setTabOrder(self.line_amb_ava, self.line_ref_ava)
        Avaliations.setTabOrder(self.line_ref_ava, self.line_luxe_ava)
        Avaliations.setTabOrder(self.line_luxe_ava, self.line_luxa_ava)
        Avaliations.setTabOrder(self.line_luxa_ava, self.text_obs_ava)
        Avaliations.setTabOrder(self.text_obs_ava, self.btn_att_ava)
        Avaliations.setTabOrder(self.btn_att_ava, self.btn_add_ava)
        Avaliations.setTabOrder(self.btn_add_ava, self.btn_cancel_ava)

    def retranslateUi(self, Avaliations):
        _translate = QtCore.QCoreApplication.translate
        Avaliations.setWindowTitle(_translate("Avaliations", "Avaliations"))
        self.label.setText(_translate("Avaliations", "Adicionar Avaliação"))
        self.label_2.setText(_translate("Avaliations", "Dimensão"))
        self.label_3.setText(_translate("Avaliations", "Atividade"))
        self.label_4.setText(_translate("Avaliations", "Nome do Colaborador"))
        self.label_5.setText(_translate("Avaliations", "Função"))
        self.label_6.setText(_translate("Avaliations", "Valor de Referência"))
        self.label_7.setText(_translate("Avaliations", "Lux (Estação)"))
        self.label_8.setText(_translate("Avaliations", "Lux (Ambiente)"))
        self.label_10.setText(_translate("Avaliations", "Ambiente"))
        self.label_9.setText(_translate("Avaliations", "Observações"))
        self.btn_att_ava.setText(_translate("Avaliations", "Atualizar"))
        self.btn_add_ava.setText(_translate("Avaliations", "Incluir"))
        self.btn_cancel_ava.setText(_translate("Avaliations", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Avaliations = QtWidgets.QMainWindow()
    ui = Ui_Avaliations()
    ui.setupUi(Avaliations)
    Avaliations.show()
    sys.exit(app.exec_())