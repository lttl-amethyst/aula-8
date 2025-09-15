import streamlit as st
st.set_page_config(page_icon ="⚖️", page_title = "Consultório de Advocacia")
st.title("Atendimento - Consultório")
if "messages" not in st.session_state:
    st.session_state.messages = []

faq = {
    "Qual é o horário de atendimento do escritório?": "Nosso escritório atende de segunda a sexta, das 09:00 às 18:00.",
    "Como posso agendar uma consulta com um advogado?": "Você pode agendar uma consulta ligando para nosso número ou enviando um e-mail. Também temos um formulário no site.",
    "Quais áreas do direito vocês atuam?": "Atuamos nas áreas de Direito Civil, Direito Penal, Direito Trabalhista e Direito de Família.",
    "Qual é o custo da consulta?": "O valor da consulta varia conforme a complexidade do caso. Entre em contato para mais informações.",
    "Onde o escritório está localizado?": "Nosso escritório fica na Rua Limoeiro, nº 456, Centro.",
    "Falar com um advogado": "Para falar com um advogado, entre em contato pelo telefone ou WhatsApp, ou agende sua consulta pelo nosso site.",
}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta: ")
for key in faq.keys():
    if st.button(key):
        pergunta = key 
    
if pergunta:
    resposta = faq.get(pergunta, "Desculpe não temos uma resposta configurada")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        st.markdown(resposta)

    if pergunta == "Falar com atendente":
        whatsapp_url = "https://wa.me/6199999999"
        st.markdown(f"[Clique aqui para falar no Whatsapp]({whatsapp_url})")


