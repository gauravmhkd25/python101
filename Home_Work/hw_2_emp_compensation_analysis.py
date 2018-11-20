# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:03:05 2018

@author: MAHAKUD
"""
import csv
from operator import itemgetter

class File:
    
    fo = None
    filename = None 
    lines=[]
    of = None
    tsal = 0
    yr = ''
    
    def __init__(self,filename):
        self.filename = filename
        self.yr = filename.split('\\')[5] #to get the year from the folder path
        
        
    def openFile(self):#OF
        
        ## OF 1 LOAD and SAVE
        with open(self.filename,'r') as csv_file:#-------------with handles the closing of files when eof is encountered
            csv_reader = csv.reader(csv_file,delimiter=',') #csv_reader reads the file with delimiter
            for row in csv_reader:#--------------------------as csv_reader is not subscriptible, appending rows to a list                      
                self.lines.append(row)
          
        print(self.yr)
        
        ## OF 2 TOTAL SALARY
        for i in range(1,len(self.lines)):
            self.tsal+=float(self.lines[i][13])
        print(self.tsal)#total salary
   
    def yearChunk(self):#YC
        
        ## YC dividing csv file into chunks
        year = []
        for i in range(1,len(self.lines)):
            year.append(self.lines[i][1])
        
        yearCnt = {}
        for y in year:
            if y not in yearCnt.keys():
                yearCnt.update({y:year.count(y)})
                
        lines=[]
        for k in yearCnt.keys():
            for i in range(1,len(self.lines)):
                if k == self.lines[i][1]:
                    lines.append(self.lines[i][0:])
        
        print(yearCnt)
        
        for key in yearCnt.keys():
            with open(f'G:\python\python101\class_ex\emp comp results\R{key}\emp_comp_{key}.csv','w',newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for line in lines:
                    if line[1] == f'{key}':
                        csv_writer.writerow(line)
        
    
    def dataSet1(self): #salary allocated to each dept 
        
        ## DS1 1 DEPT CODE and DEPT
        deptDic={}
        for i in range(len(self.lines)):
            if self.lines[i][4] not in deptDic.keys():
                deptDic.update({self.lines[i][4]:self.lines[i][5]})
        
        ## DS1 2 SALARY FOR EACH DEPT
        salary = {}
        salr=[]
        salPer={}
        
        for key in deptDic.keys():
            count = 0
            salr=[]
            for i in range(1,len(self.lines)):
                if self.lines[i][4] == key:
                   salr.append(float(self.lines[i][13]))
                   count+=1
            salary.update({key:(round(sum(salr),5))})
        #print(salary) #OF 3 test
        #print(self.lines[1][14],self.lines[501][14])
        
        ##DS1 3 PERCENTAGE of SALARY ALLOCATED
        for k,v in salary.items():
            salPer.update({k:round((v/self.tsal)*100,2)})
        print(salPer)
        
        ##DS1 4 WRITE TO csv
        print(len(deptDic),len(salary),len(salPer))
        res=[]
        ke = [k for k in deptDic.keys()]
        nam = [n for n in deptDic.values()]
        sal = [s for s in salary.values()]
        per = [p for p in salPer.values()]
        
        
        for i in range(1,len(deptDic)):
            res.append([ke[i],nam[i],sal[i],per[i]])
            
        first=itemgetter(0)
        res=sorted(res,key=first)
        
        with open(f'G:\python\python101\class_ex\emp comp results\{self.yr}\dept_salary_{self.yr}.csv','w',newline='') as out_file:
           csv_w = csv.writer(out_file)
           header = ['dept code','dept name','salary','percentage']
           csv_w.writerow(header)
           for i in res:
               csv_w.writerow(i)
        
    def dataSet2(self):#salary allocated to each job family
        ## DS2 1 JOB FAMILY CODE : JOB FAMILY
        jobFam = {}
        for i in range(len(self.lines)):
            if self.lines[i][8] not in jobFam.keys():
                jobFam.update({self.lines[i][8]:self.lines[i][9]})
       
        ## DS2 2 JOB CODE : SALARY
        salary = {}
        salr=[]
        salPer={}
        
        for key in jobFam.keys():
            count = 0
            salr=[]
            for i in range(1,len(self.lines)):
                if self.lines[i][8] == key:
                   salr.append(float(self.lines[i][13]))
                   count+=1
            salary.update({key:(round(sum(salr),5))})
        
        ## DS2 3 JOBCODE : PERCENTAGE
        for k,v in salary.items():
            salPer.update({k:round((v/self.tsal)*100,2)})
            
        ## DS2 4 WRITE TO csv
        res=[]
        ke = [k for k in jobFam.keys()]
        nam = [n for n in jobFam.values()]
        sal = [s for s in salary.values()]
        per = [p for p in salPer.values()]
        
        for i in range(1,len(jobFam)):
            res.append([ke[i],nam[i],sal[i],per[i]])
        
        first=itemgetter(0)
        res=sorted(res,key=first)
        
        with open(f'G:\python\python101\class_ex\emp comp results\{self.yr}\job_family_salary_{self.yr}.csv','w',newline='') as out_file:
           csv_w = csv.writer(out_file)
           header = ['job family code','job family name','salary','percentage']
           csv_w.writerow(header)
           for i in res:
               csv_w.writerow(i)
        
    
    def dataSet3(self):#salary allocated to each job type
        ## DS3 1 JOB CODE : JOB TYPE
        jobType = {}
        for i in range(len(self.lines)):
            if self.lines[i][10] not in jobType.keys():
                jobType.update({self.lines[i][10]:self.lines[i][11]})
       
        ## DS3 2 JOB CODE : SALARY
        salary = {}
        salr=[] #to compute sum 
        salPer={}
        
        for key in jobType.keys():
            count = 0
            salr=[]
            for i in range(1,len(self.lines)):
                if self.lines[i][10] == key:
                   salr.append(float(self.lines[i][13]))
                   count+=1
            salary.update({key:(round(sum(salr),5))})
        
        ## DS3 4 JOBCODE : PERCENTAGE
        for k,v in salary.items():
            salPer.update({k:round((v/self.tsal)*100,2)})
        
        
            
        ## DS3 5 WRITE TO csv
        res=[]
        ke = [k for k in jobType.keys()]
        nam = [n for n in jobType.values()]
        sal = [s for s in salary.values()]
        per = [p for p in salPer.values()]
        
        for i in range(1,len(jobType)):
            res.append([ke[i],nam[i],sal[i],per[i]])
            
        first=itemgetter(0)
        res=sorted(res,key=first)
        
        with open(f'G:\python\python101\class_ex\emp comp results\{self.yr}\job_type_salary_{self.yr}.csv','w',newline='') as out_file:
           csv_w = csv.writer(out_file)
           header = ['job code','job type','salary','percentage']
           csv_w.writerow(header)
           for i in res:
               csv_w.writerow(i)
    
    def dataSet4(self): # to compute the percentage of salary allocation in each fiscal year.
        
       year = []
       for i in range(len(self.lines)):
               year.append(self.lines[i][2])
       yearcnt = {}
       for y in year:
           if y not in yearcnt.keys():
               yearcnt.update({y:year.count(y)})
    
       salary = {}
       salSum=[]
       salPer={}
       
       for key in yearcnt.keys():
            count = 0
            salSum=[]
            for i in range(1,len(self.lines)):
                if self.lines[i][1] == key: # keys: 2013,14,15,16,17
                   salSum.append(float(self.lines[i][13]))
                   count+=1
            salary.update({key:(round(sum(salSum),5))})
        
        
       for k,v in salary.items():
           salPer.update({k:round((v/self.tsal)*100,2)}) 
               
               
       print(yearcnt)
       print(salary)
       print(salPer)
       ## 
       res=[]
       ke = [k for k in yearcnt.keys()]
       sal = [s for s in salary.values()]
       per = [p for p in salPer.values()]
       
       for i in range(0,len(yearcnt)):
           res.append([ke[i],sal[i],per[i]])
           
       first=itemgetter(0)
       res=sorted(res,key=first)
        
       with open('hw_result4.csv','w',newline='') as out_file:
          csv_w = csv.writer(out_file)
          header = ['year','salary allocated','percentage']
          csv_w.writerow(header)
          for i in res: 
              csv_w.writerow(i) 
      
    
        
if __name__ == '__main__':
    
    f_obj=File("PATH\emp comp results\R2016\emp_comp_2016.csv")
    f_obj.openFile()
    f_obj.yearChunk()
    f_obj.dataSet1()
    f_obj.dataSet2()
    f_obj.dataSet3()
    #f_obj.dataSet4()