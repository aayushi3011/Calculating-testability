# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:18 2019

@author: aayus
"""

fr=open('ckt_C17.txt','r')
info=fr.read()
print(info)


with open('ckt_C17.txt','r') as f:
    lines=[line.split() for line in f]
    #print(lines)
   int i
    d=[[1 for x in range(3)] for y in range(i+1)]
    #print(d)
    for i in range(len(lines)):
     
       
       
        if lines[i][2] == "inpt":
            node_pi=int(lines[i][0])
            #print(node_pi)
            d[i][0]=node_pi
            #print(d)
           
        elif lines[i][2] == "from":
            node_si=int(lines[i][0])
            node_pi=int(lines[i][3])
            d[i][0] = node_si
            d[i][1]=d[node_pi-1][1]
            d[i][2]=d[node_pi-1][2]

            #print(d)
           
           
        elif lines[i][2] == "nand":
            node_si=int(lines[i][0])
            node_1=int(lines[i][5])
            node_2=int(lines[i][6])
            #print(node_si)
            #print(node_1)
            #print(node_2)
            #print(d[node_1-1])
            #print(d[node_2-1])
            d[i][0] = node_si
            d[i][1]=d[node_1-1][2]+d[node_2-1][2]+1
            d[i][2]=min(d[node_1-1][1],d[node_2-1][1])+1
           
        elif lines[i][2] == "and":
            node_si=int(lines[i][0])
            node_1=int(lines[i][5])
            node_2=int(lines[i][6])
            #print(node_si)
            #print(node_1)
            #print(node_2)
            #print(d[node_1-1])
            #print(d[node_2-1])
            d[i][0] = node_si
            d[i][2]=d[node_1-1][2]+d[node_2-1][2]+1
            d[i][1]=min(d[node_1-1][1],d[node_2-1][1])+1
           
        elif lines[i][2] == "or":
            node_si=int(lines[i][0])
            node_1=int(lines[i][5])
            node_2=int(lines[i][6])
            #print(node_si)
            #print(node_1)
            #print(node_2)
            #print(d[node_1-1])
            #print(d[node_2-1])
            d[i][0] = node_si
            d[i][1]=d[node_1-1][1]+d[node_2-1][1]+1
            d[i][2]=min(d[node_1-1][2],d[node_2-1][2])+1
           
        elif lines[i][2] == "nor":
            node_si=int(lines[i][0])
            node_1=int(lines[i][5])
            node_2=int(lines[i][6])
            #print(node_si)
            #print(node_1)
            #print(node_2)
            #print(d[node_1-1])
            #print(d[node_2-1])
            d[i][0]=node_si
            d[i][2]=d[node_1-1][1]+d[node_2-1][1]+1
            d[i][1]=min(d[node_1-1][2],d[node_2-1][2])+1
        elif lines[i][2] == "not":
            node_si=int(lines[i][0])
            node_1=int(lines[i][5])

            #print(node_si)
            #print(node_1)
            #print(node_2)
            #print(d[node_1-1])
            #print(d[node_2-1])
            d[i][0] = node_si
            d[i][1]=d[node_1-1][1]+1
            d[i][2]=d[node_2-1][2]+1
           
            #print(d)
           
    print("controllability = \n",d)  
    x=[[1 for x in range(2)] for y in range(i+1)]
    for i in range(len(lines)):
        if lines[i][3] == "0":
            node_po=int(lines[i][0])
            #print(node_po)
            x[i][0]=node_po
            x[i][1]=0
           
            #print(x)
           
        if lines[i][4] == "2":
            node_1=int(lines[i][5])
            node_2=int(lines[i][6])
            #print(node_1)
            #print(node_2)
            x[node_1-1][0]=node_1
            x[node_2-1][0]=node_2
            if lines[i][2] == "nand" or "and":
                x[node_1-1][1]=x[i][1]+d[node_2-1][2]+1
                x[node_2-1][1]=x[i][1]+d[node_1-1][2]+1
                #print(x)
            if lines[i][2] == "or" or "nor":
                x[node_1-1][1]=x[i][1]+d[node_2-12 ][1]+1
                x[node_2-1][1]=x[i][1]+d[node_1-1][1]+1
                #print(x)    
            if lines[i][2] == "not":
                x[node_1-1][1]=x[i][1]+d[node_2-1][2]+1
               
                #print(x)
           
        elif lines[i][2] == "from":
            node_s=int(lines[i][3])
           
            node_s1=int(lines[i][0])
            if lines[i+1][2] == "from":
                node_s2=int(lines[i][0])
                x[node_s-1][0]=node_s
                x[node_s-1][1]=x[node_s1][1]
                #print(node_s)
                #print(node_s1)
                #print(node_s2)
                #print(x)
   
           
    print("observability= \n",x)