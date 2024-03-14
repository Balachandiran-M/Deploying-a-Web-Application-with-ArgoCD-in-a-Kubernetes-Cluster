from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or memory usage detected"
    
    # HTML and CSS styling for centering, border, and font size
    html_content = f"""
    <div style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);'>
        <div style='border: 2px solid black; padding: 10px; text-align: center; font-size: 20px;'>
            <p style='font-size: 24px;'>CPU UTILIZATION: {cpu_percent}%<br>Memory utilization: {mem_percent}%</p>
            <p style='font-size: 18px;'>{Message}</p>
        </div>
    </div>
    """
    
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

