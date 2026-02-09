import streamlit as st
import requests

# Function to generate sales strategy using Google Gemini API
def generate_strategy(product, audience, tone, platform, mental_triggers):
    # Assuming you have set up Google Gemini API correctly
    url = 'https://api.google.com/gemini/generate'
    payload = {
        'product': product,
        'audience': audience,
        'tone': tone,
        'platform': platform,
        'mental_triggers': mental_triggers
    }
    response = requests.post(url, json=payload)
    return response.json()

# Streamlit UI
st.title('MindClick IA Sales Strategy Generator')

# Product input
product = st.text_input('Enter Product Name')

# Audience selection
audience_options = ['General Public', 'Business Owners', 'Marketers']
selected_audience = st.selectbox('Choose Audience Type', audience_options)

# Tone selection
tone_options = ['Formal', 'Casual', 'Persuasive']
selected_tone = st.selectbox('Select Tone', tone_options)

# Platform selection
platform_options = ['Social Media', 'Email', 'Website']
selected_platform = st.selectbox('Choose Platform', platform_options)

# Mental triggers input
mental_triggers = st.multiselect('Select Mental Triggers', ['Scarcity', 'Urgency', 'Social Proof', 'Authority'])

# Generate strategy button
if st.button('Generate Sales Strategy'):
    if product and selected_audience and selected_tone and selected_platform:
        strategy = generate_strategy(product, selected_audience, selected_tone, selected_platform, mental_triggers)
        st.subheader('Generated Sales Strategy')
        st.json(strategy)
    else:
        st.warning('Please fill in all required fields!')
