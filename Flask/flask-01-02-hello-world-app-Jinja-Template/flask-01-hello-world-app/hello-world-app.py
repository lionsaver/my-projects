from flask import Flask  # bu kod "must" dır ve ilk olarak Flask kütüphanesini çeker.

app = Flask(__name__)   #BU kod satırı da "must" dır. app adında bir obje oluşturur.

# Herhangibir port girilmezse default olarak 5000 portu geçerlidir.

@app.route('/')  # web syafası birinci adresi, localhost:5000 url adresi girildiğinde bu
def hello():
    return "Hello World from Flask!!!"  

@app.route('/second')
def second():
    return 'Bize Her Yer Trabzon!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth')
def forth():
    return 'Never give up'

@app.route('/fifth/<string:id>')
def fifth(id):
    return f'Id number of this page is {id}'

if __name__ == '__main__':  # Bu kod satırı da must dır. Eğer doğruysa çalıştır şeklinde kontrol mekanizması oluşturur.
    app.run(debug=True, port=2000)  # Bu satırda çalışan bir port bulunması gerekiyor. DEfault(5000) port haricinde bir port için tanımlama yapılmalıdır.
