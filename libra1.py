import streamlit as st

# Página única: Inserção de dados e geração de texto concatenado
st.title("Concatenação dos Resumos")

# Campo para inserir todo o conteúdo
conteudo = st.text_area("Cole aqui o conteúdo dos resumos:")

# Campo para definir a sequência de concatenação
sequencia = st.text_input("Informe a sequência dos blocos (ex.: I1, C1, C2):")

# Botão de ação
if st.button("Gerar Texto"):
    try:
        # Separar os resumos
        linhas = conteudo.strip().split("\n")
        resumos = linhas

        # Criar um dicionário com os resumos
        todos_resumos = {}
        for resumo in resumos:
            if resumo.strip():
                identificador, texto = resumo.split("-", 1)
                todos_resumos[identificador.strip()] = texto.strip()

        # Construir o texto final com base na sequência
        texto_final = []
        blocos_invalidos = []
        for bloco in sequencia.split(","):
            bloco = bloco.strip()
            if bloco in todos_resumos:
                texto_final.append(f"{bloco} - {todos_resumos[bloco]}")
            else:
                blocos_invalidos.append(bloco)

        # Exibir avisos sobre blocos inválidos
        if blocos_invalidos:
            st.warning(f"Os seguintes blocos não foram encontrados ou estão vazios: {', '.join(blocos_invalidos)}")

        # Verificar se há texto para exibir
        if texto_final:
            texto_concatenado = "\n\n".join(texto_final)
            st.text_area("Texto Concatenado", value=texto_concatenado, height=300)

            # Botão para copiar
            st.download_button(
                label="Copiar Texto", 
                data=texto_concatenado, 
                file_name="texto_concatenado.txt", 
                mime="text/plain"
            )
        else:
            st.error("Nenhum bloco válido foi encontrado na sequência. Verifique e tente novamente.")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")

if st.button("Apagar Tudo"):
    st.experimental_rerun()
