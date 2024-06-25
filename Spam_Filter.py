import tkinter as tk
import pickle

Filter=tk.Tk()

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

canvas1 = tk.Canvas(Filter, width = 600, height = 400)
canvas1.configure(bg="beige")
canvas1.pack()

label1 = tk.Label(Filter, text='Email Spam Filter', bg="beige")
label1.config(font=('consolas', 16))
canvas1.create_window(300, 50, window=label1)

label2 = tk.Label(Filter, text='Type your mail', bg="beige")
label2.config(font=('consolas', 14))
canvas1.create_window(300, 150, window=label2)

entry1 = tk.Entry (Filter)
canvas1.create_window(300, 180, window=entry1)

def spam_filter():
	msg=entry1.get()
	data=[msg]
	vect=cv.transform(data).toarray()
	prediction=model.predict(vect)
	result=prediction[0]
	if result==1:
		message="spam"
	else:
		message="ham"
	label3 = tk.Label(Filter, text='Your mail is:', font=('consolas', 10), bg="beige")
	canvas1.create_window(300,310 , window=label3)

	label4=tk.Label(Filter, text=message, fg="red", font=("consolas", 12, "bold"), bg="beige")
	canvas1.create_window(300, 350, window=label4)

button1 = tk.Button(text='Predict', command=spam_filter, bg='black', fg='green', font=('consolas', 12, 'bold'))
canvas1.create_window(300, 250, window=button1)

Filter.mainloop()