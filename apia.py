import flask
import random
from flask import request, jsonify,render_template
from flask_table import Table, Col


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return render_template("start.html")

@app.route('/start1', methods=['GET'])
def start1():
	return render_template("start1.html")

@app.route('/tandap', methods=['GET'])
def tandap():
	return render_template("tandap.html")

@app.route('/welcome', methods=['GET'])
def welcome():
	return render_template("welcome.html")

@app.route('/test',methods=['GET'])
def test(): 
	return render_template('test1.html')

@app.route('/retrieve',methods=['POST'])
def retrieve() :
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
		return "ಈ ಪದವನ್ನು ಕನ್ನಡದಿಂದ ತೆಗೆದುಕೊಳ್ಳಲಾಗಿದೆ" 


@app.route('/identifyLanguage', methods=['GET'])
def identify():
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

	return render_template("identify.html",word = word)

@app.route('/oddoneout',methods=['GET'])
def oddoneout() :
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
	return render_template("oddoneout.html",word= listofwords)

@app.route('/match', methods=['GET'])
def match():
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
	return render_template("match.html",word1 = word1,word2 = word2, word3 = word3, word4 = word4,word5 = word5,value1 = value1,value2 = value2,value3 = value3,value4 = value4,value5 = value5)

@app.route('/oddoneoutvali', methods=['POST'])
def oddoneoutvali():
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

@app.route('/validate', methods=['POST'])
def validate():
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

if __name__ == '__main__':
    app.run(debug=True)

