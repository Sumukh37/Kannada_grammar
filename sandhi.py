from flask import Flask, render_template,request,make_response
from flask import request,jsonify
import pandas as pd
import random
import numpy as np
import glob
global first
global last
app = Flask(__name__)
from flask_table import Table, Col



#sandi
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('mainhome.html')
@app.route('/welcome',methods=['GET','POST'])
def welcome():
    return render_template('welcome.html')
@app.route('/page2',methods=['GET'])
def page2():
    return render_template('page2.html')
@app.route('/lopa',methods=['GET'])
def lopa():
    return render_template('lopa.html')
@app.route('/aagama',methods=['GET'])
def aagama():
    return render_template('aagama.html')
@app.route('/aadesha',methods=['GET'])
def aadesha():
    return render_template('aadesha.html')
@app.route('/abhyasamainpage',methods=['GET'])
def abhyasamainpage():
    return render_template('abhyasamainpage.html')
@app.route('/abhyasa',methods=['GET'])
def abhyasa():
    return render_template('abhyasa.html')
@app.route('/abhyasa1',methods=['GET'])
def abhyasa1():
    return render_template('abhyasa1.html')

@app.route('/merge',methods=['GET'])
def merge():
    return render_template('merge.html')
   
@app.route('/result',methods=['POST'])
def result():
	if request.method == 'POST':
		global first
		global last
		first= request.form['first']
		last= request.form['last']
		first=first.rstrip()
		last=last.rstrip()
		data=pd.read_csv("dict.csv",encoding = 'utf-8')
		u=0
		for i in data.word2:
			t1=data.w1[u]
			t2=data.w2[u]
			if t1==first and t2==last:
					#sandhi=i
					#split=data.word1[u]
					break
			u=u+1
		if first!=t1 or last!=t2:
					return render_template('notin.html')            
		elif first=="" or last=="":
					return render_template('empty.html')
		return render_template('mine.html',sandhi=i,split=data.word[u])
    

    
@app.route('/notin',methods=['POST'])
def add():
		text3= request.form['one']
		text4= request.form['two']
		text3=text1.rstrip()
		text4=text2.rstrip()
		if form.is_submitted():
			return render_template('merge.html')
		return render_template('merge.html')


@app.route("/fresult", methods= ['GET','POST'])
def fresult():
	global first
	global last
	output3 = first
	output4 = last    
	output2 = request.form['one']
	output1 = request.form['two']
   
   
   #final_output=output1 +"\t\t\t"+ output2 +"\t\t" + output3+'\t\t'+output4
	final_output=output1 +","+ output2 +"," + output3+","+output4
	if output1 != "":save(final_output)
	return render_template('merge.html')

def save(text, filepath=r'C:\Users\Madhurya Shankar\Desktop\Sandhi splitter\kannada sandi_merger_and_splitter\dict.csv'):
	lexicon_rows=[]
	lexicon = pd.read_csv(r'C:\Users\Madhurya Shankar\Desktop\Sandhi splitter\kannada sandi_merger_and_splitter\dict.csv')
	lexicon = lexicon.replace(np.nan,"", regex=True)
	for index, rows in lexicon.iterrows():
		row_stg=str(rows.word)+','+str(rows.word2)+','+str(rows.w1)+','+str(rows.w2)
		lexicon_rows.append(row_stg) 
    
	if text not in lexicon_rows:
		with open(r"C:\Users\Madhurya Shankar\Desktop\Sandhi splitter\kannada sandi_merger_and_splitter\dict.csv", "a",encoding='utf-8') as f:
			f.write(text)
			f.write('\n')
@app.route('/mcq',methods=['GET','POST'])
def mcq():
	data=pd.read_csv("mine.csv",encoding = 'utf-8')
	index=random.randint(2,35)
	text1=data.iloc[index]['word']
	text1=text1.rstrip()
	return render_template('mcq.html', text1=text1)

@app.route('/fill',methods=['POST'])

