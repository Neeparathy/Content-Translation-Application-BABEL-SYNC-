import streamlit as st
from googletrans import Translator
import base64
from PIL import Image

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text


def about_page():
    st.markdown("""
    <style>
    .about-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)
    st.subheader("About This Application")
    st.markdown("""
    <div class="about-box">
        This is a Language Translation & Document Text Extraction App developed using Streamlit.
        It allows users to translate text between various Indian languages and perform document translation for text files.
    """, unsafe_allow_html=True)



    
# Language codes for Indian languages
indian_languages = {
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Bengali': 'bn',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Punjabi': 'pa',
    'Urdu': 'ur'
}

# Common translation function
def translate_and_display(text, target_language):
    translated_text = translate_text(text, target_language)
    st.write('Translated Text:', translated_text)





#LOGO --- SHOULD BE FIRST ALWAYS
im = Image.open('C:\\Users\\npnee\\logo.png')
st.set_page_config(page_title="BABEL SYNC", page_icon=im)


# Streamlit UI

menu_options = ['Home','Translate Text', 'Translate Document', 'About']  # Add 'About' to menu options
input_option = st.sidebar.selectbox('Menu', menu_options)



if input_option == 'Home':
    # BACKGROUND IMAGE
    def set_bg_hack(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack('C:\\Users\\npnee\\b.png')
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: left;
            margin-top: 300px;  # Adjust the margin-top value to move the title down
            font-size: 10px;
            font-family: 'Arial';
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 style='text-align: left; margin-top: 0.5px;margin-left: 10px;  font-size: 120px;'>BABEL</h1>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: left;
            margin-top: 300px;  # Adjust the margin-top value to move the title down
            font-size: 10px;
            font-family: 'Arial';
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 style='text-align: left; margin-top: 0.5px;margin-left: 10px;  font-size: 120px;'>SYNC</h1>", unsafe_allow_html=True)
if input_option == 'Translate Text':
    def set_bg_hack(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack('C:\\Users\\npnee\\b1.png')
    st.title('BABEL SYNC')
    text_input = st.text_area('Enter text to translate', '')
    target_language_text = st.selectbox('Select Target Language', list(indian_languages.keys()))

    if st.button('Translate'):
        language_code_text = indian_languages[target_language_text]
        translate_and_display(text_input, language_code_text)

elif input_option == 'Translate Document':
    def set_bg_hack(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack('C:\\Users\\npnee\\b1.png')
    st.title('BABEL SYNC')
    uploaded_file = st.file_uploader('Upload Document', type=['txt'])

    if uploaded_file is not None:
        file_details = {
            "FileName": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size
        }

        target_language_doc = st.selectbox('Select Target Language', list(indian_languages.keys()))

        if st.button('Translate'):
            if uploaded_file.type == 'text/plain':
                file_contents = uploaded_file.getvalue().decode("utf-8")
                st.write('File Contents:', file_contents)  # Debug statement
                language_code_doc = indian_languages[target_language_doc]
                translate_and_display(file_contents, language_code_doc)

elif input_option == 'About':
    def set_bg_hack(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack('C:\\Users\\npnee\\b1.png')
    st.title('BABEL SYNC')
    about_page()  # Call the about_page function to display the "About" content
