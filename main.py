from db_config import app

@app.route("/")
def home():
    return 'Hello World'

if __name__=="__main__":
    app.run(port=5060,debug=True)