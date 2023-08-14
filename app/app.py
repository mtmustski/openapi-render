from api_doc import ApiDoc
import json
import os
import yaml

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    api_docs = []
    for json_file in os.listdir(os.path.join("static", "api-docs")):
        if json_file.endswith(".json"):
            api_docs.append(get_api_doc(json_file))

    return render_template('index.html', api_docs=api_docs)


@app.route('/<api_doc>', methods=['GET'])
def openapi(api_doc):
    return render_template('openapi-render.html', api=get_api_doc(api_doc + ".json"))


def get_api_doc(json_file):
    with open(os.path.join("static", "api-docs", json_file)) as config:
        config = json.loads(config.read())
        with open(os.path.join("static", "api-docs", config['source'])) as api:
            api = yaml.safe_load(api.read())
            return ApiDoc(api['info']['title'], api['info']['description'], api['info']['version'],
                          api['info']['contact']['name'], api['info']['contact']['url'],
                          json_file.replace(".json", ""), config['project_page'],
                          os.path.join("static", "api-docs", config['source']))


if __name__ == "__main__":
    app.run()
