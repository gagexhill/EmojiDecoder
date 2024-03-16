from flask import Flask, render_template, request, jsonify

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json() or {}
        user_text = data.get('user_text', '')
        if user_text:
            result = emojidecoder.main(user_text)
            return jsonify(result)
        else:
            return jsonify({"error": "No text provided"}), 400  # Bad request
    return render_template('index.html')