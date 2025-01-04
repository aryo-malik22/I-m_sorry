import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff; /* White background */
    }
    .title {
        color: white;
        background-color: #ff69b4; /* Pink color */
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 36px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .subheader {
        color: #ff1493; /* Deep pink */
        font-size: 24px;
        margin-top: 20px;
        cursor: pointer;
        text-align: center;
        padding: 10px;
        border: 2px solid #ff1493;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .subheader:hover {
        background-color: #ffb3d9; /* Light pink on hover */
    }
    .response {
        color: #ff69b4; /* Pink color */
        font-size: 18px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">For Kasih Riesdiani Azzahara</div>', unsafe_allow_html=True)

if st.button("Please read this"):
    st.write("I'm deeply sorry for making you discomfort because I said something that I shouldn't have said.")

if st.button("There's more, please read this too :)"):
    st.write("I do not want this to become the end of our conversation and I want to keep it on and on, "
         "we promised each other that we will do every wishlist that we have, so let's do it together as planned.")

if st.button("HAPPY BIRTHDAY DIANNNN"):
    st.write("Happy birthday Kasih Riesdiani Azzahra, may this year become the best year that you'll have.")

if st.button("One more surprise"):
    st.balloons()
    st.success("You are amazing! Let's make wonderful memories together!")
