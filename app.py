import socket
import streamlit as st

def test_tcp_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
        return True
    except socket.error:
        return False


st.title("TCP Port Test")

host = st.text_input("Hostname", "IP Adress")
port = st.number_input("Port", 0, 65535, step=1)

st.markdown("<en>", unsafe_allow_html=True)

if st.button("TCP Test"):
    result = test_tcp_port(host, port)
    if result:
        st.success("TCP port is open!")
    else:
        st.error("TCP port is close.")
