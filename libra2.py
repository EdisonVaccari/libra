# CÓDIGO PARA CONCATENAÇÃO NO STREAMLIT FUNCIONANDO
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
        resumos = []
        bloco_atual = ""
        for linha in linhas:
            if linha.strip():
                if " - " in linha:  # Nova entrada com identificador e título
                    if bloco_atual:  # Salvar o bloco atual antes de começar o próximo
                        resumos.append(bloco_atual.strip())
                    bloco_atual = linha.strip()  # Começar um novo bloco
                else:
                    bloco_atual += f" {linha.strip()}"  # Continuar adicionando ao bloco atual
        if bloco_atual:  # Salvar o último bloco
            resumos.append(bloco_atual.strip())

        # Criar um dicionário com os resumos
        todos_resumos = {}
        linhas_invalidas = []
        for resumo in resumos:
            partes = resumo.split(" - ", 1)  # Divide pelo primeiro " - "
            if len(partes) == 2:  # Garante que existem exatamente duas partes
                identificador, texto = partes
                todos_resumos[identificador.strip()] = texto.strip()
            else:
                linhas_invalidas.append(resumo.strip())

        # Exibir aviso se houver linhas inválidas
        if linhas_invalidas:
            st.warning(f"As seguintes linhas não seguem o formato esperado e foram ignoradas:\n{', '.join(linhas_invalidas)}")

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

# Botão para apagar tudo
if st.button("Apagar Tudo"):
    st.experimental_rerun()
CD 