
color1 = "F1F2F6" 
color2 = "FF8600"
color3 = "AEB8FE" #font color
color4 = "758BFD"
color5 = "27187E" #background color

backgroundColor = color5
fontColor = color3

def mainStyleSheet():
    styleSheet = (f"""                  
    QMainWindow {{
        background-color: #{backgroundColor};
        font-family: Poppins;
        font-size: 16px;
        color: #{fontColor};
    }}

    QPushButton {{
        background-color: #{color1};
        color: #black;
        font-weight: bold;
        padding: 16px;
        font-family: Poppins;
        font-size: 16px;
        border: none;
        border-radius: 4px;
    }}
    
    QLabel {{
        font-family: Poppins;
        font-size: 16px;
        font-weight: semi-bold;
        color: #{fontColor};
    }}
    """)
    
    return styleSheet