from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    playbooks = os.listdir('playbooks')
    return render_template('index.html', playbooks=playbooks)

@app.route('/run/<playbook>')
def run_playbook(playbook):
    playbook_path = os.path.join('playbooks', playbook)
    command = f"ansible-playbook -i hosts {playbook_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify(stdout=result.stdout, stderr=result.stderr)

@app.route('/run_all')
def run_all_playbooks():
    playbooks = os.listdir('playbooks')
    results = {}
    for playbook in playbooks:
        playbook_path = os.path.join('playbooks', playbook)
        command = f"ansible-playbook -i hosts {playbook_path}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[playbook] = {'stdout': result.stdout, 'stderr': result.stderr}
    return jsonify(results)

@app.route('/upload', methods=['POST'])
def upload_playbook():
    file = request.files['file']
    file.save(os.path.join('playbooks', file.filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
