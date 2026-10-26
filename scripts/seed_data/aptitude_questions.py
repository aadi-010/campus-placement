"""
Aptitude questions seed data with 100 mathematically verified original questions
across Quantitative Aptitude, Logical Reasoning, and Verbal Ability
"""

APTITUDE_QUESTIONS = [
    # =========================================================================
    # QUANTITATIVE APTITUDE (1 - 45)
    # =========================================================================
    # 1. Percentages (1-5)
    {
        "category": "Quantitative Aptitude", "topic": "Percentages", "difficulty": "Easy",
        "question": "If the price of sugar increases by 25%, by what percentage must a household reduce its consumption so that total expenditure remains unchanged?",
        "options": ["15%", "20%", "25%", "30%"],
        "correct_option": 1,
        "explanation": "Let initial price = 100 and initial consumption = 100. Initial expenditure = 10,000. New price = 125. Required consumption = 10,000 / 125 = 80. Reduction = (100 - 80) = 20%.",
        "shortcut": "Reduction % = [r / (100 + r)] * 100. Here, [25 / 125] * 100 = 20%."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Percentages", "difficulty": "Medium",
        "question": "A student scored 32% marks in an exam and failed by 16 marks. Another student scored 44% and got 20 marks more than the passing marks. What are the maximum marks of the exam?",
        "options": ["250", "300", "350", "400"],
        "correct_option": 1,
        "explanation": "Difference in percentage = 44% - 32% = 12%. Difference in marks = 20 - (-16) = 36 marks. If 12% = 36, then 1% = 3 marks. Hence, Maximum marks = 100% = 300.",
        "shortcut": "Maximum marks = (Marks difference / % difference) * 100 = (36 / 12) * 100 = 300."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Percentages", "difficulty": "Easy",
        "question": "Two numbers are 20% and 50% more than a third number respectively. What is the ratio of the two numbers?",
        "options": ["2 : 5", "3 : 5", "4 : 5", "6 : 7"],
        "correct_option": 2,
        "explanation": "Let third number = 100. First number = 120, Second number = 150. Ratio = 120 : 150 = 4 : 5.",
        "shortcut": "Ratio = (100 + 20) : (100 + 50) = 120 : 150 = 4 : 5."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Percentages", "difficulty": "Medium",
        "question": "The population of a town increases by 10% in the first year and decreases by 10% in the second year. If the initial population was 50,000, what is the population at the end of two years?",
        "options": ["49,000", "49,500", "50,000", "50,500"],
        "correct_option": 1,
        "explanation": "After 1st year: 50,000 * 1.10 = 55,000. After 2nd year: 55,000 * 0.90 = 49,500. Net change is a 1% loss (10^2 / 100 = 1%). 50,000 - 500 = 49,500.",
        "shortcut": "When a value increases and decreases by same % r, net change is always a decrease of (r^2 / 100)%. Here 1% decrease: 50,000 * 0.99 = 49,500."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Percentages", "difficulty": "Hard",
        "question": "Fresh fruit contains 68% water and dry fruit contains 20% water. How much dry fruit can be obtained from 100 kg of fresh fruit?",
        "options": ["32 kg", "40 kg", "48 kg", "52 kg"],
        "correct_option": 1,
        "explanation": "The quantity of fruit pulp remains constant. Pulp in 100 kg fresh fruit = (100 - 68)% of 100 = 32 kg. In dry fruit, pulp is (100 - 20)% = 80%. Let dry fruit weight = W. 80% of W = 32 kg => W = 32 / 0.8 = 40 kg.",
        "shortcut": "Pulp weight is invariant: 32% * 100 = 80% * W => W = 40 kg."
    },

    # 2. Profit and Loss (6-10)
    {
        "category": "Quantitative Aptitude", "topic": "Profit and Loss", "difficulty": "Easy",
        "question": "A merchant sells an article for $840 and incurs a loss of 20%. At what price should he sell it to gain 15%?",
        "options": ["$1,050", "$1,150", "$1,200", "$1,207.50"],
        "correct_option": 3,
        "explanation": "Selling price = 80% of Cost Price (CP) = $840. CP = 840 / 0.80 = $1,050. To gain 15%, New SP = 1.15 * 1050 = $1,207.50.",
        "shortcut": "Target SP = 840 * (115 / 80) = 840 * 1.4375 = $1,207.50."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Profit and Loss", "difficulty": "Medium",
        "question": "A dishonest shopkeeper professes to sell his goods at cost price but uses a false weight of 950 grams for 1 kg. What is his actual profit percentage?",
        "options": ["5%", "5.26%", "5.55%", "6.25%"],
        "correct_option": 1,
        "explanation": "Profit = Error / (True value - Error) * 100. Here error = 1000 - 950 = 50 grams. Profit % = (50 / 950) * 100 = 100 / 19 ≈ 5.26%.",
        "shortcut": "Profit % = (Gain in grams / Actual weight given) * 100 = (50 / 950) * 100 = 5.26%."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Profit and Loss", "difficulty": "Easy",
        "question": "If the cost price of 15 articles is equal to the selling price of 12 articles, what is the profit percentage?",
        "options": ["20%", "25%", "30%", "33.33%"],
        "correct_option": 1,
        "explanation": "15 * CP = 12 * SP => SP / CP = 15 / 12 = 5 / 4. Profit % = [(5 - 4) / 4] * 100 = 25%.",
        "shortcut": "Profit % = [(Goods bought - Goods sold) / Goods sold] * 100 = [(15 - 12) / 12] * 100 = 25%."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Profit and Loss", "difficulty": "Medium",
        "question": "A shopkeeper allows two successive discounts of 20% and 10% on an item. If marked price is $500, what is the selling price?",
        "options": ["$350", "$360", "$375", "$380"],
        "correct_option": 1,
        "explanation": "After 20% discount: 500 * 0.80 = 400. After additional 10% discount: 400 * 0.90 = $360.",
        "shortcut": "Net multiplier = 0.80 * 0.90 = 0.72. SP = 500 * 0.72 = $360."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Profit and Loss", "difficulty": "Hard",
        "question": "A trader sold two bicycles for $2,400 each. On one he made a profit of 20% and on the other he lost 20%. What was his net profit or loss overall?",
        "options": ["No profit, no loss", "Loss of 4%", "Profit of 4%", "Loss of 2%"],
        "correct_option": 1,
        "explanation": "When two items are sold at the same selling price, one at a gain of x% and other at a loss of x%, there is always a net loss of (x / 10)^2 %. Here, (20 / 10)^2 = 4% loss.",
        "shortcut": "Net Loss % = (common gain or loss % / 10)^2 = (20/10)^2 = 4% loss."
    },

    # 3. Time and Work (11-15)
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Easy",
        "question": "A can finish a piece of work in 12 days and B can finish it in 24 days. Working together, in how many days will they complete the work?",
        "options": ["6 days", "8 days", "10 days", "16 days"],
        "correct_option": 1,
        "explanation": "A's 1-day work = 1/12, B's 1-day work = 1/24. Combined 1-day work = 1/12 + 1/24 = 3/24 = 1/8. Total days = 8 days.",
        "shortcut": "Total days = (A * B) / (A + B) = (12 * 24) / (12 + 24) = 288 / 36 = 8 days."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Medium",
        "question": "A and B can complete a work in 15 days and 10 days respectively. They started the work together, but B left after 2 days. In how many days will A finish the remaining work?",
        "options": ["8 days", "10 days", "12 days", "14 days"],
        "correct_option": 1,
        "explanation": "Take total work = LCM(15, 10) = 30 units. Efficiency of A = 2 units/day, B = 3 units/day. In first 2 days, together they do 2 * (2 + 3) = 10 units. Remaining work = 30 - 10 = 20 units. Time taken by A alone = 20 / 2 = 10 days.",
        "shortcut": "Total units method: 30 units total. (A+B) 2 days = 10 units. Remainder 20 units / A's rate (2) = 10 days."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Medium",
        "question": "12 men or 18 women can do a harvest in 14 days. In how many days can 8 men and 16 women do the same work?",
        "options": ["6 days", "8 days", "9 days", "10 days"],
        "correct_option": 2,
        "explanation": "12 men = 18 women => 1 man = 1.5 women. 8 men = 12 women. Total workers = 12 women + 16 women = 28 women. 18 women * 14 days = 28 women * D days => D = (18 * 14) / 28 = 9 days.",
        "shortcut": "Convert all workers to women: 8 men = 12 women. Group = 28 women. Days = (18 * 14) / 28 = 9 days."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Hard",
        "question": "A is twice as efficient as B and takes 30 days less than B to finish a task. How many days will they take working together?",
        "options": ["15 days", "18 days", "20 days", "25 days"],
        "correct_option": 2,
        "explanation": "Ratio of efficiency A:B = 2:1 => Ratio of time taken A:B = 1:2. Difference in time ratio units = 1 unit = 30 days. So A takes 30 days and B takes 60 days. Together: (30 * 60) / (30 + 60) = 1800 / 90 = 20 days.",
        "shortcut": "Together days = (30 * 60) / (30 + 60) = 20 days."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Medium",
        "question": "Pipe A can fill a tank in 6 hours and Pipe B can empty it in 8 hours. If both pipes are opened simultaneously, in how many hours will the tank be full?",
        "options": ["14 hours", "20 hours", "24 hours", "28 hours"],
        "correct_option": 2,
        "explanation": "Net filling rate per hour = 1/6 - 1/8 = (4 - 3)/24 = 1/24 tank per hour. Therefore, tank will be filled in 24 hours.",
        "shortcut": "Time = (A * B) / (B - A) = (6 * 8) / (8 - 6) = 48 / 2 = 24 hours."
    },

    # 4. Time, Speed and Distance (16-20)
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Easy",
        "question": "A train 180 meters long is traveling at 72 km/h. How many seconds will it take to pass an electric pole?",
        "options": ["7 seconds", "8 seconds", "9 seconds", "10 seconds"],
        "correct_option": 2,
        "explanation": "Convert speed to m/s: 72 * (5/18) = 20 m/s. Distance to cross pole = length of train = 180 m. Time = Distance / Speed = 180 / 20 = 9 seconds.",
        "shortcut": "km/h to m/s multiply by 5/18: 72 km/h = 20 m/s. 180 / 20 = 9 s."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Medium",
        "question": "A person travels from city A to city B at 60 km/h and returns from B to A at 40 km/h. What is his average speed for the entire round trip?",
        "options": ["48 km/h", "50 km/h", "52 km/h", "54 km/h"],
        "correct_option": 0,
        "explanation": "Average speed for equal distances = Harmonic mean = (2 * x * y) / (x + y). Here, (2 * 60 * 40) / (60 + 40) = 4800 / 100 = 48 km/h.",
        "shortcut": "Avg speed = 2xy / (x + y) = (2 * 60 * 40) / 100 = 48 km/h."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Medium",
        "question": "Two trains 140 m and 160 m long are running in opposite directions on parallel tracks at speeds of 60 km/h and 48 km/h respectively. In how much time will they cross each other completely?",
        "options": ["9 seconds", "10 seconds", "12 seconds", "15 seconds"],
        "correct_option": 1,
        "explanation": "Total distance = 140 + 160 = 300 m. Relative speed in opposite directions = 60 + 48 = 108 km/h. In m/s = 108 * (5/18) = 30 m/s. Time = 300 / 30 = 10 seconds.",
        "shortcut": "Time = (Sum of lengths) / (Relative speed in m/s) = 300 / (108 * 5/18) = 300 / 30 = 10 s."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Hard",
        "question": "Walking at 3/4th of his normal speed, a student reaches college 15 minutes late. What is his normal time to reach college?",
        "options": ["30 mins", "40 mins", "45 mins", "60 mins"],
        "correct_option": 2,
        "explanation": "Speed ratio (new : usual) = 3 : 4 => Time ratio (new : usual) = 4 : 3. Difference in time = 1 unit = 15 minutes. Normal time = 3 units = 3 * 15 = 45 minutes.",
        "shortcut": "Usual time = Late time * (numerator) / (denominator - numerator) = 15 * 3 / (4 - 3) = 45 mins."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Medium",
        "question": "A boat can travel with the speed of 13 km/h in still water. If the speed of the stream is 4 km/h, find the time taken by the boat to go 68 km downstream.",
        "options": ["3 hours", "4 hours", "5 hours", "6 hours"],
        "correct_option": 1,
        "explanation": "Downstream speed = speed of boat + stream speed = 13 + 4 = 17 km/h. Time taken = Distance / Downstream speed = 68 / 17 = 4 hours.",
        "shortcut": "Downstream speed = 13 + 4 = 17 km/h. 68 / 17 = 4 hours."
    },

    # 5. Ratios and Proportions (21-25)
    {
        "category": "Quantitative Aptitude", "topic": "Ratios and Proportions", "difficulty": "Easy",
        "question": "If A : B = 2 : 3 and B : C = 4 : 5, find the ratio A : B : C.",
        "options": ["8 : 12 : 15", "6 : 8 : 10", "8 : 10 : 15", "2 : 4 : 5"],
        "correct_option": 0,
        "explanation": "Multiply A:B by 4 -> 8:12. Multiply B:C by 3 -> 12:15. Hence A : B : C = 8 : 12 : 15.",
        "shortcut": "A = 2*4=8, B = 3*4=12, C = 3*5=15. Ratio = 8 : 12 : 15."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Ratios and Proportions", "difficulty": "Medium",
        "question": "A bag contains 50p, 25p, and 10p coins in the ratio 5 : 9 : 4, amounting to $206 in total. What is the number of 50p coins?",
        "options": ["180", "200", "220", "240"],
        "correct_option": 1,
        "explanation": "Value per unit ratio = (5 * 0.50) + (9 * 0.25) + (4 * 0.10) = 2.50 + 2.25 + 0.40 = $5.15. Number of ratio units = 206 / 5.15 = 40. Number of 50p coins = 5 * 40 = 200.",
        "shortcut": "Unit value = 5.15. Units = 206 / 5.15 = 40. 50p coins = 5 * 40 = 200."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Ratios and Proportions", "difficulty": "Medium",
        "question": "The ratio of the ages of two persons is 3 : 5. After 5 years, the ratio of their ages will be 2 : 3. What is the present age of the younger person?",
        "options": ["10 years", "12 years", "15 years", "20 years"],
        "correct_option": 2,
        "explanation": "Let ages be 3x and 5x. (3x + 5) / (5x + 5) = 2/3. Cross-multiplying: 3(3x + 5) = 2(5x + 5) => 9x + 15 = 10x + 10 => x = 5. Present age of younger person = 3 * 5 = 15 years.",
        "shortcut": "9x + 15 = 10x + 10 => x = 5. Younger age = 3 * 5 = 15 years."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Ratios and Proportions", "difficulty": "Easy",
        "question": "What is the fourth proportional to 4, 9, and 12?",
        "options": ["18", "21", "24", "27"],
        "correct_option": 3,
        "explanation": "In proportion a : b :: c : d, product of extremes = product of means (a * d = b * c). Here, 4 * d = 9 * 12 = 108 => d = 108 / 4 = 27.",
        "shortcut": "d = (b * c) / a = (9 * 12) / 4 = 27."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Ratios and Proportions", "difficulty": "Hard",
        "question": "A mixture of 60 liters of milk and water contains milk and water in the ratio 2 : 1. How much water must be added to make the ratio 1 : 2?",
        "options": ["40 liters", "50 liters", "60 liters", "80 liters"],
        "correct_option": 2,
        "explanation": "Initial milk = (2/3) * 60 = 40 L, water = 20 L. Water is added, so milk remains 40 L. In new ratio 1 : 2, 1 part milk = 40 L, so 2 parts water = 80 L. Water to add = 80 - 20 = 60 liters.",
        "shortcut": "Milk stays 40L. New water must be 40 * 2 = 80L. 80 - 20 = 60L to add."
    },

    # 6. Averages & Number Systems (26-33)
    {
        "category": "Quantitative Aptitude", "topic": "Averages", "difficulty": "Easy",
        "question": "The average of five consecutive even numbers is 28. What is the smallest of these numbers?",
        "options": ["22", "24", "26", "28"],
        "correct_option": 1,
        "explanation": "In an arithmetic progression with an odd number of terms, the middle term is the average. Middle term (3rd term) = 28. The terms are 24, 26, 28, 30, 32. Smallest = 24.",
        "shortcut": "Middle term = 28. Two terms prior are 26 and 24. Smallest = 24."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Averages", "difficulty": "Medium",
        "question": "The average age of a class of 24 students is 15 years. If the teacher's age is included, the average increases by 1 year. What is the teacher's age?",
        "options": ["35 years", "38 years", "40 years", "42 years"],
        "correct_option": 2,
        "explanation": "Sum of 24 students = 24 * 15 = 360. New average of 25 people = 16. Sum of 25 people = 25 * 16 = 400. Teacher's age = 400 - 360 = 40 years.",
        "shortcut": "Teacher's age = New Average + (Old members * Increase) = 16 + (24 * 1) = 40 years."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Number Systems", "difficulty": "Easy",
        "question": "What is the remainder when (7^19 + 2) is divided by 6?",
        "options": ["1", "2", "3", "5"],
        "correct_option": 2,
        "explanation": "7 mod 6 = 1. Therefore, 7^19 mod 6 = 1^19 = 1. Remainder = (1 + 2) mod 6 = 3.",
        "shortcut": "7 ≡ 1 (mod 6). 1^19 + 2 = 1 + 2 = 3."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Number Systems", "difficulty": "Medium",
        "question": "What is the unit digit of the product (7^95 * 3^58)?",
        "options": ["1", "3", "7", "9"],
        "correct_option": 1,
        "explanation": "Cyclicity of 7 is 4: 95 mod 4 = 3 => unit digit of 7^95 is 7^3 = 343 => 3. Cyclicity of 3 is 4: 58 mod 4 = 2 => unit digit of 3^58 is 3^2 = 9. Product unit digit = 3 * 9 = 27 => 7? Wait, 3 * 9 = 27 (unit digit 7). Wait, option C is 7! Wait: 95 / 4 gives remainder 3 (7^3 unit digit 3). 58 / 4 gives remainder 2 (3^2 unit digit 9). 3 * 9 = 27 -> unit digit 7. Option C is 7.",
        "correct_option": 2,
        "explanation": "Power cyclicity for 7 is [7, 9, 3, 1] (period 4). 95 mod 4 = 3 => unit digit 3. For 3 is [3, 9, 7, 1] (period 4). 58 mod 4 = 2 => unit digit 9. Unit digit of product = (3 * 9) mod 10 = 7.",
        "shortcut": "7^3 gives 3, 3^2 gives 9. 3 * 9 = 27 => unit digit 7."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Number Systems", "difficulty": "Easy",
        "question": "The HCF and LCM of two numbers are 12 and 144 respectively. If one of the numbers is 36, what is the other number?",
        "options": ["24", "48", "60", "72"],
        "correct_option": 1,
        "explanation": "For any two numbers, Product of numbers = HCF * LCM. 36 * B = 12 * 144 => B = (12 * 144) / 36 = 144 / 3 = 48.",
        "shortcut": "Other number = (HCF * LCM) / Given number = (12 * 144) / 36 = 48."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Number Systems", "difficulty": "Hard",
        "question": "How many trailing zeros are there in 100! (100 factorial)?",
        "options": ["20", "22", "24", "26"],
        "correct_option": 2,
        "explanation": "Number of trailing zeros is determined by the power of 5 in 100!: floor(100/5) + floor(100/25) + floor(100/125) = 20 + 4 + 0 = 24 zeros.",
        "shortcut": "Trailing zeros = [100/5] + [100/25] = 20 + 4 = 24."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Averages", "difficulty": "Medium",
        "question": "The average score of a batsman in 19 innings is 45 runs. How many runs must he score in the 20th inning to raise his average to 48?",
        "options": ["95", "100", "105", "108"],
        "correct_option": 2,
        "explanation": "Old total = 19 * 45 = 855. New total = 20 * 48 = 960. Runs needed = 960 - 855 = 105 runs.",
        "shortcut": "Required runs = New Average + [Old innings * Increase] = 48 + [19 * 3] = 48 + 57 = 105."
    },

    # 7. Probability, Permutations & Combinations (34-40)
    {
        "category": "Quantitative Aptitude", "topic": "Probability", "difficulty": "Easy",
        "question": "Two unbiased dice are rolled together. What is the probability of getting a sum of 8?",
        "options": ["5/36", "1/6", "7/36", "1/9"],
        "correct_option": 0,
        "explanation": "Total outcomes = 6 * 6 = 36. Pairs summing to 8: (2,6), (3,5), (4,4), (5,3), (6,2) -> 5 outcomes. Probability = 5/36.",
        "shortcut": "Favorable pairs = 5. Total = 36. Probability = 5/36."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Probability", "difficulty": "Medium",
        "question": "A card is drawn from a well-shuffled pack of 52 playing cards. What is the probability of drawing a face card (Jack, Queen, King) or an Ace?",
        "options": ["3/13", "4/13", "5/13", "16/52"],
        "correct_option": 1,
        "explanation": "Face cards = 12 (3 in each of 4 suits). Aces = 4. Total favorable = 12 + 4 = 16. Probability = 16/52 = 4/13.",
        "shortcut": "4 face cards + aces per suit out of 13 cards per suit = 4/13."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Probability", "difficulty": "Medium",
        "question": "A bag contains 4 red balls, 5 blue balls, and 3 green balls. If two balls are drawn at random without replacement, what is the probability that both are blue?",
        "options": ["5/33", "5/36", "1/6", "2/11"],
        "correct_option": 0,
        "explanation": "Total balls = 4 + 5 + 3 = 12. P(both blue) = (5/12) * (4/11) = 20 / 132 = 5/33.",
        "shortcut": "(5C2) / (12C2) = 10 / 66 = 5/33."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Permutations and Combinations", "difficulty": "Easy",
        "question": "In how many different ways can the letters of the word 'LEADER' be arranged?",
        "options": ["120", "240", "360", "720"],
        "correct_option": 2,
        "explanation": "Word 'LEADER' has 6 letters with 'E' repeating 2 times. Total permutations = 6! / 2! = 720 / 2 = 360.",
        "shortcut": "6! / 2! = 720 / 2 = 360."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Permutations and Combinations", "difficulty": "Medium",
        "question": "A committee of 5 members is to be formed from 6 men and 4 women. In how many ways can the committee be formed if it must contain exactly 3 men and 2 women?",
        "options": ["60", "90", "120", "150"],
        "correct_option": 2,
        "explanation": "Number of ways = (6C3) * (4C2). 6C3 = (6 * 5 * 4) / (3 * 2 * 1) = 20. 4C2 = (4 * 3) / (2 * 1) = 6. Total = 20 * 6 = 120 ways.",
        "shortcut": "6C3 * 4C2 = 20 * 6 = 120."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Permutations and Combinations", "difficulty": "Hard",
        "question": "In how many ways can 7 people sit around a circular dining table?",
        "options": ["120", "360", "720", "5,040"],
        "correct_option": 2,
        "explanation": "Circular permutations of n distinct objects is given by (n - 1)!. For 7 people: (7 - 1)! = 6! = 720.",
        "shortcut": "(n - 1)! = 6! = 720."
    },

    # 8. Simple and Compound Interest (41-45)
    {
        "category": "Quantitative Aptitude", "topic": "Simple and Compound Interest", "difficulty": "Easy",
        "question": "At what rate of simple interest per annum will a sum of money double itself in 8 years?",
        "options": ["10%", "12.5%", "15%", "16.66%"],
        "correct_option": 1,
        "explanation": "Let principal = P. Simple interest = P. Time = 8 years. SI = (P * R * T) / 100 => P = (P * R * 8) / 100 => R = 100 / 8 = 12.5%.",
        "shortcut": "Rate = 100 / Years = 100 / 8 = 12.5%."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Simple and Compound Interest", "difficulty": "Medium",
        "question": "What is the difference between compound interest and simple interest on $5,000 for 2 years at 10% per annum?",
        "options": ["$40", "$50", "$60", "$75"],
        "correct_option": 1,
        "explanation": "For 2 years, CI - SI = P * (R / 100)^2. Here, 5000 * (10 / 100)^2 = 5000 * 0.01 = $50.",
        "shortcut": "Difference = P * (R/100)^2 = 5000 * 0.01 = $50."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Simple and Compound Interest", "difficulty": "Medium",
        "question": "A sum of money placed at compound interest doubles itself in 4 years. In how many years will it amount to 8 times itself at the same rate?",
        "options": ["8 years", "12 years", "16 years", "20 years"],
        "correct_option": 1,
        "explanation": "Under compound interest, growth is geometric: 2 times in 4 years, 4 times (2^2) in 8 years, 8 times (2^3) in 12 years.",
        "shortcut": "If 2^1 in 4 yrs, then 2^3 in (3 * 4) = 12 years."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Simple and Compound Interest", "difficulty": "Hard",
        "question": "What is the compound interest on $16,000 for 9 months at 20% per annum, compounded quarterly?",
        "options": ["$2,482", "$2,522", "$2,642", "$2,720"],
        "correct_option": 1,
        "explanation": "Compounded quarterly: Rate per quarter = 20% / 4 = 5%. 9 months = 3 quarters. Amount = 16000 * (1 + 5/100)^3 = 16000 * (21/20)^3 = 16000 * (9261 / 8000) = 2 * 9261 = $18,522. CI = 18,522 - 16,000 = $2,522.",
        "shortcut": "Quarterly rate = 5%, n = 3 periods. Amount = 16000 * (1.05)^3 = 18522. CI = 2522."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Simple and Compound Interest", "difficulty": "Easy",
        "question": "If $1,200 yields an interest of $216 in 3 years at simple interest, what is the rate of interest per annum?",
        "options": ["5%", "6%", "7%", "8%"],
        "correct_option": 1,
        "explanation": "R = (SI * 100) / (P * T) = (216 * 100) / (1200 * 3) = 21600 / 3600 = 6%.",
        "shortcut": "Annual interest = 216 / 3 = 72. Rate = 72 / 1200 * 100 = 6%."
    },

    # =========================================================================
    # LOGICAL REASONING (46 - 75)
    # =========================================================================
    # 9. Number Series (46-50)
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Easy",
        "question": "Find the missing number in the sequence: 4, 9, 16, 25, 36, ?",
        "options": ["42", "45", "49", "64"],
        "correct_option": 2,
        "explanation": "The terms are consecutive squares: 2^2, 3^2, 4^2, 5^2, 6^2, 7^2 = 49.",
        "shortcut": "7^2 = 49."
    },
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Medium",
        "question": "Find the missing number in the series: 2, 6, 12, 20, 30, 42, ?",
        "options": ["52", "54", "56", "60"],
        "correct_option": 2,
        "explanation": "Differences between consecutive terms are increasing even numbers: 6-2=4, 12-6=6, 20-12=8, 30-20=10, 42-30=12. Next difference is 14: 42 + 14 = 56. (Alternatively, n^2 + n).",
        "shortcut": "7^2 + 7 = 49 + 7 = 56."
    },
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Medium",
        "question": "Identify the next number in the pattern: 3, 7, 15, 31, 63, ?",
        "options": ["120", "125", "127", "131"],
        "correct_option": 2,
        "explanation": "Each term is generated by (2 * prev + 1): 3*2+1=7, 7*2+1=15, 15*2+1=31, 31*2+1=63. Next term = 63 * 2 + 1 = 127.",
        "shortcut": "Formula is 2^(n+1) - 1: 2^7 - 1 = 128 - 1 = 127."
    },
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Hard",
        "question": "Find the wrong number in the series: 8, 27, 64, 100, 216, 343",
        "options": ["27", "64", "100", "216"],
        "correct_option": 2,
        "explanation": "All numbers are perfect cubes: 2^3=8, 3^3=27, 4^3=64, 5^3=125 (given as 100), 6^3=216, 7^3=343. 100 is wrong.",
        "shortcut": "5^3 = 125, but 100 is given."
    },
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Easy",
        "question": "Complete the sequence: 5, 11, 23, 47, 95, ?",
        "options": ["189", "191", "195", "199"],
        "correct_option": 1,
        "explanation": "Pattern is (x * 2 + 1): 5*2+1=11, 11*2+1=23, 23*2+1=47, 47*2+1=95. Next is 95 * 2 + 1 = 191.",
        "shortcut": "95 * 2 + 1 = 191."
    },

    # 10. Coding-Decoding (51-55)
    {
        "category": "Logical Reasoning", "topic": "Coding-Decoding", "difficulty": "Easy",
        "question": "In a certain code language, if 'MADRAS' is coded as 'NBESBT', how is 'BOMBAY' coded in that language?",
        "options": ["CPNCBX", "CPNCBZ", "CPOCBZ", "CQOCBZ"],
        "correct_option": 1,
        "explanation": "Each letter is shifted by +1: M->N, A->B, D->E, R->S, A->B, S->T. For BOMBAY: B->C, O->P, M->N, B->C, A->B, Y->Z => CPNCBZ.",
        "shortcut": "Shift each letter by +1."
    },
    {
        "category": "Logical Reasoning", "topic": "Coding-Decoding", "difficulty": "Medium",
        "question": "If 'TEACHER' is coded as 'VGCEJGT', what will be the code for 'CHILDREN'?",
        "options": ["EJKNFTP", "EJKNFTGP", "EJKNFGTO", "EJKNEGTO"],
        "correct_option": 1,
        "explanation": "Each letter is shifted by +2: T(+2)->V, E(+2)->G, A(+2)->C, C(+2)->E, etc. For CHILDREN: C->E, H->J, I->K, L->N, D->F, R->T, E->G, N->P => EJKNFTGP.",
        "shortcut": "+2 forward alphabet shift for all letters."
    },
    {
        "category": "Logical Reasoning", "topic": "Coding-Decoding", "difficulty": "Easy",
        "question": "If 'ROSE' is coded as '6821' and 'CHAIR' is coded as '73456', how is 'SEARCH' coded?",
        "options": ["214673", "214763", "216473", "241673"],
        "correct_option": 0,
        "explanation": "Direct letter substitution: S=2, E=1, A=4, R=6, C=7, H=3. Hence SEARCH = 214673.",
        "shortcut": "Direct mapping: S->2, E->1, A->4, R->6, C->7, H->3."
    },
    {
        "category": "Logical Reasoning", "topic": "Coding-Decoding", "difficulty": "Medium",
        "question": "If 'WATER' is written as 'YCVGT', how is 'HIKER' written in that code?",
        "options": ["JKMGT", "JKMGV", "JKMHT", "IKMGT"],
        "correct_option": 0,
        "explanation": "Pattern is +2: W(+2)=Y, A(+2)=C, T(+2)=V, E(+2)=G, R(+2)=T. H(+2)=J, I(+2)=K, K(+2)=M, E(+2)=G, R(+2)=T => JKMGT.",
        "shortcut": "Add 2 to each letter."
    },
    {
        "category": "Logical Reasoning", "topic": "Coding-Decoding", "difficulty": "Hard",
        "question": "In a coded language, '134' means 'good and tasty', '478' means 'see good pictures', and '729' means 'pictures are faint'. Which digit stands for 'see'?",
        "options": ["4", "7", "8", "9"],
        "correct_option": 2,
        "explanation": "In statements 1 and 2, common word is 'good' and common digit is '4', so good=4. In statements 2 and 3, common word is 'pictures' and common digit is '7', so pictures=7. In statement 2 ('478' = 'see good pictures'), the remaining digit '8' must stand for 'see'.",
        "shortcut": "good=4, pictures=7 => see=8."
    },

    # 11. Blood Relations (56-60)
    {
        "category": "Logical Reasoning", "topic": "Blood Relations", "difficulty": "Easy",
        "question": "Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?",
        "options": ["Brother", "Uncle", "Father", "Cousin"],
        "correct_option": 2,
        "explanation": "The 'only son of my mother' for Suresh is Suresh himself. Therefore, the boy is the son of Suresh, so Suresh is the Father.",
        "shortcut": "Only son of Suresh's mother = Suresh. Boy is his son."
    },
    {
        "category": "Logical Reasoning", "topic": "Blood Relations", "difficulty": "Medium",
        "question": "A is the brother of B. B is the daughter of C. D is the father of A. How is C related to D?",
        "options": ["Wife", "Mother", "Sister", "Daughter"],
        "correct_option": 0,
        "explanation": "A and B are siblings (A is son, B is daughter). D is their father. Since B is the daughter of C as well, C must be the mother of the children, and hence C is the wife of D.",
        "shortcut": "D is father, children have mother C => C is wife of D."
    },
    {
        "category": "Logical Reasoning", "topic": "Blood Relations", "difficulty": "Medium",
        "question": "If P + Q means P is the father of Q; P - Q means P is the sister of Q; P * Q means P is the brother of Q. Which of the following means that M is the niece of N?",
        "options": ["N * K + M - T", "N * K + M * T", "N - K * M + T", "N + K - M"],
        "correct_option": 0,
        "explanation": "In 'N * K + M - T': N is brother of K; K is father of M; M is sister of T (so M is female). Being the daughter of N's brother K, M is the niece of N.",
        "shortcut": "K is father of M, M is female (- T), N is brother of K => M is niece."
    },
    {
        "category": "Logical Reasoning", "topic": "Blood Relations", "difficulty": "Easy",
        "question": "Introducing a woman, a man said, 'Her mother is the only daughter of my mother-in-law.' How is the man related to the woman?",
        "options": ["Father", "Brother", "Husband", "Uncle"],
        "correct_option": 0,
        "explanation": "Only daughter of man's mother-in-law is the man's wife. Woman's mother is the man's wife. Therefore, the man is her Father.",
        "shortcut": "Only daughter of mother-in-law = wife. Mother is wife => man is Father."
    },
    {
        "category": "Logical Reasoning", "topic": "Blood Relations", "difficulty": "Hard",
        "question": "Looking at a portrait, John said, 'I have no brothers or sisters, but that man's father is my father's son.' Whose portrait was it?",
        "options": ["His own", "His son's", "His father's", "His nephew's"],
        "correct_option": 1,
        "explanation": "Since John has no siblings, 'my father's son' is John himself. 'That man's father is [John]'. Therefore, the portrait is of his son.",
        "shortcut": "My father's son = John. That man's father = John => That man is John's son."
    },

    # 12. Direction Sense & Syllogisms (61-68)
    {
        "category": "Logical Reasoning", "topic": "Direction Sense", "difficulty": "Easy",
        "question": "A person walks 10 meters North, turns right and walks 15 meters, then turns right again and walks 10 meters. How far and in which direction is he from the starting point?",
        "options": ["15 meters East", "15 meters West", "10 meters East", "25 meters South"],
        "correct_option": 0,
        "explanation": "North 10m and South 10m cancel out along the vertical axis. The net horizontal displacement is 15 meters to the East.",
        "shortcut": "10m North + 10m South = 0. Remaining vector = 15m East."
    },
    {
        "category": "Logical Reasoning", "topic": "Direction Sense", "difficulty": "Medium",
        "question": "Starting from point A, Rahul walks 6 km South, turns West and walks 8 km. What is the shortest distance between his current position and point A?",
        "options": ["10 km", "12 km", "14 km", "16 km"],
        "correct_option": 0,
        "explanation": "Shortest distance = hypotenuse of right-angled triangle = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 km.",
        "shortcut": "Pythagorean triplet (6, 8, 10). Distance = 10 km."
    },
    {
        "category": "Logical Reasoning", "topic": "Direction Sense", "difficulty": "Medium",
        "question": "One morning after sunrise, Vikram was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was Vikram facing?",
        "options": ["East", "West", "North", "South"],
        "correct_option": 3,
        "explanation": "In the morning, the sun is in the East, so shadows fall towards the West. If the shadow is to Vikram's right, his right side points West. A person whose right is West must be facing South.",
        "shortcut": "Morning shadow points West. Right = West => Facing South."
    },
    {
        "category": "Logical Reasoning", "topic": "Syllogisms", "difficulty": "Easy",
        "question": "Statements: All cats are dogs. All dogs are birds.\nConclusions: \nI. All cats are birds.\nII. All birds are cats.",
        "options": ["Only I follows", "Only II follows", "Both I and II follow", "Neither I nor II follows"],
        "correct_option": 0,
        "explanation": "Since Cats ⊆ Dogs and Dogs ⊆ Birds, it directly follows that Cats ⊆ Birds (All cats are birds). Conclusion II (All birds are cats) does not necessarily follow.",
        "shortcut": "Transitive subset: A ⊆ B ⊆ C => A ⊆ C. Only I follows."
    },
    {
        "category": "Logical Reasoning", "topic": "Syllogisms", "difficulty": "Medium",
        "question": "Statements: Some apples are oranges. All oranges are grapes.\nConclusions: \nI. Some apples are grapes.\nII. No grape is an apple.",
        "options": ["Only I follows", "Only II follows", "Either I or II follows", "Neither follows"],
        "correct_option": 0,
        "explanation": "Since some apples are oranges and all oranges are grapes, the overlapping apples must also be grapes. Thus, 'Some apples are grapes' definitely follows.",
        "shortcut": "I-type + A-type statement = I-type conclusion (Some apples are grapes)."
    },
    {
        "category": "Logical Reasoning", "topic": "Syllogisms", "difficulty": "Hard",
        "question": "Statements: Some pens are books. No book is a chair.\nConclusions: \nI. Some pens are not chairs.\nII. Some chairs are pens.",
        "options": ["Only I follows", "Only II follows", "Both follow", "Neither follows"],
        "correct_option": 0,
        "explanation": "The portion of pens that are books cannot be chairs (since no book is a chair). Therefore, those specific pens are not chairs. Conclusion I definitely follows.",
        "shortcut": "Some pens are books; no books are chairs => Those pens cannot be chairs. Only I follows."
    },
    {
        "category": "Logical Reasoning", "topic": "Seating Arrangements", "difficulty": "Medium",
        "question": "Five friends P, Q, R, S, and T are standing in a row facing North. Q is to the immediate right of P. T is to the left of P but right of S. R is to the right of Q. Who is standing in the middle?",
        "options": ["P", "Q", "R", "T"],
        "correct_option": 0,
        "explanation": "Left to right: S is left of T. T is left of P. P is left of Q. Q is left of R. Row order: S, T, P, Q, R. The middle person is P.",
        "shortcut": "Sequence: S - T - P - Q - R. Middle is P."
    },
    {
        "category": "Logical Reasoning", "topic": "Puzzles", "difficulty": "Medium",
        "question": "A clock shows 3:15. What is the angle between the hour hand and the minute hand?",
        "options": ["0°", "7.5°", "12°", "15°"],
        "correct_option": 1,
        "explanation": "Angle = |30 * H - (11/2) * M| = |30 * 3 - (11/2) * 15| = |90 - 82.5| = 7.5°.",
        "shortcut": "At 3:15, minute hand is at 3, but hour hand has moved (15/60) * 30° = 7.5°."
    },

    # 13. Logical Puzzles (69-75)
    {
        "category": "Logical Reasoning", "topic": "Puzzles", "difficulty": "Easy",
        "question": "If January 1, 2024 was a Monday, what day of the week was December 31, 2024? (2024 is a leap year)",
        "options": ["Monday", "Tuesday", "Wednesday", "Sunday"],
        "correct_option": 1,
        "explanation": "A leap year has 366 days (52 weeks + 2 odd days). In a leap year, the year ends on the day of the week following the day it began. Monday + 1 day = Tuesday.",
        "shortcut": "Leap year starts and ends on consecutive days (starts Mon -> ends Tue)."
    },
    {
        "category": "Logical Reasoning", "topic": "Puzzles", "difficulty": "Hard",
        "question": "There are 8 identical-looking coins, one of which is counterfeit and lighter than the others. Using a two-pan balance scale, what is the minimum number of weighings needed to guarantee finding the lighter coin?",
        "options": ["2", "3", "4", "5"],
        "correct_option": 0,
        "explanation": "Divide 8 coins into 3 groups: 3, 3, and 2.\nWeighing 1: Weigh 3 vs 3. If unequal, lighter coin is in the lighter 3-coin group. If equal, it is in the 2-coin group.\nWeighing 2: From the suspected group (either 3 coins: weigh 1 vs 1, or 2 coins: weigh 1 vs 1), the lighter coin is identified. Total = 2 weighings.",
        "shortcut": "Powers of 3: 3^2 = 9 >= 8, so 2 weighings are sufficient."
    },
    {
        "category": "Logical Reasoning", "topic": "Puzzles", "difficulty": "Medium",
        "question": "A snail is at the bottom of a 30-foot well. Each day it climbs up 3 feet, but at night it slips down 2 feet. How many days will it take to reach the top?",
        "options": ["27 days", "28 days", "29 days", "30 days"],
        "correct_option": 1,
        "explanation": "Net climb per 24 hours = 3 - 2 = 1 foot. After 27 days, it reaches 27 feet. On day 28, it climbs 3 feet: 27 + 3 = 30 feet, reaching the top and escaping before slipping. Total = 28 days.",
        "shortcut": "Days = (Depth - Climb) / Net + 1 = (30 - 3)/1 + 1 = 28 days."
    },
    {
        "category": "Logical Reasoning", "topic": "Direction Sense", "difficulty": "Easy",
        "question": "A man walks 5 km East, turns right and walks 4 km, then turns left and walks 5 km. Which direction is he facing now?",
        "options": ["North", "South", "East", "West"],
        "correct_option": 2,
        "explanation": "Facing East -> turns right (faces South) -> turns left (faces East again).",
        "shortcut": "Right + Left = 0 degrees net turn. Still facing East."
    },
    {
        "category": "Logical Reasoning", "topic": "Seating Arrangements", "difficulty": "Hard",
        "question": "Six people A, B, C, D, E, F sit in a circle facing the center. A is opposite to D. B is between A and C. E is to the immediate right of D. Who is sitting opposite to B?",
        "options": ["C", "E", "F", "D"],
        "correct_option": 1,
        "explanation": "Let circle positions 1 to 6 clockwise. A at 1, D opposite at 4. E is immediate right of D (position 3). Since B is between A and C, B is at 6 and C is at 5. Remaining position 2 is F. Opposite to position 6 (B) is position 3 (E).",
        "shortcut": "Circle geometry: Opposite of B is E."
    },
    {
        "category": "Logical Reasoning", "topic": "Number Series", "difficulty": "Medium",
        "question": "Find the missing number: 1, 8, 27, 64, 125, ?",
        "options": ["196", "216", "256", "343"],
        "correct_option": 1,
        "explanation": "Sequence of cubes: 1^3, 2^3, 3^3, 4^3, 5^3, 6^3 = 216.",
        "shortcut": "6^3 = 216."
    },
    {
        "category": "Logical Reasoning", "topic": "Direction Sense", "difficulty": "Medium",
        "question": "A compass was damaged such that North-East is shown as North, and South-East is shown as East. What will West be shown as?",
        "options": ["North-West", "South-West", "South", "East"],
        "correct_option": 0,
        "explanation": "Directions are rotated 45 degrees anti-clockwise (NE becomes N, SE becomes E). Thus, West rotates 45 degrees anti-clockwise to become North-West.",
        "shortcut": "45° counter-clockwise shift: West -> North-West."
    },

    # =========================================================================
    # VERBAL ABILITY (76 - 100)
    # =========================================================================
    # 14. Synonyms & Antonyms (76-83)
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Easy",
        "question": "Choose the word that is most nearly SYNONYMOUS in meaning to 'CANDID':",
        "options": ["Secretive", "Frank", "Deceptive", "Arrogant"],
        "correct_option": 1,
        "explanation": "'Candid' means truthful, straightforward, and sincere. 'Frank' is an exact synonym.",
        "shortcut": "Candid camera / candid truth = honest & frank."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Medium",
        "question": "Choose the word that is most nearly OPPOSITE in meaning to 'METICULOUS':",
        "options": ["Careless", "Thorough", "Detailed", "Scrupulous"],
        "correct_option": 0,
        "explanation": "'Meticulous' means showing great attention to detail and precision. Its antonym is 'Careless' or 'Sloppy'.",
        "shortcut": "Meticulous = extremely careful. Antonym = careless."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Medium",
        "question": "Select the SYNONYM of the word 'PRAGMATIC':",
        "options": ["Idealistic", "Practical", "Theoretical", "Speculative"],
        "correct_option": 1,
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.",
        "shortcut": "Pragmatic = practical."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Hard",
        "question": "Choose the word OPPOSITE in meaning to 'EPHEMERAL':",
        "options": ["Transient", "Fleeting", "Permanent", "Short-lived"],
        "correct_option": 2,
        "explanation": "'Ephemeral' means lasting for a very short time. Its opposite is 'Permanent' or 'Enduring'.",
        "shortcut": "Ephemeral = fleeting. Antonym = permanent."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Easy",
        "question": "Choose the SYNONYM of 'ABUNDANT':",
        "options": ["Plentiful", "Scarce", "Meager", "Deficient"],
        "correct_option": 0,
        "explanation": "'Abundant' means existing or available in large quantities; overflowing. 'Plentiful' is the synonym.",
        "shortcut": "Abundant = in large supply = plentiful."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Medium",
        "question": "Find the ANTONYM of 'PLACATE':",
        "options": ["Appease", "Soothe", "Provoke", "Calm"],
        "correct_option": 2,
        "explanation": "'Placate' means to make someone less angry or hostile. The opposite is to 'Provoke' or 'Enrage'.",
        "shortcut": "Placate = calm down. Opposite = provoke."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Easy",
        "question": "Select the SYNONYM of 'LUCID':",
        "options": ["Unclear", "Vague", "Clear", "Ambiguous"],
        "correct_option": 2,
        "explanation": "'Lucid' means expressed clearly; easy to understand. 'Clear' is the synonym.",
        "shortcut": "Lucid explanation = clear explanation."
    },
    {
        "category": "Verbal Ability", "topic": "Synonyms and Antonyms", "difficulty": "Hard",
        "question": "Find the ANTONYM of 'GREGARIOUS':",
        "options": ["Sociable", "Reclusive", "Extroverted", "Companionable"],
        "correct_option": 1,
        "explanation": "'Gregarious' describes a person fond of company and sociable. 'Reclusive' (solitary, withdrawn) is the direct antonym.",
        "shortcut": "Gregarious = enjoys company. Reclusive = avoids people."
    },

    # 15. Sentence Correction & Grammar (84-93)
    {
        "category": "Verbal Ability", "topic": "Sentence Correction", "difficulty": "Easy",
        "question": "Identify the grammatically correct sentence:",
        "options": [
            "Neither of the two candidates have submitted their resume.",
            "Neither of the two candidates has submitted his or her resume.",
            "Neither of the two candidates have submitted his resume.",
            "Neither of the two candidates were submitting resumes."
        ],
        "correct_option": 1,
        "explanation": "'Neither' is singular and takes a singular verb ('has') and singular pronoun ('his or her').",
        "shortcut": "'Neither of the [plural]' takes singular verb (has)."
    },
    {
        "category": "Verbal Ability", "topic": "Sentence Correction", "difficulty": "Medium",
        "question": "Correct the underlined phrase: 'She insisted on me accompanying her to the symposium.'",
        "options": [
            "on me to accompany",
            "on my accompanying",
            "for me accompanying",
            "to my accompanying"
        ],
        "correct_option": 1,
        "explanation": "A gerund ('accompanying') must be preceded by a possessive pronoun ('my', not objective 'me'). Hence 'on my accompanying'.",
        "shortcut": "Possessive pronoun + Gerund (my accompanying)."
    },
    {
        "category": "Verbal Ability", "topic": "Sentence Correction", "difficulty": "Medium",
        "question": "Choose the correct option to complete: 'Hardly had he entered the room ______ the lights went out.'",
        "options": ["then", "when", "than", "that"],
        "correct_option": 1,
        "explanation": "The correlative conjunction pair for 'Hardly / Scarcely' is 'when' (whereas 'No sooner' pairs with 'than').",
        "shortcut": "Hardly/Scarcely ... when. No sooner ... than."
    },
    {
        "category": "Verbal Ability", "topic": "Grammar", "difficulty": "Easy",
        "question": "Fill in the blank: 'The team of researchers ______ published its landmark discovery.'",
        "options": ["have", "has", "are", "were"],
        "correct_option": 1,
        "explanation": "'Team' is a collective noun acting as a single unit here, indicated by the singular pronoun 'its'. It takes the singular verb 'has'.",
        "shortcut": "Collective noun acting as one unit + 'its' -> singular verb 'has'."
    },
    {
        "category": "Verbal Ability", "topic": "Grammar", "difficulty": "Medium",
        "question": "Choose the correct sentence regarding conditional tense:",
        "options": [
            "If I was you, I would accept the job offer.",
            "If I were you, I would accept the job offer.",
            "If I am you, I will accept the job offer.",
            "If I had been you, I will accept the offer."
        ],
        "correct_option": 1,
        "explanation": "In hypothetical, contrary-to-fact subjunctive statements, 'were' is used regardless of the subject ('If I were you').",
        "shortcut": "Subjunctive mood: 'If I were you'."
    },
    {
        "category": "Verbal Ability", "topic": "Grammar", "difficulty": "Easy",
        "question": "Identify the part with an error: 'Each of the students (A) / are required to submit (B) / their assignment on Friday (C).'",
        "options": ["Part A", "Part B", "Part C", "No error"],
        "correct_option": 1,
        "explanation": "'Each' is singular and requires a singular verb: 'is required' instead of 'are required'.",
        "shortcut": "'Each of the...' always takes singular verb 'is'."
    },
    {
        "category": "Verbal Ability", "topic": "Grammar", "difficulty": "Medium",
        "question": "Select the correct preposition: 'He is accustomed ______ working late into the night.'",
        "options": ["with", "to", "at", "for"],
        "correct_option": 1,
        "explanation": "The idiom is 'accustomed to', which is followed by a gerund ('working').",
        "shortcut": "Accustomed to + gerund."
    },
    {
        "category": "Verbal Ability", "topic": "Sentence Correction", "difficulty": "Hard",
        "question": "Choose the best substitution for the underlined part: 'Being that it was raining, the cricket match was cancelled.'",
        "options": [
            "Being it was raining",
            "Since it was raining",
            "It being that it was raining",
            "Because of it rained"
        ],
        "correct_option": 1,
        "explanation": "'Being that' is non-standard and colloquial English. The standard causal conjunction is 'Since' or 'Because'.",
        "shortcut": "Replace informal 'being that' with 'Since' or 'Because'."
    },
    {
        "category": "Verbal Ability", "topic": "Sentence Correction", "difficulty": "Medium",
        "question": "Select the option with correct parallel structure:",
        "options": [
            "He likes swimming, running, and to bike.",
            "He likes swimming, running, and biking.",
            "He likes to swim, running, and biking.",
            "He likes swimming, to run, and to bike."
        ],
        "correct_option": 1,
        "explanation": "Parallel structure requires items in a list to share the same grammatical form (all gerunds: swimming, running, biking).",
        "shortcut": "Parallelism: Keep all list items in matching -ing forms."
    },
    {
        "category": "Verbal Ability", "topic": "Grammar", "difficulty": "Easy",
        "question": "Choose the correct pronoun: 'Between you and ______, this project will succeed.'",
        "options": ["I", "me", "myself", "mine"],
        "correct_option": 1,
        "explanation": "'Between' is a preposition, and prepositions require objective case pronouns ('between you and me', never 'between you and I').",
        "shortcut": "Preposition + objective case (me, not I)."
    },

    # 16. Reading Comprehension & Vocabulary (94-100)
    {
        "category": "Verbal Ability", "topic": "Reading Comprehension", "difficulty": "Medium",
        "question": "Read the passage: 'Artificial Intelligence systems rely heavily on algorithmic fairness. When algorithms are trained on historically skewed data, they inadvertently codify and amplify societal prejudices under the facade of objective computation.'\nAccording to the passage, why do biased AI systems appear objective?",
        "options": [
            "Because they are designed by impartial researchers.",
            "Because mathematical computation gives an impression of neutrality.",
            "Because they use exclusively modern datasets.",
            "Because algorithms actively eliminate historical bias."
        ],
        "correct_option": 1,
        "explanation": "The passage notes that prejudices are amplified 'under the facade of objective computation'—meaning the mathematical nature of computation gives a misleading appearance of neutrality.",
        "shortcut": "'Facade of objective computation' points directly to option B."
    },
    {
        "category": "Verbal Ability", "topic": "Reading Comprehension", "difficulty": "Medium",
        "question": "Read the excerpt: 'In software development, premature optimization is often termed the root of all evil. Engineers frequently expend disproportionate effort speeding up non-critical paths while ignoring foundational architecture.'\nWhat is the primary cautionary message of this excerpt?",
        "options": [
            "Optimization should never be performed.",
            "Foundational architecture should be prioritized before micro-optimizing non-bottlenecks.",
            "All software paths are equally critical.",
            "Engineers should write slow code intentionally."
        ],
        "correct_option": 1,
        "explanation": "The text warns against spending effort on non-critical micro-optimizations while neglecting core architecture.",
        "shortcut": "Prioritize foundational design over micro-optimizations."
    },
    {
        "category": "Verbal Ability", "topic": "Vocabulary", "difficulty": "Easy",
        "question": "What is the meaning of the idiom 'To burn the midnight oil'?",
        "options": [
            "To waste fuel unnecessarily",
            "To work or study late into the night",
            "To start a late-night fire",
            "To make hasty decisions"
        ],
        "correct_option": 1,
        "explanation": "'Burn the midnight oil' is a well-known idiom meaning to work or study late into the night.",
        "shortcut": "Studying/working late = burning midnight oil."
    },
    {
        "category": "Verbal Ability", "topic": "Vocabulary", "difficulty": "Medium",
        "question": "What is the meaning of the word 'UBIQUITOUS'?",
        "options": ["Extremely rare", "Present everywhere", "Ancient and obsolete", "Highly dangerous"],
        "correct_option": 1,
        "explanation": "'Ubiquitous' means present, appearing, or found everywhere (omnipresent).",
        "shortcut": "Ubiquitous = everywhere (e.g., smartphones are ubiquitous)."
    },
    {
        "category": "Verbal Ability", "topic": "Vocabulary", "difficulty": "Hard",
        "question": "Select the word that describes a person who speaks multiple languages fluently:",
        "options": ["Polymath", "Polyglot", "Philologist", "Etymologist"],
        "correct_option": 1,
        "explanation": "A 'Polyglot' is a person who knows and is able to use several languages. (A polymath is a person of wide learning in multiple subjects).",
        "shortcut": "Poly (many) + glot (tongues/languages) = Polyglot."
    },
    {
        "category": "Verbal Ability", "topic": "Vocabulary", "difficulty": "Medium",
        "question": "What does the Latin phrase 'Status Quo' mean in modern English?",
        "options": [
            "The existing state of affairs",
            "A catastrophic failure",
            "A great accomplishment",
            "A legal summons"
        ],
        "correct_option": 0,
        "explanation": "'Status quo' refers to the current, existing state of political or social affairs without alteration.",
        "shortcut": "Status quo = existing state of affairs."
    },
    {
        "category": "Verbal Ability", "topic": "Reading Comprehension", "difficulty": "Hard",
        "question": "Read: 'Resilience is not the absence of stress, but the capacity to recover swiftly from adversity. High-performing engineering teams cultivate psychological safety, which emboldens individuals to report errors without fear of retribution.'\nWhich factor fosters resilience according to the text?",
        "options": [
            "Complete elimination of workplace stress",
            "Psychological safety that permits transparent error reporting",
            "Penalizing minor mistakes strictly",
            "Strict non-disclosure agreements"
        ],
        "correct_option": 1,
        "explanation": "The text states teams cultivate psychological safety, which emboldens individuals to report errors without fear, fostering recovery and resilience.",
        "shortcut": "Direct mapping: 'cultivate psychological safety... report errors without fear'."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time, Speed and Distance", "difficulty": "Medium",
        "question": "A boat travels 24 km upstream and 36 km downstream, taking 6 hours each time. What is the speed of the water current?",
        "options": ["1 km/h", "1.5 km/h", "2 km/h", "2.5 km/h"],
        "correct_option": 0,
        "explanation": "Downstream speed (v + s) = 36 / 6 = 6 km/h. Upstream speed (v - s) = 24 / 6 = 4 km/h. Speed of current s = (Downstream - Upstream) / 2 = (6 - 4) / 2 = 1 km/h.",
        "shortcut": "Current speed = (Downstream - Upstream) / 2 = (6 - 4)/2 = 1 km/h."
    },
    {
        "category": "Quantitative Aptitude", "topic": "Time and Work", "difficulty": "Hard",
        "question": "Three pipes A, B, and C can fill a cistern in 6 hours. After working together for 2 hours, C is closed and A and B fill the remaining part in 7 hours. In how many hours can C alone fill the cistern?",
        "options": ["10 hours", "12 hours", "14 hours", "16 hours"],
        "correct_option": 2,
        "explanation": "Work done by (A + B + C) in 2 hours = 2/6 = 1/3. Remaining work = 1 - 1/3 = 2/3. (A + B) do 2/3 work in 7 hours => (A + B)'s 1-hour work = (2/3) / 7 = 2/21. C's 1-hour work = (A + B + C) - (A + B) = 1/6 - 2/21 = (7 - 4)/42 = 3/42 = 1/14. Therefore, C alone fills it in 14 hours.",
        "shortcut": "C's 1-hour work = 1/6 - (2/3)/7 = 1/6 - 2/21 = 1/14 => 14 hours."
    }
]
