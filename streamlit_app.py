import streamlit as st
import requests

BRAINSHOP_API_KEY = "uiBgOSyDQETwDSzj"
BRAINSHOP_BRAIN_ID = "179489"
BRAINSHOP_URL = f"http://api.brainshop.ai/get?bid={BRAINSHOP_BRAIN_ID}&key={BRAINSHOP_API_KEY}&uid=1&msg="

def get_brainshop_response(message):
    response = requests.get(BRAINSHOP_URL + message)
    return response.json()["cnt"]

def main():
    st.title("BrainShop ChatBot with Streamlit")

    user_input = st.text_input("You:", key="input")
    if st.button("Send"):
        if user_input:
            bot_response = get_brainshop_response(user_input)
            st.text(f"Bot: {bot_response}")


if __name__ == "__main__":
    main()
