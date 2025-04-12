import pandas as pd
import tkinter as tk
import customtkinter as ctk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image, ImageTk
import pymysql

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

sel_query= 'select * from srec.srectable;'

df=pd.read_sql(sel_query,conn)

print(df)

conn.commit()
cursor.close()
conn.close()

 

questions = df['question'].tolist()  
answers = df['answers'].tolist()  

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(questions)

def find_answer(user_input):
    user_input_tfidf = vectorizer.transform([user_input])  
    similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)  

    best_match_index = similarity_scores.argmax()
    best_match_score = similarity_scores[0, best_match_index]

    if best_match_score > 0.1:  
        return answers[best_match_index]
    else:
        return "Sorry, I don't have an answer for that question. Could you please rephrase it?"

image_paths = ["SREC_collage.jpg", "Hostel.jpg", "CIVIL_lab.jpg", "MECH_lab.jpg", "MECH_hod.jpg",'ece_hod.jpg',"IT_lab.jpg",'principal.jpg','placement.py','cse_lab.jpg','cse_hod.jpg']

def send_message():
    user_message = user_input_box.get()  
    
    if user_message.strip():
        chat_history.configure(state=tk.NORMAL)
        chat_history.insert(tk.END, "You: " + user_message + "\n", "user")

        response_message = find_answer(user_message)  
        chat_history.insert(tk.END, "Bot: " + response_message + "\n", "bot")
        display_images(user_message)
        chat_history.insert(tk.END, "\n", "space")

        chat_history.configure(state=tk.DISABLED)
        chat_history.yview(tk.END)  

    user_input_box.delete(0, tk.END)  

root = ctk.CTk()
root.title("SREC CHAT BOT")
root.geometry("700x600")  
root.resizable(False, False)


chat_frame = ctk.CTkFrame(root, width=870, height=200, corner_radius=5)
chat_frame.place(x=25, y=20)

chat_history = tk.Text(chat_frame, wrap=tk.WORD, font=("Arial", 12), height=20, width=90, state=tk.DISABLED, bg="#f5f5f5", padx=10, pady=10)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history["yscrollcommand"] = scrollbar.set

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
    img = Image.open(img_path)
    img = img.resize((320, 320), Image.Resampling.LANCZOS)  
    photo = ImageTk.PhotoImage(img)

    
    img_label.configure(image=photo)
    img_label.image = photo



image_frame = ctk.CTkFrame(root, width=350, height=280, corner_radius=10)
image_frame.place(x=25, y=330)

img_label = tk.Label(image_frame, bg="#f5f5f5")
img_label.pack(expand=True)


user_input_box = ctk.CTkEntry(root, placeholder_text="Type your message here...", width=250, font=("Arial", ))
user_input_box.place(x=320, y=430)

send_button = ctk.CTkButton(root, text="Send", width=150, command=send_message)
send_button.place(x=370, y=470)


chat_history.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_history.tag_configure("bot", foreground="black", font=("Arial", 12))
chat_history.tag_configure("space", foreground="white", font=("Arial", 12))


root.mainloop()
