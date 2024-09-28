from datetime import datetime
class Address:
    def __init__(self,house_num,town,city):
        self.__house_num=house_num
        self.__town=town
        self.__city=city

    @property
    def house_num(self):
        return self.__house_num
    @house_num.setter
    def house_num(self,d):
        self.__house_num=d

    @property
    def town(self):
        return self.__town
    @town.setter
    def town(self,d):
        self.__town=d

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,d):
        self.__city=d

    def __str__(self):
        vstr=''
        vstr+=str(self.__house_num)
        vstr+=','
        vstr+=str(self.__town)
        vstr+=','
        vstr+=str(self.__city)
        return vstr

class Bill: 
    def __init__(self,bill_no,bill_date,customer_name,address,signature):
        self.__bill_no=bill_no
        self.__bill_date=bill_date
        self.__customer_name=customer_name
        self.__address=address
        self.__signature=signature
        self.__items=[]

    @property
    def bill_no(self):
        return self.__bill_no
    @bill_no.setter
    def bill_no(self,d):
        self.__bill_no=d

    @property
    def bill_date(self):
        return self.__bill_date
    @bill_date.setter
    def bill_date(self,d):
        self.__bill_date=d

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self,d):
        self.__customer_name=d

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,d):
        self.__address=d

    @property
    def signature(self):
        return self.__signature
    @signature.setter
    def signature(self,d):
        self.__signature=d


    def add_item(self,quantity,particulars,rate):
        item={'quantity':quantity,'particulars':particulars,'rate':rate}
        self.__items.append(item)

        
    def total(self):
        total=0
        for item in self.__items:
            total+=item["quantity"]*item["rate"]
        return total
        
    def __str__(self):
        vstr=''
        vstr+=' _______________________________________________________________________________'
        vstr+='\n|                                  MOBILO                                       |'
        vstr+='\n|                                MOBILE CITY                                    |'
        vstr+='\n|               DEALS IN ALL KINDS OF MOBILE SETS & ACCESSORIES                 |'
        vstr+='\n|                             Cell: 0315-0000000                                |'              
        vstr+='\n|_______________________________________________________________________________|'
        vstr+=f'\n| No: {str(self.__bill_no)}\t\t\t\t\t\t Date: {str(self.__bill_date)}  |'
        vstr+=' \n| Name: '
        vstr+=self.__customer_name
        vstr+='  \t\t\t\t\t\t\t        |\n| Address: '
        vstr+=str(self.__address)
        vstr+='  \t\t\t\t\t        |\n|_______________________________________________________________________________|'
        vstr+='\n|\tQty.\t|\tParticulars\t|\tRate\t|\tAmount\t\t|'
        vstr+='\n|-------------------------------------------------------------------------------|\n'
        total=0
        for item in self.__items:
            total+=item["quantity"]*item["rate"]
            vstr+=f'|\t{str(item["quantity"])}\t|\t{str(item["particulars"])}\t\t|\t{str(item["rate"])}\t|\t{str(item["quantity"]*item["rate"])}\t\t|\n'
        vstr+='|-------------------------------------------------------------------------------|\n'
        vstr+=f'|Signature: {self.__signature}\t\t\t Total: \t{total}\t\t|\n'
        vstr+='|_______________________________________________________________________________|\n'
        vstr+=f'|\tAddress: Basement # 2, Allah Wala Plaza, G-9 Markaz, Islamabad\t\t|'
        vstr+='\n|_______________________________________________________________________________|'
        return vstr

def main():
    address=Address('30-G','Gulberg','Lahore.')
    d=datetime(2023,10,20)
    date=d.strftime('%d-%B-%Y')
    b=Bill(10,date,'Haris Ahmad',address,'H^Aris__Ahma..._')
    b.add_item(10,'Mouse',1500)
    b.add_item(2,'LCD',5500)
    b.add_item(4,'Camera',55000)
    b.add_item(1,'Scanner',80000)
    b.add_item(2,'Printer',95000)
    print(b)

if __name__=="__main__":
    main()
