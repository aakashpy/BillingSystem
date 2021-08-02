from SE import *
from dial import *
import datetime

veg_dict = {
    'Vada Pav': 'Rs. 30', 'Sabudana Vada': 'Rs. 50', 'Misal Pav': 'Rs. 70', 'Pav Bhaji': 'Rs. 100',
    'Seekh Kabab': 'Rs. 120', 'Tandoori Aloo': 'Rs. 120', 'Baby Corn Masala': 'Rs. 150',
    'Paneer Tikka': 'Rs. 170', 'Paneer Malai': 'Rs. 170',
    'Tandoori Mushroom': 'Rs. 150', 'Paneer Chilli': 'Rs. 180', 'Paneer 65': 'Rs. 190',
    'Paneer Crispy': 'Rs. 200',
    'Aloo Matar': 'Rs. 130', 'Dum Aloo': 'Rs. 110', 'Veg Makhani': 'Rs. 150', 'Veg Kolhapuri': 'Rs. 160',
    'Veg Kofta': 'Rs. 160', 'Veg Kadai': 'Rs. 150', 'Palak Paneer': 'Rs. 130', 'Paneer Kadai': 'Rs. 150',
    'Paneer Mushroom': 'Rs. 150', 'Paneer Makhni': 'Rs. 160', 'Paneer Burji': 'Rs. 150',
    'Dal Fry': 'Rs. 120', 'Jeera Rice': 'Rs. 130', 'Fried Rice': 'Rs. 140', 'Schezwan Rice': 'Rs. 150',
    'Veg Pulav': 'Rs. 150',
    'Veg Biryani': 'Rs. 170'
}
nveg_dict = {
    'Honey Chicken Dry': 'Rs. 170', 'Crispy Chicken': 'Rs. 175', 'Chicken Manchurian': 'rs. 160',
    'Chicken Crispy': 'Rs. 160', 'Chicken Finger': 'Rs. 160', 'Chicken Chilly': 'Rs. 155',
    'Roast Chicken': 'Rs. 170', 'Chicken 65': 'Rs. 160', 'Pepper Chicken': 'Rs. 160',
    'Chicken Schezwan': 'Rs. 160', 'Chicken Oyster': 'Rs. 170', 'Roasted Lamb': 'Rs. 165',
    'Chicken Mumtaaz': 'Rs. 195', 'Chicken Kolhapuri': 'Rs. 180', 'Chicken Lazeez': 'Rs. 175',
    'Chicken Kaleji': 'Rs. 180', 'Chicken Hyderabadi': 'Rs. 180', 'Chicken Masala(Dry)': 'Rs. 175',
    'Chicken Garlic': 'Rs. 170', 'Bhuna Chicken': 'Rs. 200', 'Egg Masala': 'Rs. 100', 'Egg Burji': 'Rs. 80',
    'Chilly Prawns(Dry)': 'Rs. 180', 'Chilly Prawns(Gravy)': 'Rs. 180',
    'Surmai Fry/Gravy': 'Rs. 300', 'Paplet Fry/Gravy': 'Rs. 350',
    'Chicken Tikka Biryani': 'Rs. 300', 'Chicken Dum Biryani': 'Rs. 300', 'Prawns Biryani': 'Rs. 340',
    'Mutton Dum Biryani': 'Rs. 350'
}

