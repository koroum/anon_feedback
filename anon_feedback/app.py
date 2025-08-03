from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import sqlite3
import os


app = Flask(__name__)

# Database setup
DATABASE = 'feedback.db'

def init_db():
    """Initialize the database with feedback table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            starred BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def index():
    """Main page with feedback form and list"""
    return render_template('index.html')

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """Get all feedback with optional sorting"""
    sort_by = request.args.get('sort', 'date')
    
    conn = get_db_connection()
    
    if sort_by == 'starred':
        feedbacks = conn.execute(
            'SELECT * FROM feedback ORDER BY starred DESC, created_at DESC'
        ).fetchall()
    else:  # default to date
        feedbacks = conn.execute(
            'SELECT * FROM feedback ORDER BY created_at DESC'
        ).fetchall()
    
    conn.close()
    
    # Convert to list of dictionaries
    feedback_list = []
    for feedback in feedbacks:
        feedback_list.append({
            'id': feedback['id'],
            'content': feedback['content'],
            'created_at': feedback['created_at'],
            'starred': bool(feedback['starred'])
        })
    
    return jsonify(feedback_list)

@app.route('/api/feedback', methods=['POST'])
def create_feedback():
    """Create new feedback"""
    data = request.get_json()
    
    if not data or not data.get('content'):
        return jsonify({'error': 'Content is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO feedback (content) VALUES (?)',
        (data['content'],)
    )
    feedback_id = cursor.lastrowid
    conn.commit()
    
    # Get the created feedback
    feedback = conn.execute(
        'SELECT * FROM feedback WHERE id = ?', (feedback_id,)
    ).fetchone()
    conn.close()
    
    return jsonify({
        'id': feedback['id'],
        'content': feedback['content'],
        'created_at': feedback['created_at'],
        'starred': bool(feedback['starred'])
    }), 201

@app.route('/api/feedback/<int:feedback_id>/star', methods=['PUT'])
def toggle_star(feedback_id):
    """Toggle star status of feedback"""
    conn = get_db_connection()
    
    # Get current starred status
    feedback = conn.execute(
        'SELECT starred FROM feedback WHERE id = ?', (feedback_id,)
    ).fetchone()
    
    if not feedback:
        conn.close()
        return jsonify({'error': 'Feedback not found'}), 404
    
    # Toggle starred status
    new_starred = not bool(feedback['starred'])
    conn.execute(
        'UPDATE feedback SET starred = ? WHERE id = ?',
        (new_starred, feedback_id)
    )
    conn.commit()
    
    # Get updated feedback
    updated_feedback = conn.execute(
        'SELECT * FROM feedback WHERE id = ?', (feedback_id,)
    ).fetchone()
    conn.close()
    
    return jsonify({
        'id': updated_feedback['id'],
        'content': updated_feedback['content'],
        'created_at': updated_feedback['created_at'],
        'starred': bool(updated_feedback['starred'])
    })

@app.route('/api/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """Delete feedback"""
    conn = get_db_connection()
    
    # Check if feedback exists
    feedback = conn.execute(
        'SELECT id FROM feedback WHERE id = ?', (feedback_id,)
    ).fetchone()
    
    if not feedback:
        conn.close()
        return jsonify({'error': 'Feedback not found'}), 404
    
    # Delete feedback
    conn.execute('DELETE FROM feedback WHERE id = ?', (feedback_id,))
    conn.commit()
    conn.close()
    
    return '', 204

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
