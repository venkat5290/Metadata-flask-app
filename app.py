from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    #defining the urls
    name_url = "http://metadata.google.internal/computeMetadata/v1/instance/name"
    id_url = "http://metadata.google.internal/computeMetadata/v1/instance/id"
    hostname_url = "http://metadata.google.internal/computeMetadata/v1/instance/hostname"
    zone_url = "http://metadata.google.internal/computeMetadata/v1/instance/zone"
    machinetype_url = "http://metadata.google.internal/computeMetadata/v1/instance/machine-type"
    project_url = "http://metadata.google.internal/computeMetadata/v1/project/project-id"
    internalip_url = "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip"
    externalip_url = "http://metadata/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip"

    instance_ep = {}
    for prop in ["name_url", "id_url", "hostname_url", "zone_url", "machinetype_url", "project_url", "internalip_url", "externalip_url"]:
        instance_ep[prop] = eval(prop)

    instance = getMetadata(instance_ep)

    return render_template('index.html', instance=instance)


def getMetadata(d):
    instance = {}
    for key in d.keys():
        url = d[key]
        r = requests.get(url, headers={"Metadata-Flavor": "Google"})
        instance[key.split('_')[0]] = r.text

    return instance


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=8000)




