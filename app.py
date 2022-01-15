from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toDo.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Araba(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    araba_adi = db.Column(db.String())
    araba_modeli = db.Column(db.Text)
    durum = db.Column(db.Boolean)
    musteri_id = db.Column(db.Integer, db.ForeignKey('musteri.id'))


class Musteri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    musteri_adi = db.Column(db.String())
    kiralama_suresi = db.Column(db.Text)
    arabalar = db.relationship('Araba', backref='musteri')



@app.route('/',methods=["POST","GET"])
def index():  # put application's code here
    todos = Araba.query.all()
    return render_template("musteri.html", todos = todos)


@app.route('/musteri',methods=["POST","GET"])
def musteri():  # put application's code here
    todos = Musteri.query.all()
    return render_template("musteri.html", todos = todos)


@app.route('/add', methods=["POST"])
def addTodo():
    araba_adi = request.form.get("araba_adi")
    araba_modeli = request.form.get("araba_modeli")

    newTodo = Araba(araba_adi = araba_adi, araba_modeli = araba_modeli, durum =True)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/addmusteri', methods=["POST"])

def addToMusteri():
    musteri_adi = request.form.get("musteri_adi")
    kiralama_suresi = request.form.get("kiralama_suresi")

    newMusteri = Musteri(musteri_adi = musteri_adi, kiralama_suresi = kiralama_suresi)
    db.session.add(newMusteri)
    db.session.commit()
    return redirect(url_for("musteri"))

@app.route("/deletemusteri/<string:id>")
def delete(id):
    todo = Musteri.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/complete/<string:id>")
def complete(id):
    todo = Araba.query.filter_by(id=id).first()
    if(todo.durum == False):
        todo.durum = True
    else:
        todo.durum = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    todo = Araba.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
