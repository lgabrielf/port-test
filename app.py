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

def test_udp_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(2)
            s.sendto(b'', (host, port))
            s.recvfrom(1024)
        return True
    except socket.error:
        return False

st.title("TCP/UDP Port Test")

host = st.text_input("Hostname", "IP Adress")
port = st.number_input("Port", 0, 65535, step=1)

st.markdown("<en>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("TCP Test"):
        result = test_tcp_port(host, port)
        if result:
            st.success("TCP port is open!")
        else:
            st.error("TCP port is close.")

with col2:
    if st.button("UDP Test"):
        result = test_udp_port(host, port)
        if result:
            st.success("UDP port is open!")
        else:
            st.error("UDP port is close.")