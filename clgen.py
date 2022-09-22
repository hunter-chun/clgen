import openai as ai
import streamlit as st

ai.api_key = "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"

with st.sidebar:
    model_used = st.selectbox(
     'GPT-3 Model',
    #  ('DaVinci', 'Curie', 'Babbage', 'Ada'))
    ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))
    max_tokens = st.text_input("Max # of tokens:","1900")
    temperature = st.text_input("Temperature: ","0.99")
    top_p = st.text_input("Top P: ","1")

with st.form(key='myform'):
    company = st.text_input("Company Name:", "Google")
    role = st.text_input("Position title:", "SWE")
    contact_person = st.text_input("Recipient:","Hirey McManager")
    your_name = st.text_input("What is your full name?","Hunter Chun")
    experience = st.text_input("I have experience in","NLP, ML and Data Science. ")
    job_desc = st.text_input("This position excites me because","this role will allow me to work. ")
    passions = st.text_input("I am passionate about","problem solving and civic duty.")
    submit_button = st.form_submit_button(label='Submit')

prompt= ("Write a cover letter to " + contact_person +
        " from " + your_name +" for a " + role + " job at "+
        company + "." + " I have experience in " + experience + 
        "I am excited about the job because " + job_desc + 
        "I am passionate about " +passions )

if submit_button:
    response = ai.Completion.create(
        engine = model_used,
        prompt = prompt,
        max_tokens=int(max_tokens),
        temperature = float(temperature),
        top_p = int(top_p),
        n=1,
        frequency_penalty = 0.3,
        presence_penalty= 0.9
    )

    text = response['choices'][0]['text']
    print("prompt - ", prompt)
    print("response - ",response)

    st.subheader("Cover Letter Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Cover Letter")
    st.write(text)
    st.download_button(label='Download Cover Letter', file_name='cover_letter.txt', data=text)



    with open('cl.txt','a') as f:
        f.write(text)