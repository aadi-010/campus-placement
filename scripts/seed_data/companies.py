"""
Company preparation tracks seed data for CampusPrep
"""

COMPANIES = [
    {
        "name": "Tata Consultancy Services (TCS)",
        "slug": "tcs",
        "tier": "Service-Based",
        "overview": "TCS conducts the National Qualifier Test (TCS NQT) for hiring freshers across Ninja, Digital, and Prime cadences. Preparation emphasizes speed in quantitative aptitude, foundational programming logic, and clear communication.",
        "recruitment_stages": [
            {"stage": 1, "name": "TCS NQT (Cognitive & Technical)", "description": "Online assessment testing Numerical Ability, Reasoning Ability, Verbal Ability, and Advanced Coding."},
            {"stage": 2, "name": "Technical Interview", "description": "Assessment of core CS concepts, programming language syntax, DBMS queries, and academic projects."},
            {"stage": 3, "name": "Managerial & HR Round", "description": "Behavioral questions, adaptability to shifts and locations, and company values alignment."}
        ],
        "skill_areas": ["Numerical Ability", "Reasoning", "C / Python Basics", "DBMS", "Software Engineering"],
        "aptitude_topics": ["Percentages", "Time and Work", "Time, Speed and Distance", "Number Systems", "Number Series", "Sentence Correction"],
        "coding_topics": ["Arrays", "Strings", "Searching", "Basic Sorting"],
        "technical_topics": ["OOPs Concepts", "SQL Queries", "Normalization", "SDLC Models"],
        "hr_topics": ["Why TCS?", "Relocation Flexibility", "Handling Project Deadlines", "Strengths & Weaknesses"],
        "checklist_items": [
            "Review TCS NQT previous year quantitative questions",
            "Practice 20 array and string manipulation coding problems",
            "Revise SQL JOINs and basic ACID properties",
            "Prepare a 2-minute elevator pitch for your final year capstone project",
            "Complete 1 full-length TCS NQT mock test on CampusPrep"
        ]
    },
    {
        "name": "Infosys",
        "slug": "infosys",
        "tier": "Service-Based",
        "overview": "Infosys hires engineering graduates through the Infosys Certification and on-campus recruitment for System Engineer and Specialist Programmer roles. The online test is well-known for pseudocode and puzzle-solving questions.",
        "recruitment_stages": [
            {"stage": 1, "name": "Online Test", "description": "Sections include Mathematical Ability, Reasoning Ability, Verbal Ability, Pseudocode analysis, and Numerical Puzzles."},
            {"stage": 2, "name": "Technical Interview", "description": "Discussion on programming fundamentals, data structures, debugging code snippets, and web development basics."},
            {"stage": 3, "name": "HR Interview", "description": "Communication skills, willingness to learn new technologies, and academic background discussion."}
        ],
        "skill_areas": ["Pseudocode", "Cryptarithmetic / Puzzles", "Java / Python", "Data Structures", "Verbal Ability"],
        "aptitude_topics": ["Puzzles", "Seating Arrangements", "Ratios and Proportions", "Data Interpretation", "Reading Comprehension"],
        "coding_topics": ["Recursion", "Hash Maps", "Strings", "Two Pointers"],
        "technical_topics": ["OOP Principles (Java/Python)", "Stack vs Heap Memory", "Database Indexing", "REST APIs"],
        "hr_topics": ["Tell me about yourself", "Why Infosys?", "How do you handle conflict in a team?"],
        "checklist_items": [
            "Practice 15 pseudocode dry-run tracing problems",
            "Solve 10 seating arrangement and syllogism puzzles",
            "Prepare deep explanation of OOP pillars with real-world examples",
            "Review your resume projects and be ready to explain architectural choices"
        ]
    },
    {
        "name": "Wipro",
        "slug": "wipro",
        "tier": "Service-Based",
        "overview": "Wipro recruits freshers primarily through the Elite National Talent Hunt (NLTH) for Project Engineer roles. The assessment features quantitative aptitude, logical reasoning, verbal ability, coding, and an automated essay writing test.",
        "recruitment_stages": [
            {"stage": 1, "name": "Elite NTH Online Test", "description": "Aptitude, logical, verbal, essay writing evaluation, and 2 programming challenges."},
            {"stage": 2, "name": "Technical Interview", "description": "Covers programming fundamentals, data structures, basic algorithms, and project walkthrough."},
            {"stage": 3, "name": "HR Round", "description": "Verification of academic credentials, career goals, shift adaptability, and service agreement agreement."}
        ],
        "skill_areas": ["Quantitative Ability", "Logical Deduction", "Written Communication", "Basic DSA"],
        "aptitude_topics": ["Profit and Loss", "Simple and Compound Interest", "Blood Relations", "Direction Sense", "Sentence Completion"],
        "coding_topics": ["Arrays", "Searching", "Math & Number Theory"],
        "technical_topics": ["Pointers / References", "SQL Group By and Having", "Operating System Processes"],
        "hr_topics": ["Wipro Spirit & Core Values", "Willingness to Relocate", "Handling Workplace Pressure"],
        "checklist_items": [
            "Complete practice on Profit & Loss and Simple/Compound Interest",
            "Write two 200-word essays on tech trends to practice writing fluency",
            "Solve standard array search and frequency count problems in Python",
            "Review Operating System process states and CPU scheduling"
        ]
    },
    {
        "name": "Accenture",
        "slug": "accenture",
        "tier": "Service-Based",
        "overview": "Accenture conducts a multi-stage assessment for Associate Software Engineer (ASE) and Advanced ASE (AASE) roles. Stage 1 includes Cognitive & Technical questions; Stage 2 is Coding; followed by a Communication Assessment.",
        "recruitment_stages": [
            {"stage": 1, "name": "Cognitive and Technical Assessment", "description": "Critical Thinking, Analytical Reasoning, Abstract Reasoning, English Ability, Common Application & MS Office, Cloud, and Network Security."},
            {"stage": 2, "name": "Coding Assessment", "description": "Hands-on coding round with 2 algorithmic problems to be solved in 45 minutes."},
            {"stage": 3, "name": "Communication Assessment", "description": "Automated voice-based test checking pronunciation, reading fluency, and comprehension."},
            {"stage": 4, "name": "Interview", "description": "Combined technical and behavioral interview focusing on learning agility and project work."}
        ],
        "skill_areas": ["Cloud Basics", "Computer Networks", "Analytical Reasoning", "Communication", "Data Structures"],
        "aptitude_topics": ["Coding-Decoding", "Direction Sense", "Averages", "Probability", "Grammar"],
        "coding_topics": ["Arrays", "Bit Manipulation", "Strings", "Hash Maps"],
        "technical_topics": ["Cloud Architecture Basics", "Network Security Protocols", "OOP Concepts"],
        "hr_topics": ["Tell me about a time you adapted to change", "Why Accenture?", "Future career vision"],
        "checklist_items": [
            "Study cloud basics (IaaS vs PaaS vs SaaS) and network security fundamentals",
            "Solve 15 bitwise and string transformation coding challenges",
            "Practice speaking English aloud for 15 minutes daily for the audio assessment",
            "Prepare STAR-format answers for behavioral interview situations"
        ]
    },
    {
        "name": "Cognizant",
        "slug": "cognizant",
        "tier": "Service-Based",
        "overview": "Cognizant hires via GenC, GenC Elevate, and GenC Next tracks. GenC focuses on foundational aptitude and communication; Elevate and Next require strong problem-solving and full-stack/cloud skill sets.",
        "recruitment_stages": [
            {"stage": 1, "name": "Aptitude & Communication Test", "description": "Numerical reasoning, verbal ability, and logical reasoning test."},
            {"stage": 2, "name": "Technical Assessment / Coding", "description": "Intermediate data structure questions and database query writing."},
            {"stage": 3, "name": "Technical & HR Interview", "description": "Discussion on your preferred tech stack, problem-solving approach, and project live demonstration."}
        ],
        "skill_areas": ["Logical Reasoning", "Database Systems", "Core Java / Python", "Data Structures"],
        "aptitude_topics": ["Number Series", "Syllogisms", "Percentages", "Vocabulary", "Grammar"],
        "coding_topics": ["Linked Lists", "Sorting Algorithms", "Recursion", "Strings"],
        "technical_topics": ["Relational Database Design", "Primary vs Foreign Key Constraints", "Exception Handling"],
        "hr_topics": ["Why Cognizant?", "Describe a time you failed", "Team collaboration experience"],
        "checklist_items": [
            "Complete 30 logical reasoning questions on Syllogisms and Number Series",
            "Practice implementing Singly Linked List operations",
            "Revise database Normalization up to 3NF",
            "Be prepared to explain exception handling hierarchies in Python or Java"
        ]
    },
    {
        "name": "Capgemini",
        "slug": "capgemini",
        "tier": "Service-Based",
        "overview": "Capgemini assessments are recognized for Pseudocode, Game-Based Aptitude, and Spoken English rounds, followed by technical evaluation for Analyst and Senior Analyst roles.",
        "recruitment_stages": [
            {"stage": 1, "name": "Pseudocode Round", "description": "Tests logic tracing, bitwise operators, loop conditions, and recursion."},
            {"stage": 2, "name": "English Communication Test", "description": "Grammar, sentence completion, reading passages, and vocabulary."},
            {"stage": 3, "name": "Game-Based Aptitude", "description": "Cognitive agility mini-games (grid challenges, motion challenge, digit memorization)."},
            {"stage": 4, "name": "Technical & HR Interview", "description": "Interview evaluating project depth, technical fundamentals, and cultural alignment."}
        ],
        "skill_areas": ["Pseudocode Logic", "Cognitive Agility", "Verbal Fluency", "Basic Algorithms"],
        "aptitude_topics": ["Grammar", "Vocabulary", "Sentence Correction", "Logical Puzzles"],
        "coding_topics": ["Arrays", "Searching", "Basic Recursion"],
        "technical_topics": ["OOP Polymorphism & Inheritance", "SQL Subqueries", "Data Structures Selection"],
        "hr_topics": ["Self Introduction", "Handling conflict with teammates", "Why Capgemini?"],
        "checklist_items": [
            "Practice 25 bitwise operation and loop pseudocode problems",
            "Review English grammar rules: Subject-Verb agreement, Tenses, Modifiers",
            "Prepare detailed project architecture diagrams for your portfolio project"
        ]
    },
    {
        "name": "Amazon",
        "slug": "amazon",
        "tier": "Tech Giant",
        "overview": "Amazon hires software development engineers (SDE-1) through rigorous rounds focusing on Data Structures & Algorithms, Object-Oriented Design, and Amazon's 16 Leadership Principles.",
        "recruitment_stages": [
            {"stage": 1, "name": "Online Assessment (OA1 & OA2)", "description": "Two coding questions on DSA, followed by a Work Style Assessment based on Leadership Principles."},
            {"stage": 2, "name": "Technical Rounds (2-3 rounds)", "description": "Deep DSA problem-solving (Trees, Graphs, DP), Low-Level Design (LLD), and code quality."},
            {"stage": 3, "name": "Bar Raiser Round", "description": "Independent senior interviewer evaluating technical competence and Leadership Principle adherence."}
        ],
        "skill_areas": ["Data Structures & Algorithms", "Low-Level Design", "Leadership Principles", "System Design Basics"],
        "aptitude_topics": ["Permutations and Combinations", "Probability", "Logical Deduction"],
        "coding_topics": ["Trees", "Dynamic Programming", "Hash Maps", "Graphs", "Binary Search", "Heaps"],
        "technical_topics": ["Low-Level Object Oriented Design", "Time & Space Complexity Proofs", "Concurrency Basics"],
        "hr_topics": ["Customer Obsession", "Ownership", "Bias for Action", "Earn Trust", "Deliver Results"],
        "checklist_items": [
            "Master BFS/DFS on binary trees and graphs",
            "Solve Top 50 LeetCode Medium problems with optimal time/space complexities",
            "Prepare 2 stories for every one of Amazon's Leadership Principles using the STAR method",
            "Practice designing a parking lot or library management system using clean OOP principles",
            "Take timed coding challenges without an IDE auto-complete"
        ]
    },
    {
        "name": "Microsoft",
        "slug": "microsoft",
        "tier": "Tech Giant",
        "overview": "Microsoft recruits for Software Engineer roles through university programs (e.g. Engage, on-campus). Interviews emphasize algorithmic efficiency, clean modular code, edge-case testing, and growth mindset.",
        "recruitment_stages": [
            {"stage": 1, "name": "Online Coding Round", "description": "3 algorithmic coding challenges testing Arrays, Strings, Trees, and Dynamic Programming."},
            {"stage": 2, "name": "Technical Interview 1 & 2", "description": "Live coding, data structure selection, trade-off analysis, and dry-running code with custom test cases."},
            {"stage": 3, "name": "AA (As Appropriate) / Director Round", "description": "System architecture, behavioral alignment, culture fit, and passion for technology."}
        ],
        "skill_areas": ["Data Structures & Algorithms", "Clean Code Architecture", "System Design Basics", "Growth Mindset"],
        "aptitude_topics": ["Combinatorics", "Logical Puzzles", "Mathematical Reasoning"],
        "coding_topics": ["Linked Lists", "Trees", "Dynamic Programming", "Stacks and Queues", "Binary Search"],
        "technical_topics": ["Memory Management", "Operating Systems (Threads, Semaphores)", "Database Transactions"],
        "hr_topics": ["Why Microsoft?", "Tell me about a time you took a big risk", "Growth Mindset in Action"],
        "checklist_items": [
            "Practice writing bug-free code on a blank whiteboard / doc editor",
            "Master tree traversals and dynamic programming memoization techniques",
            "Revise Operating Systems fundamentals: Multithreading, Deadlocks, Virtual Memory",
            "Formulate answers demonstrating continuous learning and collaboration"
        ]
    }
]
