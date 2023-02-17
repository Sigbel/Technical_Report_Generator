import sys
import sqlite3
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QTabBar
from PyQt5.QtCore import Qt
from datetime import datetime
from interface.main_window import *
from interface.avaliations import *
from report_creator.report_template import PagesPDFGenerator
from reportlab.lib.pagesizes import A4

class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.dt = datetime.now()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Avaliations()
        self.ui.setupUi(self.window)
        self.avaliations = []
        
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

        self.cur.execute('CREATE TABLE IF NOT EXISTS report ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            'obj TEXT DEFAULT "lorem ipsum" NOT NULL,'
            'equip TEXT DEFAULT "lorem ipsum" NOT NULL,'
            'methods TEXT DEFAULT "lorem ipsum" NOT NULL,'
            'proc TEXT DEFAULT "lorem ipsum" NOT NULL)')

        self.con.commit()
        self.cur.close()

        # -------- Inicialization --------
        self.tabWidget.setCurrentIndex(0)
        self.set_read_only(1, 'clients')
        self.set_read_only(1, 'report')
        self.btn_save_t1.setEnabled(0)
        self.btn_att_t1.setEnabled(0)
        self.btn_save_t2.setEnabled(0)
        self.btn_cancel_t2.setEnabled(0)
        self.btn_quit.setEnabled(0)
        self.update_combo(1)
        self.date_r.setDate(self.dt)
        self.initial_inclusion()
        self.update_table2_buttons(0)

        if not os.path.isdir("pdfs"):
            os.makedirs("pdfs")

        # Temp variables
        self.old_tab = 0
        self.current_tab = 0
        self.index = 0

        # Hide tab bar
        self.tabBar = self.tabWidget.findChild(QTabBar)
        self.tabBar.hide()

        # Fill tables
            # Clients
        self.table_clients.repaint()
        self.update_tables_data(1)
            # Avalations
        self.table_clients.repaint()
        self.update_tables_data(2)

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
        self.btn_att_t1.clicked.connect(lambda: self.update_client())
        self.btn_del_t1.clicked.connect(lambda: self.del_client())
        self.table_clients.clicked.connect(lambda: self.table_click(1, True))

        # Report Buttons
        self.btn_editP_t2.clicked.connect(lambda: self.pre_update_report())
        self.btn_gen_t2.clicked.connect(lambda: self.generate_pdf())
        self.btn_addA_t2.clicked.connect(lambda: self.openWindow('ava'))
        self.btn_editA_t2.clicked.connect(lambda: self.pass_information('main'))
        self.btn_del_t2.clicked.connect(lambda: self.del_avaliation())
        # self.btn_addI_t2.clicked.connect()
        # self.btn_altI_t2.clicked.connect()
        # self.btn_dell_t2.clicked.connect()
        self.btn_save_t2.clicked.connect(lambda: self.update_report())
        self.btn_cancel_t2.clicked.connect(lambda: self.report_cancel())
        self.btn_prox_t2.clicked.connect(lambda: self.next_report())
        self.table_avaliations.clicked.connect(lambda: self.table_click(2, False))

        # Avaliation Buttons
        self.ui.btn_add_ava.clicked.connect(lambda: self.pass_information('ava'))
        self.ui.btn_cancel_ava.clicked.connect(lambda: self.avaliation_cancel())
        self.ui.btn_att_ava.clicked.connect(lambda: self.update_avaliation())

    def openWindow(self, window):
        if window == 'ava':
            self.ui.btn_add_ava.setEnabled(1)
            self.ui.btn_att_ava.setEnabled(0)
        elif window == 'main':
            self.ui.btn_att_ava.setEnabled(1)
        self.window.setFixedSize(429,572)
        self.window.show()       

    def select_tab_index(self, value):
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

        elif mode == 2:
            index = (self.table_avaliations.selectionModel().currentIndex())
            value0 = index.sibling(index.row(), 0).data()
            value1 = index.sibling(index.row(), 1).data()
            value2 = index.sibling(index.row(), 2).data()
            value3 = index.sibling(index.row(), 3).data()
            value4 = index.sibling(index.row(), 4).data()
            value5 = index.sibling(index.row(), 5).data()
            value6 = index.sibling(index.row(), 6).data()
            value7 = index.sibling(index.row(), 7).data()
            value8 = index.sibling(index.row(), 8).data()

            data = [value0, value1, value2, value3, value4, value5, value6, value7, value8]
            self.index = self.avaliations.index(data)

    def update_tables(self, mode):
        if mode == 1:
            self.table_clients.repaint()
            self.update_tables_data(1)
        elif mode == 2:
            self.table_avaliations.repaint()
            self.update_tables_data(2)

    def update_tables_data(self, mode):
        if mode == 1:
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
        elif mode == 2:
            self.table_avaliations.setRowCount(len(self.avaliations))
            self.table_avaliations.setColumnCount(9)   

            for i in range(0, len(self.avaliations)):
                for j in range(0,9):
                    self.table_avaliations.setItem(i, j, QTableWidgetItem(str(self.avaliations[i][j])))
            
    def update_combo(self, mode):
        self.combo_client.clear()
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        if mode == 1:
            self.cur.execute("SELECT r_name FROM clients")
            data = self.cur.fetchall()

            for i in data:
                for j in i:
                    self.combo_client.addItem(j)

        self.cur.close()

    def update_table2_buttons(self, enabled):
        if enabled == 0:
            self.btn_editA_t2.setEnabled(0)
            self.btn_del_t2.setEnabled(0)
        if enabled == 1:
            self.btn_editA_t2.setEnabled(1)
            self.btn_del_t2.setEnabled(1)

    def pre_update_client(self):
        self.btn_att_t1.setEnabled(1)
        self.set_read_only(0, 'clients')

    def pre_update_report(self):
        self.btn_save_t2.setEnabled(1)
        self.btn_cancel_t2.setEnabled(1)
        self.set_read_only(0, 'report')

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
            fields = [self.text_obj, self.text_equip, self.text_met, self.text_proc]

            for i in fields:
                i.clear()

            if not cancel:
                self.btn_save_t2.setEnabled(1)
            else:
                self.btn_save_t2.setEnabled(0)
        
        if read_only == True:
            self.set_read_only(1, local)
        else:
            self.set_read_only(0, local)

    def set_read_only(self, mode, local):
        fields_c = [self.line_r_name, self.line_cnpj, self.line_act, self.line_adress, self.line_zcode,
            self.line_risk, self.line_nfun]
        fields_r = [self.text_obj, self.text_equip, self.text_met, self.text_proc]

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
    
    def report_cancel(self):
        self.set_read_only(1, 'report')
        self.btn_save_t2.setEnabled(0)
        self.btn_cancel_t2.setEnabled(0)

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
        elif mode == 7:
            msg.setWindowTitle('Informação')
            msg.setText("Relatório atualizado com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 8:
            msg.setWindowTitle('Erro')
            msg.setText("Todos os campos devem ser preenchidos")
            msg.setIcon(QMessageBox.Warning)
        elif mode == 9:
            msg.setWindowTitle('Erro')
            msg.setText("Preencha o nome do arquivo!")
            msg.setIcon(QMessageBox.Warning)
        elif mode == 10:
            msg.setWindowTitle('Atenção')
            msg.setText('Esta ação resultará em exclusão da atividade selecionada.')
            msg.setInformativeText('Deseja continuar?')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setIcon(QMessageBox.Warning)
        elif mode == 11:
            msg.setWindowTitle('Informação')
            msg.setText("Avaliação incluida com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 12:
            msg.setWindowTitle('Informação')
            msg.setText("Avaliação atualizada com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 13:
            msg.setWindowTitle('Informação')
            msg.setText("Relatório reiniciado.")
            msg.setIcon(QMessageBox.Information)
        elif mode == 14:
            msg.setWindowTitle('Informação')
            msg.setText("Relatório gerado com sucesso!")
            msg.setIcon(QMessageBox.Information)
        elif mode == 15:
            msg.setWindowTitle('Erro')
            msg.setText("Os campos: Dimensão, Valor de Referência, Lux (Estação) e Lux (Ambiente)")
            msg.setInformativeText('Devem ser numéricos!')
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
        self.update_combo(1)
        self.clean_line_edits(1, True, False)
        self.btn_save_t1.setEnabled(0)
        self.show_popup(2)

    def update_client(self):
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
        self.update_combo(1)
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
        self.update_combo(1)

    def initial_inclusion(self):
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        self.cur.execute("""SELECT * FROM report""")
        data = self.cur.fetchall()

        if len(data) == 0:
            self.cur.execute("""INSERT INTO report (
            obj, equip, methods, proc) VALUES (
                'lorem ipsum', 'lorem ipsum', 'lorem ipsum', 'lorem ipsum')""")

            self.con.commit()
            
        self.cur.execute("""SELECT * FROM report""")
        data = self.cur.fetchall()

        self.cur.close()

        self.text_obj.setText(data[0][1])
        self.text_equip.setText(data[0][2])
        self.text_met.setText(data[0][3])
        self.text_proc.setText(data[0][4])

    def update_report(self):
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

        self.cur.execute(f"""UPDATE report
                                SET obj='{self.text_obj.toPlainText()}',
                                equip='{self.text_equip.toPlainText()}',
                                methods='{self.text_met.toPlainText()}',
                                proc='{self.text_proc.toPlainText()}'

                                WHERE id='1'
                                """)

        self.con.commit()
        self.cur.close()

        self.show_popup(7)
        self.btn_save_t2.setEnabled(0)
        self.btn_cancel_t2.setEnabled(0)
        self.set_read_only(1, 'report')

    def pass_information(self, window):
        if window == 'ava':
            fields = [self.ui.line_dim_ava, self.ui.line_act_ava, self.ui.line_name_ava, self.ui.line_func_ava,
                    self.ui.line_ref_ava, self.ui.line_luxe_ava, self.ui.line_luxa_ava, self.ui.line_amb_ava]
            show = False
            test = ''

            # Blank fields text
            for i in fields:
                if i.text() == '':
                    show = True
                    test = 'blank'

            # Numeric fields
            n_fields = [self.ui.line_dim_ava, self.ui.line_ref_ava, self.ui.line_luxa_ava, self.ui.line_luxe_ava]
            for i in n_fields:
                if i.text().isnumeric() == False:
                    show = True
                    test = 'n_field'
            
            if show:
                if test == 'blank':
                    self.show_popup(8)
                elif test == 'n_field':
                    self.show_popup(15)    
                return

            self.avaliations.append([
                self.ui.line_dim_ava.text(),
                self.ui.line_act_ava.text(),
                self.ui.line_name_ava.text(),
                self.ui.line_func_ava.text(),
                self.ui.line_ref_ava.text(),
                self.ui.line_luxe_ava.text(),
                self.ui.line_luxa_ava.text(),
                self.ui.line_amb_ava.text(),
                self.ui.text_obs_ava.toPlainText(),
            ])
            
            self.table_clients.repaint()
            self.update_tables_data(2)

            for i in fields:
                i.clear()
            self.ui.text_obs_ava.clear()

            self.window.close()

            self.show_popup(11)
            self.update_table2_buttons(1)

        elif window == 'main':
            list_t = self.avaliations[self.index]

            self.ui.line_dim_ava.setText(list_t[0])
            self.ui.line_act_ava.setText(list_t[1])
            self.ui.line_name_ava.setText(list_t[2])
            self.ui.line_func_ava.setText(list_t[3])
            self.ui.line_ref_ava.setText(list_t[4])
            self.ui.line_luxe_ava.setText(list_t[5])
            self.ui.line_luxa_ava.setText(list_t[6])
            self.ui.line_amb_ava.setText(list_t[7])
            self.ui.text_obs_ava.setText(list_t[8])
            
            self.ui.btn_add_ava.setEnabled(0)
            self.openWindow('main')

    def avaliation_cancel(self):
        fields = [self.ui.line_dim_ava, self.ui.line_act_ava, self.ui.line_name_ava, self.ui.line_func_ava,
                self.ui.line_ref_ava, self.ui.line_luxe_ava, self.ui.line_luxa_ava, self.ui.line_amb_ava]
        
        for i in fields:
            i.clear()
        self.ui.text_obs_ava.clear()

        self.window.close()
    
    def update_avaliation(self):
        fields = [self.ui.line_dim_ava, self.ui.line_act_ava, self.ui.line_name_ava, self.ui.line_func_ava,
                    self.ui.line_ref_ava, self.ui.line_luxe_ava, self.ui.line_luxa_ava, self.ui.line_amb_ava]
        list_t = [
                self.ui.line_dim_ava.text(),
                self.ui.line_act_ava.text(),
                self.ui.line_name_ava.text(),
                self.ui.line_func_ava.text(),
                self.ui.line_ref_ava.text(),
                self.ui.line_luxe_ava.text(),
                self.ui.line_luxa_ava.text(),
                self.ui.line_amb_ava.text(),
                self.ui.text_obs_ava.toPlainText(),
            ]
        
        self.avaliations.pop(self.index)
        self.avaliations.insert(self.index, list_t)

        self.table_clients.repaint()
        self.update_tables_data(2)

        for i in fields:
            i.clear()
        self.ui.text_obs_ava.clear()

        self.window.close()

    def del_avaliation(self):
        # User agreement check
        situation = self.show_popup(10)
        if situation == QMessageBox.Ok:
            pass
        else:
            return

        self.avaliations.pop(self.index)

        if len(self.avaliations) == 0:
            self.update_table2_buttons(0)

        self.table_clients.repaint()
        self.update_tables_data(2)

    def generate_pdf(self):
        show = False
        # Tests 
            # Blank Field (PDF Name)
        if self.line_pdfname_t2.text() == '':
            show = True

        if show:
            self.show_popup(9)
            return

        # formating name
        text = 'pdfs/' + self.line_pdfname_t2.text() + '.pdf'
        
        # Number of pages
        page_counter = 2 + len(self.avaliations)

        self.pdf = PagesPDFGenerator(
            self.avaliations, 
            self.line_cab_t2.text(),
            self.combo_client.currentText(),
            text, 
            pagesize=A4)

        for i in range(page_counter):
            self.pdf.showPage()
        self.pdf.save()

        self.show_popup(14)

    def next_report(self):
        self.avaliations = []
        self.line_pdfname_t2.setText('')

        self.table_clients.repaint()
        self.update_tables_data(2)

        self.show_popup(13)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = Main_Page()
    main_page.show()
    app.exec_()