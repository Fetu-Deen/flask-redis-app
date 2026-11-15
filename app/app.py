
from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'cache'),
    port=int(os.getenv('REDIS_PORT', '6379')),
    decode_responses=True
)

# Shared styling
STYLE = """
<style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: Arial, sans-serif;
        color: #f8fafc;
        background:
            radial-gradient(circle at top left, #1e3a5f, transparent 45%),
            linear-gradient(135deg, #0f172a, #111827);
    }

    .card {
        width: 90%;
        max-width: 500px;
        padding: 50px 35px;
        text-align: center;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }

    .badge {
        display: inline-block;
        padding: 8px 14px;
        margin-bottom: 20px;
        border-radius: 30px;
        background: rgba(52, 211, 153, 0.12);
        color: #6ee7b7;
        font-size: 12px;
        letter-spacing: 1px;
    }

    h1 {
        font-size: 30px;
        margin-bottom: 15px;
    }

    p {
        color: #94a3b8;
        line-height: 1.7;
        margin-bottom: 30px;
    }

    .button {
        display: inline-block;
        padding: 14px 25px;
        border-radius: 10px;
        background: #6366f1;
        color: white;
        text-decoration: none;
        font-weight: bold;
        transition: 0.2s ease;
    }

    .button:hover {
        background: #4f46e5;
        transform: translateY(-2px);
    }

    .number {
        font-size: 65px;
        font-weight: bold;
        color: #818cf8;
        margin: 25px 0;
    }

    .footer {
        margin-top: 35px;
        font-size: 12px;
        color: #64748b;
    }
</style>
"""

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Redis Counter</title>
        {STYLE}
    </head>
    <body>
        <div class="card">
            <div class="badge">● REDIS-POWERED COUNTER</div>
            <h1>Welcome!</h1>
            <p>
                Your application is running with Flask and Redis.
                Curious about how many times the counter has been accessed?
            </p>
            <a href="/count" class="button">See Number of Visits →</a>
            <div class="footer">Built with Flask · Redis · Docker</div>
        </div>
    </body>
    </html>
    """

@app.route('/count')
def get_count():
    count = r.incr('visits')

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visit Counter</title>
        {STYLE}
    </head>
    <body>
        <div class="card">
            <div class="badge">● COUNTER UPDATED</div>
            <h1>Total Visits</h1>
            <div class="number">{count}</div>
            <p>Your counter is stored and managed by Redis.</p>
            <a href="/" class="button">← Back Home</a>
            <div class="footer">Flask + Redis Counter Application</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
