from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

project_proposals = [
 {
     "netid": "abc123",
     "title": "Pizza on U",
     "description": "A site that adds a slice of pizza to images",
     "modules": ["flask", "pil"]
 },        
 {
     "netid": "xyz789",
     "title": "Catfinity",
     "description": "Creates a collage of random cat images",
     "modules": ["pil", "requests"]
 },        
 {
     "netid": "ynot42",
     "title": "hippost",
     "description": "An image board for hippo enthusiasts",
     "modules": ["flask", "pil"]
 }        
]

@app.route('/')
def hello_world():
    return render_template("home.html")
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if(request.method == 'GET'):
        return render_template("projects.html", project_proposals=project_proposals)
    else:
        modules=request.form['modules'].split(",")
        tmpItem={"netid":request.form['netid'], "title":request.form['title'], "description":request.form['description'], "modules":modules}
        project_proposals.append(tmpItem)
        return redirect('/projects')

@app.route('/report')
def report():
    module_counts={};
    for val in project_proposals:
        for i in range(len(val['modules'])):
            if(module_counts.has_key(val['modules'][i])):
                module_counts[val['modules'][i]]+=1;
            else:
                module_counts[val['modules'][i]]=1;
    return render_template('/report.html', module_counts=module_counts)
    

if __name__ == '__main__':
    app.debug = True
    app.run()