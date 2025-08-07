# app.py (Versão Final com Upload Manual)

import streamlit as st
import pandas as pd
import io

st.write(f"ATENÇÃO: O limite de upload que o servidor está usando é: {st.get_option('server.maxUploadSize')} MB")

# --- Configuração da Página ---
st.set_page_config(page_title="Simulador de Premiação", page_icon="🏆", layout="wide")
st.title("🏆 Simulador de Campanhas de Premiação")
st.markdown("Configure as metas, carregue a base de vendas na barra lateral e gere o relatório.")

# --- Funções de Lógica ---
def parse_mes_ano(mes_ano_str):
    try:
        mes, ano = mes_ano_str.split('/')
        return int(f"{ano}{mes}")
    except:
        return None

# --- Interface Principal ---
st.header("1. Defina as Metas das Campanhas")

with st.expander("⭐ CAMPANHA 1 (Jan / Fev / Mar)"):
    col1, col2 = st.columns(2); c1_p1_mes_ano = col1.text_input("Mês/Ano (P1)", "01/2025", key="c1p1m"); c1_p1_valor = col2.number_input("Valor Meta (P1)", value=230, min_value=0, key="c1p1v"); c1_p2_mes_ano = col1.text_input("Mês/Ano (P2)", "02/2025", key="c1p2m"); c1_p2_valor = col2.number_input("Valor Meta (P2)", value=250, min_value=0, key="c1p2v"); c1_p2e_mes_ano = col1.text_input("Mês/Ano (P2 Extra)", "02/2025", key="c1p2em"); c1_p2e_valor = col2.number_input("Valor Meta (P2 Extra)", value=400, min_value=0, key="c1p2ev"); c1_p3_mes_ano = col1.text_input("Mês/Ano (P3)", "03/2025", key="c1p3m"); c1_p3_valor = col2.number_input("Valor Meta (P3)", value=280, min_value=0, key="c1p3v"); c1_p3e_mes_ano = col1.text_input("Mês/Ano (P3 Extra)", "03/2025", key="c1p3em"); c1_p3e_valor = col2.number_input("Valor Meta (P3 Extra)", value=480, min_value=0, key="c1p3ev")
with st.expander("⭐ CAMPANHA 2 (Abr / Mai / Jun)"):
    col1, col2 = st.columns(2); c2_p1_mes_ano = col1.text_input("Mês/Ano (P1) C2", "04/2025", key="c2p1m"); c2_p1_valor = col2.number_input("Valor Meta (P1) C2", value=230, min_value=0, key="c2p1v"); c2_p2_mes_ano = col1.text_input("Mês/Ano (P2) C2", "05/2025", key="c2p2m"); c2_p2_valor = col2.number_input("Valor Meta (P2) C2", value=250, min_value=0, key="c2p2v"); c2_p2e_mes_ano = col1.text_input("Mês/Ano (P2 Extra) C2", "05/2025", key="c2p2em"); c2_p2e_valor = col2.number_input("Valor Meta (P2 Extra) C2", value=550, min_value=0, key="c2p2ev"); c2_p3_mes_ano = col1.text_input("Mês/Ano (P3) C2", "06/2025", key="c2p3m"); c2_p3_valor = col2.number_input("Valor Meta (P3) C2", value=300, min_value=0, key="c2p3v"); c2_p3e_mes_ano = col1.text_input("Mês/Ano (P3 Extra) C2", "06/2025", key="c2p3em"); c2_p3e_valor = col2.number_input("Valor Meta (P3 Extra) C2", value=700, min_value=0, key="c2p3ev")
with st.expander("⭐ CAMPANHA 3 (Jul / Ago / Set)"):
    col1, col2 = st.columns(2); c3_p1_mes_ano = col1.text_input("Mês/Ano (P1) C3", "07/2025", key="c3p1m"); c3_p1_valor = col2.number_input("Valor Meta (P1) C3", value=0, min_value=0, key="c3p1v"); c3_p2_mes_ano = col1.text_input("Mês/Ano (P2) C3", "08/2025", key="c3p2m"); c3_p2_valor = col2.number_input("Valor Meta (P2) C3", value=0, min_value=0, key="c3p2v"); c3_p2e_mes_ano = col1.text_input("Mês/Ano (P2 Extra) C3", "08/2025", key="c3p2em"); c3_p2e_valor = col2.number_input("Valor Meta (P2 Extra) C3", value=0, min_value=0, key="c3p2ev"); c3_p3_mes_ano = col1.text_input("Mês/Ano (P3) C3", "09/2025", key="c3p3m"); c3_p3_valor = col2.number_input("Valor Meta (P3) C3", value=0, min_value=0, key="c3p3v"); c3_p3e_mes_ano = col1.text_input("Mês/Ano (P3 Extra) C3", "09/2025", key="c3p3em"); c3_p3e_valor = col2.number_input("Valor Meta (P3 Extra) C3", value=0, min_value=0, key="c3p3ev")