def fill():
	if request.method == 'POST':
		text1= request.form['two']
		text2= request.form['one']
		text1=text1.rstrip()
		text2=text2.rstrip()
		data=pd.read_csv("mine.csv",encoding = 'utf-8')
		u=0
		for i in data.word:
			t1=data.word2[u]
			#t2=data.w2[u]
			if i==text1:
				#sandhi=i
				break
			u=u+1
		if text2==t1:
			return render_template('fill.html')
		else:
			return render_template('correctans.html',ans=data.word2[u])

@app.route('/match',methods=['GET'])
def match():
	return render_template('merge.html')

@app.route('/matchres',methods=['POST'])
def matchres():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='2' and text2=='3' and text3=='1' and text4=='2' and text5=='1' and text6=='3':
			return render_template('matchres.html')
		else:
			return render_template('matcherror.html')
@app.route('/match1',methods=['GET'])
def match1():
	return render_template('match1.html')
@app.route('/matchres1',methods=['POST'])
def matchres1():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='3' and text2=='1' and text3=='2' and text4=='3' and text5=='3' and text6=='3':
			return render_template('matchres1.html')
		else:
			return render_template('matcherror1.html')

@app.route('/match2',methods=['GET'])
def match2():
	return render_template('match2.html')
@app.route('/matchres2',methods=['POST'])
def matchres2():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='2' and text2=='3' and text3=='1' and text4=='2' and text5=='3' and text6=='1':
			return render_template('matchres2.html')
		else:
			return render_template('matcherror2.html')

@app.route('/match3',methods=['GET'])
def match3():
	return render_template('match3.html')
@app.route('/matchres3',methods=['POST'])
def matchres3():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='3' and text2=='1' and text3=='2' and text4=='2' and text5=='2' and text6=='3':
			return render_template('matchres3.html')
		else:
			return render_template('matcherror3.html')

@app.route('/smcq',methods=['GET','POST'])
def smcq():
	data=pd.read_csv("mine.csv",encoding = 'utf-8')
	index=random.randint(2,35)
	text1=data.iloc[index]['word']
	text1=text1.rstrip()
	return render_template('smcq.html', text1=text1)

@app.route('/sfill',methods=['POST'])
def sfill():
	if request.method == 'POST':
		text1= request.form['two']
		text2= request.form['one']
		text3=request.form['three']
		text4=request.form['four']
		text1= text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		data=pd.read_csv("mine.csv",encoding = 'utf-8')
		u=0
		for i in data.word:
			t1=data.word2[u]
			#t2=data.w1[u]
			#t4=data.w2[u]
			#t2=data.w2[u]
			if i==text1:
				#sandhi=i
				break
			u=u+1
		if text3==data.word2[u] and text2==data.w1[u] and text4==data.w2[u]:  
			return render_template('sfill.html')
		elif text3==data.word2[u] and text2!=data.w1[u] or text4!=data.w2[u]:  
			return render_template('scorrectans.html',ans2=data.word2[u],ans1=data.w1[u],ans3=data.w2[u])
		elif text3!=data.word1[u] and text2==data.w1[u] and text4==data.w2[u]:  
			return render_template('scorrectans.html',ans2=data.word2[u],ans1=data.w1[u],ans3=data.w2[u])        
		else:
			return render_template('scorrectans.html',ans2=data.word2[u],ans1=data.w1[u],ans3=data.w2[u])            
@app.route('/sssplitter',methods=['GET'])
def sssplitter():
	return render_template('sssplitter.html')
@app.route('/sresult',methods=['POST'])
def sresult():
	if request.method == 'POST':
		text1= request.form['first']
		text1=text1.rstrip()
		data=pd.read_csv("mine.csv",encoding = 'utf-8')
		u=0
		for i in data.word:
			if i==text1:
				break
			else:
				u=u+1
		return render_template('sresult.html',sandhi=data.word2[u],split=data.word1[u])
                
@app.route('/shondisi',methods=['GET'])
def shondisi():
	return render_template('shondisi.html')

@app.route('/smatchres',methods=['POST'])
def smatchres():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='3' and text2=='1' and text3=='2' and text4=='2' and text5=='1' and text6=='3':
			return render_template('smatchres.html')
		else:
			return render_template('smatcherr.html')
@app.route('/shondisi1',methods=['GET'])
def shondisi1():
	return render_template('shondisi1.html')

