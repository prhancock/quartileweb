import quartiles
from flask import Flask, redirect, url_for, request, render_template 
from urllib.parse import urlencode
app = Flask(__name__)

@app.route('/', methods=['GET'])
def getInput():
    inputValues=request.args.get('inputValues',','.join(map(str,["" for _ in range(20)])))
    error=request.args.get('error','')
    inputList=[x for x in inputValues.split(',')]
    return render_template('quartileInput.html', inputValues=inputList,errorMsg=errorString(error))

@app.route('/puzzlesubmission',methods = ['POST'])
def submission():
  val = request.form.getlist('val[]')
  if any(item == "" for item in val):
      return redirect(url_for('getInput', inputValues=','.join(map(str,val)), error='emptyFields'))
  else:
      wordList = quartiles.getWords(val)
      return render_template('quartileResult.html', result = val, wordList = wordList)

def errorString(error):
    if error=='emptyFields':
        return 'Error: Incomplete Fields'
    elif error=='':
        return ''
    else:
        return 'Unknown error'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
