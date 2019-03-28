# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:49:33 2019

@author: Avinash
"""
import csv

def user_status():
    x = "1: Teacher"
    y = "2: Student"
    print (x);
    print (y);
    enter_data = input("Enter your Status: ")
    enter_data = int(enter_data)
    if enter_data == 1:
        teacher();
    else:
        student();
        
        
        
def teacher():
    Mylist = list()
    Mylist.append("1: Engineering")
    Mylist.append("2: Medical")
    print (Mylist)
    enter_data = input("Enter your field: ")
    enter_data = int(enter_data)
    if enter_data == 1:
        eng_Teacher();
    else:
        med_Teacher();
        
        
def student():
    Mylist = list()
    Mylist.append("1: Engineering")
    Mylist.append("2: Medical")
    print (Mylist)
    enter_data = input("Enter your field: ")
    enter_data = int(enter_data)
    if enter_data == 1:
        eng_Student();
    else:
        med_Student();
    

def eng_Student():
    output = []
    correct_answer = []
    count = 0
    ans_list = []
    f = open('engineering.csv')
    for line in f:
        cells = line.split(",")   
        output.append((cells[0], cells[1],cells[2], cells[3], cells[4], cells[5]))
        correct_answer.append((cells[6].replace('\n','')))
    f.close
    print("Your Answer must be in the form of abcd")    
    for i in range(1,len(output)):
        print(output[0][0]," : ",output[i][0])
        print(output[0][1]," : ",output[i][1])
        print(output[0][2]," : ",output[i][2])
        print(output[0][3]," : ",output[i][3])
        print(output[0][4]," : ",output[i][4])
        print(output[0][5]," : ",output[i][5])
        x = input("Enter your answer: ")
        print ("\n")
        ans_list.append(x)
    print ("\n")
    print("Your Answers are: ")
    print(ans_list)
    print("\n")
    print("The Correct Answers are: ")
    print(correct_answer)
    print("\n")
    for i in range(1,len(correct_answer)):
        if correct_answer[i]== ans_list[i-1]:
            count = count+1
    print("Your Correct Answers are: ")
    print(count)
    
    
def med_Student():
    output = []
    correct_answer = []
    count = 0
    ans_list = []
    f = open('medical.csv')
    for line in f:
        cells = line.split(",")   
        output.append((cells[0], cells[1],cells[2], cells[3], cells[4], cells[5]))
        correct_answer.append((cells[6].replace('\n','')))
    f.close    
    for i in range(1,len(output)):
        print(output[0][0]," : ",output[i][0])
        print(output[0][1]," : ",output[i][1])
        print(output[0][2]," : ",output[i][2])
        print(output[0][3]," : ",output[i][3])
        print(output[0][4]," : ",output[i][4])
        print(output[0][5]," : ",output[i][5])
        x = input("Enter your answer: ")
        print ("\n")
        ans_list.append(x)
    print ("\n")
    print("Your Answers are: ")
    print(ans_list)
    print("\n")
    print("The Correct Answers are: ")
    print(correct_answer)
    print("\n")
    for i in range(1,len(correct_answer)):
        if correct_answer[i]== ans_list[i-1]:
            count = count+1
    print("Your Correct Answers are: ")
    print(count)


def eng_Teacher():
    enter_many = input("Enter how many questions: ")
    with open('engineering.csv','a',newline='') as csvfile:
        #fieldnames = ['Question_Number','Question','Option_A','Option_B','Option_C','Option_D','Correct_option']
        writer = csv.writer(csvfile)
        
        #writer.writeheader;
        enter_many = int(enter_many)
        for i in range(0, enter_many):
            print("Question  Number", i+1);
            enter_question = input("Enter Question")
            option_A = input("Enter Option A: ")
            option_B = input("Enter Option B: ")
            option_C = input("Enter Option C: ")
            option_D = input("Enter Option D: ")
            correct_option = input("Enter correct Option: ")
            writer.writerow([i+1 ,enter_question,option_A,option_B,option_C,option_D,correct_option])
    user_status();
        
        
        
def med_Teacher():
    enter_many = input("Enter how many questions: ")
    with open('medical.csv','a',newline='') as csvfile:
        #fieldnames = ['Question_Number','Question','Option_A','Option_B','Option_C','Option_D','Correct_option']
        writer = csv.writer(csvfile)  
        #writer.writeheader;
        enter_many = int(enter_many)
        for i in range(0, enter_many):
            print("Question  Number", i+1);
            enter_question = input("Enter Question: ")
            option_A = input("Enter Option A: ")
            option_B = input("Enter Option B: ")
            option_C = input("Enter Option C: ")
            option_D = input("Enter Option D: ")
            correct_option = input("Enter correct Option: ")
            writer.writerow([i+1 ,enter_question,option_A,option_B,option_C,option_D,correct_option])
    user_status();
             
      

user_status();


      