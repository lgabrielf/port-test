import socket
import streamlit as st

def test_tcp_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Define um timeout de 2 segundos
            s.connect((host, port))
        return True
    except socket.error:
        return False

def test_udp_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(2)  # Define um timeout de 2 segundos
            s.sendto(b'', (host, port))
            s.recvfrom(1024)
        return True
    except socket.error:
        return False

# Interface com Streamlit
st.title("Teste de Portas TCP/UDP")

host = st.text_input("Host", "localhost")
port = st.number_input("Porta", 0, 65535, step=1)

if st.button("Testar TCP"):
    result = test_tcp_port(host, port)
    if result:
        st.success("Porta TCP está aberta!")
    else:
        st.error("Porta TCP está fechada.")

if st.button("Testar UDP"):
    result = test_udp_port(host, port)
    if result:
        st.success("Porta UDP está aberta!")
    else:
        st.error("Porta UDP está fechada.")
