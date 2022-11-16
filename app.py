from flask import Flask, render_template, request
from os import mkdir, path, chdir, system, listdir, getcwd
from uuid import uuid4
import shutil

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    path_atual = getcwd()
    if request.method == "POST":
        url_repo = request.form.get("url")
        username = url_repo.split("/")[3]
        folder_name = f"{uuid4()}-{username}"
        
        if path.exists("./repos-downloaded/"):
            mkdir(path = f"./repos-downloaded/{folder_name}")
        else:
            mkdir(path="./repos-downloaded/")
            mkdir(path = f"./repos-downloaded/{folder_name}")
        
        chdir(f"./repos-downloaded/{folder_name}")
        system("echo 'Dentro da pasta'")
        system(f"git clone {url_repo}")
    
    for file in listdir("./"):
        chdir(file)
        for file2 in listdir("./"):
            if file2.endswith(".hex"):
                if path.exists("../../../file-to-test/"):
                    shutil.copy(f"./{file2}", f"../../../file-to-test/{folder_name}.hex")
                else:
                    mkdir(path="../../../file-to-test")
                    shutil.copy(f"./{file2}", f"../../../file-to-test/{folder_name}.hex")

    chdir(path_atual)
    return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True) 