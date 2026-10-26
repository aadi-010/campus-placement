"""
CampusPrep Database Seeder Script
Populates verified questions, challenges, tracks, resources, and demo student profile.
Run via: python scripts/seed.py
"""
import json
import os
import sys
from datetime import datetime, timedelta

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.aptitude import AptitudeQuestion, AptitudeAttempt, Bookmark
from app.models.coding import CodingChallenge, CodingSubmission
from app.models.interview import InterviewQuestion, InterviewProgress
from app.models.company import CompanyTrack, CompanyChecklist
from app.models.resource import PlacementResource
from app.models.mock_test import MockTest, MockTestAttempt, MockTestResponse

from scripts.seed_data.aptitude_questions import APTITUDE_QUESTIONS
from scripts.seed_data.coding_challenges import CHALLENGES
from scripts.seed_data.interview_questions import INTERVIEW_QUESTIONS
from scripts.seed_data.companies import COMPANIES
from scripts.seed_data.resources import RESOURCES
from scripts.seed_data.mock_tests import MOCK_TESTS

def seed_database():
    app = create_app('development')
    with app.app_context():
        print(" -> Creating database tables...")
        db.create_all()

        # 1. Seed Aptitude Questions
        print(f" -> Seeding Aptitude Questions ({len(APTITUDE_QUESTIONS)} items)...")
        existing_q_count = AptitudeQuestion.query.count()
        if existing_q_count < len(APTITUDE_QUESTIONS):
            # Clear or add missing
            AptitudeQuestion.query.delete()
            for q_data in APTITUDE_QUESTIONS:
                q = AptitudeQuestion(
                    category=q_data['category'],
                    topic=q_data['topic'],
                    difficulty=q_data['difficulty'],
                    question=q_data['question'],
                    options_json=json.dumps(q_data['options']),
                    correct_option=q_data['correct_option'],
                    explanation=q_data['explanation'],
                    shortcut_hint=q_data.get('shortcut')
                )
                db.session.add(q)
            db.session.commit()
            print(f"    [+] Seeded {len(APTITUDE_QUESTIONS)} aptitude questions.")
        else:
            print(f"    [OK] Aptitude questions already up to date ({existing_q_count} items).")

        # 2. Seed Coding Challenges
        print(f" -> Seeding Coding Challenges ({len(CHALLENGES)} items)...")
        existing_c_count = CodingChallenge.query.count()
        if existing_c_count < len(CHALLENGES):
            CodingChallenge.query.delete()
            for c_data in CHALLENGES:
                examples = [{
                    'input': c_data.get('sample_inputs', ''),
                    'output': c_data.get('sample_outputs', ''),
                    'explanation': c_data.get('explanations', '')
                }]
                c = CodingChallenge(
                    title=c_data['title'],
                    slug=c_data['slug'],
                    topic=c_data['topic'],
                    difficulty=c_data['difficulty'],
                    description=c_data['description'],
                    constraints=c_data.get('constraints'),
                    examples_json=json.dumps(examples),
                    hints_json=json.dumps(c_data.get('hints', [])),
                    starter_code_python=c_data.get('starter_code', ''),
                    test_cases_json=json.dumps(c_data['test_cases'])
                )
                db.session.add(c)
            db.session.commit()
            print(f"    [+] Seeded {len(CHALLENGES)} coding challenges.")
        else:
            print(f"    [OK] Coding challenges already up to date ({existing_c_count} items).")

        # 3. Seed Interview Questions
        print(f" -> Seeding Interview Questions ({len(INTERVIEW_QUESTIONS)} items)...")
        existing_i_count = InterviewQuestion.query.count()
        if existing_i_count < len(INTERVIEW_QUESTIONS):
            InterviewQuestion.query.delete()
            for i_data in INTERVIEW_QUESTIONS:
                mistakes = i_data.get('common_mistakes', [])
                mistakes_str = '\n'.join(mistakes) if isinstance(mistakes, list) else str(mistakes)
                iq = InterviewQuestion(
                    category=i_data['category'],
                    subtopic=i_data.get('topic', 'General'),
                    difficulty=i_data['difficulty'],
                    question=i_data['question'],
                    answer=i_data['answer'],
                    key_points_json=json.dumps(i_data['key_points']),
                    common_mistakes=mistakes_str
                )
                db.session.add(iq)
            db.session.commit()
            print(f"    [+] Seeded {len(INTERVIEW_QUESTIONS)} interview questions.")
        else:
            print(f"    [OK] Interview questions already up to date ({existing_i_count} items).")

        # 4. Seed Company Tracks
        print(f" -> Seeding Company Tracks ({len(COMPANIES)} items)...")
        existing_comp_count = CompanyTrack.query.count()
        if existing_comp_count < len(COMPANIES):
            CompanyTrack.query.delete()
            for comp_data in COMPANIES:
                ct = CompanyTrack(
                    name=comp_data['name'],
                    slug=comp_data['slug'],
                    tier=comp_data['tier'],
                    overview=comp_data['overview'],
                    recruitment_stages_json=json.dumps(comp_data['recruitment_stages']),
                    skill_areas_json=json.dumps(comp_data['skill_areas']),
                    aptitude_topics_json=json.dumps(comp_data['aptitude_topics']),
                    coding_topics_json=json.dumps(comp_data['coding_topics']),
                    technical_topics_json=json.dumps(comp_data['technical_topics']),
                    hr_topics_json=json.dumps(comp_data['hr_topics']),
                    checklist_items_json=json.dumps(comp_data['checklist_items'])
                )
                db.session.add(ct)
            db.session.commit()
            print(f"    [+] Seeded {len(COMPANIES)} company tracks.")
        else:
            print(f"    [OK] Company tracks already up to date ({existing_comp_count} items).")

        # 5. Seed Placement Resources
        print(f" -> Seeding Placement Resources ({len(RESOURCES)} items)...")
        existing_r_count = PlacementResource.query.count()
        if existing_r_count < len(RESOURCES):
            PlacementResource.query.delete()
            for r_data in RESOURCES:
                pr = PlacementResource(
                    title=r_data['title'],
                    category=r_data['category'],
                    description=r_data['description'],
                    external_url=r_data['external_url'],
                    resource_type=r_data['resource_type'],
                    estimated_time=r_data['estimated_time'],
                    is_featured=r_data.get('is_featured', False)
                )
                db.session.add(pr)
            db.session.commit()
            print(f"    [+] Seeded {len(RESOURCES)} placement resources.")
        else:
            print(f"    [OK] Placement resources already up to date ({existing_r_count} items).")

        # 6. Seed Mock Tests (linking to verified Aptitude questions)
        print(" -> Seeding Mock Tests (4 assessments)...")
        existing_mt_count = MockTest.query.count()
        if existing_mt_count < 4:
            MockTest.query.delete()

            quant_ids = [q.id for q in AptitudeQuestion.query.filter_by(category='Quantitative Aptitude').limit(15).all()]
            logical_ids = [q.id for q in AptitudeQuestion.query.filter_by(category='Logical Reasoning').limit(15).all()]
            verbal_ids = [q.id for q in AptitudeQuestion.query.filter_by(category='Verbal Ability').limit(15).all()]
            mixed_ids = (
                [q.id for q in AptitudeQuestion.query.filter_by(category='Quantitative Aptitude').limit(10).all()] +
                [q.id for q in AptitudeQuestion.query.filter_by(category='Logical Reasoning').limit(10).all()] +
                [q.id for q in AptitudeQuestion.query.filter_by(category='Verbal Ability').limit(10).all()]
            )

            tests_data = [
                ("Quantitative Aptitude Mock Assessment", "Quantitative", "Timed 15-question numerical ability, arithmetic speed, and percentage test.", 25, quant_ids),
                ("Logical Reasoning Mock Assessment", "Logical", "Timed 15-question deductive patterns, series, coding-decoding, and puzzle challenge.", 25, logical_ids),
                ("Verbal Ability & English Assessment", "Verbal", "Timed 15-question grammar, sentence correction, and vocabulary assessment.", 20, verbal_ids),
                ("Full Placement Simulator (Mixed)", "Mixed Placement", "Comprehensive 30-question screening assessment simulating top campus recruitment drives.", 35, mixed_ids)
            ]

            for title, cat, desc, duration, q_ids in tests_data:
                mt = MockTest(
                    title=title,
                    category=cat,
                    description=desc,
                    duration_minutes=duration,
                    total_questions=len(q_ids),
                    questions_json=json.dumps(q_ids)
                )
                db.session.add(mt)
            db.session.commit()
            print("    [+] Seeded 4 mock test assessments.")
        else:
            print(f"    [OK] Mock tests already up to date ({existing_mt_count} items).")

        # 7. Create Demo Student Account and pre-populated progress
        print(" -> Creating Demo Student Account (demo@campusprep.edu)...")
        demo_user = User.query.filter_by(email='demo@campusprep.edu').first()
        if not demo_user:
            demo_user = User(
                email='demo@campusprep.edu',
                full_name='Aditya Sharma',
                college='National Institute of Technology',
                graduation_year=2025,
                target_role='Software Development Engineer',
                current_streak=5
            )
            demo_user.set_password('Demo@1234')
            db.session.add(demo_user)
            db.session.commit()
            print("    [+] Created demo user: demo@campusprep.edu / Demo@1234")
        else:
            demo_user.set_password('Demo@1234')
            demo_user.current_streak = 5
            db.session.commit()
            print("    [OK] Demo user refreshed.")

        # Seed realistic activity for demo student if empty
        user_attempts_count = AptitudeAttempt.query.filter_by(user_id=demo_user.id).count()
        if user_attempts_count == 0:
            print(" -> Pre-populating demo practice attempts and analytics...")
            questions = AptitudeQuestion.query.limit(20).all()
            for idx, q in enumerate(questions):
                # 80% correct rate
                is_correct = (idx % 5 != 0)
                selected = q.correct_option if is_correct else ((q.correct_option + 1) % 4)
                attempt_time = datetime.utcnow() - timedelta(days=idx % 7, hours=idx % 12)
                attempt = AptitudeAttempt(
                    user_id=demo_user.id,
                    question_id=q.id,
                    selected_option=selected,
                    is_correct=is_correct,
                    attempted_at=attempt_time
                )
                db.session.add(attempt)

            # Pre-populate Coding submissions
            challenges = CodingChallenge.query.limit(5).all()
            for ch in challenges:
                sub = CodingSubmission(
                    user_id=demo_user.id,
                    challenge_id=ch.id,
                    language='python',
                    source_code=ch.starter_code_python,
                    status='Accepted',
                    passed_tests=len(ch.test_cases),
                    total_tests=len(ch.test_cases),
                    execution_time_ms=45,
                    submitted_at=datetime.utcnow() - timedelta(days=2)
                )
                db.session.add(sub)

            # Pre-populate Interview progress
            interview_qs = InterviewQuestion.query.limit(12).all()
            for iq in interview_qs:
                ip = InterviewProgress(
                    user_id=demo_user.id,
                    question_id=iq.id,
                    is_reviewed=True,
                    personal_notes="Reviewed key architectural points and STAR framing.",
                    reviewed_at=datetime.utcnow() - timedelta(days=1)
                )
                db.session.add(ip)

            # Pre-populate Completed Mock Test Attempt
            quant_mock = MockTest.query.filter_by(category='Quantitative').first()
            if quant_mock:
                m_attempt = MockTestAttempt(
                    user_id=demo_user.id,
                    mock_test_id=quant_mock.id,
                    started_at=datetime.utcnow() - timedelta(hours=3),
                    deadline_at=datetime.utcnow() - timedelta(hours=2, minutes=35),
                    submitted_at=datetime.utcnow() - timedelta(hours=2, minutes=37),
                    score=80.0,
                    total_questions=15,
                    correct_count=12,
                    incorrect_count=3,
                    unattempted_count=0,
                    time_spent_seconds=1380,
                    status='completed'
                )
                db.session.add(m_attempt)

            # Pre-populate Company Checklists for TCS
            tcs = CompanyTrack.query.filter_by(slug='tcs').first()
            if tcs:
                db.session.add(CompanyChecklist(user_id=demo_user.id, company_id=tcs.id, item_index=0, is_completed=True))
                db.session.add(CompanyChecklist(user_id=demo_user.id, company_id=tcs.id, item_index=1, is_completed=True))

            # Pre-populate Bookmarks
            first_q = AptitudeQuestion.query.first()
            if first_q:
                db.session.add(Bookmark(user_id=demo_user.id, item_type='aptitude', item_id=first_q.id))

            db.session.commit()
            print("    [+] Demo activity successfully generated.")

        print("\n=== SEEDING COMPLETED SUCCESSFULLY ===")
        print("Demo Account:")
        print("  Email:    demo@campusprep.edu")
        print("  Password: Demo@1234\n")

if __name__ == '__main__':
    seed_database()
