# 💬 Anonymous Feedback Application

A beautiful, modern web application for collecting anonymous feedback with Flask and SQLite.

## ✨ Features

- 📝 Submit anonymous feedback
- 📅 Automatic timestamp recording
- ⭐ Star important feedback
- 🗑️ Delete feedback entries
- 🔄 Sort by date or starred status
- 📱 Responsive design
- 🎨 Beautiful modern UI

## 🛠️ Installation & Setup

### Prerequisites

1. **Install Python 3.8+**
   - Download from: https://python.org/downloads/
   - During installation, make sure to check "Add Python to PATH"

2. **Verify Python installation**
   ```bash
   python --version
   pip --version
   ```

### Quick Start

1. **Navigate to the project directory**
   ```bash
   cd d:\project\uma\CascadeProjects\windsurf-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

That's it! The application will automatically create the SQLite database on first run.

## 🚀 Usage

### Submit Feedback
1. Open the application in your browser
2. Type your feedback in the text area
3. Click "Submit Feedback"
4. Your feedback is now stored anonymously!

### Manage Feedback
- **⭐ Star feedback**: Click the star icon to mark important feedback
- **🗑️ Delete feedback**: Click the trash icon to remove feedback
- **📊 Sort feedback**: Use "Newest First" or "Starred First" buttons

### API Endpoints

The application also provides a REST API:

- `GET /api/feedback` - Get all feedback
- `POST /api/feedback` - Create new feedback
- `PUT /api/feedback/{id}/star` - Toggle star status
- `DELETE /api/feedback/{id}` - Delete feedback

## 📁 Project Structure

```
windsurf-project/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Web interface
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── feedback.db        # SQLite database (created automatically)
```

## 🔧 Configuration

### Database
- Uses SQLite by default (no setup required)
- Database file: `feedback.db` (created automatically)
- For production, you can easily switch to PostgreSQL

### Server Settings
- Default port: 5000
- Debug mode: Enabled (disable for production)
- Host: 0.0.0.0 (accessible from network)

## 🌐 Production Deployment

For production deployment:

1. **Disable debug mode** in `app.py`:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

2. **Use a production WSGI server** like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Consider using PostgreSQL** for better performance:
   - Install PostgreSQL
   - Update database connection in `app.py`

## 🎨 Customization

### Styling
- All CSS is in `templates/index.html`
- Uses modern gradient design with hover effects
- Fully responsive for mobile devices

### Features
- Easy to add new fields to feedback
- Simple to modify sorting options
- Can add user authentication if needed

## 🐛 Troubleshooting

### Common Issues

1. **"Python not found"**
   - Make sure Python is installed and added to PATH
   - Try using `python3` instead of `python`

2. **Port already in use**
   - Change the port in `app.py`: `app.run(port=5001)`

3. **Permission errors**
   - Make sure you have write permissions in the project directory

### Getting Help

If you encounter any issues:
1. Check the console output for error messages
2. Ensure all dependencies are installed correctly
3. Verify Python version compatibility

## 📄 License

This project is open source and available under the MIT License.
