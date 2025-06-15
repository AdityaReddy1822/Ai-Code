# video_api.py
from flask import Flask, request, jsonify
import os
from moviepy.editor import *

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_video():
    prompt = request.json.get('prompt', 'Default Text')
    filename = f"reel_{str(abs(hash(prompt)))[:6]}.mp4"
    output_path = f"/app/static/{filename}"

    # Generate a simple video
    clip = TextClip(prompt, fontsize=70, color='white', size=(1080, 1920), bg_color='black')
    clip = clip.set_duration(7)
    clip.write_videofile(output_path, fps=24)

    return jsonify({
        "video_url": f"https://your-server.com/static/{filename}"
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
