from flask import Flask  # import해서 flask를 갖고온다.

app = Flask(__name__)  # 폴더이름이 들어온다.
app.run(debug=True)
