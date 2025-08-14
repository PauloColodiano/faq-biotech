import streamlit as st

# Função para carregar a base do FAQ
def carregar_faq(caminho_arquivo):
    faq = {}
    pergunta = None
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        for linha in file:
            linha = linha.strip()
            if linha.startswith("**Q:**"):
                pergunta = linha.replace("**Q:**", "").strip().lower()
            elif linha.startswith("**A:**") and pergunta:
                resposta = linha.replace("**A:**", "").strip()
                faq[pergunta] = resposta
                pergunta = None
    return faq

# Carregar base
faq_base = carregar_faq("prompts/faq-base.md")

# Interface Streamlit
st.title("🤖 Biotech Knowledge Bot (Offline)")
st.write("Digite sua pergunta em inglês para receber uma resposta da base de conhecimento.")

pergunta_usuario = st.text_input("Your question:")

if pergunta_usuario:
    pergunta_usuario_lower = pergunta_usuario.strip().lower()
    resposta = faq_base.get(pergunta_usuario_lower)
    if resposta:
        st.success(resposta)
    else:
        st.warning("Sorry, I don't have an answer for that yet.")
