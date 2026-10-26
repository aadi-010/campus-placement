"""
Mock test catalog configuration seed data
"""

MOCK_TESTS = [
    {
        "title": "Quantitative Aptitude Mock Assessment",
        "category": "Quantitative",
        "duration_minutes": 25,
        "configuration": {
            "category_filter": "Quantitative Aptitude",
            "question_count": 15,
            "difficulty": "All",
            "pass_percentage": 60,
            "instructions": [
                "This assessment contains 15 questions covering Numerical Ability, Percentages, Time & Work, Profit & Loss, and Ratios.",
                "Total time allotted is 25 minutes. The countdown starts as soon as you click Start.",
                "Each question has exactly one correct answer.",
                "There is no negative marking for incorrect responses.",
                "The server automatically submits and grades your test when the timer expires."
            ]
        }
    },
    {
        "title": "Logical Reasoning Mock Assessment",
        "category": "Logical",
        "duration_minutes": 25,
        "configuration": {
            "category_filter": "Logical Reasoning",
            "question_count": 15,
            "difficulty": "All",
            "pass_percentage": 60,
            "instructions": [
                "This assessment contains 15 questions testing Number Series, Syllogisms, Blood Relations, Coding-Decoding, and Direction Sense.",
                "Total time allotted is 25 minutes.",
                "Use the question palette to mark questions for review or navigate quickly.",
                "You can change your selected answer any time before the test is submitted."
            ]
        }
    },
    {
        "title": "Verbal Ability & English Assessment",
        "category": "Verbal",
        "duration_minutes": 20,
        "configuration": {
            "category_filter": "Verbal Ability",
            "question_count": 15,
            "difficulty": "All",
            "pass_percentage": 65,
            "instructions": [
                "This assessment evaluates vocabulary, sentence correction, reading comprehension, and grammatical accuracy.",
                "Total time allotted is 20 minutes.",
                "Read each sentence and passage carefully before selecting your answer.",
                "Answers are auto-saved per question."
            ]
        }
    },
    {
        "title": "Full Placement Simulator (Mixed)",
        "category": "Mixed",
        "duration_minutes": 35,
        "configuration": {
            "category_filter": "All",
            "question_count": 25,
            "difficulty": "All",
            "pass_percentage": 70,
            "instructions": [
                "Simulates a comprehensive first-round campus placement screening test.",
                "Contains a balanced mix of Quantitative Aptitude, Logical Reasoning, and Verbal Ability questions.",
                "Total time allotted is 35 minutes.",
                "Simulates real online test constraints: server-side time tracking and instant analytical scorecard on completion."
            ]
        }
    }
]
