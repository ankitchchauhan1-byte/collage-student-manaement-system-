import pandas as pd
import numpy as np
import mysql.connector 
try:
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="collage")

   
except :
    print("inable to connect")
cursor=conn.cursor()

      



class Record_Office:

    
    def __init__(self):
        self.registation_no=None
        self.name=''
        self.father_name=''
        self.mother_name=''
        self.total_fee=None
        self.left_fee=None
        self.course=''
        self.paid_fee=0
        self.year=None
        self.gender=None
        self.mobile_no=None
        self.date_of_birth=None
        self.email=None
        self.address=None

       
        self.data()
    def fee (self):
        if self.course=="btech":
            self.total_fee=100000
        elif self.course=="iti":
            self.total_fee=30000
        elif self.course=="bca":
            self.total_fee=57000
        elif self.course=="mca":
            self.total_fee=60000
        elif self.course=="mtech":
            self.total_fee= 70000
        elif self.course=="bsc":
            self.total_fee=25000
        elif self.course=="b.pharm":
            self.total_fee=80000
        elif self.course=="d.pharm":
            self.total_fee=70000
        elif self.course=="bsc nursing":
            self.total_fee=60000
        else:
            self.total_fee=int((input("enter total_fee")))

        return self.total_fee
    def data(self):
        user=input("""enter your choice:
                   enter 'add student' to add student
                   enter 'submit fee' to submit fee
                   enter 'veiw student all detail' to view student detail 
                   enter 'delete' to delete to record of the student 
                   enter 'update student detail' to update the student detail 
                   choose operation you perform :  """)
        

        if user=="add student":
            try:
                print("add student detail")
                
                
                self.registation_no=int(input("enter registation_no"))
                self.name=input("enter name")
                self.father_name=input("enter father name")
                self.mother_name=input("enter student mother name")
                self.course=input("enter course")
              
                self.fee()
               
                self.left_fee=self.total_fee
                self.year=input("enter admission year")  
                self.paid_fee=0   
                self.gender=input ("enter student gender")
                self.mobile_no=int(input ("enter student moblie no"))
                self.date_of_birth=input("enter date of birth")
                self.email=input("enter student email")
                self.address=input("enter student address")
                
                                  
            
                sql="insert into student (name,fee,course,year,registation_no,left_fee,paid_fee,gender,date_of_birth,email,address,father_name,mother_name,mobile_no) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(self.name,self.total_fee,self.course,self.year,self.registation_no,self.left_fee,self.paid_fee,self.gender,self.date_of_birth,self.email,self.address,self.father_name,self.mother_name,self.mobile_no)
                cursor.execute(sql,data)
                conn.commit()
                print("student add successfully")
            except Exception as e:
                print(e)
 
           
        elif user=="view student all detail":
            user=int(input("enter registation_no"))
            try:
                sql="select*from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                if row is None:
                    print("invalid registation_no")
                else:
                    print(row)
                    print("student detail")
            except:
                print("invalid registation_no")


        elif user=="delete":
           user=int(input("enter registation_no"))
           if cursor.rowcount ==None:
               print("invalid registation_no")
           else:
            sql="delete from student where registation_no=%s"
            cursor.execute(sql,(user,))
            conn.commit()
            print("delete successfully")
        elif user =="update student detail":
           
            user1=input("""how can i help you
                        1. to change the name press 'name'
                        2. to change the course press 'course'
                        3. to change the address press 'address'
                        enter your choice:  """)
            if user1=="name":
                user =int(input("enter old registation_no"))
                
                sql="select name from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                
                if row!=None:
                    name=row[0]
                    new_name=input("enter new name")
                    sql="update student set name =%s where registation_no=%s"
                    cursor.execute(sql,(new_name,user))
                    conn.commit()
                    print("name successully change")
                else:
                    print("registation no is not found")
            elif user1=='address':
                try:
                    user =int(input("enter old registation_no"))
                    
                    sql="select address  from student where registation_no=%s"
                    cursor.execute(sql,(user,))
                    row=cursor.fetchone()
                    
                    if row!=None:
                        address=row[0]
                        new_address=input("enter new address")
                        sql="update student set address =%s where registation_no=%s"
                        cursor.execute(sql,(new_address,user))
                        conn.commit()
                        print("address successully change")
                    else:
                        print("registation no is not found")
                except:
                    print("something went wrong")
            elif user1=='father_name':
                try:
                    user =int(input("enter old registation_no"))
                    
                    sql="select father_name  from student where registation_no=%s"
                    cursor.execute(sql,(user,))
                    row=cursor.fetchone()
                    
                    if row!=None:
                        address=row[0]
                        new_father_name=input("enter new father_name")
                        sql="update student set father_name =%s where registation_no=%s"
                        cursor.execute(sql,(new_father_name,user))
                        conn.commit()
                        print("father_name successully change")
                    else:
                        print("registation no is not found")
                except:
                        print("something went wrong")
            elif user1=='mother_name':
                user =int(input("enter old registation_no"))
                
                sql="select mother_name  from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                
                if row!=None:
                    address=row[0]
                    new_mother_name=input("enter new mother_name")
                    sql="update student set mother_name =%s where registation_no=%s"
                    cursor.execute(sql,(new_mother_name,user))
                    conn.commit()
                    print("mother_name successully change")
                else:
                    print("registation no is not found")

            elif user1=='mobile_no':
                user =int(input("enter old registation_no"))
                
                sql="select mobile_no  from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                
                if row!=None:
                    mobile_no=row[0]
                    new_address=input("enter new mobile_no")
                    sql="update student set mobile_no =%s where registation_no=%s"
                    cursor.execute(sql,(new_address,user))
                    conn.commit()
                    print( "mobile_no successully change")
                else:
                    print("registation no is not found")

            elif user1=='date_of_birth':
                user =int(input("enter old registation_no"))
                
                sql="select date_of_birth  from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                
                if row!=None:
                    date_of_birth=row[0]
                    new_date_of_birth=input("enter new date_of_birth")
                    sql="update student set date_of_birth =%s where registation_no=%s"
                    cursor.execute(sql,(new_date_of_birth,user))
                    conn.commit()
                    print("date_of_birth successully change")
                else:
                    print("registation no is not found")
            elif user1=="course":
                user =int(input("enter old registation_no"))
                sql="select paid_fee from student where registation_no=%s"
                cursor.execute(sql,(user,))
                row=cursor.fetchone()
                
                
                if row !=None:
                    paid_fee=row[0]
                    self.course=input("enter new course")
                    fee=paid_fee
                    new_fee=self.fee()
                    user3=new_fee-fee
                    sql="update student set course=%s,fee=%s,left_fee=%s,paid_fee=%s where registation_no=%s"
                    cursor.execute(sql,(self.course,new_fee,user3,fee,user))
                    conn.commit()
                    print("course change successfully")
        
                   
                    
                  
                else :
                    print("registation no is not found ")
            else:
                print("something went wrong")
        elif user =="submit fee":
            user_input=int(input("enter registatio_no"))
            sql="select * from student where registation_no=%s "
            cursor.execute(sql,(user_input,))
            row =cursor.fetchone()
            print(row)
            sql="select left_fee,paid_fee,fee from student where registation_no=%s "
            cursor.execute(sql,(user_input,))
            rows =cursor.fetchone()
            if rows!=None:
                left_fee,paid_fee,fee=rows
                submit_fee=int(input("enter fee amount"))
                if submit_fee>0:
                    print("data")
                   
                    if submit_fee>0 and submit_fee<=left_fee:
                        left_fee-=submit_fee
                        paid_fee+=submit_fee
                        
                        sql="update student set left_fee=%s,paid_fee=%s where registation_no=%s"
                    
                        data=(left_fee,paid_fee,user_input)
                        cursor.execute(sql,data)
                        conn.commit()
                        print("fee successfully submit")
                    else:
                        print("you submit extra fee. you need to pay this particular amount only",left_fee)
                        

                else :
                    print("invalid fee amount ")
            else:
                print("regitation_no not found")
        elif user=='order by':
            cursor.execute("select registation_no from")    
        else:

            print("somthing went wrong. Try again")
        
