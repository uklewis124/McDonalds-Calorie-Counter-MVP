from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def preprocess_data(data):
    risk_level = []
    risk_level_text = []
    for i in range(len(data)):
        cc = data['Calories'][i]
        if cc < 200:
            risk_level.append('low-risk')
            risk_level_text.append('Low Risk')
        elif cc < 400:
            risk_level.append('med-risk')
            risk_level_text.append('Medium Risk')
        else:
            risk_level.append('high-risk')
            risk_level_text.append('High Risk')
    
    data["risk_level"] = risk_level
    data["risk_level_text"] = risk_level_text
    return data


@app.route('/')
def index():
    new_df = preprocess_data(pd.read_csv('data/menu.csv'))

    items = new_df.to_dict('records')

    return render_template('index.html', items = items)

if __name__ == "__main__":
    app.run(debug=True)