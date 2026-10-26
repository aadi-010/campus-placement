# CampusPrep — Campus Placement Preparation Hub

> **Prepare Smarter. Practice Better. Get Placed.**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Flask 3.1.3](https://img.shields.io/badge/flask-3.1.3-black.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/database-SQLite%20%2F%20SQLAlchemy-lightgrey.svg)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/tests-16%20passed%20(pytest)-success.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A unified, full-stack placement preparation SaaS platform built for college students preparing for campus hiring drives. Built for a college hackathon with a focus on genuine functionality, rigorous security, transparent placement readiness metrics, and a distraction-free, professional light-mode aesthetic inspired by Linear and Notion.

---

## 📌 Problem Statement

Campus placement preparation resources are scattered across dozens of disjointed websites, ad-heavy forums, outdated PDF cheatsheets, and unstructured spreadsheets. As a result:
1. **Lack of Centralized Tracking:** Students have no single place to track quantitative aptitude, algorithmic coding, CS theory, and HR behavioral questions.
2. **Superficial Practice:** Many question sites provide bare answers without mathematically verified step-by-step derivations or shortcut tricks.
3. **Unrealistic Mock Simulations:** Most platforms lack server-enforced countdown deadlines, leading to inaccurate assessment of time management.
4. **Vague Placement Readiness:** Students cannot identify their specific topic vulnerabilities or quantify their overall readiness.

---

## 💡 Solution

**CampusPrep** aggregates the entire placement journey into a cohesive, production-quality dashboard:
- **Aptitude Arena:** 100+ verified original questions across Quantitative Aptitude, Logical Reasoning, and Verbal Ability with step-by-step mathematical solutions and exam shortcuts.
- **Coding Lab:** 40+ challenges across 10 core computer science topics with an AST-sandboxed isolated code execution engine and test runner.
- **Interview Room:** 60+ technical (OOP, DBMS, OS, Networks, DSA, Web) and HR behavioral interview questions with model responses, key points, and study notes.
- **Timed Mock Tests:** Server-enforced countdown timers, question palettes, automated scoring, and topic-wise breakdown.
- **Company Preparation Tracks:** Dedicated tracks for TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini, Amazon, and Microsoft with interactive preparation checklists.
- **Placement Resource Library:** Searchable, curated external reference guides and documentation from trustworthy educational sources.
- **My Progress & Analytics:** Transparent 4-pillar placement readiness formula, Chart.js progression charts, and topic vulnerability detection.

---

## 🛠 Technology Stack

### Backend
- **Language:** Python 3.11+ (Tested on Python 3.14)
- **Framework:** Flask 3.1.3
- **ORM:** SQLAlchemy 2.1+ / Flask-SQLAlchemy 3.1.1
- **Database:** SQLite (local development and hackathon demonstration)
- **Authentication:** Flask-Login 0.6.3 (session-based authentication)
- **Password Security:** Werkzeug 3.1.9 (`scrypt` password hashing)
- **CSRF Protection:** Flask-WTF 1.3.0
- **Testing:** Pytest 9.1.1
- **Production Server:** Gunicorn

### Frontend
- **Markup:** Semantic HTML5 with Jinja2 templating
- **Styling:** Custom Vanilla CSS3 Design System (light mode, `#F7F9FC` background, `#3567D6` brand blue)
- **Interactivity:** Modern ES6+ JavaScript (Fetch API, Async/Await)
- **Icons:** Lucide Icons (lightweight SVG icons)
- **Visualizations:** Chart.js 4.4.1 (progress and score trends)

---

## 🏛 System Architecture

```text
campusprep/
├── app/
│   ├── __init__.py               # Application factory & Blueprint registration
│   ├── config.py                 # Development, Testing, Production configurations
│   ├── extensions.py             # db, login_manager, csrf instances
│   ├── models/                   # SQLAlchemy Models
│   │   ├── user.py               # User, authentication, streak, daily goal
│   │   ├── aptitude.py           # AptitudeQuestion, AptitudeAttempt, Bookmark
│   │   ├── coding.py             # CodingChallenge, CodingSubmission, CodingDraft
│   │   ├── interview.py          # InterviewQuestion, InterviewProgress
│   │   ├── mock_test.py          # MockTest, MockTestAttempt, MockTestResponse
│   │   ├── company.py            # CompanyTrack, CompanyChecklist
│   │   └── resource.py           # PlacementResource
│   ├── routes/                   # RESTful Controllers & Views
│   │   ├── auth.py               # Registration, Login, Logout, Profile
│   │   ├── dashboard.py          # Personalized student dashboard & roadmap
│   │   ├── aptitude.py           # Catalog, Practice mode, Evaluation API
│   │   ├── coding.py             # Split IDE, Subprocess code runner, Drafts
│   │   ├── interviews.py         # Q&A knowledge base & Practice mode
│   │   ├── mock_tests.py         # Timed assessments, Deadline enforcement
│   │   ├── companies.py          # Company tracks & Interactive checklists
│   │   ├── resources.py          # Curated external library & Search
│   │   ├── progress.py           # Analytics, Topic accuracy, Chart data
│   │   └── api.py                # Bookmark toggle & Profile REST endpoints
│   ├── services/
│   │   ├── readiness.py          # Documented 4-pillar readiness calculation
│   │   └── code_runner.py        # AST static safety validator + Isolated subprocess
│   ├── static/
│   │   ├── css/style.css         # SaaS design tokens, components, grid system
│   │   └── js/                   # main.js, aptitude.js, coding.js, interview.js, mock_test.js
│   └── templates/                # Jinja2 templates for all views
├── scripts/
│   ├── seed.py                   # Master database seed runner
│   └── seed_data/                # Verified questions, challenges, and tracks
├── tests/                        # 16 Pytest unit and integration test suites
├── instance/                     # Local SQLite database storage
├── requirements.txt              # Production and development dependencies
├── run.py                        # Entrypoint server script
├── render.yaml                   # Production deployment manifest
└── .env.example                  # Environment configuration template
```

---

## 📊 Placement Readiness Formula

The **Placement Readiness Score** provides an estimate of student preparation across 4 distinct pillars (0–100%):

$$\text{Readiness Score} = \text{Aptitude (30\%)} + \text{Coding (30\%)} + \text{Interview (20\%)} + \text{Mock Tests (20\% bodega)}$$

1. **Aptitude Mastery (30 points max):**
   - Volume: Unique questions attempted vs 50-question benchmark (15 pts)
   - Accuracy: Unique correct questions / unique attempted (15 pts)
2. **Coding Verification (30 points max):**
   - Volume: Unique challenges verified and accepted vs 20-problem benchmark (20 pts)
   - Submission Accuracy: Accepted submissions / total submissions (10 pts)
3. **Interview Preparation (20 points max):**
   - Coverage: Questions reviewed with model answers vs 30-question benchmark (20 pts)
4. **Timed Mock Tests (20 points max):**
   - Volume: Completed mock tests vs 5-test benchmark (10 pts)
   - Performance: Average score across completed timed assessments (10 pts)

> **Important Disclosure:** This score is an indicative practice readiness estimate designed to guide focused self-study, not an official guarantee of company placement.

---

## 🔒 Security Architecture

1. **Password Hashing:** Passwords are never stored in plaintext; salted hashes are generated via `werkzeug.security.generate_password_hash`.
2. **CSRF Protection:** All form submissions and mutating JSON `POST` requests include synchronizer tokens verified by Flask-WTF.
3. **Isolated Code Execution:**
   - **AST Validation:** Parses Python AST prior to execution to detect and ban restricted modules (`os`, `sys`, `subprocess`, `socket`, `requests`, `multiprocessing`) and restricted functions (`eval`, `exec`, `open`, `__import__`).
   - **Process Isolation:** Runs code via independent subprocess with a strict 3.0-second CPU time limit.
4. **Server-Side Deadline Enforcement:** Mock test timers are stored and verified on the server (`deadline_at`). Client-side timer manipulations cannot bypass server-side expiration checks.
5. **Data Isolation:** All database queries are filtered by `user_id == current_user.id` to prevent cross-account data leakage.

---

## ⚡ Quick Start & Installation

### Prerequisites
- Python 3.11 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/campusprep.git
cd campusprep
```

### 2. Create and Activate a Virtual Environment

**Windows PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a local `.env` file based on `.env.example`:

**Windows PowerShell:**
```powershell
Copy-Item .env.example .env
```

**macOS / Linux:**
```bash
cp .env.example .env
```

### 5. Seed Database with Verified Questions
Populates 100 aptitude questions, 40 coding challenges, 60 interview questions, 8 company tracks, 4 mock assessments, 22 resources, and a demo student account:

```bash
python scripts/seed.py
```

### 6. Run the Application
```bash
python run.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your web browser.

---

## 🎭 Demo Student Credentials

For live hackathon evaluations, use the pre-populated demo account:

- **Email:** `demo@campusprep.edu`
- **Password:** `Demo@1234`
- **Pre-populated Activity:** 20 aptitude attempts, 5 accepted coding challenges, 12 reviewed interview answers, 1 completed mock test (80.0%), and 51% readiness score.

You can also click **Register** to create a fresh student profile.

---

## 🧪 Running Automated Tests

Run the full Pytest test suite:

```bash
python -m pytest -v
```

### Test Coverage Highlights:
- `tests/test_auth.py`: Registration, login/logout, duplicate account rejection, password hashing, protected route guards.
- `tests/test_aptitude.py`: Question sanitization (no leaked answers), backend correctness evaluation, persistence.
- `tests/test_coding.py`: AST sandbox security checks, correct code evaluation, wrong answer detection, timeout enforcement (TLE), runtime error handling.
- `tests/test_mock_tests.py`: Server-side deadline calculation, auto-expiration, answer auto-saving, score computation.
- `tests/test_readiness.py`: 4-pillar readiness calculation, zero-state for new students, scaling with verified activity.

---

## 🌐 Production Deployment

### Option 1: Deploy to Vercel (Recommended — Serverless)

CampusPrep is 100% pre-configured for Vercel deployment using serverless Python functions via [`vercel.json`](vercel.json) and [`api/index.py`](api/index.py).

#### Via Vercel Dashboard (1-Click):
1. Push your repository to GitHub.
2. Go to [Vercel Dashboard](https://vercel.com/new) and click **Add New Project** -> **Import Git Repository**.
3. Select your `campus-placement` repo.
4. Framework Preset: Leave as **Other**.
5. Add Environment Variables:
   - `FLASK_ENV` = `production`
   - `SECRET_KEY` = `<any-strong-random-key>`
   - `DATABASE_URL` *(Optional, recommended for persistence)* = Your PostgreSQL connection string from [Supabase](https://supabase.com/) or [Neon](https://neon.tech/) (e.g., `postgresql://user:pass@host/db`).
     > *Note:* If `DATABASE_URL` is omitted, CampusPrep uses a serverless `/tmp` SQLite database seeded automatically on first boot!
6. Click **Deploy**.

#### Via Vercel CLI:
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy preview
vercel

# Deploy to production
vercel --prod
```

---

### Option 2: Deploy to Render (Persistent Web Service)

CampusPrep is also ready for continuous hosting on Render using Gunicorn:

1. Connect your GitHub repository to [Render](https://render.com/).
2. Select **Web Service** and choose **Python 3**.
3. Set the following build and start commands:
   - **Build Command:** `pip install -r requirements.txt && python scripts/seed.py`
   - **Start Command:** `gunicorn run:app`
4. Set Environment Variables:
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: `<your-random-production-secret-key>`

The included [`render.yaml`](render.yaml) automatically configures this deployment pipeline.

---

## 📋 REST API Overview

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new student account |
| `POST` | `/auth/login` | Authenticate student and establish session |
| `GET` | `/auth/logout` | Terminate session and log out safely |
| `GET` | `/api/dashboard` | JSON snapshot of live stats, streak, and readiness |
| `GET` | `/aptitude/api/questions` | Filtered aptitude questions (answers excluded) |
| `POST` | `/aptitude/api/submit` | Evaluate submitted aptitude answer on backend |
| `POST` | `/coding/api/run` | Execute Python code against sample test cases |
| `POST` | `/coding/api/submit` | Evaluate solution against all test cases & persist |
| `POST` | `/coding/api/draft` | Auto-save coding workspace draft |
| `POST` | `/interview/api/review` | Mark question as reviewed and save personal notes |
| `POST` | `/mock-tests/start/<id>` | Start timed assessment and establish deadline |
| `POST` | `/mock-tests/api/<id>/answer` | Auto-save test response for question |
| `POST` | `/mock-tests/submit/<id>` | Finalize assessment and compute scorecard |
| `POST` | `/companies/api/<id>/checklist` | Toggle company preparation checklist item |
| `POST` | `/api/bookmark/toggle` | Toggle bookmark on question, challenge, or resource |
| `GET` | `/progress/api/chart-data` | Retrieve JSON dataset for Chart.js progression |

---

## ⚖️ Known Limitations & Future Improvements

- **Isolated Code Runner:** The local sandbox employs Python AST parsing and timed subprocess execution. In a high-traffic enterprise deployment, containerized Docker sandboxes or gVisor microVMs (e.g. AWS Lambda / Judge0) would provide enhanced isolation.
- **AI Interview Evaluation:** Practice mode currently facilitates self-guided evaluation against verified model answers and key points. Future releases can incorporate local LLMs (e.g., Gemma 4) for automated speech and text feedback.
- **Multi-Language Coding:** Python 3 is currently supported. Future iterations will add C++, Java, and JavaScript runners.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
