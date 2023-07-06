from flask import Flask,render_template,request,make_response

import os

import glob
flag=False
dict2={}
list=[]
list2=[]
qus=[]
ans=[]
app=Flask(__name__)
@app.route('/')
def index():
        if flag:
                print(flag)
                return render_template('admin.html')
        else:
                print(flag)
                return render_template('index.html')




@app.route('/search')
def search():
        import json
        from random import randint
        def random_question1():
                with open('quiz_data.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        return questions[random_index]['question'],questions[random_index]['answer']

        range1=random_question1()
        qus=range1[0]
        print(qus)
        ans=range1[1]
        if ans=='a':
                n=1
        else:
                n=2
        return render_template('search.html',result1=qus,m=n)

    


@app.route('/introduction',methods=["POST","GET"])
def introduction():

        return render_template('introduction.html')

@app.route('/fill')
def fill():
        import json
        import random
        file =open("h1.json","r", encoding='utf8')
        data=json.load(file)
        global list2
        global dict2
        global list
        list=[]
        list2=[]
        dict2={}
       
        l=data.keys()
        for i in l:
                list.append(i)
        
        for i in range(4):
                list2.append(random.choice(list))
       
        for i in list2:
                dict2[i]=data[i]
        
        n1=list2[0]
        n2=list2[1]
        n3=list2[2]
        n4=list2[3]
        print(list2)

        return render_template('fill.html',n1=n1,n2=n2,n3=n3,n4=n4)


@app.route('/match',methods=["POST","GET"])
def match():
        if request.method=='POST':
                import json
                import random
                file =open("h1.json","r", encoding='utf8')
                data=json.load(file)
                global list2
                global dict2
                global list
                print(list2)
               
                
                #print(dict2)
                n1=list2[0]
                n2=list2[1]
                n3=list2[2]
                n4=list2[3]
                #print(n1,n2,n3,n4)
                
                v1=request.form["v1"]
                v2=request.form["v2"]
                v3=request.form["v3"]
                v4=request.form["v4"]
             

                v1=v1.strip()
                v2=v2.strip()
                v3=v3.strip()
                v4=v4.strip()
                print(len(v1),len(v2),len(v3),len(v4))
                d1=dict2[n1][0]
                d2=dict2[n2][0]
                d3=dict2[n3][0]
                d4=dict2[n4][0]
                print(len(d1),len(d2),len(d3),len(d4))
                print(v1,v2,v3,v4)
                print(d1,d2,d3,d4)
                


                if v1==d1:
                        m1="ಸರಿ"
                else:
                        m1="ತಪ್ಪು"
                if v2==d2:
                        m2="ಸರಿ"
                else:
                        m2="ತಪ್ಪು"
                if v3==d3:
                        m3="ಸರಿ"
                else:
                        m3="ತಪ್ಪು"
                if v4==d4:
                        m4="ಸರಿ"
                else:
                        m4="ತಪ್ಪು"

                list2=[]
                dict2={}
                list=[]


        return render_template('fill.html',n1=n1,n2=n2,n3=n3,n4=n4,m1=d1,m2=d2,m3=d3,m4=d4,l1=v1,l2=v2,l3=v3,l4=v4,r1=m1,r2=m2,r3=m3,r4=m4)



@app.route('/test')
def test():
        return render_template('test.html')  



@app.route('/test1',methods=["POST","GET"])
def test1():
        if request.method=='POST':
                val=request.form["word"]
                import json
                file =open("hello.json","r", encoding='utf8')
                data=json.load(file)
                def translate(w):
                        if w in data:
                                return data[w]
                        else:
                                return "The term does not exist."
                output = translate(val)
                return render_template('test.html',result=output,message=val)  

@app.route('/find')
def find():
        import json
        from random import randint

        def random_question():

                with open('module2.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        ans=questions[random_index]
                        return ans

        range1=random_question()
        qus=range1['question']
        ans=range1['answer']
        qus=qus.split("\n")
        ans=ans.strip()        
        return render_template('find.html',q1=qus[0],q2=qus[1],a1=ans)          

 
                   



                   
      

@app.route('/hno',methods=["POST","GET"])
def hno():
        if request.method=='POST':
                import json
                from random import randint


                
                global qus
                global ans
                

                v1=request.form["v1"]
                v2=request.form["v2"]
                v3=request.form["v3"]
                v4=request.form["v4"]
                v5=request.form["v5"]

                s=qus.split("\n")
                e1=[]
                l1=[]
                l2=[]
                for i in s:
                        if i=="":
                                break
                        e=i.split("-")
                        e1.append(e)
                for i in e1:
                        l1.append(i[0])
                        l2.append(i[1])
                print(l1)
                print(l2)

                anew=ans.split(",")
                alist=[]
                for i in anew:
                        try:
                                anew1=i.split("-")
                                alist.append(anew1[1])
                        except:
                                pass
                print(alist)
                if v1==alist[0]:
                        m1="ಸರಿ"
                else:
                        m1="ತಪ್ಪು"
                if v2==alist[1]:
                        m2="ಸರಿ"
                else:
                        m2="ತಪ್ಪು"
                if v3==alist[2]:
                        m3="ಸರಿ"
                else:
                        m3="ತಪ್ಪು"
                if v4==alist[3]:
                        m4="ಸರಿ"
                else:
                        m4="ತಪ್ಪು"
                if v5==alist[4]:
                        m5="ಸರಿ"
                else:
                        m5="ತಪ್ಪು"        

                return render_template('hnotice.html',q1=l1[0],q2=l1[1],q3=l1[2],q4=l1[3],
                q5=l1[4],r1=l2[0],r2=l2[1],r3=l2[2],r4=l2[3],r5=l2[4],p1=alist[0],p2=alist[1],p3=alist[2],p4=alist[3],p5=alist[4],
                l1=v1,l2=v2,l3=v3,l4=v4,l5=v5,rr1=m1,rr2=m2,rr3=m3,rr4=m4,rr5=m5) 

        




        
       

@app.route('/hnotice')
def hnotice():
        import json
        from random import randint


        def random_question1():

                with open('MTF1.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        return questions[random_index]['question'],questions[random_index]['answer']

        range1=random_question1()
        global qus
        global ans
        qus=range1[0]
        ans=range1[1]

        s=qus.split("\n")
        e1=[]
        l1=[]
        l2=[]
        for i in s:
                if i=="":
                        break
                e=i.split("-")
                e1.append(e)
        for i in e1:
                l1.append(i[0])
                l2.append(i[1])
        print(l1)
        print(l2)

        anew=ans.split(",")
        alist=[]
        for i in anew:
                try:
                        anew1=i.split("-")
                        alist.append(anew1[1])
                except:
                        pass
        print(alist)

        return render_template('hnotice.html',q1=l1[0],q2=l1[1],q3=l1[2],q4=l1[3],q5=l1[4],r1=l2[0],r2=l2[1],r3=l2[2],r4=l2[3],r5=l2[4]) 




if __name__ == "__main__":
        app.run(debug=True)



flag=False
dict2={}
list=[]
list2=[]
qus=[]
ans=[]

@app.route('/indext')
def indext():
        if flag:
                print(flag)
                return render_template('admint.html')
        else:
                print(flag)
                return render_template('indext.html')




@app.route('/searcht')
def searcht():
        import json
        from random import randint
        def random_question1():
                with open('quiz_data.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        return questions[random_index]['question'],questions[random_index]['answer']

        range1=random_question1()
        qus=range1[0]
        print(qus)
        ans=range1[1]
        if ans=='a':
                n=1
        else:
                n=2
        return render_template('searcht.html',result1=qus,m=n)

    


@app.route('/introductiont',methods=["POST","GET"])
def introductiont():

        return render_template('introduction.html')

@app.route('/fillt')
def fillt():
        import json
        import random
        file =open("h1.json","r", encoding='utf8')
        data=json.load(file)
        global list2
        global dict2
        global list
        list=[]
        list2=[]
        dict2={}
       
        l=data.keys()
        for i in l:
                list.append(i)
        
        for i in range(4):
                list2.append(random.choice(list))
       
        for i in list2:
                dict2[i]=data[i]
        
        n1=list2[0]
        n2=list2[1]
        n3=list2[2]
        n4=list2[3]
        print(list2)

        return render_template('fillt.html',n1=n1,n2=n2,n3=n3,n4=n4)


@app.route('/matcht',methods=["POST","GET"])
def matcht():
        if request.method=='POST':
                import json
                import random
                file =open("h1.json","r", encoding='utf8')
                data=json.load(file)
                global list2
                global dict2
                global list
                print(list2)
               
                
                #print(dict2)
                n1=list2[0]
                n2=list2[1]
                n3=list2[2]
                n4=list2[3]
                #print(n1,n2,n3,n4)
                
                v1=request.form["v1"]
                v2=request.form["v2"]
                v3=request.form["v3"]
                v4=request.form["v4"]
             

                v1=v1.strip()
                v2=v2.strip()
                v3=v3.strip()
                v4=v4.strip()
                print(len(v1),len(v2),len(v3),len(v4))
                d1=dict2[n1][0]
                d2=dict2[n2][0]
                d3=dict2[n3][0]
                d4=dict2[n4][0]
                print(len(d1),len(d2),len(d3),len(d4))
                print(v1,v2,v3,v4)
                print(d1,d2,d3,d4)
                


                if v1==d1:
                        m1="ಸರಿ"
                else:
                        m1="ತಪ್ಪು"
                if v2==d2:
                        m2="ಸರಿ"
                else:
                        m2="ತಪ್ಪು"
                if v3==d3:
                        m3="ಸರಿ"
                else:
                        m3="ತಪ್ಪು"
                if v4==d4:
                        m4="ಸರಿ"
                else:
                        m4="ತಪ್ಪು"

                list2=[]
                dict2={}
                list=[]


        return render_template('fillt.html',n1=n1,n2=n2,n3=n3,n4=n4,m1=d1,m2=d2,m3=d3,m4=d4,l1=v1,l2=v2,l3=v3,l4=v4,r1=m1,r2=m2,r3=m3,r4=m4)



@app.route('/testt')
def testt():
        return render_template('testt.html')  



@app.route('/test1t',methods=["POST","GET"])
def test1t():
        if request.method=='POST':
                val=request.form["word"]
                import json
                file =open("hello.json","r", encoding='utf8')
                data=json.load(file)
                def translate(w):
                        if w in data:
                                return data[w]
                        else:
                                return "The term does not exist."
                output = translate(val)
                return render_template('testt.html',result=output,message=val)  

@app.route('/findt')
def findt():
        import json
        from random import randint

        def random_question():

                with open('module2.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        ans=questions[random_index]
                        return ans

        range1=random_question()
        qus=range1['question']
        ans=range1['answer']
        qus=qus.split("\n")
        ans=ans.strip()        
        return render_template('findt.html',q1=qus[0],q2=qus[1],a1=ans)          

 
                   



                   
      

@app.route('/hnot',methods=["POST","GET"])
def hnot():
        if request.method=='POST':
                import json
                from random import randint


                
                global qus
                global ans
                

                v1=request.form["v1"]
                v2=request.form["v2"]
                v3=request.form["v3"]
                v4=request.form["v4"]
                v5=request.form["v5"]

                s=qus.split("\n")
                e1=[]
                l1=[]
                l2=[]
                for i in s:
                        if i=="":
                                break
                        e=i.split("-")
                        e1.append(e)
                for i in e1:
                        l1.append(i[0])
                        l2.append(i[1])
                print(l1)
                print(l2)

                anew=ans.split(",")
                alist=[]
                for i in anew:
                        try:
                                anew1=i.split("-")
                                alist.append(anew1[1])
                        except:
                                pass
                print(alist)
                if v1==alist[0]:
                        m1="ಸರಿ"
                else:
                        m1="ತಪ್ಪು"
                if v2==alist[1]:
                        m2="ಸರಿ"
                else:
                        m2="ತಪ್ಪು"
                if v3==alist[2]:
                        m3="ಸರಿ"
                else:
                        m3="ತಪ್ಪು"
                if v4==alist[3]:
                        m4="ಸರಿ"
                else:
                        m4="ತಪ್ಪು"
                if v5==alist[4]:
                        m5="ಸರಿ"
                else:
                        m5="ತಪ್ಪು"        

                return render_template('hnoticet.html',q1=l1[0],q2=l1[1],q3=l1[2],q4=l1[3],
                q5=l1[4],r1=l2[0],r2=l2[1],r3=l2[2],r4=l2[3],r5=l2[4],p1=alist[0],p2=alist[1],p3=alist[2],p4=alist[3],p5=alist[4],
                l1=v1,l2=v2,l3=v3,l4=v4,l5=v5,rr1=m1,rr2=m2,rr3=m3,rr4=m4,rr5=m5) 

        




        
       

@app.route('/hnoticet')
def hnoticet():
        import json
        from random import randint


        def random_question1():

                with open('MTF1.json',encoding ='utf8') as fp:
                        data = json.load(fp)
                        questions = data["letters"]["part one"]["meem"]["questions"]
                        random_index = randint(0, len(questions)-1)
                        return questions[random_index]['question'],questions[random_index]['answer']

        range1=random_question1()
        global qus
        global ans
        qus=range1[0]
        ans=range1[1]

        s=qus.split("\n")
        e1=[]
        l1=[]
        l2=[]
        for i in s:
                if i=="":
                        break
                e=i.split("-")
                e1.append(e)
        for i in e1:
                l1.append(i[0])
                l2.append(i[1])
        print(l1)
        print(l2)

        anew=ans.split(",")
        alist=[]
        for i in anew:
                try:
                        anew1=i.split("-")
                        alist.append(anew1[1])
                except:
                        pass
        print(alist)

        return render_template('hnoticet.html',q1=l1[0],q2=l1[1],q3=l1[2],q4=l1[3],q5=l1[4],r1=l2[0],r2=l2[1],r3=l2[2],r4=l2[3],r5=l2[4]) 

