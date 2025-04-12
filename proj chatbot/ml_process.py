import pandas as pd
import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image, ImageTk
import pymysql
import sys

dyc_img_var = 0

dyc_img_var=0


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Harshini@2127',
    database='srec'
)

cursor = conn.cursor()


print("Data inserted successfully!")

sel_query= 'select * from srec.srectable12;'

df=pd.read_sql(sel_query,conn)
 

conn.commit()
cursor.close()
conn.close()

df.dropna(subset=['QUESTIONS', 'ANSWERS'], inplace=True)
 

questions = df['QUESTIONS'].tolist()  
answers = df['ANSWERS'].tolist()  

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(questions)

def find_answer(user_input):


    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Harshini@2127',
        database='srec'
    )

    cursor = conn.cursor()
    

    print("Data inserted successfully!")

    sel_query= 'select * from srec.srectable12;'

    df=pd.read_sql(sel_query,conn)

    df.dropna(subset=['QUESTIONS', 'ANSWERS'], inplace=True)

    print(df)
 

    conn.commit()
    cursor.close()
    conn.close()

    

    questions = df['QUESTIONS'].tolist()  
    answers = df['ANSWERS'].tolist()  

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(questions)
    user_input_tfidf = vectorizer.transform([user_input])  
    similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)  

    best_match_index = similarity_scores.argmax()
    best_match_score = similarity_scores[0, best_match_index]

    if best_match_score > 0.1:  
        return answers[best_match_index]
    else:
        return "Sorry, I don't have an answer for that question. Could you please rephrase it?"

image_paths = ["SREC_collage.jpg", "Hostel.jpg", "CIVIL_lab.jpg", "MECH_lab.jpg", "MECH_hod.jpg",'ece_hod.jpg',"IT_lab.jpg",'principal.jpg','placement.py','cse_lab.jpg','cse_hod.jpg']

 



def display_images(user_message):
    print(user_message)
    global dyc_img_var

    list_arr=['hostel','lab','hod','placement','principal','library']

    hod_list=['cse','it','mech','ece']

    lab_list=['cse','it','civil','mech']
    hod_index=0

    user_message=user_message.lower()

    image_name=''

    
    
    if 'hod' in user_message.lower():
        print(user_message)
        for x in hod_list:
            if  x in user_message.lower():
                image_name=x+'_hod.jpg'
                print(image_name)

    elif  'principal' in user_message:
        
            image_name='principal.jpg'
    elif 'placement'   in user_message:
             image_name='PLACEMENT.jpg'
    elif 'hostel' in     user_message:
             image_name='hostel.jpg'
    elif  'lab' in user_message.lower():
        for x in lab_list:
            if  x in user_message.lower():
                image_name=x+'_lab.jpg'
                print(image_name)
    elif 'library' in user_message.lower():
         image_name='library.jpg'

         



    
    if dyc_img_var < len(image_paths)-1: 
        dyc_img_var += 1
    else:
        dyc_img_var = 0

        

    img_path = image_paths[dyc_img_var]
    img_path=image_name

    return img_path





