from flask import Flask
import json

app = Flask(__name__)

with open("candidates.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route("/")
def main_page():
    text = ""
    for i in data:
        for key, value in i.items():
            if key in ["picture", "id"]:
                continue
            text += f"{key}: {', '.join(value) if isinstance(value, list) else value}\n"

        text += "\n"
        
    return f"<pre>{text}</pre>"

@app.route("/candidate/<id>")
def candidate_page(id):
    id = int(id)
    text = ""
    for i in data:
        if i["id"] == id:
            text += f"<img src='{i['picture']}'>\n"
            for key, value in i.items():
                if key in ["picture", "id"]:
                    continue
                text += f"{key}: {', '.join(value) if isinstance(value, list) else value}\n"

    if text == "":
        return f"<pre>No such employee</pre>"
               
    return f"<pre>{text}</pre>"

@app.route("/skill/<id>")
def skill_page(id):
    text = ""
    for i in data:
        if id in i["skills"]:
            for key, value in i.items():
                if key in ["picture", "id", "picture"]:
                    continue
                text += f"{key}: {', '.join(value) if isinstance(value, list) else value}\n"

            text += "\n"
    if text == "":
        return f"<pre>No such skill</pre>"
    
    return f"<pre>{text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)