"""
Interview Room questions seed data with 60+ verified technical and HR questions
"""

INTERVIEW_QUESTIONS = [
    # --- TECHNICAL: OOP (1-8) ---
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Easy",
        "question": "What are the four pillars of Object-Oriented Programming? Explain each with a real-world example.",
        "answer": "The four fundamental pillars of OOP are:\n1. Encapsulation: Bundling data (attributes) and methods that operate on the data into a single unit (class), while restricting direct access to internal details (e.g., using private variables with getters and setters, like a bank account concealing its exact balance variable).\n2. Abstraction: Hiding internal implementation complexities and showing only essential features to the user (e.g., driving a car by pressing the accelerator without needing to understand fuel injection mechanics).\n3. Inheritance: Mechanism where a child class acquires properties and behaviors from a parent class, promoting code reuse (e.g., a 'SavingsAccount' inheriting from a base 'Account' class).\n4. Polymorphism: Ability of an entity to take multiple forms—either compile-time (method overloading) or runtime (method overriding, such as a base 'draw()' method implemented differently by 'Circle' and 'Square').",
        "key_points": ["Encapsulation binds data and methods together with access control", "Abstraction hides background details using interfaces/abstract classes", "Inheritance enables hierarchical classification and DRY code", "Polymorphism means 'many forms' (overloading vs overriding)"],
        "common_mistakes": ["Confusing Encapsulation with Abstraction (Encapsulation is data hiding/packaging, Abstraction is interface design)", "Giving purely abstract definitions without tangible examples"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Medium",
        "question": "What is the difference between Method Overloading and Method Overriding?",
        "answer": "Method Overloading (Compile-time / Static Polymorphism) occurs when multiple methods in the same class share the same name but have different signatures (number, type, or order of parameters). The compiler resolves which method to call at compile-time.\n\nMethod Overriding (Runtime / Dynamic Polymorphism) occurs when a subclass provides a specific implementation for a method already defined in its superclass, having the exact same name, return type, and parameters. The decision of which method to execute is resolved dynamically at runtime via virtual method tables based on the actual object instance.",
        "key_points": ["Overloading happens in the same class; Overriding requires an inheritance relationship", "Overloading must differ in parameter list; Overriding must have identical signature", "Overloading is compile-time resolution; Overriding is runtime dynamic dispatch"],
        "common_mistakes": ["Claiming changing only the return type is sufficient for overloading (in most typed languages like C++/Java, it is not)"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Medium",
        "question": "Explain the difference between an Abstract Class and an Interface.",
        "answer": "An Abstract Class is a class that cannot be instantiated and may contain both abstract methods (without body) and concrete methods (with implementation), along with state variables (instance fields). A class can only inherit from one abstract class (single inheritance in languages like Java/C#).\n\nAn Interface defines a strict contract specifying what a class must do, rather than how. Traditionally, interfaces only contain method signatures and constants, and a class can implement multiple interfaces (supporting multiple inheritance of types). Abstract classes represent an 'is-a' relationship with shared state/logic, whereas interfaces represent a 'can-do' capability.",
        "key_points": ["Abstract classes can maintain state/fields and concrete helper methods", "Interfaces define pure contracts and allow multiple inheritance", "Use abstract class for closely related classes sharing code; interface for unrelated classes supporting a common capability"],
        "common_mistakes": ["Forgetting that interfaces in modern Java (8+) can have default and static methods"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Hard",
        "question": "What are the SOLID principles in software design? Summarize each principle.",
        "answer": "SOLID represents five design principles for maintainable and scalable object-oriented software:\n1. S - Single Responsibility Principle (SRP): A class should have one, and only one, reason to change.\n2. O - Open/Closed Principle (OCP): Software entities should be open for extension, but closed for modification.\n3. L - Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types without altering program correctness.\n4. I - Interface Segregation Principle (ISP): Clients should not be forced to depend on methods they do not use (prefer small, role-specific interfaces over fat interfaces).\n5. D - Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions.",
        "key_points": ["S: One reason to change", "O: Extend behavior without editing tested code", "L: Child can replace parent cleanly (e.g. Classic Rectangle vs Square violation)", "I: Fat interfaces split into focused interfaces", "D: Invert control and inject abstractions"],
        "common_mistakes": ["Reciting acronyms without explaining the architectural motivation behind each"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Medium",
        "question": "What is the Diamond Problem in Multiple Inheritance, and how is it resolved in Python or C++?",
        "answer": "The Diamond Problem arises when a class D inherits from classes B and C, both of which inherit from a common base class A. If both B and C override a method from A, ambiguity arises as to which version class D should inherit.\n\nIn C++, this ambiguity is resolved using Virtual Inheritance (virtual base classes), ensuring only a single instance of class A is included in the object hierarchy.\n\nIn Python, it is resolved automatically using the C3 Linearization algorithm to determine the Method Resolution Order (MRO), which can be inspected using `ClassName.__mro__`.",
        "key_points": ["A -> B, C -> D diamond inheritance shape creates ambiguous method paths", "C++ uses 'virtual public A' base inheritance", "Python uses C3 linearization MRO algorithm"],
        "common_mistakes": ["Failing to mention how Python resolves this using `super()` and MRO"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Easy",
        "question": "What is the difference between Composition and Inheritance? When should you favor Composition?",
        "answer": "Inheritance represents an 'is-a' relationship (e.g., A Dog is an Animal), tightly coupling child classes to parent class implementation details.\n\nComposition represents a 'has-a' relationship (e.g., A Car has an Engine), where a class contains references to other objects to reuse functionality. Software engineering best practices favor composition over inheritance ('Favor object composition over class inheritance') because composition provides loose coupling, allows changing behavior at runtime via dependency injection, and prevents fragile base class hierarchies.",
        "key_points": ["Inheritance: is-a relationship, tight compile-time coupling", "Composition: has-a relationship, flexible runtime delegation", "Composition minimizes fragile base class ripple effects"],
        "common_mistakes": ["Claiming inheritance is obsolete—it is still useful when true polymorphism and type substitution are needed"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Easy",
        "question": "What is a Constructor and what is a Destructor?",
        "answer": "A constructor is a special member method invoked automatically when an object of a class is instantiated. Its primary purpose is to initialize the object's state and allocate necessary resources (e.g., `__init__` in Python, or class-named method in C++/Java).\n\nA destructor is invoked when an object is destroyed or goes out of scope, responsible for releasing resources such as closing file handles, network sockets, or freeing unmanaged heap memory (e.g., `~ClassName()` in C++, `__del__` in Python).",
        "key_points": ["Constructors initialize object fields upon instantiation", "Destructors clean up resources before memory deallocation", "Garbage-collected languages (Java/Python) manage memory automatically but still need resource cleanup (e.g., context managers)"],
        "common_mistakes": ["Assuming destructors in Python or Java guarantee immediate execution when memory runs low"]
    },
    {
        "category": "Technical",
        "topic": "OOPs",
        "difficulty": "Medium",
        "question": "What are Access Specifiers and why are they used?",
        "answer": "Access specifiers (or access modifiers) control the scope and visibility of class members (variables and methods) to enforce encapsulation:\n1. Public: Accessible from anywhere inside or outside the class/package.\n2. Protected: Accessible within the class itself and by derived (subclass) instances.\n3. Private: Accessible only within the class where they are declared.\n\nIn Python, access specifiers are enforced by convention: public by default, single underscore `_var` for protected/internal convention, and double underscore `__var` for private via name mangling.",
        "key_points": ["Public: open access", "Protected: accessible by class and subclasses", "Private: restricted to the declaring class", "Python uses `_` convention and `__` name mangling"],
        "common_mistakes": ["Saying private variables in Python are strictly impossible to access—name mangling allows `_ClassName__var` access"]
    },

    # --- TECHNICAL: DBMS (9-17) ---
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Easy",
        "question": "What are ACID properties in a Database Management System?",
        "answer": "ACID properties ensure reliable processing of database transactions:\n1. Atomicity: The 'all-or-nothing' rule. Either all operations of a transaction execute completely, or the database rolls back to its original state if any step fails.\n2. Consistency: A transaction must transition the database from one valid state to another, preserving all integrity constraints (e.g., foreign keys, unique rules).\n3. Isolation: Concurrent execution of transactions leaves the database in the same state as if they were executed sequentially. Uncommitted changes of one transaction are not visible to others.\n4. Durability: Once a transaction commits, its changes are permanently written to persistent storage and will not be lost, even in the event of a sudden power outage or system crash.",
        "key_points": ["A: All or nothing", "C: Constraints and invariants maintained", "I: Concurrent transactions do not interfere", "D: Committed writes persist across crashes"],
        "common_mistakes": ["Describing consistency as duplicate data synchronization across servers (that is distributed consistency/CAP theorem, not ACID consistency)"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Medium",
        "question": "Explain the different types of SQL JOINs with clear diagrams or examples.",
        "answer": "SQL JOINs combine rows from two or more tables based on a related column:\n1. INNER JOIN: Returns only records that have matching values in both tables.\n2. LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table (unmatched right columns return NULL).\n3. RIGHT (OUTER) JOIN: Returns all records from the right table, and matched records from the left table (unmatched left columns return NULL).\n4. FULL (OUTER) JOIN: Returns all records when there is a match in either the left or right table.\n5. CROSS JOIN: Returns the Cartesian product of all rows from both tables.",
        "key_points": ["Inner Join: Intersection of matching keys", "Left Join: All left rows + matched right rows (NULL for unmatched)", "Full Outer Join: Union of all rows from both tables"],
        "common_mistakes": ["Confusing LEFT JOIN with UNION (JOIN merges columns horizontally; UNION merges rows vertically)"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Medium",
        "question": "What is Database Normalization? Explain 1NF, 2NF, and 3NF.",
        "answer": "Database Normalization is the process of structuring relational database tables to reduce data redundancy and eliminate insert, update, and delete anomalies.\n- 1NF (First Normal Form): Each table column must contain atomic (indivisible) values, and each record must be unique (primary key).\n- 2NF (Second Normal Form): Must be in 1NF and have NO partial dependency—every non-prime attribute must depend on the whole candidate key, not a subset (relevant for composite keys).\n- 3NF (Third Normal Form): Must be in 2NF and have NO transitive dependencies—non-prime attributes must depend only on the candidate key and not on other non-prime attributes.",
        "key_points": ["1NF: Atomic values, no repeating groups", "2NF: 1NF + no partial dependency", "3NF: 2NF + no transitive dependency ('The key, the whole key, and nothing but the key')"],
        "common_mistakes": ["Not explaining what a partial or transitive dependency actually means"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Medium",
        "question": "What is an Index in SQL? What are the trade-offs of adding indexes?",
        "answer": "A database index is a data structure (typically a B-Tree or B+ Tree) that improves the speed of data retrieval operations on a database table at the cost of additional storage and slower write operations.\n\nAdvantages:\n- Drastically speeds up SELECT queries with WHERE filters, JOIN conditions, and ORDER BY clauses from O(N) full table scans to O(log N).\n\nTrade-offs:\n- Additional disk space required to store the index tree.\n- Slower INSERT, UPDATE, and DELETE operations because the database must update both the table data and every relevant index structure on write.",
        "key_points": ["B-Tree/B+ Tree structure", "Transforms O(N) scan to O(log N) lookup", "Speeds up reads; slows down writes and consumes storage"],
        "common_mistakes": ["Claiming we should put an index on every column in a table"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Medium",
        "question": "What is the difference between Primary Key, Unique Key, and Foreign Key?",
        "answer": "1. Primary Key: Uniquely identifies each record in a table. Cannot accept NULL values, and a table can have only one Primary Key (which automatically creates a clustered index in most engines).\n2. Unique Key: Ensures all values in a column are distinct across the table. Can accept one (or more, depending on SQL dialect) NULL value, and a table can have multiple unique keys.\n3. Foreign Key: A column or set of columns in one table that references the Primary Key or Unique Key of another table, enforcing referential integrity between related entities.",
        "key_points": ["Primary Key: 1 per table, NOT NULL, unique identifier", "Unique Key: Multiple allowed per table, allows NULLs", "Foreign Key: Enforces referential integrity across related tables"],
        "common_mistakes": ["Claiming Unique Key cannot accept any NULL values at all (most SQL engines allow one NULL)"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Hard",
        "question": "What are Transaction Isolation Levels and what read phenomena do they prevent?",
        "answer": "SQL standard defines four transaction isolation levels to balance concurrency against data consistency anomalies:\n1. Read Uncommitted: Lowest level. Suffers from Dirty Reads, Non-Repeatable Reads, and Phantom Reads.\n2. Read Committed: Prevents Dirty Reads (only reads committed data). Still prone to Non-Repeatable and Phantom reads. (Default in PostgreSQL/Oracle).\n3. Repeatable Read: Prevents Dirty Reads and Non-Repeatable Reads (guarantees reading the same row returns identical values). May still suffer from Phantom Reads in some engines. (Default in MySQL InnoDB via MVCC).\n4. Serializable: Highest level. Complete isolation as if transactions ran serially; prevents all anomalies, but introduces significant lock contention.",
        "key_points": ["Dirty Read: Reading uncommitted changes", "Non-Repeatable Read: Same row read twice returns different values", "Phantom Read: Range query returns newly inserted rows", "Levels: Read Uncommitted < Read Committed < Repeatable Read < Serializable"],
        "common_mistakes": ["Failing to define Dirty Read or Phantom Read when listing isolation levels"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Easy",
        "question": "What is the difference between DELETE, TRUNCATE, and DROP?",
        "answer": "1. DELETE: A DML (Data Manipulation Language) command that removes specific rows matching a WHERE clause. It logs individual row deletions, can be rolled back inside a transaction, and triggers database triggers.\n2. TRUNCATE: A DDL (Data Definition Language) command that deallocates all data pages in a table, effectively emptying it. It is much faster than DELETE, cannot filter rows with a WHERE clause, and resets auto-increment counters.\n3. DROP: A DDL command that completely deletes both the table data AND the table schema/structure from the database dictionary permanently.",
        "key_points": ["DELETE: DML, can filter with WHERE, logs row-by-row, triggers fire", "TRUNCATE: DDL, empties entire table, resets identity, faster", "DROP: DDL, destroys both data and schema definition"],
        "common_mistakes": ["Saying TRUNCATE cannot be rolled back in any database (in modern engines like PostgreSQL/SQL Server, TRUNCATE can be rolled back if in a transaction)"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Medium",
        "question": "What is the difference between SQL (Relational) and NoSQL databases? When should you choose each?",
        "answer": "SQL Databases (e.g., PostgreSQL, MySQL, SQLite) are relational, table-based, enforce strict predefined schemas, and prioritize ACID compliance. They excel at structured data with complex relationships and transactional consistency.\n\nNoSQL Databases (e.g., MongoDB, Redis, Cassandra) are non-relational, schema-less or dynamic schema (document, key-value, column-family, graph), and prioritize horizontal scalability and flexible data models (often following BASE / Eventual Consistency).\n\nChoose SQL when: Data structure is predictable, relational integrity and multi-table transactions are crucial (financial systems, ERP).\nChoose NoSQL when: Data is unstructured or rapidly evolving, high write throughput across clusters is needed, or hierarchical JSON document storage is natural.",
        "key_points": ["SQL: Relational, fixed schema, vertical scaling, ACID", "NoSQL: Non-relational, flexible schema, horizontal scaling, BASE", "Choose SQL for transactional consistency; NoSQL for unstructured high-velocity scale"],
        "common_mistakes": ["Claiming NoSQL is always faster than SQL (SQL with proper indexing is exceptionally fast for relational queries)"]
    },
    {
        "category": "Technical",
        "topic": "DBMS",
        "difficulty": "Easy",
        "question": "What is a View in SQL and what are its benefits?",
        "answer": "A View is a virtual table based on the result-set of a pre-defined SQL statement. A view contains rows and columns just like a real table, but it does not store the physical data itself (unless it is an indexed/materialized view).\n\nBenefits:\n1. Security: Restrict direct table access by exposing only permitted columns/rows to certain user roles.\n2. Simplicity: Encapsulates complex JOINs and aggregate calculations into a clean queryable virtual table.\n3. Data Integrity: Provides a consistent interface even if underlying schema changes (backward compatibility).",
        "key_points": ["Virtual table with no physical storage", "Hides query complexity", "Improves security and access control"],
        "common_mistakes": ["Assuming views make queries run faster automatically (regular views re-execute the underlying query)"]
    },

    # --- TECHNICAL: OPERATING SYSTEMS (18-25) ---
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "What is the difference between a Process and a Thread?",
        "answer": "A Process is an executing program instance with its own independent memory address space (Text, Data, Heap, and Stack) allocated by the operating system. Inter-process communication (IPC) requires mechanisms like pipes, sockets, or shared memory.\n\nA Thread (lightweight process) is the smallest unit of CPU execution within a process. Multiple threads of the same process share the process's code section, data section, and heap memory, but each thread maintains its own private Program Counter, registers, and Call Stack.\n\nContext switching between threads is much faster and cheaper than between processes because memory page mappings do not need to be flushed.",
        "key_points": ["Process has isolated address space; Threads share memory within the same process", "Threads have their own Stack and Program Counter", "Thread context switches have lower overhead than process context switches"],
        "common_mistakes": ["Saying threads share their stack (each thread MUST have its own independent execution stack)"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is a Deadlock? What are the four Coffman conditions necessary for a deadlock to occur?",
        "answer": "A Deadlock is a situation where two or more processes are permanently blocked because each process holds a resource that another process needs, and neither can proceed.\n\nThe four necessary Coffman conditions are:\n1. Mutual Exclusion: At least one resource must be held in a non-shareable mode.\n2. Hold and Wait: A process holding at least one resource is actively waiting to acquire additional resources held by other processes.\n3. No Preemption: Resources cannot be forcibly taken from a process; they can only be released voluntarily after completion.\n4. Circular Wait: A closed chain of processes exists such that each process holds one resource and waits for a resource held by the next process in the cycle.",
        "key_points": ["Mutual Exclusion", "Hold and Wait", "No Preemption", "Circular Wait", "Breaking ANY ONE of these four conditions prevents deadlock"],
        "common_mistakes": ["Forgetting that breaking just one condition is sufficient to eliminate deadlocks"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is Virtual Memory, Paging, and Page Fault?",
        "answer": "Virtual Memory is a memory management technique that gives programs the illusion of having a large, contiguous address space, even if physical RAM is limited and fragmented.\n\n- Paging divides virtual memory into fixed-size blocks called 'Pages', and physical RAM into blocks called 'Frames'. The OS Memory Management Unit (MMU) uses a Page Table to translate virtual addresses to physical frame addresses.\n- A Page Fault occurs when a program attempts to access a virtual memory page that is currently not mapped into physical RAM. The OS interrupts execution, fetches the missing page from disk (swap space) into RAM, updates the page table, and resumes execution.",
        "key_points": ["Virtual memory decouples logical address from physical RAM", "Pages (virtual) map to Frames (physical)", "Page fault brings page from disk swap space to RAM"],
        "common_mistakes": ["Thinking page fault is a software crash or fatal error (it is normal virtual memory handling)"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "Explain CPU Scheduling and compare Preemptive vs Non-Preemptive scheduling.",
        "answer": "CPU scheduling determines which process in the ready queue is allocated the CPU core for execution.\n\n- Non-Preemptive Scheduling: Once a process is allocated the CPU, it holds it until it either terminates or transitions to a waiting state (e.g., I/O). Examples: FCFS (First Come First Served), Non-preemptive SJF.\n- Preemptive Scheduling: The OS can interrupt and context-switch an actively running process if a higher-priority process arrives or its time quantum expires. Examples: Round Robin (RR), Preemptive SJF / SRTF, Priority Scheduling.",
        "key_points": ["Preemptive: OS can forcefully take away CPU (Round Robin, Priority)", "Non-preemptive: Process holds CPU until it yields or terminates", "Preemption enables responsive multitasking in modern OSs"],
        "common_mistakes": ["Confusing Round Robin with FCFS"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Medium",
        "question": "What is a Race Condition and how do Semaphores and Mutexes prevent it?",
        "answer": "A Race Condition occurs in concurrent programming when two or more threads attempt to access and modify shared data simultaneously, and the final outcome depends on the non-deterministic order of thread execution.\n\nSolutions:\n- Mutex (Mutual Exclusion Lock): A locking mechanism owned by a single thread at a time. Only the thread that locks the mutex can unlock it. It ensures that only one thread executes a critical section.\n- Semaphore: A signaling mechanism using an integer counter. A Binary Semaphore functions similarly to a mutex (value 0 or 1), while a Counting Semaphore allows a fixed number (N) of concurrent threads to access a pool of shared resources (using `wait()` and `signal()` operations).",
        "key_points": ["Race condition: Concurrent reads/writes yield unpredictable output", "Mutex: Locking mechanism, ownership-based", "Semaphore: Signaling mechanism with counter value"],
        "common_mistakes": ["Claiming Mutex and Binary Semaphore are 100% identical (Mutex has strict thread ownership semantics)"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Hard",
        "question": "What is Thrashing in Operating Systems?",
        "answer": "Thrashing is a state where the CPU spends significantly more time swapping virtual memory pages into and out of disk than executing user instructions.\n\nIt occurs when the total working sets of active processes exceed the available physical RAM. As page fault frequency skyrockets, processes stall waiting for disk I/O. The OS scheduler may mistakenly perceive low CPU utilization and launch more processes, worsening the bottleneck.\n\nPrevention: Using the Working Set Model or Page Fault Frequency (PFF) algorithm to suspend low-priority processes when RAM demand exceeds capacity.",
        "key_points": ["High paging activity vs low CPU productive execution", "Caused by overcommitting RAM beyond total working sets", "Resolved by suspending processes or adding RAM"],
        "common_mistakes": ["Confusing thrashing with process starvation"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "What is a System Call? Name three common categories.",
        "answer": "A System Call (syscall) is the programmatic interface that allows a user-space application to request services from the operating system kernel running in privileged mode (Ring 0).\n\nCategories:\n1. Process Control: `fork()`, `exec()`, `wait()`, `exit()`\n2. File Management: `open()`, `read()`, `write()`, `close()`\n3. Device & Network Management: `ioctl()`, `socket()`, `bind()`, `connect()`",
        "key_points": ["Bridge between user mode and kernel mode", "Transitions CPU from unprivileged to privileged execution", "Essential for hardware, file, and network operations"],
        "common_mistakes": ["Thinking standard library functions like `printf()` are raw syscalls (they wrap `write()` syscall)"]
    },
    {
        "category": "Technical",
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "question": "What is a Zombie Process vs an Orphan Process?",
        "answer": "- Zombie Process: A process that has finished execution (called `exit()`), but its entry still remains in the process table because its parent has not yet read its exit status code using `wait()`.\n- Orphan Process: A process whose parent process has terminated or crashed while the child process is still actively running. In Linux, orphan processes are adopted by the init process (`PID 1` or systemd), which regularly reaps zombie children.",
        "key_points": ["Zombie: Finished execution, awaiting parent `wait()`, consumes no memory/CPU except PID slot", "Orphan: Parent died while child is running; adopted by PID 1 (init)"],
        "common_mistakes": ["Thinking zombie processes consume large amounts of CPU (they only occupy a PID entry in the process table)"]
    },

    # --- TECHNICAL: COMPUTER NETWORKS (26-32) ---
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "question": "What is the OSI Model? List its 7 layers from bottom to top.",
        "answer": "The OSI (Open Systems Interconnection) reference model standardizes network communication protocols across 7 conceptual layers:\n1. Physical Layer: Transmits raw bits over physical mediums (cables, radio waves, optical fiber).\n2. Data Link Layer: Node-to-node frame delivery, MAC addressing, error detection (Ethernet, Wi-Fi).\n3. Network Layer: Routing data packets across networks, logical IP addressing (IPv4, IPv6, ICMP).\n4. Transport Layer: End-to-end communication, port addressing, segmentation, reliability (TCP, UDP).\n5. Session Layer: Establishes, manages, and terminates sessions between applications.\n6. Presentation Layer: Data translation, formatting, encryption (SSL/TLS), and compression.\n7. Application Layer: High-level protocols interacting directly with user applications (HTTP, DNS, SMTP, FTP).",
        "key_points": ["Please Do Not Throw Sausage Pizza Away mnemonic", "Layer 1 to 7: Physical, Data Link, Network, Transport, Session, Presentation, Application", "TCP/IP condenses layers 5-7 into Application"],
        "common_mistakes": ["Listing the layers in reverse order or mixing up Data Link and Network layer responsibilities"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "Compare TCP and UDP. When should you use each protocol?",
        "answer": "TCP (Transmission Control Protocol):\n- Connection-oriented (establishes connection via 3-Way Handshake).\n- Guarantees in-order, reliable delivery via sequence numbers and ACKs.\n- Includes flow control and congestion control, with higher protocol overhead.\n- Ideal for: Web browsing (HTTP/HTTPS), file transfers (FTP), email (SMTP), where zero data loss is critical.\n\nUDP (User Datagram Protocol):\n- Connectionless (sends standalone datagrams without establishing a handshake).\n- Unreliable (no ACKs, retransmissions, or ordering guarantees).\n- Extremely low latency and lightweight overhead.\n- Ideal for: Video streaming, VoIP, live gaming, and DNS queries, where speed matters more than occasional lost packets.",
        "key_points": ["TCP: Reliable, ordered, connection-oriented, heavier", "UDP: Unreliable, unordered, connectionless, low-latency", "TCP for data integrity; UDP for real-time streaming/gaming"],
        "common_mistakes": ["Describing UDP as 'bad' because it is unreliable (unreliability is an intentional architectural trade-off for minimal latency)"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "Explain the TCP 3-Way Handshake mechanism.",
        "answer": "The TCP 3-Way Handshake establishes a synchronized connection between client and server before data transfer:\n1. SYN: The client generates an Initial Sequence Number (ISN_c) and sends a SYN packet to the server (`SYN = 1, Seq = ISN_c`).\n2. SYN-ACK: The server receives the SYN, allocates buffers, generates its own sequence number (ISN_s), and responds with a SYN-ACK packet (`SYN = 1, ACK = 1, Seq = ISN_s, Ack_Num = ISN_c + 1`).\n3. ACK: The client acknowledges the server's sequence number by sending an ACK packet (`ACK = 1, Ack_Num = ISN_s + 1`). Both sides are now in the ESTABLISHED state and can transmit payload data.",
        "key_points": ["SYN -> SYN-ACK -> ACK sequence", "Synchronizes sequence numbers on both endpoints", "Prevents old, delayed packets from creating duplicate connections"],
        "common_mistakes": ["Forgetting to state that sequence numbers increment by 1 in the ACK replies"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "What happens under the hood when you type a URL like 'https://www.google.com' into your browser and press Enter?",
        "answer": "The full end-to-end workflow involves:\n1. URL Parsing: Browser extracts protocol (HTTPS), domain (www.google.com), and port (443).\n2. DNS Resolution: Checks browser cache -> OS cache -> router cache -> ISP recursive resolver -> Root -> TLD (.com) -> Authoritative nameserver to resolve IP address.\n3. TCP Connection: Browser initiates 3-way handshake (SYN, SYN-ACK, ACK) with the server IP.\n4. TLS Handshake: Client and server negotiate cipher suites, authenticate the server's SSL certificate, and derive symmetric session keys.\n5. HTTP Request: Browser transmits `GET / HTTP/1.1` over encrypted TLS.\n6. Server Response: Web server / reverse proxy routes request to application, returns HTTP 200 with HTML payload.\n7. Browser Rendering: Browser parses HTML to construct DOM tree, parses CSS for CSSOM, builds Render Tree, calculates Layout, and paints pixels to screen.",
        "key_points": ["DNS lookup hierarchy", "TCP 3-way handshake", "TLS certificate verification & session key exchange", "HTTP GET and 200 OK", "Browser DOM/CSSOM render pipeline"],
        "common_mistakes": ["Jumping directly from URL to HTML rendering without mentioning DNS, TCP, or TLS handshakes"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "question": "What is the difference between HTTP and HTTPS?",
        "answer": "HTTP (HyperText Transfer Protocol) transmits data as clear, unencrypted plaintext over port 80, making it vulnerable to packet sniffing, eavesdropping, and Man-in-the-Middle (MITM) attacks.\n\nHTTPS (HTTP Secure) runs HTTP on top of the SSL/TLS (Transport Layer Security) encryption protocol over port 443. It guarantees:\n1. Encryption: Data payload is encrypted using symmetric session keys derived during TLS handshake.\n2. Integrity: Data cannot be modified or corrupted in transit without detection (via MAC / HMAC hashes).\n3. Authentication: Digital certificates verified by trusted Certificate Authorities (CAs) prove the server's true identity.",
        "key_points": ["Port 80 (plaintext) vs Port 443 (encrypted)", "HTTPS adds SSL/TLS layer", "Guarantees Confidentiality, Integrity, and Authentication"],
        "common_mistakes": ["Thinking HTTPS encrypts the target IP address (IP routing information remains in cleartext IP headers)"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "question": "What are the common HTTP status code classes?",
        "answer": "HTTP response status codes are 3-digit integers categorized into five classes:\n- 1xx (Informational): Request received, continuing process (e.g., 101 Switching Protocols).\n- 2xx (Success): Action was successfully received, understood, and accepted (e.g., 200 OK, 201 Created, 204 No Content).\n- 3xx (Redirection): Further action must be taken by client (e.g., 301 Moved Permanently, 302 Found, 304 Not Modified).\n- 4xx (Client Error): Request contains bad syntax or cannot be fulfilled (e.g., 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found).\n- 5xx (Server Error): Server failed to fulfill an apparently valid request (e.g., 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).",
        "key_points": ["1xx Informational, 2xx Success, 3xx Redirection, 4xx Client Error, 5xx Server Error", "401 (needs login) vs 403 (logged in but forbidden)", "502 Bad Gateway vs 504 Gateway Timeout"],
        "common_mistakes": ["Confusing 401 Unauthorized (unauthenticated) with 403 Forbidden (authenticated, but lacking permissions)"]
    },
    {
        "category": "Technical",
        "topic": "Computer Networks",
        "difficulty": "Medium",
        "question": "What is DNS and how does recursive resolution work?",
        "answer": "DNS (Domain Name System) is the hierarchical distributed directory service that translates human-readable domain names (e.g., example.com) into machine-routable IP addresses (e.g., 93.184.216.34).\n\nRecursive Resolution Flow:\n1. Client asks local Recursive Resolver (e.g., ISP or 8.8.8.8).\n2. Resolver asks a Root Nameserver (which directs to the .com TLD server).\n3. Resolver asks the .com TLD Nameserver (which directs to the authoritative nameserver for example.com).\n4. Resolver queries the Authoritative Nameserver (which returns the IP address record, e.g. A record).\n5. Resolver caches the result according to TTL and returns the IP to the client.",
        "key_points": ["Translates hostname to IP address", "Root Server -> TLD Server -> Authoritative Nameserver", "TTL controls caching lifespan"],
        "common_mistakes": ["Thinking the client directly queries root servers for every single website visit"]
    },

    # --- TECHNICAL: DATA STRUCTURES & ALGORITHMS (33-40) ---
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Easy",
        "question": "What is the difference between an Array and a Linked List?",
        "answer": "- Array: Contiguous memory allocation. Supports O(1) random access by index. Insertion and deletion in the middle takes O(N) due to element shifting. Size is typically fixed (or dynamic arrays resize by copying to new memory in amortized O(1)). Cache-friendly due to spatial locality.\n\n- Linked List: Non-contiguous memory allocation where nodes store data and a pointer/reference to the next node. Sequential access only (lookup is O(N)). Insertion and deletion at a known pointer position is O(1) with no shifting required. Requires extra memory for pointers and has poorer cache locality.",
        "key_points": ["Array: O(1) random access, contiguous memory, high cache locality", "Linked List: O(N) access, O(1) insertion at pointer, extra pointer memory", "Array has fixed size or amortized resize; Linked list grows dynamically"],
        "common_mistakes": ["Saying inserting into a linked list is always O(1) (finding the insertion spot still takes O(N) traversal)"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "How does a Hash Map work internally and how are collisions handled?",
        "answer": "A Hash Map stores key-value pairs. It uses a hash function to convert a key into an integer hash code, which is then mapped to an array bucket index using modulo arithmetic (`hash % bucket_count`).\n\nCollision Resolution Techniques:\n1. Separate Chaining: Each bucket holds a linked list (or balanced binary tree, like Red-Black tree in Java 8+) of all entries that hash to the same bucket index.\n2. Open Addressing: All elements reside directly in the bucket array. On collision, alternative buckets are probed:\n   - Linear Probing: index + 1, index + 2...\n   - Quadratic Probing: index + 1^2, index + 2^2...\n   - Double Hashing: step size determined by a second hash function.\n\nAverage time complexity for search/insert/delete is O(1); worst-case degraded to O(N) if many keys collide.",
        "key_points": ["Hash function maps key to bucket index", "Separate Chaining uses linked lists/trees per bucket", "Open Addressing searches for empty slots via probing", "Average O(1), worst case O(N)"],
        "common_mistakes": ["Claiming hash maps are always O(1) regardless of hash function quality"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "Compare QuickSort and MergeSort. When would you choose one over the other?",
        "answer": "- MergeSort:\n  - Divide-and-conquer algorithm that recursively splits the array into halves and merges them.\n  - Guaranteed O(N log N) time complexity in Best, Average, and Worst cases.\n  - Stable sort (preserves relative order of duplicate elements).\n  - Requires O(N) auxiliary space for arrays.\n\n- QuickSort:\n  - Partitions array around a pivot element.\n  - Average time complexity is O(N log N); Worst case is O(N^2) if poor pivots are chosen (e.g. sorted array with first element as pivot).\n  - In-place sort requiring only O(log N) stack space.\n  - Unstable sort.\n\nChoose QuickSort for in-memory array sorting where space and cache performance matter. Choose MergeSort for linked lists or when stability and worst-case guarantees are required.",
        "key_points": ["MergeSort: Always O(N log N), stable, O(N) space", "QuickSort: Average O(N log N), worst O(N^2), in-place, unstable", "QuickSort has smaller constant factors for arrays"],
        "common_mistakes": ["Forgetting that standard QuickSort has an O(N^2) worst case"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Easy",
        "question": "What is the difference between a Stack and a Queue?",
        "answer": "- Stack: Follows the LIFO (Last In, First Out) principle. The most recently added element is removed first. Operations: `push()` adds to top, `pop()` removes from top, `peek()` inspects top. Used in function call stacks, undo/redo mechanisms, and balanced parenthesis evaluation.\n\n- Queue: Follows the FIFO (First In, First Out) principle. Elements are added at the rear (enqueue) and removed from the front (dequeue). Used in CPU process scheduling queues, print spoolers, and Breadth-First Search (BFS) graph traversals.",
        "key_points": ["Stack: LIFO (Last In First Out)", "Queue: FIFO (First In First Out)", "Stack used in DFS/Recursion; Queue used in BFS/Task pipelines"],
        "common_mistakes": ["Confusing queue operations with deque (double-ended queue)"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "What is a Binary Search Tree (BST) and what is its worst-case time complexity?",
        "answer": "A Binary Search Tree (BST) is a binary tree where each node satisfies the BST property: all values in its left subtree are strictly smaller than the node's value, and all values in its right subtree are strictly greater than the node's value.\n\nComplexity:\n- Balanced BST (AVL, Red-Black): Search, insertion, and deletion take O(log N) time.\n- Unbalanced / Skewed BST: If elements are inserted in sorted order, the tree degenerates into a linear linked list of height N, causing search, insertion, and deletion to degrade to O(N) worst-case time complexity.",
        "key_points": ["Left child < Parent < Right child", "In-order traversal of BST yields sorted values", "Average O(log N), worst case O(N) when skewed", "Self-balancing trees (AVL/Red-Black) prevent degradation"],
        "common_mistakes": ["Assuming a plain BST always guarantees O(log N) operations"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Medium",
        "question": "Explain the difference between BFS (Breadth-First Search) and DFS (Depth-First Search).",
        "answer": "- BFS (Breadth-First Search):\n  - Explores nodes level by level, visiting all immediate neighbors before moving deeper.\n  - Implemented iteratively using a Queue.\n  - Finds the shortest path on unweighted graphs.\n  - Memory complexity: O(V) to store nodes at the current level.\n\n- DFS (Depth-First Search):\n  - Explores as far along each branch as possible before backtracking.\n  - Implemented recursively or iteratively using a Stack.\n  - Used for topological sorting, cycle detection, and maze solving.\n  - Memory complexity: O(H) where H is the maximum path depth / recursion height.",
        "key_points": ["BFS uses Queue; explores level by level; optimal for unweighted shortest path", "DFS uses Stack/recursion; explores deep branch first; ideal for cycle detection", "Time complexity for both on adjacency list: O(V + E)"],
        "common_mistakes": ["Using DFS to find shortest path on an unweighted graph"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Hard",
        "question": "What is Dynamic Programming (DP) and how does it differ from Divide and Conquer?",
        "answer": "Dynamic Programming is an algorithmic technique for solving complex optimization problems by breaking them down into simpler subproblems, solving each subproblem once, and storing their solutions to avoid redundant recalculation.\n\nTwo essential prerequisites for DP:\n1. Overlapping Subproblems: The same subproblems are solved repeatedly (unlike MergeSort/Binary Search where subproblems are independent and non-overlapping).\n2. Optimal Substructure: An optimal solution to the problem contains within it optimal solutions to subproblems.\n\nApproaches:\n- Top-Down (Memoization): Recursive approach storing results in a cache/dictionary.\n- Bottom-Up (Tabulation): Iterative approach building up solutions in a DP table.",
        "key_points": ["Requires Overlapping Subproblems and Optimal Substructure", "Divide & Conquer subproblems are independent; DP subproblems overlap", "Top-Down (Memoization) vs Bottom-Up (Tabulation)"],
        "common_mistakes": ["Calling MergeSort dynamic programming (MergeSort subproblems do NOT overlap)"]
    },
    {
        "category": "Technical",
        "topic": "Data Structures",
        "difficulty": "Easy",
        "question": "What is Big-O notation and why is it important?",
        "answer": "Big-O notation is a mathematical notation that describes the limiting behavior and upper bound of an algorithm's runtime or space usage as the input size (N) grows towards infinity.\n\nIt allows engineers to analyze and compare algorithmic scalability independently of specific machine hardware, processor speed, or programming language compiler optimizations.\n\nCommon complexities from best to worst: O(1) Constant < O(log N) Logarithmic < O(N) Linear < O(N log N) Linearithmic < O(N^2) Quadratic < O(2^N) Exponential < O(N!) Factorial.",
        "key_points": ["Describes worst-case upper bound asymptotic growth", "Hardware-independent measurement of scalability", "Drop constants and non-dominant terms (e.g. 5N^2 + 10N -> O(N^2))"],
        "common_mistakes": ["Including constants or lower-order terms like O(2N + 3)"]
    },

    # --- TECHNICAL: PYTHON & WEB (41-48) ---
    {
        "category": "Technical",
        "topic": "Python",
        "difficulty": "Medium",
        "question": "What is the GIL (Global Interpreter Lock) in Python and how does it affect multithreading?",
        "answer": "The Global Interpreter Lock (GIL) is a mutex in CPython (the standard Python interpreter) that allows only one native thread to execute Python bytecode at a time, even on multi-core processors. It was designed to ensure thread-safe memory management for CPython's reference counting garbage collector.\n\nImpact:\n- CPU-bound tasks (e.g., heavy mathematical computations, image processing) do NOT achieve true multi-core parallelism using Python's `threading` module.\n- I/O-bound tasks (e.g., network requests, database queries, file reading) benefit from `threading` or `asyncio` because the thread releases the GIL while waiting for I/O operations.\n- For CPU parallelism, developers use the `multiprocessing` module (which spawns separate OS processes with independent Python interpreters and memory spaces).",
        "key_points": ["GIL restricts CPython bytecode execution to one thread at a time", "Protects reference counting memory management", "CPU-bound tasks require `multiprocessing`; I/O-bound tasks run fine with `threading`"],
        "common_mistakes": ["Claiming Python threads are completely useless (they are highly effective for I/O-bound operations)"]
    },
    {
        "category": "Technical",
        "topic": "Python",
        "difficulty": "Easy",
        "question": "What is the difference between mutable and immutable types in Python?",
        "answer": "- Immutable Types: Objects whose state or contents cannot be changed after creation. Any modification creates a new object in memory with a new `id()`. Examples: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`.\n- Mutable Types: Objects whose contents can be modified in-place without changing their memory address. Examples: `list`, `dict`, `set`, custom classes.\n\nSignificance: Only immutable (hashable) objects can be used as keys in Python dictionaries or elements in sets. Passing a mutable object as a default function argument (`def func(x=[])`) can cause unexpected shared state bugs.",
        "key_points": ["Immutable: Cannot change in-place (`int`, `str`, `tuple`)", "Mutable: In-place modifications allowed (`list`, `dict`, `set`)", "Only immutable/hashable types can be dictionary keys"],
        "common_mistakes": ["Thinking a tuple containing a list cannot have its inner list modified (the tuple reference is immutable, but the contained list remains mutable)"]
    },
    {
        "category": "Technical",
        "topic": "Python",
        "difficulty": "Medium",
        "question": "What is a Python Generator and how does the `yield` keyword work?",
        "answer": "A Generator is a special type of iterator that generates values on-the-fly one at a time using the `yield` keyword, rather than computing and storing the entire dataset in memory at once (lazy evaluation).\n\nWhen a function containing `yield` is called, it returns a generator object without executing the function body immediately. Each time `next()` is called on the generator, execution proceeds until it hits a `yield` statement, which produces the value and pauses execution state (local variables and instruction pointer are saved). Subsequent `next()` calls resume right after the `yield`.\n\nAdvantage: Extreme memory efficiency when processing large files, infinite streams, or big datasets.",
        "key_points": ["`yield` produces a value and pauses function execution state", "Lazy evaluation saves memory by computing elements on demand", "Implements Python iterator protocol (`__iter__`, `__next__`)"],
        "common_mistakes": ["Confusing `return` (terminates function) with `yield` (pauses and preserves state)"]
    },
    {
        "category": "Technical",
        "topic": "Python",
        "difficulty": "Easy",
        "question": "What is the difference between `==` and `is` in Python?",
        "answer": "- `==` (Equality Operator): Compares the values or contents of two objects by calling their `__eq__()` method. If both objects hold equivalent data, it evaluates to `True`.\n- `is` (Identity Operator): Checks whether two variables refer to the exact same memory address (i.e., `id(a) == id(b)`).\n\nExample:\n`a = [1, 2, 3]`\n`b = [1, 2, 3]`\n`a == b` is `True` (same values), but `a is b` is `False` (different heap allocations).\n`is` is standard for checking against singletons like `None` (`x is None`).",
        "key_points": ["`==` compares value / content equality", "`is` compares memory identity / object reference", "Always use `is None` instead of `== None`"],
        "common_mistakes": ["Using `is` for integer comparisons (Python intern pools small integers -5 to 256, which can create misleading `True` results)"]
    },
    {
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Easy",
        "question": "What is a RESTful API? What are the standard HTTP methods used?",
        "answer": "A REST (Representational State Transfer) API is an architectural style for network communications based on stateless, client-server interactions and standardized resource-oriented endpoints.\n\nCore Constraints:\n- Stateless: Each client request must contain all information required to complete it; server stores no client session context.\n- Resource-oriented URLs: Entities represented as nouns (e.g., `/api/students/12`).\n\nHTTP Methods:\n- GET: Retrieve a resource (Idempotent and Safe).\n- POST: Create a new resource (Not idempotent).\n- PUT: Replace an existing resource completely (Idempotent).\n- PATCH: Partially update an existing resource.\n- DELETE: Remove a resource (Idempotent).",
        "key_points": ["Stateless client-server architecture", "Resource URLs as nouns, not verbs", "GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove)"],
        "common_mistakes": ["Using verbs in endpoint paths like `/api/getStudent` instead of `GET /api/students`"]
    },
    {
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Medium",
        "question": "What is CSRF (Cross-Site Request Forgery) and how is it prevented?",
        "answer": "CSRF is a web security vulnerability where an attacker tricks an authenticated user's browser into executing unwanted, state-changing actions on a trusted web application where the user has an active session cookie.\n\nBecause the browser automatically sends session cookies with cross-site requests, the vulnerable server cannot tell whether the user intentionally submitted the form or was tricked by a malicious third-party site.\n\nDefense:\n1. Anti-CSRF Synchronizer Tokens: Server generates a unique, cryptographically random token tied to the user's session. Forms must include this token in hidden inputs or request headers (`X-CSRFToken`). The server validates the token on POST/PUT requests.\n2. SameSite Cookie Attribute: Setting `SameSite=Strict` or `SameSite=Lax` prevents cookies from being sent on cross-origin requests.",
        "key_points": ["Tricks browser into sending ambient auth cookies to perform unauthorized actions", "Prevented using Synchronizer CSRF tokens verified on mutating requests", "Prevented using `SameSite=Lax` or `Strict` cookie attributes"],
        "common_mistakes": ["Thinking CSRF and XSS are the same (XSS executes malicious JavaScript inside the site; CSRF forces unwanted HTTP requests from an external origin)"]
    },
    {
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Medium",
        "question": "What is SQL Injection (SQLi) and how is it prevented?",
        "answer": "SQL Injection occurs when untrusted user input is directly concatenated into a dynamic SQL query string, allowing an attacker to manipulate the query structure, bypass authentication, access unauthorized data, or delete tables.\n\nExample vulnerable query:\n`SELECT * FROM users WHERE email = '\" + user_input + \"'`\nInput `' OR '1'='1` dumps all user records.\n\nPrevention:\n1. Parameterized Queries / Prepared Statements: Separates code from data. The database compiles the query template first, treating user input purely as literal parameters.\n2. Use an ORM (e.g. SQLAlchemy, Hibernate): ORMs parameterize queries automatically under the hood.\n3. Input validation and principle of least privilege for database credentials.",
        "key_points": ["Direct string concatenation into SQL allows attackers to execute arbitrary database commands", "Prevented using Parameterized Queries / Prepared Statements", "ORMs like SQLAlchemy parameterize queries automatically"],
        "common_mistakes": ["Relying on blacklist string sanitization (attackers can easily bypass regex filters)"]
    },
    {
        "category": "Technical",
        "topic": "Software Engineering",
        "difficulty": "Easy",
        "question": "Explain Git branching and the difference between `git merge` and `git rebase`.",
        "answer": "Git branches represent lightweight movable pointers to commits, enabling parallel development of features, fixes, and experiments without disrupting the main branch.\n\n- `git merge`:\n  - Combines the histories of two branches by creating a 3-way merge commit.\n  - Non-destructive: preserves the exact chronological history and commit timestamps of the feature branch.\n  - Disadvantage: Can clutter git log history with many merge commits.\n\n- `git rebase`:\n  - Replays the commits from the feature branch on top of the latest commit of the base branch.\n  - Produces a perfectly linear, clean project history.\n  - Disadvantage: Rewrites commit SHA hashes; should never be used on shared public branches.",
        "key_points": ["Branches are pointers to commit objects", "`git merge` creates a merge commit preserving exact history", "`git rebase` rewrites commits for a clean linear history", "Golden Rule: Never rebase a public shared branch"],
        "common_mistakes": ["Rebasing public `main` branch and causing conflict chaos for collaborators"]
    },

    # --- HR & BEHAVIORAL (49-60) ---
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Easy",
        "question": "Tell me about yourself.",
        "answer": "Use the Present-Past-Future framework:\n'I am currently a final-year Computer Science student passionate about building scalable web applications and distributed systems. Recently, I led development on a placement preparation platform built with Python, Flask, and SQLite, where I designed real-time mock test engines and automated progress analytics. In the past, I built a strong foundation in core algorithms and database systems through competitive programming and academic projects. Moving forward, I am looking to join a high-performing engineering team where I can contribute to mission-critical software and continue expanding my engineering craft.'",
        "key_points": ["Present: Current role, education, and primary technical passions", "Past: Concrete project accomplishments and foundation built", "Future: Why this company matches your career aspirations", "Keep response between 90-120 seconds"],
        "common_mistakes": ["Reciting your high school history or reading your resume verbatim"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "What are your greatest strengths and greatest weaknesses?",
        "answer": "Strengths: Pick 2 job-relevant skills backed by evidence.\n'One of my core strengths is structured problem-solving under ambiguity. When building our hackathon project, I broke down complex requirements into modular components, enabling our team to deliver ahead of deadline. Another strength is continuous learning—I proactively learned isolated code sandboxing to ensure safe evaluation of student submissions.'\n\nWeaknesses: Pick a genuine area of improvement, and explain active steps you take to address it.\n'Early on, I struggled with perfectionism and over-engineering features before having a working baseline. I realized this slowed down iteration velocity. To improve, I adopted the MVP approach: I now define strict timeboxes for foundational prototypes, gather feedback early, and iterate progressively.'",
        "key_points": ["Pair strengths with tangible project proof", "Weakness must be genuine, non-critical, and accompanied by active remediation", "Never use humble-brags like 'I work too hard'"],
        "common_mistakes": ["Saying 'I don't have any weaknesses' or claiming a fatal flaw like 'I miss deadlines'"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "Why should we hire you over other candidates?",
        "answer": "'You should hire me because I combine solid technical fundamentals with a proven ability to deliver production-quality working software. Beyond academics, I have demonstrated ownership by building end-to-end full-stack applications with real authentication, database modeling, and unit testing. I am adaptable, take feedback constructively, and communicate clearly across teams. I am not just looking for a job; I am excited about your specific technological domain and ready to add immediate value from day one.'",
        "key_points": ["Focus on value delivered, execution track record, and technical curiosity", "Highlight soft skills: ownership, communication, adaptability", "Align with company culture and engineering challenges"],
        "common_mistakes": ["Disparaging other candidates or sounding entitled"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "Describe a challenging technical project you worked on and how you overcame obstacles. (STAR Method)",
        "answer": "Situation: In our college hackathon, we built an EdTech platform requiring a coding sandbox to evaluate Python solutions.\nTask: I was responsible for designing the execution pipeline without compromising host server security or crashing the Flask process.\nAction: Direct subprocess execution was risky, so I implemented AST (Abstract Syntax Tree) static analysis to detect and ban dangerous modules (`os`, `sys`, `socket`) before execution. Then, I wrapped code runs in isolated subprocesses with 3-second hard timeouts and CPU limits.\nResult: The feature ran smoothly during live testing, prevented denial-of-service attempts, and our team finished with zero downtime.",
        "key_points": ["Situation: Context and initial challenge", "Task: Your specific role and objective", "Action: Concrete technical decisions and leadership taken", "Result: Quantifiable outcome and impact"],
        "common_mistakes": ["Focusing only on 'we' instead of clarifying your specific individual contribution"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "Explain a situation where you failed, and what you learned from the experience.",
        "answer": "Situation: During my third year, I led a team building a course recommendation portal for our department symposium.\nTask: We committed to delivering a complex machine learning recommendation engine alongside a web UI within three weeks.\nAction & Failure: I underestimated the data collection and cleaning overhead. Two days before the showcase, the recommendation engine was inaccurate and unstable. We had to roll back to a basic rule-based filter at the last minute.\nLesson: I learned the critical importance of risk assessment, realistic scoping, and building a working baseline before introducing complex models. In subsequent projects, I prioritize vertical slicing and milestone risk buffers.",
        "key_points": ["Admit a real failure with maturity and accountability", "Avoid blaming teammates, circumstances, or external factors", "Emphasize the permanent positive lessons learned and behavioral changes made"],
        "common_mistakes": ["Blaming external teammates or saying you have never failed"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "How do you handle conflict or disagreements with a team member?",
        "answer": "'I view technical disagreements as opportunities to find better solutions rather than personal confrontations. When a disagreement occurs, my approach is:\n1. Separate the person from the problem and actively listen to understand their perspective and underlying concerns.\n2. Re-anchor the discussion on shared project goals and user requirements.\n3. Rely on data and benchmarks rather than subjective opinions—for instance, writing a quick proof-of-concept or measuring latency when debating architecture.\n4. If consensus cannot be reached within a reasonable timeframe, disagree and commit to the chosen path to prevent project paralysis.'",
        "key_points": ["Active listening and empathy", "Objectivity: testing trade-offs with data/prototypes", "Disagree and commit philosophy"],
        "common_mistakes": ["Claiming you avoid conflict at all costs or insisting your way is always right"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Easy",
        "question": "Where do you see yourself in 3 to 5 years?",
        "answer": "'In 3 to 5 years, I see myself as a seasoned software engineer who has mastered the technical architecture and business domain of our products. I want to have led the design and implementation of major system components, mentored junior engineers, and contributed to key architectural decisions. Whether I grow toward technical leadership as a Staff Engineer or an engineering manager, my goal is to be a trusted subject matter expert who consistently delivers high-impact software.'",
        "key_points": ["Demonstrate ambition balanced with commitment to engineering mastery", "Highlight technical depth, system ownership, and mentoring others", "Show alignment with long-term company growth"],
        "common_mistakes": ["Saying 'I want your job' or 'I want to start my own startup in 2 years'"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "How do you prioritize tasks when faced with multiple urgent deadlines?",
        "answer": "'I use an Eisenhower Matrix approach combined with agile sprint priorities:\n1. Triage: I categorize tasks by urgency and true impact on project deliverables.\n2. Clarify Expectations: If two critical deadlines collide, I proactively communicate with stakeholders to understand true priorities and explore whether non-essential scope can be deferred.\n3. Focus Blocks: I eliminate distractions and use focused timeboxing to knock out high-impact tasks sequentially rather than context-switching frantically.\n4. Status Updates: I keep teammates informed of progress to prevent unexpected surprises.'",
        "key_points": ["Systematic framework (Impact vs Urgency)", "Proactive stakeholder communication", "Eliminate multitasking; focus on sequential execution"],
        "common_mistakes": ["Saying you simply work 24 hours without communicating trade-offs"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Easy",
        "question": "Why do you want to work for our company?",
        "answer": "'I admire your company for two main reasons:\nFirst, your engineering culture and the scale at which your systems operate. Building software that impacts millions of daily active users presents fascinating distributed systems and performance challenges that excite me as an engineer.\nSecond, your commitment to innovation and continuous learning. Speaking with current engineers, I learned that you encourage experimentation, strong code review standards, and technical ownership. That is exactly the environment where I want to build my career.'",
        "key_points": ["Demonstrate that you researched the specific company's product, tech, and culture", "Connect their mission to your personal career motivations", "Mention specific engineering scale, products, or values"],
        "common_mistakes": ["Giving a generic response that could apply to any generic company"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Easy",
        "question": "Do you have any questions for us?",
        "answer": "Always ask thoughtful, high-signal questions at the end of an interview:\n1. 'What does a typical day look like for a junior engineer joining this team?'\n2. 'What are the biggest technical or architectural challenges the team is currently tackling?'\n3. 'How does the team approach code reviews, continuous integration, and tech debt management?'\n4. 'What qualities distinguish someone who truly excels in this role during their first 90 days?'",
        "key_points": ["Never say 'No, I don't have any questions'", "Ask about team engineering practices, challenges, and success metrics", "Demonstrates enthusiasm and professional curiosity"],
        "common_mistakes": ["Asking only about salary, vacation days, or company cafeteria during a first-round technical interview"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "Describe a time when you had to learn a completely new technology under tight deadlines.",
        "answer": "'During a team hackathon, our project required implementing real-time progress charts and interactive canvas components, but none of us had prior experience with Chart.js. I took ownership of the module, studied the official documentation and API examples over one evening, built a minimal sandbox prototype, and by morning had integrated dynamic line charts and responsive bar graphs directly connected to our backend JSON endpoints. We shipped the complete analytics dashboard on schedule.'",
        "key_points": ["Initiative and resourcefulness", "Systematic learning strategy (documentation + prototyping)", "Direct positive impact on project delivery"],
        "common_mistakes": ["Claiming you learned an entire complex ecosystem in 1 hour without explaining how"]
    },
    {
        "category": "HR and Behavioral",
        "topic": "Behavioral",
        "difficulty": "Medium",
        "question": "How do you handle critical feedback or code review rejections?",
        "answer": "'I view code reviews and constructive criticism as one of the fastest avenues to grow as an engineer. Early on, receiving critical feedback felt intimidating, but I learned that critique is directed at the code, not at me personally. When a reviewer requests changes, I review their comments carefully, ask clarifying questions to understand their reasoning, and implement the necessary refactoring. If I have an alternate perspective, I discuss it respectfully with benchmarks or documentation.'",
        "key_points": ["Ego-free mindset: feedback improves code quality", "Curiosity over defensiveness", "Appreciation for rigorous code review standards"],
        "common_mistakes": ["Expressing resentment towards reviewers or claiming your code never receives review comments"]
    }
]