with st.expander("⭐ CAMPANHA 4 (Out / Nov / Dez)"):
    col1, col2 = st.columns(2); c4_p1_mes_ano = col1.text_input("Mês/Ano (P1) C4", "10/2025", key="c4p1m"); c4_p1_valor = col2.number_input("Valor Meta (P1) C4", value=0, min_value=0, key="c4p1v"); c4_p2_mes_ano = col1.text_input("Mês/Ano (P2) C4", "11/2025", key="c4p2m"); c4_p2_valor = col2.number_input("Valor Meta (P2) C4", value=0, min_value=0, key="c4p2v"); c4_p2e_mes_ano = col1.text_input("Mês/Ano (P2 Extra) C4", "11/2025", key="c4p2em"); c4_p2e_valor = col2.number_input("Valor Meta (P2 Extra) C4", value=0, min_value=0, key="c4p2ev"); c4_p3_mes_ano = col1.text_input("Mês/Ano (P3) C4", "12/2025", key="c4p3m"); c4_p3_valor = col2.number_input("Valor Meta (P3) C4", value=0, min_value=0, key="c4p3v"); c4_p3e_mes_ano = col1.text_input("Mês/Ano (P3 Extra) C4", "12/2025", key="c4p3em"); c4_p3e_valor = col2.number_input("Valor Meta (P3 Extra) C4", value=0, min_value=0, key="c4p3ev")

# --- Barra Lateral para Ações ---
st.sidebar.header("2. Execute a Simulação")
# st.sidebar.info("Para usar, primeiro arraste seu arquivo .xlsx para a lista de arquivos à esquerda.")
nome_do_arquivo = st.sidebar.text_input("Nome do arquivo .xlsx no projeto", "AFATR104_Classe_Gestora.xlsx")
botao_calcular = st.sidebar.button("Gerar Relatório de Premiação", type="primary")

