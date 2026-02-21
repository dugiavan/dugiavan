from flask import Flask, render_template

app = Flask(__name__)

# 1. Trang chủ & Bio (Giữ nguyên vì nằm ngoài folder apps)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/projects')
def projects():
    my_list = ["Landing Page 2026", "Bot Discord AI", "Hệ thống quản lý RAM 4GB"]
    return render_template('projects.html', projects=my_list)

@app.route('/english')
def english():
    my_apps = [
        {"id": "001", "title": "Endless Alphabet", "tag": "Interactive Vocabulary Engine", "link": "/game-english"},
        {"id": "002", "title": "Word Arrangement", "tag": "Grammar Logic & Structure", "link": "/word-master"},
        {"id": "003", "title": "Ancient Tales Reader", "tag": "Bilingual Narrative Processor", "link": "/story-reader"},
        {"id": "004", "title": "Word Family", "tag": "Vocabulary Patterns & Groups", "link": "/word-family"}
    ]
    # SỬA Ở ĐÂY: Thêm 'apps/' vào trước 'english.html'
    return render_template('apps/english.html', apps=my_apps)

# --- PHẦN SỬA CHÍNH: Thêm 'apps/' vào đường dẫn ---

@app.route('/game-english')
def game_english():
    return render_template('apps/game.html') # Sửa ở đây

@app.route('/word-master')
def word_master():
    return render_template('apps/xepchu.html') # Sửa ở đây

@app.route('/story-reader')
def story_reader():
    return render_template('apps/truyen.html') # Sửa ở đây

@app.route('/word-family')
def word_family():
    return render_template('apps/wordfamily.html') # Sửa ở đây
    
# 4. DÒNG NÀY LUÔN Ở CUỐI CÙNG
if __name__ == '__main__':
    app.run(debug=True)