class Open:
    def __init__(self):
        ui.menucard1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        ui.menucard2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        ui.menucard2.cellDoubleClicked.connect(self.menuCard2)
        ui.menucard1.cellDoubleClicked.connect(self.menuCard1)
        ui.quantity.valueChanged.connect(self.show_result)
        ui.vegbtn.clicked.connect(self.raise1)
        ui.nvegbtn.clicked.connect(self.raise2)
        ui.add.clicked.connect(self.add)
        ui.Gbill.clicked.connect(self.generate)
        ui.Sbill.clicked.connect(self.billread)
        ui.clear.clicked.connect(self.rewrite)
        ui.menucard2.setRowCount(len(nveg_dict))
        ui.menucard1.setRowCount(len(veg_dict))
        i = 0
        for key, value in veg_dict.items():
            ui.menucard1.setItem(i, 0, QtWidgets.QTableWidgetItem(str(key)))
            ui.menucard1.setItem(i, 1, QtWidgets.QTableWidgetItem(str(value)))
            i += 1
        j = 0
        for key, value in nveg_dict.items():
            ui.menucard2.setItem(j, 0, QtWidgets.QTableWidgetItem(str(key)))
            ui.menucard2.setItem(j, 1, QtWidgets.QTableWidgetItem(str(value)))
            j += 1
        self.sample_string1 = '''       *********WELCOME TO SDMA RESTAURANT*********
                      The Taste that brings You back'''
        self.sample_string2 = '''  Address--403 Shaitan Street,Andher Nagar,Opposite to
                       Graveyard MALAD WEST 400095'''
        self.original_string = '''<p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'>*********<span style=\' font-weight:300; text-decoration: underline;\'>WELCOME TO SDMA RESTAURANT</span>*********</p>\n
                    <p align=\'center\' style=\'-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'><br /></p>\n
                    <p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'><span style=\' font-weight:300;\'>The Taste that brings You back</span></p>\n
                    <p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'><span style=\' font-weight:300;\'>---------------------------------------------------------</span></p>\n
                    <p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'>Address--<span style=\' font-size:300;\'>403 Shaitan Street,Andher Nagar,Opposite to Graveyard MALAD WEST 400095</span></p>\n
                    <p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'><span style=\' font-weight:300;\'>---------------------------------------------------------</span></p>\n
                    <p align=\'center\' style=\' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\'><span style=\' font-weight:300;\'>ITEMS --------------------------- Quantity -------- Price'''
        self.dup_string = self.original_string
        ui.billtext.setHtml(self.dup_string)
        self.totaltxt = "Total"
        self.end_txt = "Thank You"
        self.end_txt = self.end_txt.center(57, '\n')
        self.totalcosttxt = ""
        self.totalquantity = 0
        self.totalcost = 0
        self.final_text = ""
        self.a = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:300;\">"
        self.b = "</span></p>"
        self.billno = ""
        self.x = 0

    def add(self):
        if ui.orderitem.text():
            self.x=1
            c = ui.orderitem.text().ljust(35, '-')
            d = str(ui.quantity.value())
            e = str(ui.price.text().strip("Rs. ")).rjust(19, '-')
            c = self.a + c + " " + d + " " + e + self.b
            self.totalquantity = self.totalquantity + int(ui.quantity.value())
            self.totalcost = int(self.totalcost) + int(ui.price.text().strip("Rs. "))
            self.original_string = self.original_string + c + "</body></html>"
            ui.billtext.setHtml(self.original_string)

    def generate(self):
        if ui.name.text() == "":
            uid.label.setText("Please enter Customer Name!")
            FormD.show()
        else:
            if self.x==1:
                global Bill
                Bill = datetime.datetime.now().strftime("%f")
                self.totaltxt = self.totaltxt.ljust(35, '-')
                self.totalcost = "Rs. " + str(self.totalcost)
                self.totalcosttxt = self.totalcost.rjust(18, '-')
                self.totaltxt = self.a + self.totaltxt + " " + str(self.totalquantity) + " " + self.totalcosttxt + self.b
                self.original_string = self.original_string + '''<p  style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span>*********************************************************</span></p>\n''' + \
                                   self.totaltxt + '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;\'>Bill No. -> {}</span></p>'''.format(
                Bill) + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;\'>Customer Name-> {}</span></p>'''.format(
                                       ui.name.text()) + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;\'>Payment->Cash</span></p>''' + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;\'>Date-> {}</span></p>'''.format(
                                       datetime.datetime.now().strftime("%c")) + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span >---------------------------------------------------------</span></p>''' + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;\'>Thank You</span></p>''' + \
                                   '''<p align=\'center\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\' font-weight:300;font-style:italic;\'>Visit Us Again!!!</span></p>'''
                ui.billtext.setHtml(self.original_string)
                ui.Gbill.setEnabled(False)
                ui.add.setEnabled(False)
                self.billprint()
            else:
                uid.label.setText("Please add atleast one food item!")
                FormD.show()

    def rewrite(self):
        self.x=0
        ui.billtext.clear()
        ui.name.setText("")
        ui.price.setText("")
        ui.orderitem.setText("")
        ui.billno.setText("")
        self.original_string = self.dup_string
        self.totalcost = 0
        self.totalquantity = 0
        self.totaltxt = "Total"
        ui.Gbill.setEnabled(True)
        ui.add.setEnabled(True)
        ui.billtext.setHtml(self.original_string)

    def billread(self):
        if ui.billno.text():
            try:
                text = open('{}.txt'.format(ui.billno.text()))
                lines = text.read().splitlines()[7:]
                ui.billtext.setHtml("")
                ui.billtext.setHtml(self.original_string)
                for line in lines:
                    ui.billtext.append(line)
                text.close()
            except:
                uid.label.setText("No Data Found!")
                FormD.show()

    def billprint(self):
        f = open("{}.txt".format(Bill), "x")
        content = ui.billtext.toPlainText()
        f.write(content)
        f.close()

    def show_result(self):
        value = int(ui.quantity.value())
        item = ui.orderitem.text()
        try:
            originalvprice = veg_dict[item].strip("Rs. ")
            total = int(originalvprice) * value
            ui.price.setText("Rs. " + str(total))
        except:
            originalnvprice = nveg_dict[item].strip("Rs. ")
            total = int(originalnvprice) * value
            ui.price.setText("Rs. " + str(total))

    def menuCard1(self, row):
        items = ui.menucard1.item(row, 0).text()
        price = ui.menucard1.item(row, 1).text()
        ui.orderitem.setText(items)
        ui.price.setText(price)
        ui.quantity.setValue(1)

    def menuCard2(self, row):
        price = ui.menucard2.item(row, 1).text()
        items = ui.menucard2.item(row, 0).text()
        ui.orderitem.setText(items)
        ui.price.setText(price)
        ui.quantity.setValue(1)

    def raise1(self):
        ui.menucard2.lower()
        ui.quantity.setValue(1)

    def raise2(self):
        ui.menucard1.lower()
        ui.quantity.setValue(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    FormD = QtWidgets.QWidget()
    uid = Ui_FormD()
    uid.setupUi(FormD)
    gui = Open()
    sys.exit(app.exec_())
