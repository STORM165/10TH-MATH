from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Question
from scraper import seed_database
import os

def create_app(config_name=None):
    """Application factory."""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')

    app.config.from_object(config[config_name])
    db.init_app(app)
    CORS(app)

    # Register routes
    @app.route('/')
    def index():
        """Serve main page."""
        return render_template('index.html')

    @app.route('/api/chapters', methods=['GET'])
    def get_chapters():
        """Get unique chapters."""
        chapters = db.session.query(Question.chapter).distinct().all()
        return jsonify({'chapters': [ch[0] for ch in chapters]})

    @app.route('/api/years', methods=['GET'])
    def get_years():
        """Get unique years."""
        years = db.session.query(Question.year).distinct().order_by(Question.year.desc()).all()
        return jsonify({'years': [yr[0] for yr in years]})

    @app.route('/api/questions', methods=['GET'])
    def get_questions():
        """Get questions (filtered by chapter or year)."""
        chapter = request.args.get('chapter')
        year = request.args.get('year')
        mode = request.args.get('mode', 'chapter')  # 'chapter' or 'full'

        query = Question.query

        if mode == 'chapter' and chapter:
            query = query.filter(Question.chapter == chapter)
        elif mode == 'full' and year:
            query = query.filter(Question.year == year)

        questions = query.all()

        # Exclude correct_answer from front-end
        result = []
        for q in questions:
            q_dict = q.to_dict()
            q_dict.pop('correct_answer')  # Hide answer
            q_dict.pop('explanation')  # Hide explanation
            result.append(q_dict)

        return jsonify({'questions': result, 'count': len(result)})

    @app.route('/api/submit', methods=['POST'])
    def submit_quiz():
        """Grade submitted answers."""
        data = request.get_json()
        answers = data.get('answers', {})  # {question_id: user_answer}

        results = {
            'total': 0,
            'correct': 0,
            'wrong': 0,
            'unanswered': 0,
            'percentage': 0,
            'details': []
        }

        for q_id_str, user_ans in answers.items():
            q_id = int(q_id_str)
            question = Question.query.get(q_id)
            if not question:
                continue

            results['total'] += 1

            if user_ans is None or user_ans == '':
                results['unanswered'] += 1
                is_correct = False
            else:
                is_correct = (user_ans == question.correct_answer)
                if is_correct:
                    results['correct'] += 1
                else:
                    results['wrong'] += 1

            results['details'].append({
                'id': question.id,
                'question': question.question_text,
                'user_answer': user_ans,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct,
                'explanation': question.explanation,
                'options': {
                    'A': question.option_a,
                    'B': question.option_b,
                    'C': question.option_c,
                    'D': question.option_d,
                }
            })

        if results['total'] > 0:
            results['percentage'] = round((results['correct'] / results['total']) * 100, 2)

        return jsonify(results)

    @app.route('/api/health', methods=['GET'])
    def health():
        """Health check."""
        return jsonify({'status': 'ok'})

    # Initialize database
    with app.app_context():
        db.create_all()
        seed_database()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
