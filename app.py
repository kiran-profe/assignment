from flask import Flask, jsonify, redirect, request, render_template, flash, url_for
import sqlite3
from forms import Form
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=["GET"])
def home():
    conn = sqlite3.connect("staffs.sqllite")
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM staff")
    staffs = [
        dict(id=row[0], name=row[1], number=row[2])
        for row in cursor.fetchall()
    ]
    return render_template('main.html', staffs=staffs)


@app.route('/user', methods=["GET", "POST"])
def add():
    conn = sqlite3.connect("staffs.sqllite")
    cursor = conn.cursor()
    form = Form()
    if request.method == "POST":
        new_name = request.form['user']
        new_number = request.form["number"]
        sql = """INSERT INTO staff (user, number) VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_number))
        conn.commit()
        flash(f'Added Successfully', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect("staffs.sqllite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff WHERE id=?", (id,))
    rows = cursor.fetchall()
    for r in rows:
        staff = r

    form = Form(obj=staff)

    if request.method == "POST":
        sql = """UPDATE staff
                SET user=?, number=? WHERE id=? """

        user = request.form["user"]
        number = request.form["number"]
        updated_book = {
            "id": id,
            "user": user,
            "number": number,
        }
        conn.execute(sql, (user, number, id))
        conn.commit()
        flash(f'Edited Successfully', 'success')
        return redirect(url_for('home'))
    else:

        return render_template('edit.html', item=staff, form=form, edit=True)


if __name__ == '__main__':
    app.run(debug=True)
