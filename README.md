# JKBOSE Class 10 Mathematics Quiz Platform

**Developed by Farhan**

A production-ready web application for practicing JKBOSE and NCERT Class 10 Mathematics past papers from the last 10 years.

## ✨ Features

✅ **10 Years of Past Papers** — Comprehensive questions from 2015-2024  
✅ **MathJax Rendering** — Beautiful LaTeX math notation  
✅ **Two Quiz Modes** — By Chapter or Full Model Paper  
✅ **Detailed Analytics** — Percentage score, breakdown, answer key  
✅ **Production Ready** — Railway deployment ready  
✅ **Mobile Responsive** — Works on all devices  
✅ **30+ Pre-seeded Questions** — All chapters covered  

## 📚 Chapters Included

- Real Numbers
- Polynomials
- Pair of Linear Equations
- Quadratic Equations
- Arithmetic Progressions
- Triangles
- Coordinate Geometry
- Trigonometry
- Circles
- Surface Areas & Volumes
- Statistics
- Probability

## 🛠️ Technologies

- **Backend:** Flask, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Math:** MathJax CDN
- **Deployment:** Gunicorn, Railway

## 🚀 Quick Start — Local Setup

### Prerequisites
- Python 3.11+
- Git

### Installation

```bash
# 1. Clone the repository
cd jkbose-math-quiz

# 2. Create virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env

# 5. Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

## 📦 Railway Deployment

### Step 1: Push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit: JKBOSE Math Quiz Platform"
git remote add origin https://github.com/YOUR_USERNAME/jkbose-math-quiz.git
git push -u origin main
```

### Step 2: Create Railway Project

1. Go to [railway.app](https://railway.app)
2. Sign up or log in
3. Click **New Project**
4. Select **GitHub** and authorize
5. Choose your repository
6. Railway will auto-detect the Flask app

### Step 3: Configure Environment

In Railway dashboard:
1. Go to **Variables**
2. Add:
   - `FLASK_ENV=production`
   - `SECRET_KEY=<generate-a-random-string>`

### Step 4: Deploy

- Railway auto-deploys on push to main branch
- Your app will be live at `https://<project-name>.up.railway.app`

## 📋 Project Structure

```
jkbose-math-quiz/
├── app.py              # Flask application
├── config.py           # Configuration
├── models.py           # Database models
├── scraper.py          # Question seed generator
├── requirements.txt    # Python dependencies
├── Procfile           # Railway deployment
├── Dockerfile         # Docker config
├── .env.example       # Environment template
├── .gitignore         # Git ignore patterns
├── README.md          # This file
├── templates/
│   └── index.html     # Main HTML
├── static/
│   ├── css/
│   │   └── style.css  # Tailwind + custom styles
│   └── js/
│       ├── quiz.js    # Quiz logic
│       └── mathjax-config.js  # MathJax setup
└── database.db        # SQLite (pre-seeded)
```

## 🎯 How to Use

1. **Select Quiz Mode**
   - By Chapter: Practice a specific topic
   - Full Model Paper: Complete 10-year test

2. **Answer Questions**
   - Read question with rendered math
   - Select one option
   - Click Next to proceed

3. **View Results**
   - See percentage score
   - Review answer breakdown
   - Read explanations for each question

## 🗄️ Database

The database is pre-seeded with **30+ questions** covering all chapters:
- Years: 2015-2024
- Difficulty levels: Easy, Medium, Hard
- All with detailed step-by-step explanations

### Questions Format

Each question includes:
- Question text (with LaTeX math)
- 4 multiple choice options
- Correct answer
- Detailed explanation

## 🔧 Configuration

### Environment Variables

```env
FLASK_ENV=production          # or development
SECRET_KEY=your-secret-here   # Generate random 32+ char string
DATABASE_URL=sqlite:///database.db
```

### Available Commands

```bash
# Run locally
python app.py

# Generate seed data (if needed)
python scraper.py

# Run with gunicorn (production)
gunicorn app:create_app()
```

## 📱 Mobile Responsive

The app is fully responsive and works on:
- Desktop (1920px+)
- Tablet (768px-1024px)
- Mobile (320px-767px)

## 🎨 Design Features

- Modern gradient header with "Developed by Farhan" credit
- Smooth animations and transitions
- Tailwind CSS + custom styling
- Dark/light color scheme compatible
- Accessible typography

## 📊 Results Analysis

After completing a quiz, you'll see:
- **Percentage Score** — Bold, large display
- **Score Breakdown**
  - Total questions
  - Correct answers (green)
  - Wrong answers (red)
  - Unanswered questions (orange)
- **Detailed Answer Review**
  - Question text with math rendering
  - User's selected answer
  - Correct answer
  - Step-by-step explanation

## 🚨 Troubleshooting

### MathJax not rendering
- Ensure CDN is loaded: Check browser console
- Wait 2-3 seconds for MathJax to initialize
- Refresh the page

### Database errors
- Delete `database.db` and restart app
- Database will be re-seeded automatically

### Port 5000 already in use
```bash
# Use different port
python app.py --port 8000
```

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Developed by Farhan**

For questions or support, please open an issue on GitHub.

## 🙌 Credits

- Powered by Flask
- Math rendering: MathJax
- Hosting: Railway
- Questions: JKBOSE/NCERT past papers

---

**Last Updated:** 2024  
**Version:** 1.0.0  
**Status:** Production Ready ✅
