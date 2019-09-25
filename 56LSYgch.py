from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load Database
df_database = pd.read_csv("Database/database.csv", sep=",", encoding="utf-8")


# Routing

@app.route("/<int:school_id>")
def getStudentsFromSchool(school_id):
	df = df_database[df_database['escola_criacao_id'] == school_id].copy()
	return json.dumps(df.to_dict('records'))

if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)