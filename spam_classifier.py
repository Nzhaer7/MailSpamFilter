import pickle
import streamlit as st

print("hello world")
model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
	st.title("Email Spam Classification")
	st.subheader("Build with python")
	msg=st.text_input("enter a text:")
	if st.button("predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("spam")
		else:
			st.success("ham")

main()