from flask import Flask, redirect, url_for, request, render_template 
from urllib.parse import urlencode
app = Flask(__name__)

@app.route('/', methods=['GET'], defaults={'inputValues':','.join(map(str,["" for _ in range(16)]))})
@app.route('/<inputValues>')
def getInput(inputValues):
    inputList=[x for x in inputValues.split(',')]
    return render_template('quartileInput.html', inputValues=inputList)

@app.route('/puzzlesubmission',methods = ['POST'])
def submission():
  val = request.form.getlist('val[]')
  if any(item == "" for item in val):
      return redirect(url_for('getInput', inputValues=','.join(map(str,val))))
  else:
      return render_template('quartileResult.html', result = val)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
