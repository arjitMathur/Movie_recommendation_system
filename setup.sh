#!/bin/bash
mkdir -p ~/.streamlit

cat > ~/.streamlit/config.toml << EOF
[server]
port = $PORT
address = "0.0.0.0"
headless = true
enableCORS = false
EOF
