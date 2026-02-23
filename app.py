from flask import Flask, render_template

app = Flask(__name__)

# 1. Trang chủ & Bio
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/projects')
def projects():
    # Phải đổi thành danh sách Dictionary có cả 'name' và 'url' thì HTML mới hiểu được
    my_list = [
        {"name": "My Career Blueprint", "url": "/cv"},
        {"name": "Landing Page 2026", "url": "#"},
        {"name": "Bot Discord AI", "url": "#"},
        {"name": "Hệ thống quản lý RAM 4GB", "url": "#"}
    ]
    return render_template('projects.html', projects=my_list)

@app.route('/english')
def english():
    my_apps = [
        {"id": "001", "title": "Endless Alphabet", "tag": "Interactive Vocabulary Engine", "link": "/game-english"},
        {"id": "002", "title": "Word Arrangement", "tag": "Grammar Logic & Structure", "link": "/word-master"},
        {"id": "003", "title": "Ancient Tales Reader", "tag": "Bilingual Narrative Processor", "link": "/story-reader"},
        {"id": "004", "title": "Word Family", "tag": "Vocabulary Patterns & Groups", "link": "/word-family"}
    ]
    return render_template('apps/english.html', apps=my_apps)

# 2. Các Route ứng dụng (Nằm trong folder templates/apps)
@app.route('/game-english')
def game_english():
    return render_template('apps/game.html')

@app.route('/word-master')
def word_master():
    return render_template('apps/xepchu.html')

@app.route('/story-reader')
def story_reader():
    return render_template('apps/truyen.html')

@app.route('/word-family')
def word_family():
    return render_template('apps/wordfamily.html')

# 3. Trang CV điện tử (Nằm trong folder templates)
@app.route('/cv')
def cv():
    return render_template('cv.html')

# 4. Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
