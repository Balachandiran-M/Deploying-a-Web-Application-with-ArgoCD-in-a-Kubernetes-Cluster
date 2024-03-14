from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get current CPU utilization
    cpu_text = f"<h1>CPU UTILIZATION: {cpu_percent}%</h1>"
    centered_cpu_text = f"""
    <div style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);'>
        <div style='border: 2px solid black; padding: 10px; text-align: center;'>
            {cpu_text}
        </div>
    </div>
    """
    return centered_cpu_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



