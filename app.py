import os
import json
from flask import Flask, render_template, redirect, url_for, request, flash

path = os.getcwd()
data = os.path.join(path , "data.json")

def getAllJobs():
    with open(data,"r",encoding='utf-8') as f:
        alljobs = json.load(f)

    return alljobs

def updateJob(newData):
    with open(data,"r",encoding='utf-8') as f:
        jobs = json.load(f)

    jobs.append(newData)
    return jobs

def editJob(newData, id):
    with open(data, "r", encoding='utf-8') as f:
        jobs = json.load(f)
    # type,url,created_at,company,company_url,location,title,description,how_to_apply,company_logo
    for job in jobs:
        if job['id'] == int(id):
            jb = job
            jb['id'] = newData['id']
            jb['title'] = newData['title']
            jb['type'] = newData['type']
            jb['description'] = newData['description']
            jb['location'] = newData['location']
            jb['company']['name'] = newData['company']['name']
            jb['company']['description'] = newData['company']['description']
            jb['company']['contactEmail'] = newData['company']['contactEmail']
            jb['company']['contactPhone'] = newData['company']['contactPhone']
            break

    with open(data, 'w') as f:
        json.dump(jobs, f, indent=2)
    getAllJobs()

def deleteData(id):
    print(f'from def deleteData: {id}')
    with open(data, "r", encoding='utf-8') as f:
        jobs = json.load(f)

    for i in range(len(jobs)):
        if jobs[i]["id"] == int(id):
            print(f'found data')
            jobs.pop(i)
            break

    with open(data, 'w') as f:
        json.dump(jobs, f, indent=2)
    getAllJobs()

def set_jid():
    getAllJobs()
    max_id = len(alljobs)
    return max_id

def addJob(newData):
    if newData:
        with open(data, "r", encoding='utf-8') as f:
            jobs = json.load(f)

        print(newData)
        jobs.append(newData)

        with open(data, 'w') as f:
            json.dump(jobs, f, indent=2)
        getAllJobs()

# End of Function

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods = ['POST', 'GET'])
def index():
    alljobs = getAllJobs()
    flash("Welcome to Flask Job!", "success" )
    return render_template("home.html", status="home", alljobs=alljobs)

@app.route("/jobs", methods = ['POST', 'GET'])
def jobs():
    alljobs = getAllJobs()
    return render_template("alljobs.html", status="jobs", alljobs=alljobs)

@app.route("/add_job", methods = ['POST', 'GET'])
def add_job():
    return render_template("addjob.html", status="addjob")

@app.route("/job", methods = ['POST', 'GET'])
def job():
    return render_template("job.html", status="jobs")

@app.route("/get_job/<id>", methods = ['POST', 'GET'])
def get_job(id):
    alljobs = getAllJobs()
    for job in alljobs:
        if job['id'] == int(id):
            gjb = job
            break
    return render_template("getjob.html", status="jobs", job=gjb, jid=id)

@app.route("/edit_job", methods = ['POST', 'GET'])
def edit_job():
    alljobs = getAllJobs()
    if request.method == 'POST':
        id = request.form['jobID']
        for job in alljobs:
            jb = job
            if job['id'] == int(id):
                break
        flash("Edited Job Completed!", "success")
        return render_template("editjob.html", status="addjob", job=jb)
    else:
        # alljobs = getAllJobs()
        return redirect(url_for("index", status="jobs", alljobs=alljobs))

@app.route("/update_job", methods = ['POST', 'GET'])
def update_job():
    if request.method == 'POST':
        id = request.form['jobID']
        type = request.form['type']
        jobtitle = request.form['jobtitle']
        description = request.form['description']
        salary = request.form['salary']
        location = request.form['location']
        company = request.form['company']
        companyDescription = request.form['company_description']
        contactEmail = request.form['contact_email']
        contactPhone = request.form['contact_phone']

        newData = {
            "id": int(id),
            "title": jobtitle,
            "type": type,
            "description": description,
            "location": location,
            "salary": salary,
            "company": {
                "name": company,
                "description": companyDescription,
                "contactEmail": contactEmail,
                "contactPhone": contactPhone,
            }
        }

        editJob(newData, id)
        alljobs = getAllJobs()
        flash("Job has updated!", "success")
        return render_template("home.html", status="home", alljobs=alljobs)
    else:
        alljobs = getAllJobs()
        return redirect(url_for("index", status="jobs", alljobs=alljobs))

@app.route("/delete_job", methods = ['POST', 'GET'])
def delete_job():
    alljobs = getAllJobs()
    if request.method == 'POST':
        id = request.form['deletejobID']
        print(f'from delete_job route: {id}')
        for job in alljobs:
            if job['id'] == int(id):
                djb = job
                deleteData(id)
                # print(djb)
                break
    alljobs = getAllJobs()
    flash("Job deleted!", "success")
    return render_template("home.html", status="home", alljobs=alljobs)

@app.route("/add_newjob", methods = ['POST', 'GET'])
def add_newjob():
    if request.method == 'POST':
        type = request.form['type']
        jobtitle = request.form['jobtitle']
        description = request.form['description']
        salary = request.form['salary']
        location = request.form['location']
        company = request.form['company']
        companyDescription = request.form['company_description']
        contactEmail = request.form['contact_email']
        contactPhone = request.form['contact_phone']

        max_id = set_jid()
        new_id = max_id + 1
        newData = {
            "id": int(new_id),
            "title": jobtitle,
            "type": type,
            "description": description,
            "location": location,
            "salary": salary,
            "company": {
                "name": company,
                "description": companyDescription,
                "contactEmail": contactEmail,
                "contactPhone": contactPhone,
            }
        }

        print(newData)
        addJob(newData)
        alljobs = getAllJobs()
        flash("Job added!", "success")
        return render_template("home.html", status="home", alljobs=alljobs)
    else:
        alljobs = getAllJobs()
        return redirect(url_for("index", status="jobs", alljobs=alljobs))



if __name__ == '__main__':
    alljobs = getAllJobs()
    for job in alljobs:
        print(job['id'], job['type'], job['company'])

    app.run()