@app.route('/smatchres1',methods=['POST'])
def smatchres1():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='2' and text2=='3' and text3=='1' and text4=='3' and text5=='3' and text6=='3':
			return render_template('smatchres1.html')
		else:
			return render_template('smatcherr1.html')
@app.route('/shondisi2',methods=['GET'])
def shondisi2():
	return render_template('shondisi2.html')
@app.route('/smatchres2',methods=['POST'])
def smatchres2():
	if request.method == 'POST':
		text1= request.form['1']
		text2= request.form['2']
		text3= request.form['3']
		text4= request.form['4']
		text5= request.form['5']
		text6= request.form['6']
		text1=text1.rstrip()
		text2=text2.rstrip()
		text3=text3.rstrip()
		text4=text4.rstrip()
		text5=text5.rstrip()
		text6=text6.rstrip()
		if text1=='3' and text2=='1' and text3=='2' and text4=='1' and text5=='2' and text6=='3':
			return render_template('smatchres2.html')
		else:
			return render_template('smatcherr2.html')    




#thatsama 


flag=False
dict2={}
list1=[]
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

        return render_template('introductiont.html')

@app.route('/fillt')
def fillt():
        import json
        import random
        file =open("h1.json","r", encoding='utf8')
        data=json.load(file)
        global list2
        global dict2
        global list1
        lis1t=[]
        list2=[]
        dict2={}
       
        l=data.keys()
        for i in l:
                list1.append(i)
        
        for i in range(4):
                list2.append(random.choice(list1))
       
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
                global list1
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
                list1=[]


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


#anyadeshipadagalu

@app.route('/homea', methods=['GET'])
def homea():
	return render_template("starta.html")

@app.route('/start1a', methods=['GET'])
def start1a():
	return render_template("start1a.html")

@app.route('/tandapa', methods=['GET'])
def tandapa():
	return render_template("tandapa.html")

@app.route('/welcomea', methods=['GET'])
def welcomea():
	return render_template("welcomea.html")

@app.route('/testa',methods=['GET'])
def testa(): 
	return render_template('test1a.html')

