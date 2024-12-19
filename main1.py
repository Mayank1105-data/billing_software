from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile


class Bill_App:
    
    #=======================function declaraion==========================
    def __init__(self, start_number=1000):
        self.current_number = start_number

    def generate_bill_no(self):
        bill_no = f"Bill-{self.current_number:04d}"  # Formats the number as 4 digits (e.g., Bill-1000)
        self.current_number += 1
        return bill_no
        bill_gen = BillGenerator(start_number=1001)  # Start from Bill-1001

        for _ in range(5):  # Generate 5 bills
         print(bill_gen.generate_bill_no())
    def AddItem(self):
         self.n=self.prices.get()
         self.m=self.qty.get()*self.n
         self.l.append(self.m)
         if self.product.get()=="":
           messagebox.showerror("Error,Please Select the Product") 
         else:
           self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
           self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
           self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get())))*5/100)))
           self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get())))*5/100)))))

    def gen_bill(self):
         if self.product.get()=="":
           messagebox.showerror("Error,Please Add Item")
         else:
           text=self.textarea.get(10.0,(10.0+float(len(self.l))))
           self.welcome()
           self.textarea.insert(END,text)
           self.textarea.insert(END,"\n=============================================")
           self.textarea.insert(END,f"\nSub Amount:\t\t\t{self.sub_total.get()}")
           self.textarea.insert(END,f"\nTax Amount:\t\t\t{self.tax_input.get()}")
           self.textarea.insert(END,f"\nTotal Amount:\t\t\t{self.total.get()}")
           self.textarea.insert(END,"\n=============================================")

    def save_bill(self):
      op=messagebox.askyesno("save bill","Do you want to save this")
      if op>0:
           self.bill_data=self.textarea.get(1.0,END)
           f1=open('bills/'+str(self.bill_no.get())+".txt","w")
           f1.write(self.bill_data)
           op=messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} saved successfully")
           f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def price(self,event=""):
         if self.Combo_product.get()=="sandwich":
           self.Combo_price.config(value=self.price_sandwich)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="monaco":
           self.Combo_price.config(value=self.price_monaco)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="parle":
           self.Combo_price.config(value=self.price_parle)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="krackjack":
           self.Combo_price.config(value=self.price_krackjack)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="hideseek":
           self.Combo_price.config(value=self.price_hideseek)
           self.Combo_price.current(0)
           self.qty.set(1)


         if self.Combo_product.get()=="rice":
           self.Combo_price.config(value=self.price_rice)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="oats":
           self.Combo_price.config(value=self.price_oats)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="wheat":
           self.Combo_price.config(value=self.price_wheat)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="maize":
           self.Combo_price.config(value=self.price_maize)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="corn":
           self.Combo_price.config(value=self.price_corn)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="dairymilk":
           self.Combo_price.config(value=self.price_dairymilk)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="5star":
           self.Combo_price.config(value=self.price_5star)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="munch":
           self.Combo_price.config(value=self.price_munch)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="perk":
           self.Combo_price.config(value=self.price_perk)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="snickers":
           self.Combo_price.config(value=self.price_snickers)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="kurkure":
           self.Combo_price.config(value=self.price_kurkure)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="wafers":
           self.Combo_price.config(value=self.price_wafers)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="sev":
           self.Combo_price.config(value=self.price_sev)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="frymes":
           self.Combo_price.config(value=self.price_frymes)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="apple":
           self.Combo_price.config(value=self.price_apple)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="mango":
           self.Combo_price.config(value=self.price_mango)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="chickoo":
           self.Combo_price.config(value=self.price_chickoo)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="banana":
           self.Combo_price.config(value=self.price_banana)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="pineapple":
           self.Combo_price.config(value=self.price_pineapple)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="potato":
           self.Combo_price.config(value=self.price_potato)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="onion":
           self.Combo_price.config(value=self.price_onion)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="cabbage":
           self.Combo_price.config(value=self.price_cabbage)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="tomato":
           self.Combo_price.config(value=self.price_tomato)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="waghbakri":
           self.Combo_price.config(value=self.price_waghbakri)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="tulsi":
           self.Combo_price.config(value=self.price_tulsi)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="taj mahal":
           self.Combo_price.config(value=self.price_tajmahal)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="taaza":
           self.Combo_price.config(value=self.price_taaaza)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="nescafe":
           self.Combo_price.config(value=self.price_nescafe)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="brugold":
           self.Combo_price.config(value=self.price_brugold)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="sunshine":
           self.Combo_price.config(value=self.price_sunshine)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="dew":
           self.Combo_price.config(value=self.price_dew)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="redbull":
           self.Combo_price.config(value=self.price_redbull)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="fanta":
           self.Combo_price.config(value=self.price_fanta)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="thumpsup":
           self.Combo_price.config(value=self.price_thumpsup)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="smartflour":
           self.Combo_price.config(value=self.price_smartflour)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="celeste":
           self.Combo_price.config(value=self.price_celeste)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="lean cuisine":
           self.Combo_price.config(value=self.price_leancuisine)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="mcain":
           self.Combo_price.config(value=self.price_mcain)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="aviko":
           self.Combo_price.config(value=self.price_aviko)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="greenyard":
           self.Combo_price.config(value=self.price_greenyard)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="himalaya":
           self.Combo_price.config(value=self.price_himalaya)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="vim":
           self.Combo_price.config(value=self.price_vim)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="xpert":
           self.Combo_price.config(value=self.price_xpert)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="nip":
           self.Combo_price.config(value=self.price_nip)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="exobar":
           self.Combo_price.config(value=self.price_exobar)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="ariel":
           self.Combo_price.config(value=self.price_ariel)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="bounty":
           self.Combo_price.config(value=self.price_bounty)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="calgon":
           self.Combo_price.config(value=self.price_calgon)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="brasso":
           self.Combo_price.config(value=self.price_brasso)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="odonil":
           self.Combo_price.config(value=self.price_odonil)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="godrej":
           self.Combo_price.config(value=self.price_godrej)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="airwick":
           self.Combo_price.config(value=self.price_airwick)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="ambipur":
           self.Combo_price.config(value=self.price_ambipur)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="pears":
           self.Combo_price.config(value=self.price_pears)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="lux":
           self.Combo_price.config(value=self.price_lux)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="dove":
           self.Combo_price.config(value=self.price_dove)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="dettol":
           self.Combo_price.config(value=self.price_dettol)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="sunsilk":
           self.Combo_price.config(value=self.price_sunsilk)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="treseme":
           self.Combo_price.config(value=self.price_treseme)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="garnier":
           self.Combo_price.config(value=self.price_garnier)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="pantene":
           self.Combo_price.config(value=self.price_pantene)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="axe":
           self.Combo_price.config(value=self.price_axe)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="denver":
           self.Combo_price.config(value=self.price_denver)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="beardo":
           self.Combo_price.config(value=self.price_beardo)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="fogg":
           self.Combo_price.config(value=self.price_fogg)
           self.Combo_price.current(0)
           self.qty.set(1)

         if self.Combo_product.get()=="nivea":
           self.Combo_price.config(value=self.price_nivea)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="biotique":
           self.Combo_price.config(value=self.price_biotique)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="mamaearth":
           self.Combo_price.config(value=self.price_mamaearth)
           self.Combo_price.current(0)
           self.qty.set(1)
         if self.Combo_product.get()=="wow":
           self.Combo_price.config(value=self.price_wow)
           self.Combo_price.current(0)
           self.qty.set(1)

    def Categories(self,event=""):
        if self.Combo_category.get()=="foodcupboard":
           self.Combo_subcategory.config(value=self.subCatfoodcupboard)
           self.Combo_subcategory.current(0)

        if self.Combo_category.get()=="freshfood":
           self.Combo_subcategory.config(value=self.subCatfreshfood)
           self.Combo_subcategory.current(0)

        if self.Combo_category.get()=="Drinks":
           self.Combo_subcategory.config(value=self.subCatDrinks)
           self.Combo_subcategory.current(0)

        if self.Combo_category.get()=="frozenfood":
           self.Combo_subcategory.config(value=self.subCatfrozenfood)
           self.Combo_subcategory.current(0)

        if self.Combo_category.get()=="Household":
           self.Combo_subcategory.config(value=self.subCatHousehold)
           self.Combo_subcategory.current(0)

        if self.Combo_category.get()=="healthbeauty":
           self.Combo_subcategory.config(value=self.subCathealthbeauty)
           self.Combo_subcategory.current(0)

    def welcome(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"\t\tWelcome To Our Shop")
            self.textarea.insert(END,f"\nBill No:{self.bill_no.get()}")
            self.textarea.insert(END,f"\nCustomer Name:{self.c_name.get()}")
            self.textarea.insert(END,f"\nContact No:{self.c_phon.get()}")
            self.textarea.insert(END,f"\nCustomer Email:{self.c_email.get()}")

            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\nProducts\t\t\tQTY\t\t\tPrice")
            self.textarea.insert(END,"\n==================================================\n")

    def clear(self):
      self.textarea.delete(1.0,END)
      self.c_name.set("")
      self.c_phon.set("")
      self.c_email.set("")
      #x=random.randint(1,10000)
      #self.bill_no.set(str(x))
      self.search_bill.set("")
      self.product.set("")
      self.price.set(0)
      self.qty.set(0)
      self.l.set[0]
      self.total.set("")
      self.sub_total.set("")
      self.tax_input.set('')
      self.welcome()



    def find_bill(self):
      found="no"
      for i in os.listdir("bills/"):
        if i.split('.')[0]==self.search_bill.get():
          f1=open(f'bill/{i}','r')
          self.textarea.delete(1.0,END)
          for d in f1:
            self.textarea.insert(END,d)
            f1.close()
            found="yes"
      if found=='no':
          messagebox.showerror("Error","Invalid Bill No")
    
    def product_add(self,event=""):
       if self.Combo_subcategory.get()=="biscuits":
          self.Combo_product.config(value=self.biscuits)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="cereals":
          self.Combo_product.config(value=self.cereals)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="chocolates":
          self.Combo_product.config(value=self.chocolates)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="snacks":
          self.Combo_product.config(value=self.snacks)
          self.Combo_product.current(0)

         #fresh
       if self.Combo_subcategory.get()=="fruits":
          self.Combo_product.config(value=self.fruits)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="vegetables":
          self.Combo_product.config(value=self.vegetables)
          self.Combo_product.current(0)

            #drinks
       if self.Combo_subcategory.get()=="tea":
          self.Combo_product.config(value=self.tea)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="coffee":
          self.Combo_product.config(value=self.coffee)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="softdrinks":
          self.Combo_product.config(value=self.softdrinks)
          self.Combo_product.current(0)

            #frozen
       if self.Combo_subcategory.get()=="frozenpizza":
          self.Combo_product.config(value=self.frozenpizza)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="frozenchips":
          self.Combo_product.config(value=self.frozenchips)
          self.Combo_product.current(0)
           
      #household
       if self.Combo_subcategory.get()=="dishwashing":
           self.Combo_product.config(value=self.dishwashing)
           self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="roomfreshners":
           self.Combo_product.config(value=self.roomfreshners)
           self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="housecleaners":
          self.Combo_product.config(value=self.housecleaners)
          self.Combo_product.current(0)

           #health
       if self.Combo_subcategory.get()=="soap":
          self.Combo_product.config(value=self.soap)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="shampoo":
          self.Combo_product.config(value=self.shampoo)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="deodrants":
          self.Combo_product.config(value=self.deodrants)
          self.Combo_product.current(0)

       if self.Combo_subcategory.get()=="facewash":
          self.Combo_product.config(value=self.facewash)
          self.Combo_product.current(0)

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing software")

        #------------variables-----------------------
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1,10000)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar() 



        # product categories list
        self.Category=["Select Option","foodcupboard","freshfood","Drinks","frozenfood","Household","healthbeauty"]
       
        #subfoodcupboard
        self.subCatfoodcupboard=["biscuits","cereals","chocolates","snacks"]

        self.biscuits=["sandwich","monaco","parle","krackjack","hideseek"]
        self.price_sandwich=20
        self.price_monaco=10
        self.price_parle=5
        self.price_krackjack=10
        self.price_hideseek=35
        
        self.cereals=["rice","oats","wheat","maize","corn"]
        self.price_rice=39
        self.price_wheat=27
        self.price_oats=22
        self.price_maize=19
        self.price_corn=34
        
        self.chocolates=["dairymilk","5star","munch","perk","snickers"]
        self.price_dairymilk=30
        self.price_5star=7
        self.price_munch=3
        self.price_snickers=10
        self.price_perk=4
        
        self.snacks=["kurkure","wafers","frymes","sev"]
        self.price_kurkure=20
        self.price_wafers=10
        self.price_frymes=5
        self.price_sev=10

        #sub fresh food
        self.subCatfreshfood=["fruits","vegetables"]
        self.fruits=["apple","mango","banana","chickoo","pineapple"]
        self.price_apple=70
        self.price_mango=100
        self.price_banana=30
        self.price_chickoo=55
        self.price_pineapple=90
        self.vegetables=["potato","onion","cabbage","tomato"]
        self.price_potato=20
        self.price_onion=120
        self.price_cabbage=30
        self.price_tomato=20


        #sub drinks
        self.subCatDrinks=["tea","coffee","softdrinks"]
        self.tea=["waghbakri","tulsi","tajmahal","taaaza"]
        self.price_waghbakri=320
        self.price_tulsi=180
        self.price_tajmahal=325
        self.price_taaaza=190

        self.coffee=["nescafe","brugold","sunshine"]
        self.price_nescafe=5
        self.price_brugold=330
        self.price_sunshine=220
        
        self.softdrinks=["dew","redbull","fanta","thumpsup"]
        self.price_dew=20
        self.price_redbull=120
        self.price_fanta=20
        self.price_thumpsup=20

        self.subCatfrozenfood=["frozenpizza","frozenchips"]
        #sub frozen
        self.frozenpizza=["smartflour","celeste","leancuisine"]
        self.price_smartflour=170
        self.price_celeste=190
        self.price_leancuisine=145

        self.frozenchips=["mcain","aviko","himalaya","greenyard"]
        self.price_mcain=120
        self.price_aviko=170
        self.price_himalaya=270
        self.price_greenyard=210    

        self.subCatHousehold=["dishwashing","housecleaners","roomfreshners"]
        #sub household
        self.dishwashing=["vim","xpert","exobar","nip"]
        self.price_vim=123
        self.price_xpert=80
        self.price_exobar=50
        self.price_nip=120

        self.housecleaners=["ariel","bounty","calgon","brasso"]
        self.price_ariel=420
        self.price_bounty=210
        self.price_calgon=125
        self.price_brasso=410

        self.roomfreshners=["odonil","godrej","airwick","ambipur"]
        self.price_odonil=75
        self.price_godrej=95
        self.price_airwick=148
        self.price_ambipur=170

        self.subCathealthbeauty=["soap","shampoo","deodrants","facewash"]

        #sub health
        self.soap=["pears","lux","dove","dettol"]
        self.price_pears=20
        self.price_lux=10
        self.price_dove=15
        self.price_dettol=30

        self.shampoo=["sunsilk","treseme","garnier","pantene"]
        self.price_sunsilk=230
        self.price_treseme=330
        self.price_garnier=225
        self.price_pantene=160

        self.deodrants=["axe","denver","beardo","fogg"]
        self.price_axe=125
        self.price_denver=110
        self.price_beardo=99
        self.price_fogg=89

        self.facewash=["nivea","wow","biotique","mamaearth"]
        self.price_nivea=195
        self.price_wow=180
        self.price_biotique=125
        self.price_mamaearth=410





        # image1
        img=Image.open("img/b1.jpg") 
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)

        # image 2
        img_1=Image.open("img/girls.jpg") 
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)


        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=500,y=0,width=500,height=130)

        # image 3
        img_2=Image.open("img/girl1.jpg") 
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)


        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=1000,y=0,width=520,height=130)

        lb1_title=Label(self.root,text="Grocery Billing Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        lb1_title.place(x=0,y=130,width=1530,height=58)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=185,width=1530,height=620)

        # customer label frame
        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lb1_mob=Label(cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lb1CustName=Label(cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1CustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lb1Email=Label(cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #PRODUCT label frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #Category
        self.lb1category=Label(Product_Frame,text="Select Category",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1category.grid(row=0,column=0,sticky=W,padx=5,pady=2)
    
        self.Combo_category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_category['values'] = self.Category
        self.Combo_category.bind("<<ComboboxSelected>>",self.Categories)

        # sub category
        self.lb1subcategory=Label(Product_Frame,text="SubCategory",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
    
        self.Combo_subcategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24)
        self.Combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_subcategory.bind("<<ComboboxSelected>>",self.product_add)

        #product name
        self.lb1product=Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1product.grid(row=2,column=0,sticky=W,padx=5,pady=2)
    
        self.Combo_product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combo_product.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lb1price=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1price.grid(row=0,column=2,sticky=W,padx=5,pady=2)
    
        self.Combo_price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #quantity
        self.lb1qty=Label(Product_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
    
        self.Combo_qty=ttk.Combobox(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=24)
        self.Combo_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #middle frame
        Middle_frame=Frame(Main_Frame,bd=10)
        Middle_frame.place(x=10,y=150,width=980,height=340)

        img_4=Image.open("img/good.jpg") 
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lb1_img_4=Label(Middle_frame,image=self.photoimg_4)
        lb1_img_4.place(x=0,y=0,width=490,height=340)

        img_5=Image.open("img/mall.jpg") 
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lb1_img_5=Label(Middle_frame,image=self.photoimg_5)
        lb1_img_5.place(x=490,y=0,width=490,height=340)



        #search area
        search_Frame=LabelFrame(Main_Frame,bg="white",bd=2)
        search_Frame.place(x=1000,y=10,width=500,height=35)

        self.lb1bill=Label(search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lb1bill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_entry_search=ttk.Entry(search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.btnsearch=Button(search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15)
        self.btnsearch.grid(row=0,column=2)



        #right frame bill area
        Rightlabelframe=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        Rightlabelframe.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(Rightlabelframe,orient=VERTICAL)
        self.textarea=Text(Rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        # bill counter label frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        #
        self.lb1Subtotal=Label(Bottom_Frame,text="Subtotal",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1Subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubtotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.EntrySubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lb1tax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txttax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txttax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lb1Amounttotal=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lb1Amounttotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmounttotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txtAmounttotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.btnaddtocart=Button(Btn_Frame,height=2,command=self.AddItem,text="Add TO Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnaddtocart.grid(row=0,column=0)

        self.btngeneratebill=Button(Btn_Frame,height=2,command=self.gen_bill,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btngeneratebill.grid(row=0,column=1)

        self.btnsavebill=Button(Btn_Frame,height=2,command=self.save_bill,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnsavebill.grid(row=0,column=2)

        self.btnprint=Button(Btn_Frame,height=2,command=self.iprint,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnprint.grid(row=0,column=3)

        self.btnclear=Button(Btn_Frame,height=2,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnclear.grid(row=0,column=4)

        self.btnexit=Button(Btn_Frame,height=2,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnexit.grid(row=0,column=5)
        self.welcome()
        self.l=[]
       

       

        








        


if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()