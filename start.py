from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 간단한 메모리 기반 데이터베이스
animations = []

@app.route('/')
def index():
    return render_template('index.html', animations=animations)

@app.route('/add_animation', methods=['POST'])
def add_animation():
    title = request.form.get('title')
    link = request.form.get('link')

    if title and link:
        new_animation = {'title': title, 'link': link}
        animations.append(new_animation)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
