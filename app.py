import streamlit as st
from google import genai

st.title("🚀 AI მარკეტინგის ასისტენტი ქართული ბიზნესისთვის")
st.write("შეიყვანე დეტალები და მიიღე მზა პოსტები სოციალური ქსელებისთვის ერთ წამში!")

API_KEY = "AQ.Ab8RN6IblRDn6Ezph0yYmLxT6tSBBHnv-Obgvr5WdEG7APLHFw"

business_type = st.selectbox("აირჩიე ბიზნესის ტიპი:", ["კაფე / რესტორანი", "სილამაზის სალონი", "ონლაინ მაღაზია / ტანსაცმელი", "სხვა"])
product_info = st.text_area("დაწერე ორი სიტყვით რა პროდუქტი ან აქცია გაქვს:")

if st.button("გენერაცია ✨"):
    if product_info:
        client = genai.Client(api_key=API_KEY)
        prompt = f"შენ ხარ პროფესიონალი სოციალური მედიის მარკეტოლოგი. დაწერე მიმზიდველი ინსტაგრამის პოსტი ქართულად, მეგობრული ტონით და ჰეშთეგებით, შემდეგი ბიზნესისთვის: {business_type}. დეტალები: {product_info}"
        
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )
        st.subheader("შენი მზა ტექსტი:")
        st.write(response.text)
    else:
        st.warning("გთხოვთ, ჯერ შეიტანოთ ინფორმაცია პროდუქტზე!")