# c1=Record_Office()
class Hod(Record_Office):


    def __init__(self):
       
        query="select*from student "
        data=pd.read_sql(query,conn)
        data.drop(["fee","year","paid_fee","gender","date_of_birth","email","mother_name"],axis=1,inplace=True)
        
        data=data.sort_values(by="name").reset_index(drop=True)
        data.index+=1
        data["session1"]=None
        data["session2"]=None
        data["mid_term"]=None
        print(data)
        data.to_excel('student_under_hod.xlsx',index=True)
    def get_data(self):
        user =input("")
# c=Hod()
class class_teacher(Hod):
    def __init__(self):
        self.data_entry()
        # self.class_teacher_load_file()
        

    def hod_load_file(self):
        self.df=pd.read_excel("student_under_hod.xlsx",engine="openpyxl")
        self.df.index+=1

    def class_teacher_load_file(self):
        self.df=pd.read_excel("student_under_hod.xlsx",engine="openpyxl")
        self.df.drop(["registation_no","course","left_fee","address","mobile_no"],axis=1,inplace=True)
        self.df.index = self.df.index + 1
        print(self.df)
        
    def data_entry(self):
        
        user=input("""press 'sesssion1' to enter session1 marks
                      press 'session2' to enter session2 marks
                      press 'mid_term' to enter mid_term marks
                      enter your choice:  """) 
        if user =="session1":
            
            
            user1=int(input("""to enter marks at a particular position press "0"
                            to enter marks of all student "1"  """))
            
            self.class_teacher_load_file()
            
            if user1==0:
                try:
                    self.hod_load_file()
                    roll_no=int(input("enter roll_no"))
                    
                    if roll_no in self.df.index:
                        marks=int(input("enter student marks"))
                        
                        self.df.loc[roll_no,"session1"]=marks
                        print("marks updaate successfully")
                        self.df.to_excel("student_under_hod.xlsx", index=False)
                        
                        
                    else:
                        print("invalid roll_no")
                     
                except Exception as e:
                    print(e)
                
            else:
                try:
                    self.hod_load_file()
                    for i in self.df.index:
                        
                        self.value=input("enter session1 marks for row {i} (a) for absent ")
                        if self.value.lower()=="a":

                            self.df.loc[i,"session1"]=np.nan
                            continue
                        self.df.loc[i,"session1"]=int(self.value)
                    self.df.to_excel("student_under_hod.xlsx",index=False)
                        
                    
                except:
                    print("student marks already enter ")
        elif user=="session2":
              
           user1=int(input("""to enter marks at a particular position press "0"
                            to enter marks of all student "1"  """))
            
           self.class_teacher_load_file()
            
           if user1==0:
                try:
                    self.hod_load_file()
                    roll_no=int(input("enter roll_no"))
                    
                    if roll_no in self.df.index:
                        marks=int(input("enter student marks"))
                        
                        self.df.loc[roll_no,"session2"]=marks
                        print("marks updaate successfully")
                        self.df.to_excel("student_under_hod.xlsx", index=False)
                        
                        
                    else:
                        print("invalid roll_no")
                     
                except Exception as e:
                    print(e)
                
           else:
                try:
                    self.hod_load_file()
                    for i in self.df.index:
                        
                        self.value=input("enter session2 marks for row {i} (a) for absent ")
                        if self.value.lower()=="a":

                            self.df.loc[i,"session2"]=np.nan
                            continue
                        self.df.loc[i,"session2"]=int(self.value)
                    self.df.to_excel("student_under_hod.xlsx",index=False)
                        
                    
                except:
                    print("student marks already enter ")
         
            
        elif user=="mid_term":
              
          user1=int(input("""to enter marks at a particular position press "0"
                            to enter marks of all student "1"  """))
            
          self.class_teacher_load_file()
            
          if user1==0:
                try:
                    self.hod_load_file()
                    roll_no=int(input("enter roll_no"))
                    
                    if roll_no in self.df.index:
                        marks=int(input("enter student marks"))
                        
                        self.df.loc[roll_no,"mid_term"]=marks
                        print("marks updaate successfully")
                        self.df.to_excel("student_under_hod.xlsx", index=False)
                        
                        
                    else:
                        print("invalid roll_no")
                     
                except Exception as e:
                    print(e)
                
          else:
                try:
                    self.hod_load_file()
                    for i in self.df.index:
                        
                        self.value=input("enter mid_term marks for row {i} (a) for absent ")
                        if self.value.lower()=="a":

                            self.df.loc[i,"mid_term"]=np.nan
                            continue
                        self.df.loc[i,"mid_term"]=int(self.value)
                    self.df.to_excel("student_under_hod.xlsx",index=False)
                        
                    
                except:
                    print("student marks already enter ")

            
        else:
            print("somthing went wrong. try again")
     
 
c=class_teacher()


         


