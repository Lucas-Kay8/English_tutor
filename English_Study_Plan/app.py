from flask import Flask, render_template, jsonify, request
import os
import json
import time
from vocab_loader import load_vocab, get_all_words

app = Flask(__name__)

# Constants
VOCAB_FILE = "beijing_zhongkao_vocab_21days.md"
LISTENING_FILE = "listening_data.json"
CLOZE_FILE = "cloze_data.json"
PROGRESS_FILE = "vocab_progress.json"

def get_progress_file(user_id):
    if user_id == 'test':
        return "vocab_progress_test.json"
    return PROGRESS_FILE

def load_progress(user_id='oli'):
    filename = get_progress_file(user_id)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Error decoding {filename}")
                return {"mistakes": [], "history": [], "xp": 0, "streak": 0, "hearts": 5, "completedDays": []}
    return {"mistakes": [], "history": [], "xp": 0, "streak": 0, "hearts": 5, "completedDays": []}

def save_progress(progress, user_id='oli'):
    filename = get_progress_file(user_id)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=4, ensure_ascii=False)

# Global Data Cache
_cached_vocab_data = load_vocab(VOCAB_FILE)
_cached_listening_data = None
_cached_cloze_data = None
_cached_api_vocabulary = None

def get_cached_listening_data():
    global _cached_listening_data
    if _cached_listening_data is None:
        if os.path.exists(LISTENING_FILE):
            with open(LISTENING_FILE, 'r', encoding='utf-8') as f:
                try:
                    _cached_listening_data = json.load(f)
                    print(f"Cached listening data: {len(_cached_listening_data)} items")
                except Exception as e:
                    print(f"Error loading listening data: {e}")
                    _cached_listening_data = []
        else:
            _cached_listening_data = []
    return _cached_listening_data

def get_cached_cloze_data():
    global _cached_cloze_data
    if _cached_cloze_data is None:
        if os.path.exists(CLOZE_FILE):
            with open(CLOZE_FILE, 'r', encoding='utf-8') as f:
                try:
                    _cached_cloze_data = json.load(f)
                    print(f"Cached cloze data: {len(_cached_cloze_data)} items")
                except Exception as e:
                    print(f"Error loading cloze data: {e}")
                    _cached_cloze_data = []
        else:
            _cached_cloze_data = []
    return _cached_cloze_data

def get_cached_api_vocabulary():
    global _cached_api_vocabulary
    if _cached_api_vocabulary is None:
        result = []
        import re
        for day_num, words in _cached_vocab_data.items():
            try:
                day = int(''.join(filter(str.isdigit, day_num)))
            except:
                day = 1
            for word in words:
                example_en = word.get('example_en', '')
                example_en = re.sub(r'\*\*(.+?)\*\*', r'\1', example_en)
                result.append({
                    'word': word.get('word', ''),
                    'meaning': word.get('meaning', ''),
                    'example': example_en,
                    'day': day
                })
        _cached_api_vocabulary = result
    return _cached_api_vocabulary

@app.route('/')
def index():
    return render_template('index.html', version=time.time())

@app.route('/api/vocab')
def get_vocab():
    return jsonify(_cached_vocab_data)

@app.route('/api/all_words')
def get_all_words_route():
    all_words = get_all_words(_cached_vocab_data)
    return jsonify(all_words)

@app.route('/api/listening')
def get_listening():
    return jsonify(get_cached_listening_data())

@app.route('/api/cloze')
def get_cloze():
    return jsonify(get_cached_cloze_data())

@app.route('/api/vocabulary')
def get_vocabulary():
    """返回带有 day 属性的词汇列表供前端使用"""
    return jsonify(get_cached_api_vocabulary())


@app.route('/api/progress', methods=['GET', 'POST'])
def handle_progress():
    if request.method == 'GET':
        user_id = request.args.get('user', 'oli')
        print(f"Loading progress for user: {user_id}")
        return jsonify(load_progress(user_id))
    elif request.method == 'POST':
        data = request.json
        user_id = data.get('user', 'oli')
        # 如果是POST，前端可能会把user信息放在body里，也可能分开
        # 假设前端传回的整个json是progress数据，我们需要把user字段剔除或者约定好结构
        # 这里假设前端传回的结构是 { user: 'oli', data: {...} } 或者直接把 user 放在 query param
        
        # 为了兼容之前的代码，我们约定：
        # 如果 body 里有 wrap 结构 { user: '...', progress: {...} } 则解析
        # 否则认为是纯 progress 数据，user 取自 query param 或默认为 oli
        
        progress_data = data
        if 'progress' in data and 'user' in data:
             user_id = data['user']
             progress_data = data['progress']
        
        save_progress(progress_data, user_id)
        return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8888)
