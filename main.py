import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QTabBar
from PyQt5.QtCore import Qt
from interface.main_window import *
from interface.avaliations import *

class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        

        # DB initial configuration
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS clients ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            'r_name TEXT NOT NULL,'
            'cnpj TEXT NOT NULL,' 
            'activity CHAR(30) NOT NULL,' 
            'adress CHAR(50) NOT NULL,'
            'z_code CHAR(10) NOT NULL,' 
            'risk CHAR(10) NOT NULL,' 
            'n_fun INTENGER NOT NULL)')

        self.con.commit()
        self.cur.close()

        # -------- Inicialization --------
        self.tabWidget.setCurrentIndex(0)
        self.set_read_only(1, 'clients')
        self.set_read_only(1, 'report')
        self.btn_save_t1.setEnabled(0)
        self.btn_att_t1.setEnabled(0)

        # Temp variables
        self.old_tab = 0
        self.current_tab = 0

        # Hide tab bar
        self.tabBar = self.tabWidget.findChild(QTabBar)
        self.tabBar.hide()

        # Fill tables
            # Clients
        self.table_clients.repaint()
        self.update_tables_data()

        # -------- Buttons ---------
        # General Buttons
        self.btn_r_client.clicked.connect(lambda: self.select_tab_index(0))
        self.btn_pdf.clicked.connect(lambda: self.select_tab_index(1))
        # self.btn_quit.clicked.connect()

        # Client Buttons
        self.btn_save_t1.clicked.connect(lambda: self.insert_client())
        self.btn_cancel_t1.clicked.connect(lambda: self.clean_line_edits(1, True, True))
        self.btn_add_t1.clicked.connect(lambda: self.clean_line_edits(1, False, False))
        self.btn_edit_t1.clicked.connect(lambda: self.pre_update_client() )
        self.btn_att_t1.clicked.connect(lambda: self.update_client(1))
        self.btn_del_t1.clicked.connect(lambda: self.del_client())
        self.table_clients.clicked.connect(lambda: self.table_click(1, True))

        # Report Buttons
        # self.btn_editA_t2.clicked.connect()
        # self.btn_preP_t2.clicked.connect()
        # self.btn_gen_t2.clicked.connect()
        self.btn_addA_t2.clicked.connect(lambda: self.openWindow())
        # self.btn_editA_t2.clicked.connect()
        # self.btn_del_t2.clicked.connect()
        # self.btn_addI_t2.clicked.connect()
        # self.btn_altI_t2.clicked.connect()
        # self.btn_del_t2.clicked.connect()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Avaliations()
        self.ui.setupUi(self.window)
        self.window.setFixedSize(429,572)
        self.window.show()       

    def select_tab_index(self, value: int):
        self.tabWidget.setCurrentIndex(value)
        self.old_tab = self.current_tab
        self.current_tab = value   

    def table_click(self, mode, complete):
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()

        if mode == 1:
            index = (self.table_clients.selectionModel().currentIndex())
            value0 = index.sibling(index.row(), 0).data()
            value1 = index.sibling(index.row(), 1).data()
            value2 = index.sibling(index.row(), 2).data()
            value3 = index.sibling(index.row(), 3).data()
            value4 = index.sibling(index.row(), 4).data()
            value5 = index.sibling(index.row(), 5).data()
            value6 = index.sibling(index.row(), 6).data()
            value7 = index.sibling(index.row(), 7).data()
        
            consulta = f"""SELECT * FROM clients WHERE 
                id='{value0}' and r_name='{value1}' and cnpj='{value2}' and activity='{value3}' and
                adress='{value4}' and z_code='{value5}' and risk='{value6}' and n_fun='{value7}'"""

            self.cur.execute(consulta)
            data = self.cur.fetchall()

            if complete:
                self.line_r_name.setText(data[0][1])
                self.line_cnpj.setText(data[0][2])
                self.line_act.setText(data[0][3])
                self.line_adress.setText(data[0][4])
                self.line_zcode.setText(data[0][5])
                self.line_risk.setText(data[0][6])
                self.line_nfun.setText(str(data[0][7]))
            
                self.btn_save_t1.setEnabled(0)
                self.set_read_only(1, 'clients')

            self.cur.close()
            return data


    def update_tables(self, mode):
        if mode == 1:
            self.table_clients.repaint()
            self.update_tables_data()

    def update_tables_data(self):
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        self.cur.execute("""SELECT * FROM clients""")
        data = self.cur.fetchall()

        self.table_clients.setRowCount(len(data))
        self.table_clients.setColumnCount(8)   

        for i in range(0, len(data)):
            for j in range(0,8):
                self.table_clients.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        
        self.cur.close()

    def clean_line_edits(self, mode, read_only, cancel):
        local = ''
        if mode == 1:
            local = 'clients'
            fields = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
            self.line_risk, self.line_nfun]

            for i in fields:
                i.clear()

            if not cancel:
                self.btn_save_t1.setEnabled(1)
            else:
                self.btn_save_t1.setEnabled(0)

        elif mode == 2:
            local = 'report'
        
        if read_only == True:
            self.set_read_only(1, local)
        else:
            self.set_read_only(0, local)

    def set_read_only(self, mode, local):
        fields_c = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
            self.line_risk, self.line_nfun]
        fields_r = [self.line_obj, self.line_equip, self.line_met, self.line_proc]

        if local == 'clients':
            data = fields_c
        elif local == 'report':
            data = fields_r

        if mode == 1:
            for i in data:
                i.setReadOnly(True)
        elif mode == 0:
            for i in data:
                i.setReadOnly(False)
    
    def pre_update_client(self):
        self.btn_att_t1.setEnabled(1)
        self.set_read_only(0, 'clients')

    def show_popup(self, mode):
        msg = QMessageBox()
        if mode == 1:
            msg.setWindowTitle('Erro')
            msg.setText("Todos os campos devem ser preenchidos!")
            msg.setIcon(QMessageBox.Warning)
        elif mode == 2:
            msg.setWindowTitle('Informação')
            msg.setText("Cliente cadastrado com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 3:
            msg.setWindowTitle('Informação')
            msg.setText("Cadastro de cliente atualizado com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 4:
            msg.setWindowTitle('Erro')
            msg.setText("Selecione um registro antes de atualizar")
            msg.setIcon(QMessageBox.Warning)
        elif mode == 5:
            msg.setWindowTitle('Erro')
            msg.setText("Selecione um registro antes de deletar")
            msg.setIcon(QMessageBox.Warning)
        elif mode == 6:
            msg.setWindowTitle('Atenção')
            msg.setText('Esta ação resultará em exclusão do registro selecionado.')
            msg.setInformativeText('Deseja continuar?')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setIcon(QMessageBox.Warning)
        
        return msg.exec_()

    def insert_client(self):
        """Function to add clients to databank"""
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        # Fields Tests
        show = False
        fields = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
        self.line_risk, self.line_nfun]

        # Checks:
            # Blank Fields:
        for i in fields:
            if i.text() == '':
                show = True

        if show:
            self.show_popup(1)
            return

        self.cur.execute(f"""INSERT INTO clients (
            r_name, cnpj, activity, adress, z_code, risk, n_fun) VALUES (
                '{self.line_r_name.text()}',
                '{self.line_cnpj.text()}',
                '{self.line_act.text()}',
                '{self.line_adress.text()}',
                '{self.line_zcode.text()}',
                '{self.line_risk.text()}',
                '{self.line_nfun.text()}')""")

        self.con.commit()
        self.cur.close()

        self.update_tables(1)
        self.clean_line_edits(1, True, False)
        self.btn_save_t1.setEnabled(0)
        self.show_popup(2)

    def update_client(self, mode):
        """Function to uptade clients from databank"""
        fields = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
        self.line_risk, self.line_nfun]
        data = self.table_click(1, False)
        show = False

        # Blank fields check
        for i in fields:
            if i.text() == '':
                show = True
                break

        if show:
            self.show_popup(4)
            return
        
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        self.cur.execute(f"""UPDATE clients
                                SET r_name='{self.line_r_name.text()}',
                                cnpj='{self.line_cnpj.text()}',
                                activity='{self.line_act.text()}',
                                adress='{self.line_adress.text()}',
                                z_code='{self.line_zcode.text()}',
                                risk='{self.line_risk.text()}',
                                n_fun='{self.line_nfun.text()}'

                                WHERE id='{data[0][0]}'
                                """)

        self.con.commit()
        self.cur.close()

        self.update_tables(1)
        self.btn_att_t1.setEnabled(0)
        self.btn_save_t1.setEnabled(0)
        self.clean_line_edits(1, True, True)
        self.show_popup(3)

    def del_client(self):
        data = self.table_click(1, False)

        fields = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
        self.line_risk, self.line_nfun]
        data = self.table_click(1, False)
        show = False

        # Blank fields check
        for i in fields:
            if i.text() == '':
                show = True
                break

        if show:
            self.show_popup(5)
            return

        # User agreement check
        situation = self.show_popup(6)
        if situation == QMessageBox.Ok:
            pass
        else:
            return

        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        self.cur.execute(f"""DELETE FROM clients
                                WHERE id={data[0][0]}""")

        self.con.commit()
        self.cur.close()

        self.update_tables(1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = Main_Page()
    main_page.show()
    app.exec_()