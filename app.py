import streamlit as st
import google.generativeai as genai

st.title("🚀 AI მარკეტინგული ასისტენტი")
st.write("შეიყვანე დეტალები და მიიღე საუკეთესო სარეკლამო ტექსტი!")

# ვცდილობთ ავიღოთ გასაღები Streamlit-ის საიდუმლო სეიფიდან ავტომატურად
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    # თუ სეიფში არ არის, ვთხოვთ მომხმარებელს გვერდზე შეიყვანოს
    api_key = st.text_input("ჩასვი შენი API გასაღები (AIzaSy...):", type="password")
    if api_key:
        genai.configure(api_key=api_key)

business_type = st.selectbox("ბიზნესის ტიპი:", ["კაფე / რესტორანი", "ონლაინ მაღაზია", "სილამაზის სალონი", "სხვადასხვა სერვისი"])
product_info = st.text_area("დაწერე ორი სიტყვით რა პროდუქტი ან სერვისი გაქვს:")

if st.button("გენერაცია ✨"):
    if not api_key:
        st.warning("გთხოვთ, ჯერ მიუთითოთ API გასაღები!")
    elif product_info:
        prompt = f"შექმენი სარეკლამო სოციალური ქსელის პოსტი შემდეგი ბიზნესისთვის: {business_type}. პროდუქტის/სერვისის აღწერა: {product_info}"
        
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            st.subheader("შენი ახალი ტექსტი:")
            st.write(response.text)
        except Exception as e:
            st.error(f"მოხდა შეცდომა: {e}")
    else:
        st.warning("გთხოვთ, ჯერ შეიყვანოთ ინფორმაცია პროდუქტის შესახებ!")
