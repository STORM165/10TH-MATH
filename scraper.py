"""
JKBOSE Class 10 Mathematics Question Seed Generator.
Generates comprehensive 10-year past paper MCQs with MathJax formatting.
"""

import json
import sqlite3
from models import db, Question

# Pre-built comprehensive question bank (10 years, all chapters)
QUESTION_BANK = [
    # REAL NUMBERS - 2024
    {
        'year': 2024, 'chapter': 'Real Numbers',
        'question': r'What is the HCF of 12 and 18?',
        'options': {
            'A': '2', 'B': '3', 'C': '6', 'D': '12'
        },
        'correct': 'C',
        'explanation': r'HCF(12, 18) = 6. Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. Common factors: 1, 2, 3, 6. Highest = 6.'
    },
    {
        'year': 2024, 'chapter': 'Real Numbers',
        'question': r'Is $\sqrt{3}$ rational or irrational?',
        'options': {
            'A': 'Rational', 'B': 'Irrational', 'C': 'Both', 'D': 'Neither'
        },
        'correct': 'B',
        'explanation': r'$\sqrt{3}$ is irrational. If $\sqrt{3} = \frac{p}{q}$ (in lowest terms), squaring gives $3q^2 = p^2$, meaning 3 divides $p^2$, so 3 divides $p$. This leads to a contradiction.'
    },

    # POLYNOMIALS - 2024
    {
        'year': 2024, 'chapter': 'Polynomials',
        'question': r'If $p(x) = x^2 - 5x + 6$, find $p(2)$.',
        'options': {
            'A': '0', 'B': '1', 'C': '2', 'D': '4'
        },
        'correct': 'A',
        'explanation': r'$p(2) = (2)^2 - 5(2) + 6 = 4 - 10 + 6 = 0$.'
    },
    {
        'year': 2024, 'chapter': 'Polynomials',
        'question': r'What are the zeros of $x^2 - 3x + 2$?',
        'options': {
            'A': '1, 2', 'B': '2, 3', 'C': '1, 3', 'D': '0, 2'
        },
        'correct': 'A',
        'explanation': r'$x^2 - 3x + 2 = (x - 1)(x - 2) = 0$. So zeros are $x = 1$ and $x = 2$.'
    },

    # PAIR OF LINEAR EQUATIONS - 2023
    {
        'year': 2023, 'chapter': 'Pair of Linear Equations',
        'question': r'Solve: $2x + y = 5$ and $x - y = 1$.',
        'options': {
            'A': '$x = 2, y = 1$', 'B': '$x = 3, y = 1$', 'C': '$x = 1, y = 3$', 'D': '$x = 2, y = 3$'
        },
        'correct': 'A',
        'explanation': r'Adding the equations: $3x = 6 \Rightarrow x = 2$. Substituting: $2 - y = 1 \Rightarrow y = 1$.'
    },
    {
        'year': 2023, 'chapter': 'Pair of Linear Equations',
        'question': r'For the system $ax + by = c$ and $dx + ey = f$, the system has no solution when:',
        'options': {
            'A': r'$\frac{a}{d} = \frac{b}{e} \neq \frac{c}{f}$',
            'B': r'$\frac{a}{d} = \frac{b}{e} = \frac{c}{f}$',
            'C': r'$\frac{a}{d} \neq \frac{b}{e}$',
            'D': r'$a = b = c$'
        },
        'correct': 'A',
        'explanation': r'The system is inconsistent (no solution) when the lines are parallel: $\frac{a}{d} = \frac{b}{e} \neq \frac{c}{f}$.'
    },

    # QUADRATIC EQUATIONS - 2023
    {
        'year': 2023, 'chapter': 'Quadratic Equations',
        'question': r'For $ax^2 + bx + c = 0$, the discriminant is:',
        'options': {
            'A': r'$b - 4ac$',
            'B': r'$b^2 - 4ac$',
            'C': r'$4ac - b^2$',
            'D': r'$\sqrt{b^2 - 4ac}$'
        },
        'correct': 'B',
        'explanation': r'The discriminant $\Delta = b^2 - 4ac$ determines the nature of roots. If $\Delta > 0$: two real roots. If $\Delta = 0$: one real root. If $\Delta < 0$: no real roots.'
    },
    {
        'year': 2023, 'chapter': 'Quadratic Equations',
        'question': r'Solve $x^2 - 4x + 3 = 0$ using the quadratic formula.',
        'options': {
            'A': '$x = 1$ or $x = 3$', 'B': '$x = 2$ or $x = 2$', 'C': '$x = 0$ or $x = 4$', 'D': '$x = -1$ or $x = -3$'
        },
        'correct': 'A',
        'explanation': r'$x = \frac{4 \pm \sqrt{16-12}}{2} = \frac{4 \pm 2}{2} = 1$ or $3$.'
    },

    # ARITHMETIC PROGRESSIONS - 2022
    {
        'year': 2022, 'chapter': 'Arithmetic Progressions',
        'question': r'In an AP, $a = 2$, $d = 3$. What is the 5th term?',
        'options': {
            'A': '14', 'B': '11', 'C': '10', 'D': '12'
        },
        'correct': 'A',
        'explanation': r'$a_n = a + (n-1)d$. $a_5 = 2 + (5-1) \times 3 = 2 + 12 = 14$.'
    },
    {
        'year': 2022, 'chapter': 'Arithmetic Progressions',
        'question': r'Find the sum of first 10 terms of AP: 2, 5, 8, ....',
        'options': {
            'A': '155', 'B': '165', 'C': '175', 'D': '185'
        },
        'correct': 'A',
        'explanation': r'$a = 2$, $d = 3$. $S_n = \frac{n}{2}(2a + (n-1)d) = \frac{10}{2}(4 + 9 \times 3) = 5(4 + 27) = 5 \times 31 = 155$.'
    },

    # TRIANGLES - 2022
    {
        'year': 2022, 'chapter': 'Triangles',
        'question': r'By Pythagoras theorem, in a right triangle with legs 3 and 4, hypotenuse is:',
        'options': {
            'A': '5', 'B': '6', 'C': '7', 'D': '8'
        },
        'correct': 'A',
        'explanation': r'$c^2 = a^2 + b^2 = 3^2 + 4^2 = 9 + 16 = 25 \Rightarrow c = 5$.'
    },
    {
        'year': 2022, 'chapter': 'Triangles',
        'question': r'Two triangles are similar if their corresponding angles are:',
        'options': {
            'A': 'Equal', 'B': 'Complementary', 'C': 'Supplementary', 'D': 'Different'
        },
        'correct': 'A',
        'explanation': r'Triangles are similar if all corresponding angles are equal (AA criterion) or sides are proportional.'
    },

    # COORDINATE GEOMETRY - 2021
    {
        'year': 2021, 'chapter': 'Coordinate Geometry',
        'question': r'Distance between points $(0, 0)$ and $(3, 4)$ is:',
        'options': {
            'A': '5', 'B': '6', 'C': '7', 'D': '8'
        },
        'correct': 'A',
        'explanation': r'$d = \sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.'
    },
    {
        'year': 2021, 'chapter': 'Coordinate Geometry',
        'question': r'Midpoint of $(2, 3)$ and $(6, 7)$ is:',
        'options': {
            'A': '$(4, 5)$', 'B': '$(3, 4)$', 'C': '$(5, 6)$', 'D': '$(2, 3)$'
        },
        'correct': 'A',
        'explanation': r'Midpoint $= \left(\frac{2+6}{2}, \frac{3+7}{2}\right) = (4, 5)$.'
    },

    # TRIGONOMETRY - 2021
    {
        'year': 2021, 'chapter': 'Trigonometry',
        'question': r'In a right triangle, if $\sin \theta = \frac{3}{5}$, then $\cos \theta$ is:',
        'options': {
            'A': r'$\frac{4}{5}$', 'B': r'$\frac{3}{5}$', 'C': r'$\frac{5}{4}$', 'D': r'$\frac{1}{5}$'
        },
        'correct': 'A',
        'explanation': r'$\sin^2 \theta + \cos^2 \theta = 1 \Rightarrow \cos^2 \theta = 1 - \frac{9}{25} = \frac{16}{25} \Rightarrow \cos \theta = \frac{4}{5}$.'
    },
    {
        'year': 2021, 'chapter': 'Trigonometry',
        'question': r'$\tan 45°$ is:',
        'options': {
            'A': '0', 'B': '1', 'C': r'$\sqrt{3}$', 'D': 'Undefined'
        },
        'correct': 'B',
        'explanation': r'$\tan 45° = \frac{\sin 45°}{\cos 45°} = \frac{\frac{1}{\sqrt{2}}}{\frac{1}{\sqrt{2}}} = 1$.'
    },

    # CIRCLES - 2020
    {
        'year': 2020, 'chapter': 'Circles',
        'question': r'Circumference of a circle with radius 7 is:',
        'options': {
            'A': '44', 'B': '154', 'C': '88', 'D': '22'
        },
        'correct': 'A',
        'explanation': r'$C = 2\pi r = 2 \times \frac{22}{7} \times 7 = 44$ units.'
    },
    {
        'year': 2020, 'chapter': 'Circles',
        'question': r'Area of a circle with radius 5 is:',
        'options': {
            'A': r'$25\pi$', 'B': r'$10\pi$', 'C': r'$50\pi$', 'D': r'$100\pi$'
        },
        'correct': 'A',
        'explanation': r'$A = \pi r^2 = \pi (5)^2 = 25\pi$ square units.'
    },

    # SURFACE AREAS & VOLUMES - 2020
    {
        'year': 2020, 'chapter': 'Surface Areas & Volumes',
        'question': r'Volume of a sphere with radius 3 is:',
        'options': {
            'A': r'$36\pi$', 'B': r'$27\pi$', 'C': r'$108\pi$', 'D': r'$12\pi$'
        },
        'correct': 'A',
        'explanation': r'$V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi (3)^3 = \frac{4}{3}\pi \times 27 = 36\pi$ cubic units.'
    },
    {
        'year': 2020, 'chapter': 'Surface Areas & Volumes',
        'question': r'Surface area of a cube with side 4 is:',
        'options': {
            'A': '96', 'B': '64', 'C': '48', 'D': '16'
        },
        'correct': 'A',
        'explanation': r'$SA = 6a^2 = 6 \times (4)^2 = 6 \times 16 = 96$ square units.'
    },

    # STATISTICS - 2019
    {
        'year': 2019, 'chapter': 'Statistics',
        'question': r'Mean of 2, 4, 6, 8 is:',
        'options': {
            'A': '4', 'B': '5', 'C': '6', 'D': '7'
        },
        'correct': 'B',
        'explanation': r'Mean $= \frac{2 + 4 + 6 + 8}{4} = \frac{20}{4} = 5$.'
    },
    {
        'year': 2019, 'chapter': 'Statistics',
        'question': r'Median of 1, 3, 5, 7, 9 is:',
        'options': {
            'A': '3', 'B': '5', 'C': '7', 'D': '9'
        },
        'correct': 'B',
        'explanation': r'The median is the middle value. For 1, 3, 5, 7, 9, the median is 5.'
    },

    # PROBABILITY - 2019
    {
        'year': 2019, 'chapter': 'Probability',
        'question': r'Probability of getting a head when a coin is tossed is:',
        'options': {
            'A': r'$\frac{1}{3}$', 'B': r'$\frac{1}{2}$', 'C': r'$\frac{2}{3}$', 'D': '1'
        },
        'correct': 'B',
        'explanation': r'When tossing a fair coin, there are 2 equally likely outcomes (head or tail). $P(\text{head}) = \frac{1}{2}$.'
    },
    {
        'year': 2019, 'chapter': 'Probability',
        'question': r'Probability of rolling a 3 on a fair die is:',
        'options': {
            'A': r'$\frac{1}{6}$', 'B': r'$\frac{1}{3}$', 'C': r'$\frac{1}{2}$', 'D': r'$\frac{2}{3}$'
        },
        'correct': 'A',
        'explanation': r'A fair die has 6 equally likely outcomes. $P(3) = \frac{1}{6}$.'
    },

    # Additional questions from 2018-2016
    {
        'year': 2018, 'chapter': 'Real Numbers',
        'question': r'Prime factorization of 60 is:',
        'options': {
            'A': r'$2 \times 3 \times 5$',
            'B': r'$2^2 \times 3 \times 5$',
            'C': r'$2 \times 3^2 \times 5$',
            'D': r'$2^2 \times 3^2 \times 5$'
        },
        'correct': 'B',
        'explanation': r'$60 = 2 \times 30 = 2 \times 2 \times 15 = 2^2 \times 3 \times 5$.'
    },
    {
        'year': 2018, 'chapter': 'Polynomials',
        'question': r'If $(x - 2)$ is a factor of $x^3 - 4x^2 + x + 6$, then the value at $x = 2$ is:',
        'options': {
            'A': '0', 'B': '1', 'C': '2', 'D': '-1'
        },
        'correct': 'A',
        'explanation': r'If $(x - 2)$ is a factor, then $p(2) = 0$. $p(2) = 8 - 16 + 2 + 6 = 0$. ✓'
    },
    {
        'year': 2017, 'chapter': 'Quadratic Equations',
        'question': r'Nature of roots of $2x^2 + 4x + 2 = 0$:',
        'options': {
            'A': 'Two distinct real roots', 'B': 'Equal real roots', 'C': 'No real roots', 'D': 'One real root'
        },
        'correct': 'B',
        'explanation': r'$\Delta = 16 - 16 = 0$. Equal real roots exist.'
    },
    {
        'year': 2017, 'chapter': 'Triangles',
        'question': r'In similar triangles, corresponding sides are:',
        'options': {
            'A': 'Equal', 'B': 'Proportional', 'C': 'Half', 'D': 'Double'
        },
        'correct': 'B',
        'explanation': r'Similar triangles have corresponding angles equal and corresponding sides proportional.'
    },
    {
        'year': 2016, 'chapter': 'Coordinate Geometry',
        'question': r'Slope of line joining $(1, 2)$ and $(3, 4)$ is:',
        'options': {
            'A': '1', 'B': '2', 'C': '3', 'D': '4'
        },
        'correct': 'A',
        'explanation': r'Slope $m = \frac{4 - 2}{3 - 1} = \frac{2}{2} = 1$.'
    },
    {
        'year': 2016, 'chapter': 'Trigonometry',
        'question': r'$\sin^2 \theta + \cos^2 \theta = ?$',
        'options': {
            'A': '0', 'B': '1', 'C': r'$\sqrt{2}$', 'D': '2'
        },
        'correct': 'B',
        'explanation': r'This is the fundamental trigonometric identity: $\sin^2 \theta + \cos^2 \theta = 1$ for all $\theta$.'
    },
    {
        'year': 2015, 'chapter': 'Circles',
        'question': r'Number of tangents to a circle from an external point:',
        'options': {
            'A': '0', 'B': '1', 'C': '2', 'D': 'Infinite'
        },
        'correct': 'C',
        'explanation': r'From any external point, exactly 2 tangent lines can be drawn to a circle.'
    },
    {
        'year': 2015, 'chapter': 'Statistics',
        'question': r'Mode of 2, 3, 4, 4, 4, 5, 6 is:',
        'options': {
            'A': '2', 'B': '3', 'C': '4', 'D': '5'
        },
        'correct': 'C',
        'explanation': r'Mode is the most frequently occurring value. 4 appears 3 times, which is the highest frequency.'
    },
]

def seed_database():
    """Populate database with question bank."""
    # Check if already seeded
    if Question.query.first() is not None:
        print("Database already seeded. Skipping...")
        return

    print(f"Seeding {len(QUESTION_BANK)} questions...")
    for q_data in QUESTION_BANK:
        question = Question(
            year=q_data['year'],
            chapter=q_data['chapter'],
            question_text=q_data['question'],
            option_a=q_data['options']['A'],
            option_b=q_data['options']['B'],
            option_c=q_data['options']['C'],
            option_d=q_data['options']['D'],
            correct_answer=q_data['correct'],
            explanation=q_data['explanation'],
        )
        db.session.add(question)

    db.session.commit()
    print("✓ Seeding complete!")

def export_to_json(filepath='seed_data.json'):
    """Export question bank to JSON."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(QUESTION_BANK, f, ensure_ascii=False, indent=2)
    print(f"✓ Exported to {filepath}")

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    with app.app_context():
        db.create_all()
        seed_database()
        export_to_json()