@app.route('/retrievea',methods=['POST'])
def retrievea() :
	with open('annotation.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()
	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	D2 = {"MA":"ಮರಾಠಿ","PA":"ಪಾರ್ಸಿ","AR":"ಅರೇಬಿಕ್","UR":"ಉರ್ದು","LA":"ಲ್ಯಾಟಿನ್","TU":"ತುಳು","FR":"ಫ್ರೆಂಚ್","PO":"ಪೋರ್ಚುಗೀಸ್","PE":"ಪರ್ಷಿಯನ್","EN":"ಇಂಗ್ಲಿಷ್"}
	word = request.form.get('testinput')
	
	if word in D:
		return "ಈ ಪದವನ್ನು "+D2[D[word]]+" ಭಾಷೆ ಇಂದ ಪಡೆಯಲಾಗಿದೆ "
	else:
		return "ಕ್ಷಮಿಸಿ ಬೇರೆ ಪದ ನೀಡಿ" 


@app.route('/identifyLanguagea', methods=['GET'])
def identifya():
	with open('annotation.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()

	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
	#line = line.translate(None, '\ufeff')
	#l[0] = l[0].replace('\\ufeff','')
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	word = random.choice(list(D.keys()))

	return render_template("identifya.html",word = word)

@app.route('/oddoneouta',methods=['GET'])
def oddoneouta() :
	with open('annotation.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()

	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
	#line = line.translate(None, '\ufeff')
	#l[0] = l[0].replace('\\ufeff','')
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	c=1
	D2 = {"MA":"ಮರಾಠಿ","PA":"ಪಾರ್ಸಿ","AR":"ಅರೇಬಿಕ್","UR":"ಉರ್ದು","LA":"ಲ್ಯಾಟಿನ್","TU":"ತುಳು","FR":"ಫ್ರೆಂಚ್","PO":"ಪೋರ್ಚುಗೀಸ್","PE":"ಪರ್ಷಿಯನ್","EN":"ಇಂಗ್ಲಿಷ್"}	
	word = random.choice(list(D.keys()))
	listofwords=[word]
	listofwordlan=[D[word]]
	while c!=3 :
		word = random.choice(list(D.keys()))
		if D[word] in listofwordlan :
			listofwordlan.append(D[word])
			listofwords.append(word)
			c+=1
	while True :
		word = random.choice(list(D.keys()))
		if D[word] in listofwordlan :
			continue
		else :
			listofwordlan.append(D[word])
			listofwords.append(word)
			break
	#listofwords.append(listofwordlan[-1])
	#Dummy={'words' : listofwords, 'correct' : listofwordlan[-1]}
	return render_template("oddoneouta.html",word= listofwords)

@app.route('/matcha', methods=['GET'])
def matcha():
	with open('annotation.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()

	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
	#line = line.translate(None, '\ufeff')
	#l[0] = l[0].replace('\\ufeff','')
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	D2 = {"MA":"ಮರಾಠಿ","PA":"ಪಾರ್ಸಿ","AR":"ಅರೇಬಿಕ್","UR":"ಉರ್ದು","LA":"ಲ್ಯಾಟಿನ್","TU":"ತುಳು","FR":"ಫ್ರೆಂಚ್","PO":"ಪೋರ್ಚುಗೀಸ್","PE":"ಪರ್ಷಿಯನ್","EN":"ಇಂಗ್ಲಿಷ್"}
	keys = list(D.keys())
	word1 = random.choice(keys)
	selected_words = [word1]
	L = [D2[D[word1]]]
	keys.remove(word1)
	for i in range(4):
		for j in keys:
			print("dsfjs",D[j],j)
			if D2[D[j]] in L:
				continue
			else:
				selected_words.append(j)
				L.append(D2[D[j]])
				keys.remove(j)
				break
	word2 = selected_words[1]
	word3 = selected_words[2]
	word4 = selected_words[3]
	word5 = selected_words[4]
	
	random.shuffle(L)
	value1 = L[0]
	value2 = L[1]
	value3 = L[2]
	value4 = L[3]		
	value5 = L[4]	
	return render_template("matcha.html",word1 = word1,word2 = word2, word3 = word3, word4 = word4,word5 = word5,value1 = value1,value2 = value2,value3 = value3,value4 = value4,value5 = value5)

@app.route('/oddoneoutvalia', methods=['POST'])
def oddoneoutvalia():
	typedword = request.form.get('enteredword')
	ans=request.form.getlist('word')
	"""s2 = ""
	for i in ans:
		s2 = s2 + i	
	ans = s2.split(',')"""
	ans=ans[0].strip('\t\n')
	ans=ans.split(',')
	print(ans)
	if typedword==ans[-1].rstrip(']') :
		return "ಸರಿಯಾದ ಉತ್ತರ"
	else :
		
		return "ಕ್ಷಮಿಸಿ ತಪ್ಪಾದ ಉತ್ತರ. ಸರಿಯಾದ ಉತ್ತರ : "+ans[-1].strip(']')

@app.route('/validatea', methods=['POST'])
def validatea():
	typeReq = request.form.get('type')
	with open('annotation.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()
	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	D2 = {"MA":"ಮರಾಠಿ","PA":"ಪಾರ್ಸಿ","AR":"ಅರೇಬಿಕ್","UR":"ಉರ್ದು","LA":"ಲ್ಯಾಟಿನ್","TU":"ತುಳು","FR":"ಫ್ರೆಂಚ್","PO":"ಪೋರ್ಚುಗೀಸ್","PE":"ಪರ್ಷಿಯನ್","EN":"ಇಂಗ್ಲಿಷ್"}

	if typeReq == 'identify':
		lang = request.form.get('lang').strip()
		word = request.form.get('word').strip()
		if D2[D[word]] == lang:
			return "ಅಭಿನಂದನೆಗಳು!! ನೀವು ಸರಿಯಾದ ಉತ್ತರವನ್ನು ನೀಡಿದ್ದೀರಿ"
		else:
			return "ಕ್ಷಮಿಸಿ ತಪ್ಪಾದ ಉತ್ತರ. ಸರಿಯಾದ ಉತ್ತರ : " +D2[D[word]]

	if typeReq == 'match':
		ans = request.form.getlist('ans')
		ans1 = ""
		for i in ans:
			ans1 = ans1 + i	
		ans = ans1.split(',')
		for i in range(5):
			ans[i] = int(ans[i])
		
		col1 = request.form.getlist('word')
		s1 = ""
		for i in col1:
			s1 = s1 + i	
		col1 = s1.split(',')
		#for i in range(5):
		#	col1[i] = int(col1[i])
		
		col2 = request.form.getlist('lang')
		s2 = ""
		for i in col2:
			s2 = s2 + i	
		col2 = s2.split(',')
		#for i in range(5):
		#	col2[i] = int(col2[i])
		#flag = 0
		correct_ans = []
		bad_chars = ['.', ' ', '1', "2","3","4","5"]
		for i in range(5):
			for j in col2[ans[i]-1]:
				if j in bad_chars:
					col2[ans[i]-1] = col2[ans[i]-1].replace(j,'')
			if col2[ans[i]-1] != D2[D[col1[i]]]:
				class ItemTable(Table):
					name = Col('')
					description = Col('')

				# Get some objects
				class Item(object):
					def __init__(self, name, description):
						self.name = name
						self.description = description
				items = [Item("ಕ್ಷಮಿಸಿ ನೀವು ತಪ್ಪು ಉತ್ತರ ನೀಡಿದ್ದೀರಿ. ","ಸರಿಯಾದ ಉತ್ತರ : "),
                Item("",""),
                Item("",""),
                Item("ಪದಗಳು", "ಭಾಷೆಗಳು"),
                Item("",""),
                Item("",""),
                Item(col1[0],D2[D[col1[0]]]),			
         		Item(col1[1],D2[D[col1[1]]]),
         		Item(col1[2],D2[D[col1[2]]]),
				Item(col1[3],D2[D[col1[3]]]),
				Item(col1[4],D2[D[col1[4]]])]
				table = ItemTable(items)
				return table.__html__()
				#flag = 1	
				#correct_ans.append(D2[D[col1[i]]]) 
			else:
				continue
		return "ಅಭಿನಂದನೆಗಳು!! ನೀವು ಸರಿಯಾದ ಉತ್ತರವನ್ನು ನೀಡಿದ್ದೀರಿ"
		#if flag == 1:
		#	return "Sorry!! Wrong answer"
		#else:
		#	return "You are correct!!"

#viruddha

@app.route('/homev', methods=['GET'])
def homev():
	return render_template("startv.html")


@app.route('/testv',methods=['GET'])
def testv(): 
	return render_template('test1v.html')

@app.route('/retrievev',methods=['POST'])
def retrievev() :
	with open('annotationv.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()
	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	
	word = request.form.get('testinput')
	
	if word in D:
		return "ಈ ಪದದ ವಿರುದ್ಧ ಪದ : "+D[word]
	else:
		return "ಕ್ಷಮಿಸಿ, ಬೇರೆ ಪದ ಪ್ರಯತ್ನಿಸಿ" 

@app.route('/identifyLanguagev',methods=['GET'])
def identifyv():
    with open('annotationv.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()

    D = {}
    count = 0
    for i in lines:
        l = i.split()
        #line = line.translate(None, '\ufeff')
        #l[0] = l[0].replace('\\ufeff', '')
        l[0] = l[0].strip('\ufeff')
        D[l[0]] = l[1]

    word = random.choice(list(D.keys()))
    num = random.randrange(1, 4)

    if num == 1:
        op1 = D[word]
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 2:
        op1 = random.choice(list(D.values()))
        op2 = D[word]
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 3:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 =  D[word]
        op4 = random.choice(list(D.values()))
    else:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = D[word]
    return render_template("identifyv.html",word=word,op1=op1, op2=op2, op3=op3, op4=op4)







@app.route('/validatev', methods=['POST'])
def validatev():
	typeReq = request.form.get('type')
	with open('annotationv.txt',encoding='utf-8') as f: #copy the lines in the file into a list as list elements
   		lines = f.read().splitlines()
	D = {}
	count = 0
	for i in lines : # read the lines into a dictionary	
		l = i.split()
		l[0] = l[0].strip('\\ufeff')
		D[l[0]] = l[1]
	

	if typeReq == 'identify':
		lang = request.form.get('lang').strip()
		word = request.form.get('word').strip()
		if D[word] == lang:
			return "ಅಭಿನಂದನೆಗಳು!! ನೀವು ಸರಿಯಾದ ಉತ್ತರವನ್ನು ನೀಡಿದ್ದೀರಿ"
		else:
			return "ಕ್ಷಮಿಸಿ ತಪ್ಪಾದ ಉತ್ತರ. ಸರಿಯಾದ ಉತ್ತರ : " + D[word]
		


#nudigattu

@app.route('/homen', methods=['GET'])
def homen():
	return render_template("startn.html")




@app.route('/identifyLanguagen',methods=['GET'])
def identifyn():
    with open('samplen.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()

    D = {}
    count = 0
    for line in lines:
        words = line.split(':')
        D[words[0]] = ' '.join(words[1:])  # Join remaining words with a space

    word = random.choice(list(D.keys()))
    
    num = random.randrange(1, 4)

    if num == 1:
        op1 = D[word]
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 2:
        op1 = random.choice(list(D.values()))
        op2 = D[word]
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 3:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 =  D[word]
        op4 = random.choice(list(D.values()))
    else:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = D[word]
    return render_template("identifyn.html",word=word,op1=op1,op2=op2,op3=op3,op4=op4)







@app.route('/validaten', methods=['POST'])
def validaten():
    typeReq = request.form.get('type')
    with open('samplen.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()
    D = {}
    count = 0
    for line in lines:
        words = line.split(':')
        D[words[0]] = ' '.join(words[1:])

    if typeReq == 'identify':
        lang = request.form.get('lang').strip()
        word = request.form.get('word').strip()
        if D[word] == lang:
            return "ಅಭಿನಂದನೆಗಳು!! ನೀವು ಸರಿಯಾದ ಉತ್ತರವನ್ನು ನೀಡಿದ್ದೀರಿ"
        else:
            return "ಕ್ಷಮಿಸಿ ನಿಮ್ಮ ಉತ್ತರ ತಪ್ಪು. ಸರಿಯಾದ ಉತ್ತರ :"+D[word]
	

#samanarthaka

@app.route('/homes', methods=['GET'])
def homes():
	return render_template("starts.html")




@app.route('/identifyLanguages',methods=['GET'])
def identifys():
    with open('samples.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()

    D = {}
    count = 0
    for line in lines:
        words = line.split('-')
        D[words[0]] = ' '.join(words[1:])  # Join remaining words with a space

    word = random.choice(list(D.keys()))
    
    num = random.randrange(1, 4)

    if num == 1:
        op1 = D[word]
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 2:
        op1 = random.choice(list(D.values()))
        op2 = D[word]
        op3 = random.choice(list(D.values()))
        op4 = random.choice(list(D.values()))
    elif num == 3:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 =  D[word]
        op4 = random.choice(list(D.values()))
    else:
        op1 = random.choice(list(D.values()))
        op2 = random.choice(list(D.values()))
        op3 = random.choice(list(D.values()))
        op4 = D[word]
    return render_template("identifys.html",word=word,op1=op1,op2=op2,op3=op3,op4=op4)







@app.route('/validates', methods=['POST'])
def validates():
    typeReq = request.form.get('type')
    with open('samples.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()
    D = {}
    count = 0
    for line in lines:
        words = line.split('-')
        D[words[0]] = ' '.join(words[1:])

    if typeReq == 'identify':
        lang = request.form.get('lang').strip()
        word = request.form.get('word').strip()
        if D[word] == lang:
            return "ಅಭಿನಂದನೆಗಳು!! ನೀವು ಸರಿಯಾದ ಉತ್ತರವನ್ನು ನೀಡಿದ್ದೀರಿ"
        else:
            return "ಕ್ಷಮಿಸಿ ನಿಮ್ಮ ಉತ್ತರ ತಪ್ಪು. ಸರಿಯಾದ ಉತ್ತರ :"+D[word]



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
