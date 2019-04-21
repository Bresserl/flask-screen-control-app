from flask import Blueprint, render_template, url_for, flash, redirect, request, send_file
from werkzeug.urls import url_parse
import os
from io import BytesIO
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import Login_form, Video_upload_form, File_upload_form, Text_upload_form
from app.models import Person, Text, File, Video
from flask_login import current_user, login_user, logout_user, login_required


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def show_content():
    file_data = File.query.filter_by(id=6).first()
    return send_file(BytesIO(file_data.file), attachment_filename='file.png')
    return render_template('show_content.html')
# to do : automate this ^


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.upload_mainpage'))
    form = Login_form()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.upload_mainpage')
            return redirect(next_page)
        return redirect(url_for('main.upload_mainpage'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
    return render_template('logout.html')


@main.route('/upload')
@login_required
def upload_mainpage():
    return render_template('manage.html')


@main.route('/upload/file', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = File_upload_form()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file!')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file!')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            newFile = File(title=file.filename, file=file.read())
            db.session.add(newFile)
            db.session.commit()
        return redirect(url_for('main.upload_mainpage'))
    return render_template('file.html', form=form)


@main.route('/upload/video', methods=['GET', 'POST'])
@login_required
def upload_video():
    form = Video_upload_form()
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']
        if url and title:
            newFile = Video(url=url, title=title)
            db.session.add(newFile)
            db.session.commit()
            return redirect(url_for('main.upload_mainpage'))
        return redirect(url_for('main.upload_video'))
    return render_template('video.html', form=form)


@main.route('/upload/text', methods=['GET', 'POST'])
@login_required
def upload_text():
    form = Text_upload_form()
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if title and text:
            newFile = Text(title=title, text=text)
            db.session.add(newFile)
            db.session.commit()
            return redirect(url_for('main.upload_mainpage'))
        return redirect(url_for('main.upload_text'))
    return render_template('text.html', form=form)


@main.route('/database')
@login_required
def database():
    return render_template('database.html')
