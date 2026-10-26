"""
Placement Resource Library seed data with verified educational links
"""

RESOURCES = [
    # 1. Aptitude Notes
    {
        "title": "IndiaBIX Quantitative Aptitude Formulas & Practice",
        "category": "Aptitude Notes",
        "description": "Comprehensive reference formulas, shortcuts, and topic-wise practice questions for campus aptitude rounds.",
        "external_url": "https://www.indiabix.com/aptitude/questions-and-answers/",
        "resource_type": "Interactive",
        "estimated_time": "30 mins",
        "is_featured": True
    },
    {
        "title": "GeeksforGeeks Aptitude Preparation Guide",
        "category": "Aptitude Notes",
        "description": "Structured tutorials covering Quantitative Aptitude, Logical Reasoning, and Verbal Ability with step-by-step solved examples.",
        "external_url": "https://www.geeksforgeeks.org/aptitude-questions-and-answers/",
        "resource_type": "Guide",
        "estimated_time": "25 mins",
        "is_featured": False
    },

    # 2. Coding Roadmaps
    {
        "title": "Roadmap.sh Computer Science Curriculum",
        "category": "Coding Roadmaps",
        "description": "Step-by-step visual roadmap covering core CS fundamentals, algorithms, systems, and engineering best practices.",
        "external_url": "https://roadmap.sh/computer-science",
        "resource_type": "Roadmap",
        "estimated_time": "15 mins",
        "is_featured": True
    },
    {
        "title": "Roadmap.sh Backend Developer Roadmap",
        "category": "Coding Roadmaps",
        "description": "Comprehensive visual guide to mastering databases, REST APIs, authentication, caching, and cloud deployments.",
        "external_url": "https://roadmap.sh/backend",
        "resource_type": "Roadmap",
        "estimated_time": "20 mins",
        "is_featured": False
    },
    {
        "title": "NeetCode Roadmap — Structured DSA Learning",
        "category": "Coding Roadmaps",
        "description": "Visual hierarchical dependency chart of Data Structures and Algorithms topics for software engineering interviews.",
        "external_url": "https://neetcode.io/roadmap",
        "resource_type": "Interactive",
        "estimated_time": "15 mins",
        "is_featured": True
    },

    # 3. DSA Guides
    {
        "title": "Tech Interview Handbook — Algorithmic Patterns",
        "category": "DSA Guides",
        "description": "Curated guide to common interview coding patterns including Two Pointers, Sliding Window, and Fast & Slow Pointers.",
        "external_url": "https://www.techinterviewhandbook.org/coding-interview-study-plan/",
        "resource_type": "Guide",
        "estimated_time": "45 mins",
        "is_featured": True
    },
    {
        "title": "Open Data Structures (Pat Morin)",
        "category": "DSA Guides",
        "description": "Rigorous open-access textbook on fundamental data structures with asymptotic complexity analysis and code implementations.",
        "external_url": "https://opendatastructures.org/",
        "resource_type": "Documentation",
        "estimated_time": "60 mins",
        "is_featured": False
    },
    {
        "title": "VisuAlgo — Visualizing Data Structures and Algorithms",
        "category": "DSA Guides",
        "description": "Interactive animated visualizations of sorting algorithms, binary search trees, graph traversals, and recursion.",
        "external_url": "https://visualgo.net/en",
        "resource_type": "Interactive",
        "estimated_time": "30 mins",
        "is_featured": False
    },

    # 4. Resume Preparation
    {
        "title": "Jake's Resume Overleaf Template (Single-Page LaTeX)",
        "category": "Resume Preparation",
        "description": "Industry-standard, ATS-friendly LaTeX resume template recommended for campus and off-campus tech placements.",
        "external_url": "https://www.overleaf.com/latex/templates/jakes-resume/syzsqbwpwgkg",
        "resource_type": "Documentation",
        "estimated_time": "20 mins",
        "is_featured": True
    },
    {
        "title": "Harvard Office of Career Services Resume & Cover Letter Guide",
        "category": "Resume Preparation",
        "description": "Action verbs, impact-driven bullet point formatting using the X-Y-Z formula, and layout principles for university students.",
        "external_url": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "resource_type": "Guide",
        "estimated_time": "25 mins",
        "is_featured": False
    },

    # 5. Interview Preparation
    {
        "title": "Tech Interview Handbook — Behavioral Interview Guide",
        "category": "Interview Preparation",
        "description": "Strategies for answering non-technical questions, articulating leadership traits, and using the STAR storytelling method.",
        "external_url": "https://www.techinterviewhandbook.org/behavioral-interview-questions/",
        "resource_type": "Guide",
        "estimated_time": "30 mins",
        "is_featured": True
    },
    {
        "title": "Pramp / Interviewing.io Technical Interview Cheatsheet",
        "category": "Interview Preparation",
        "description": "Framework for communicating during live coding interviews: clarifying constraints, discussing trade-offs, and debugging.",
        "external_url": "https://www.pramp.com/resources/interview-tips",
        "resource_type": "Article",
        "estimated_time": "15 mins",
        "is_featured": False
    },

    # 6. Core CS Concepts
    {
        "title": "Database Systems Concepts & SQL Tutorial (W3Schools)",
        "category": "Core CS Concepts",
        "description": "Hands-on SQL practice covering SELECT, JOIN, GROUP BY, subqueries, indexing, and transactional isolation levels.",
        "external_url": "https://www.w3schools.com/sql/",
        "resource_type": "Interactive",
        "estimated_time": "40 mins",
        "is_featured": True
    },
    {
        "title": "Operating Systems: Three Easy Pieces (OSTEP)",
        "category": "Core CS Concepts",
        "description": "Free online textbook covering virtualization, concurrency (threads, locks, semaphores), and persistence (file systems).",
        "external_url": "https://pages.cs.wisc.edu/~remzi/OSTEP/",
        "resource_type": "Documentation",
        "estimated_time": "60 mins",
        "is_featured": False
    },
    {
        "title": "Computer Networks: Stanford CS144 Notes",
        "category": "Core CS Concepts",
        "description": "Explanations of TCP/IP stack, DNS, routing protocols, HTTP/HTTPS, handshake mechanisms, and socket programming.",
        "external_url": "https://web.stanford.edu/class/cs144/",
        "resource_type": "Documentation",
        "estimated_time": "45 mins",
        "is_featured": False
    },
    {
        "title": "Refactoring Guru: Design Patterns Cheatsheet",
        "category": "Core CS Concepts",
        "description": "Visual reference for Creational, Structural, and Behavioral OOP design patterns with real-world code examples.",
        "external_url": "https://refactoring.guru/design-patterns",
        "resource_type": "Guide",
        "estimated_time": "30 mins",
        "is_featured": True
    },

    # 7. Git and GitHub
    {
        "title": "Pro Git Book (Official Git Documentation)",
        "category": "Git and GitHub",
        "description": "The complete reference guide to version control, branching strategies, rebasing, merge conflicts, and commit hygiene.",
        "external_url": "https://git-scm.com/book/en/v2",
        "resource_type": "Documentation",
        "estimated_time": "35 mins",
        "is_featured": True
    },
    {
        "title": "Learn Git Branching — Interactive Game",
        "category": "Git and GitHub",
        "description": "Visual and interactive sandbox for learning git commit, branch, merge, rebase, cherry-pick, and reset commands.",
        "external_url": "https://learngitbranching.js.org/",
        "resource_type": "Interactive",
        "estimated_time": "25 mins",
        "is_featured": False
    },
    {
        "title": "GitHub Skills — Hands-on Micro Courses",
        "category": "Git and GitHub",
        "description": "Interactive GitHub-native tutorials on pull requests, reviewing code, writing READMEs, and GitHub Actions.",
        "external_url": "https://skills.github.com/",
        "resource_type": "Interactive",
        "estimated_time": "30 mins",
        "is_featured": False
    },

    # 8. Communication Skills
    {
        "title": "BBC Learning English — Professional Communication",
        "category": "Communication Skills",
        "description": "Audio and video modules on professional English, polite disagreement, presentations, and interview fluency.",
        "external_url": "https://www.bbc.co.uk/learningenglish/english/features/english-at-work",
        "resource_type": "Video",
        "estimated_time": "20 mins",
        "is_featured": True
    },
    {
        "title": "Toastmasters International Public Speaking Tips",
        "category": "Communication Skills",
        "description": "Practical guides on managing speaking anxiety, structuring concise oral responses, and active listening.",
        "external_url": "https://www.toastmasters.org/resources/public-speaking-tips",
        "resource_type": "Article",
        "estimated_time": "15 mins",
        "is_featured": False
    },
    {
        "title": "Grammarly Handbook — Professional Writing",
        "category": "Communication Skills",
        "description": "Concise rules for business email etiquette, avoiding common grammatical errors, and sentence clarity.",
        "external_url": "https://www.grammarly.com/blog/category/handbook/",
        "resource_type": "Guide",
        "estimated_time": "20 mins",
        "is_featured": False
    }
]