# --- Lógica Principal de Cálculo ---
# --- Lógica Principal de Cálculo ---
if botao_calcular:
    if nome_do_arquivo:
        with st.spinner("Aguarde, os cálculos estão em andamento..."):
            regras_brutas = [
                {'mes_ano': c1_p1_mes_ano, 'valor': c1_p1_valor, 'premio': 'Prêmio 1'}, {'mes_ano': c1_p2_mes_ano, 'valor': c1_p2_valor, 'premio': 'Prêmio 2'}, {'mes_ano': c1_p2e_mes_ano, 'valor': c1_p2e_valor, 'premio': 'Prêmio 2 + Extra'}, {'mes_ano': c1_p3_mes_ano, 'valor': c1_p3_valor, 'premio': 'Prêmio 3'}, {'mes_ano': c1_p3e_mes_ano, 'valor': c1_p3e_valor, 'premio': 'Prêmio 3 + Extra'},
                {'mes_ano': c2_p1_mes_ano, 'valor': c2_p1_valor, 'premio': 'Prêmio 1'}, {'mes_ano': c2_p2_mes_ano, 'valor': c2_p2_valor, 'premio': 'Prêmio 2'}, {'mes_ano': c2_p2e_mes_ano, 'valor': c2_p2e_valor, 'premio': 'Prêmio 2 + Extra'}, {'mes_ano': c2_p3_mes_ano, 'valor': c2_p3_valor, 'premio': 'Prêmio 3'}, {'mes_ano': c2_p3e_mes_ano, 'valor': c2_p3e_valor, 'premio': 'Prêmio 3 + Extra'},
                {'mes_ano': c3_p1_mes_ano, 'valor': c3_p1_valor, 'premio': 'Prêmio 1'}, {'mes_ano': c3_p2_mes_ano, 'valor': c3_p2_valor, 'premio': 'Prêmio 2'}, {'mes_ano': c3_p2e_mes_ano, 'valor': c3_p2e_valor, 'premio': 'Prêmio 2 + Extra'}, {'mes_ano': c3_p3_mes_ano, 'valor': c3_p3_valor, 'premio': 'Prêmio 3'}, {'mes_ano': c3_p3e_mes_ano, 'valor': c3_p3e_valor, 'premio': 'Prêmio 3 + Extra'},
                {'mes_ano': c4_p1_mes_ano, 'valor': c4_p1_valor, 'premio': 'Prêmio 1'}, {'mes_ano': c4_p2_mes_ano, 'valor': c4_p2_valor, 'premio': 'Prêmio 2'}, {'mes_ano': c4_p2e_mes_ano, 'valor': c4_p2e_valor, 'premio': 'Prêmio 2 + Extra'}, {'mes_ano': c4_p3_mes_ano, 'valor': c4_p3_valor, 'premio': 'Prêmio 3'}, {'mes_ano': c4_p3e_mes_ano, 'valor': c4_p3e_valor, 'premio': 'Prêmio 3 + Extra'},
            ]
            regras_premiacao = []
            for regra in regras_brutas:
                if regra['valor'] > 0:
                    anomes_fmt = parse_mes_ano(regra['mes_ano'])
                    if anomes_fmt:
                        regras_premiacao.append({'anomes': anomes_fmt, 'valor': regra['valor'], 'premio': regra['premio']})
            
            st.info(f"⚙️ {len(regras_premiacao)} regras ativas foram configuradas.")

            # O BLOCO TRY/EXCEPT FOI REMOVIDO PARA DEBUGAR
            # O CÓDIGO AGORA VAI QUEBRAR E MOSTRAR O ERRO REAL

            # AQUI É A MUDANÇA: Lê o arquivo pelo nome
            df = pd.read_excel(nome_do_arquivo)
            
            df['AnoMes'] = (df['AnoMes'] % 10000) * 100 + (df['AnoMes'] // 10000)
            if df['PRC_CATALOGO'].dtype == 'object':
                df['PRC_CATALOGO'] = df['PRC_CATALOGO'].astype(str).str.replace(',', '.').astype(float)
            else:
                df['PRC_CATALOGO'] = df['PRC_CATALOGO'].astype(float)
            
            st.info("📊 Base de vendas carregada. Agrupando dados...")
            
            df_agrupado = df.groupby(['CLIENTE', 'AnoMes', 'REGIAO']).agg(PRC_CATALOGO_TOTAL=('PRC_CATALOGO', 'sum')).reset_index()
            
            def definir_premio_dinamico(row, regras):
                anomes_cliente = row['AnoMes']
                valor_cliente = row['PRC_CATALOGO_TOTAL']
                regras_do_mes = [r for r in regras if r['anomes'] == anomes_cliente]
                if not regras_do_mes: return 'Sem Prêmio'
                regras_do_mes_ordenadas = sorted(regras_do_mes, key=lambda x: x['valor'], reverse=True)
                for regra in regras_do_mes_ordenadas:
                    if valor_cliente >= regra['valor']: return regra['premio']
                return 'Sem Prêmio'
            
            st.info("🧠 Aplicando regras e calculando as premiações...")
            
            df_agrupado['Resultado'] = df_agrupado.apply(lambda row: definir_premio_dinamico(row, regras_premiacao), axis=1)
            df_premiados = df_agrupado[df_agrupado['Resultado'] != 'Sem Prêmio'].copy()
            df_premiados.rename(columns={'CLIENTE': 'cliente', 'PRC_CATALOGO_TOTAL': 'PRC CATALOGO', 'REGIAO': 'REGIÃO', 'AnoMes': 'ANO/MÊS'}, inplace=True)
            df_final = df_premiados[['cliente', 'PRC CATALOGO', 'REGIÃO', 'ANO/MÊS', 'Resultado']]
            df_final['PRC CATALOGO'] = df_final['PRC CATALOGO'].apply(lambda x: f'{x:,.2f}'.replace(",", "TEMP").replace(".", ",").replace("TEMP", "."))
            
            st.success("✅ Cálculos finalizados com sucesso!")
            st.header("3. Resultados")
            st.dataframe(df_final)
            
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_final.to_excel(writer, index=False, sheet_name='Premiados')
            
            st.sidebar.download_button(label="📥 Baixar Relatório de Premiados (.xlsx)", data=output.getvalue(), file_name='resultado_premiacao_dinamico.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    else:
        st.warning("⚠️ Por favor, digite o nome do arquivo da base de vendas antes de gerar o relatório.")