import google.generativeai as genai 
import random as rd 
import numpy as np 
import PIL.Image
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

API_KEY = 'AIzaSyC6lbjbuytc4d8yjoC7qvNE_jHdjHnbN8E'
genai.configure(api_key=API_KEY,)

def IsItPrime(n:int):
    if n == 0 :
        return False
    elif 0 < n <= 3:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0 :
                return False
        return True

def LLM(Prompt,img=None):
    
    if img != None:
        model = genai.GenerativeModel('gemini-pro-vision')
        img = PIL.Image.open(img)
        
        response = model.generate_content([Prompt, img],generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                max_output_tokens=512,
                temperature=0.9))
    else:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(Prompt,generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                max_output_tokens=1024,
                temperature=0.9))
    return (response.text).replace('*','').replace('#','')
def reportPrompt(temp,SM,NPK,SL,img):
    return LLM(f'Your task is to make a professional and arranged report on the condition of the tree based on the tests in first and the photo. NPK test values : {NPK}, soil moisture test value : {SM}, air temperature test value : {temp}, sunlight intensity : {SL}, Foucse in the test values and don\'t give me factors that not compared with tests. Format : today\'s date, plant type, Tests result, Visual Inspection, general codition, diagnosis, recomendation and advices if needed',img)

def randNPK():
    return [str(rd.randint(100,7000))+' PPM',str(rd.randint(0,800))+' PPM',str(rd.randint(50,800))+' PPM']

def randSM():
    return str(rd.randint(0,100))+'%'

def randTemp():
    return str(rd.randint(10,45))+'C'

def randSL():
    return str(rd.randint(1000,3000))+'lux'

def randPhoto():
    global x
    photos = {0:'AlOasisProjectSimulation /photos/0.webp',1:'AlOasisProjectSimulation /photos/1.webp',2:'AlOasisProjectSimulation /photos/2.jpg',3:'AlOasisProjectSimulation /photos/3.webp',4:'AlOasisProjectSimulation /photos/4.jpeg',5:'AlOasisProjectSimulation /photos/5.jpg',6:'AlOasisProjectSimulation /photos/6.jpg',7:'AlOasisProjectSimulation /photos/7.jpeg',8:'AlOasisProjectSimulation /photos/8.jpg',9:'AlOasisProjectSimulation /photos/9.webp',10:'AlOasisProjectSimulation /photos/10.jpeg',11:'AlOasisProjectSimulation /photos/11.jpg',12:'AlOasisProjectSimulation /photos/12.jpg',13:'AlOasisProjectSimulation /photos/13.jpg',14:'AlOasisProjectSimulation /photos/14.jpg',15:'AlOasisProjectSimulation /photos/15.jpg'}
    x = rd.randint(0,16)
    return photos[x]

