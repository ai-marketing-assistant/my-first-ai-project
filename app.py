
 import streamlit as st
from google import genai

st.title("🚀 AI მარკეტინგული ასისტენტი")
st.write("შეიყვანე დეტალები და მიიღე საუკეთესო სარეკლამო ტექსტი!")

API_KEY = "AQ.Ab8RN6iB1RDn6Ezph..."  # შენი გასაღები

client = genai.Client(api_key=API_KEY)

business_type = st.selectbox("ბიზნესის ტიპი:", ["კაფე / რესტორანი", "ონლაინ მაღაზია", "სილამაზის სალონი", "სხვადასხვა სერვისი"])
product_info = st.text_area("დაწერე ორი სიტყვით რა პროდუქტი ან სერვისი გაქვს:")

if st.button("გენერაცია ✨"):
    if product_info:
        prompt = f"შექმენი სარეკლამო სოციალური ქსელის პოსტი შემდეგი ბიზნესისთვის: {business_type}. პროდუქტის/სერვისის აღწერა: {product_info}"
        
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt,
            )
            st.subheader("შენი ახალი ტექსტი:")
            st.write(response.text)
        except Exception as e:
            st.error(f"მოხდა შეცდომა: {e}")
    else:
        st.warning("გთხოვთ, ჯერ შეიყვანოთ ინფორმაცია პროდუქტის შესახებ!")
