from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications import VGG16
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import os
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.shortcuts import redirect
from tensorflow.python.keras.backend import reverse

from django.contrib.auth.models import User
from django.contrib import auth
import random

img_height, img_width = 206, 278
# 모델 로드
model_graph = tf.compat.v1.Graph()
with model_graph.as_default():
   tf_session = tf.compat.v1.Session()
   with tf_session.as_default():
       model = load_model('./models/except_hurt_aug.h5')

# Create your views here.
def index(request):
    context={'a':1}
    return render(request, 'Faceapp/index.html', context)

'''
predicImage 
기능 : 업로드 사진 감정 분석기능

by 형주
'''
def predictImage(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login')
    else:
        #파일 업로드 하면 /media + image.png으로 저장된다.
        fileObj=request.FILES['filePath']
        fs=FileSystemStorage()
        filePathName = fs.save(fileObj.name, fileObj)
        filePathName = fs.url(filePathName)
        testimage='.'+filePathName
        #저장된 파일을 로드하여, 이미자 사이즈를 img_height, img_width 크기로 조정
        img = image.load_img(testimage, target_size=(img_height,img_width))
        img_tensor = image.img_to_array(img)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        #axis=0 or 1은 행열 붙이는 방향을 의미
        img_tensor /= 255.# RGB 계수와 연관이 있는 값

        #로드된 모델에 이미지를 넣어 분석한다.
        with model_graph.as_default():
            with tf_session.as_default():
                predi=model.predict(img_tensor)
                # 분석 결과는 1 * 6 행렬 형태로 반환되며, [1][0] ~ [1][5]
                result = np.argmax(predi)+1
                emotion_dt = datetime.now().strftime("%m%d")
        user = request.user

        #1. 분노, 2. 당황, 3. 행복, 4. 중립, 5. 슬픔, 6. 불안 (3,4번 사이 상처였으나 삭제) 
        #emotion 리스트를 생성하고, 분석 화면에 result 인덱스와 매칭되는 감정을 리턴
        emotion_list = ['Anger', 'Embarassment', 'Happy', 'Neutrality', 'Sad', 'Unrest']
        result_text = emotion_list[result-1]
        comment = request.POST['comment']
        emotion = Emotion(content=result, emotion_dt=emotion_dt, content_str=result_text, comment=comment, author=user)
        emotion.save()

        #데이터베이스에 감정별로 저장된 음악과 결과를 매칭하여 뮤직비디오 리스트 저장
        #뮤직 비디로 리스트 중 하나를 랜덤으로 shuffle_video 저장
        music_video = Music.objects.filter(emotion_code=result)
        shuffle_video = random.choice(music_video)

        #저장경로, 분석결과, 뮤직비디오 url을 context에 저장
        context={'filePathName':filePathName, 'predict':result_text, 'music_video':shuffle_video}
        return render(request,'Faceapp/index.html',context) 

def mood_calendar(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login')
    else:
        user = request.user
        emotion = Emotion.objects.filter(author_id=user)
        context={ 'emotion':emotion }
        return render(request, 'Faceapp/mood_calendar.html', context)

def note(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login')
    else:
        return render(request, 'Faceapp/note.html')

def mypage(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login')
    else:
        user = request.user
        emotion_results = Emotion.objects.filter(author_id=user)
        # emotion_results = Emotion.objects.all()

        array = []
        for Emotion.object in emotion_results:
            array.append(Emotion.object.content_str)
        unique_emotion = list(set(array))
        
        dd = {}
        for emotion1 in unique_emotion:
            dd[emotion1] = array.count(emotion1)

        context = {
            'graph_labels': list(dd.keys()),
            'graph_values': list(dd.values()),
            'emotions': emotion_results
        }
        return render(request, 'Faceapp/mypage.html', context)


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')

    return render(request, 'Faceapp/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'Faceapp/login.html', {'error':'username or password is incorrect!'})
    else:
        return render(request, 'Faceapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