photosURL = {0:'https://drive.google.com/file/d/1Icp2BmrcGtl3Qm9tSQrNNjZsF55sTFzs/view?usp=sharing',1:'https://drive.google.com/file/d/18nZ3uMjGoLW6-IBuARdLs1M_xLRBIwVj/view?usp=sharing',2:'https://drive.google.com/file/d/1U9hwaZ4VN_Cto-BzSoJ3tjdoM3sCRQSq/view?usp=sharing',3:'https://drive.google.com/file/d/1wsul9uF6DWvibVLAffLsF3xai5400dZx/view?usp=sharing',4:'https://drive.google.com/file/d/1QSsWPdtlx7nKXsIeL37QNkmUEvtLOyUE/view?usp=sharing',5:'https://drive.google.com/file/d/15qimFRt6vRHB3WDTR7J28y6opGzlnObJ/view?usp=sharing',6:'https://drive.google.com/file/d/1dhDGgDTzgKxztcaywUdCvNNcnYyOiV2o/view?usp=sharing',7:'https://drive.google.com/file/d/17q1wpSPXTqHPjwaRbKhqQLi_pXbdi7Mk/view?usp=sharing',8:'https://drive.google.com/file/d/1qBqGomdpMpZrCHnhulI3MD4UX0MF_TzG/view?usp=sharing',9:'https://drive.google.com/file/d/1C5NyWM3koMq6ywJkmIH1tTI-pRKAc-qz/view?usp=sharing',10:'https://drive.google.com/file/d/1oW_OAcOeZGj_82PJ_benflbri-xrKNk0/view?usp=sharing',11:'https://drive.google.com/file/d/18FVI4HNkgLM1-QZUco_mcHl79Rd038e4/view?usp=sharing',12:'https://drive.google.com/file/d/10Olxdi2-9MJrMs0Nj2n3NG9wSQ_E16Ra/view?usp=sharing',13:'https://drive.google.com/file/d/19IJgFIvG1YYvRIXbS-GfvQj5iIeCeMxv/view?usp=sharing',14:'https://drive.google.com/file/d/1_dSId9IhxEP9sd1tMh9qaKLTIm9Ch3hC/view?usp=sharing',15:'https://drive.google.com/file/d/1khZG-nhA8_KYqlMfjY8UQ3BfVXSXePkD/view?usp=sharing'}
pestsURL = ['https://drive.google.com/file/d/1dUWt4vLH9mDL5IxzCCdRAy_VPYCLLozM/view?usp=sharing','https://drive.google.com/file/d/1v1hDtqMSq3_nooBJYv86NWownGcQKGB4/view?usp=sharing','https://drive.google.com/file/d/1Ks0jmB5-a5Rw7Uu994Teho8fxJ16SMui/view?usp=sharing','https://drive.google.com/file/d/17_vvsgDDVy7Y3lTSazpjmg2072PSoDMo/view?usp=sharing','https://drive.google.com/file/d/1spGWk3F-0Q8LcV62b9JxTAL3H3nymBLV/view?usp=sharing']
pestsPhotos = ['AlOasisProjectSimulation /pestsphotos/1.jpeg','AlOasisProjectSimulation /pestsphotos/2.jpeg','AlOasisProjectSimulation /pestsphotos/3.jpeg','AlOasisProjectSimulation /pestsphotos/4.webp','AlOasisProjectSimulation /pestsphotos/5.jpeg']
def NPKcompare(x):
    r = []
    for i in range(len(x)):
        x1 = int(x[i][:-3])
        if i == 0:
            if x1 < 200 :
                r.append(x[i]+' '+str(np.round(np.abs((200-x1)/2)))+'%'+' lower')
            elif x1 > 5000:
                r.append(x[i]+' '+str(np.round(np.abs((5000-x1)/50)))+'%'+' more')
            else:
                r.append(x[i]+" good")
        elif i == 1:
            if x1 < 50 :
                r.append(x[i]+' '+str(np.round(np.abs((50-x1)/0.5)))+'%'+' lower')
            elif x1 > 500:
                r.append(x[i]+' '+str(np.round(np.abs((500-x1)/5)))+'%'+' more')
            else:
                r.append(x[i]+" good")
        else:
            if x1 < 100 :
                r.append(x[i]+' '+str(np.round(np.abs((100-x1))))+'%'+' lower')
            elif x1 > 500:
                r.append(x[i]+' '+str(np.round(np.abs((500-x1)/5)))+'%'+' more')
            else:
                r.append(x[i]+" good")
            
    return 'Nitrogen: '+r[0]+', Phosphorus: '+r[1]+', Potassium '+r[2]


def tempCompare(x):
	x1 = int(x[:-1])
	if x1 < 21 :
		return 'Temperature : '+(x+' '+str(np.round(np.abs((21-x1)/21)*100))+'%'+' less')
		
	elif x1 > 24:
		return 'Temperature : '+(x+' '+str(np.round(np.abs((24-x1)/24)*100))+'%'+' more')
    
	else:
		return 'Temperature : '+(x+" good")

def SLCompare(x):
    x1 = int(x[:-3])
    if x1 < 2000 :
        return (x+' '+str(np.round(np.abs((2000-x1)/2000)*100))+'%'+' less')
		
    elif x1 > 5000:
         return (x+' '+str(np.round(np.abs((5000-x1)/5000)*100))+'%'+' more')
    
    else:
         return (x+" good")

def SMCompare(x):
     x1 = int(x[:-1])
     if x1 < 40 :
         return (x+' (Underwaterd)')
		
     elif x1 > 75:
         return (x+' (Overwaterd)')
    
     else:
         return (x+" good")

def warningPrompt(img):
    return LLM('your task is telling the user that there is a pest found in professional and arrangegd way. Format : Today\'s date, about the pest, its dangers, reasons for its presence, how to remove it, how to prevent its return, additional tips.',img)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/req', methods=['POST'])
def req():
    r = rd.randint(0,101)
    if IsItPrime(r) or r % 17 == 0 or r % 23 == 0:
        i = rd.randint(0,4)
        return jsonify({'report': warningPrompt(pestsPhotos[i]),'img':pestsURL[i],'type':'warning'})
    else:
        NPK = NPKcompare(randNPK())
        temp = tempCompare(randTemp())
        SM = SMCompare(randSM())
        SL = SLCompare(randSL())
        img = randPhoto()
        return jsonify({'report': reportPrompt(temp,SM,NPK,SL,img),'img':photosURL[x],'type':'report'})

if __name__ == '__main__':
    app.run(debug=True)