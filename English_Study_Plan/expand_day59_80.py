"""
扩充 Day 59-80 的听力和完形填空数据
以及补充缺失的 Day 26 完形数据
"""
import json
import os

def append_json(filepath, new_items):
    """追加数据到 JSON 文件，自动跳过已存在的 day"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    existing_days = {item['day'] for item in data}
    filtered_new = [item for item in new_items if item['day'] not in existing_days]
    data.extend(filtered_new)
    # 按 day 排序
    data.sort(key=lambda x: x['day'])
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return len(filtered_new)

# ===== 听力数据 Day 59-80 =====
new_listening = [
    {
        "id": "L59", "day": 59,
        "title": "The Power of Positive Thinking",
        "text": "A positive attitude can change your life. When you wake up in the morning, try to think about something good that might happen today. Studies show that people who stay positive are often healthier and more successful. My PE teacher always tells us to keep a positive mindset during physical exercise. He says that even when running feels hard, thinking positively can reduce the pain and motivate us to keep going. I tried this method last week during a long-distance run, and it really worked! I felt less tired and even enjoyed the experience.",
        "questions": [
            {"id": 1, "question": "What does a positive attitude help with?", "options": ["Making more money", "Being healthier and more successful", "Sleeping longer"], "answer": 1},
            {"id": 2, "question": "What does the PE teacher suggest?", "options": ["Run faster", "Keep a positive mindset", "Skip exercise"], "answer": 1},
            {"id": 3, "question": "What happened when the speaker tried positive thinking?", "options": ["He ran slower", "He felt less tired", "He stopped running"], "answer": 1}
        ]
    },
    {
        "id": "L60", "day": 60,
        "title": "Finding Solutions Together",
        "text": "In our class, we often have group discussions to find solutions to problems. Last week, our teacher asked us to think about how pollution affects our city. We divided into small groups and shared our ideas. Some students suggested planting more trees, while others talked about reducing plastic waste. The average student came up with at least three ideas. What surprised me was the connection between everyone's thoughts. Although we had different opinions, they all pointed to one thing: we need to work together for a better environment. The comfort of knowing that everyone cares gave me hope.",
        "questions": [
            {"id": 1, "question": "What was the discussion topic?", "options": ["School rules", "How pollution affects the city", "A new book"], "answer": 1},
            {"id": 2, "question": "How many ideas did the average student share?", "options": ["One", "At least three", "None"], "answer": 1},
            {"id": 3, "question": "What did the speaker feel after the discussion?", "options": ["Bored", "Hopeful", "Angry"], "answer": 1}
        ]
    },
    {
        "id": "L61", "day": 61,
        "title": "Recycling at School",
        "text": "Our school started a recycling program last month. We learned that many natural resources are limited, so we should recycle as much as possible. The program teaches us to separate paper, plastic, and metal waste. Some students had an argument about whether recycling really makes a difference. Our science teacher showed us data proving that recycling one ton of paper saves seventeen trees. This fact raised everyone's self-esteem because we realized our small actions matter. Even recycling a single bottle can help protect the Earth.",
        "questions": [
            {"id": 1, "question": "What does the school recycling program teach?", "options": ["How to cook", "How to separate waste", "How to plant trees"], "answer": 1},
            {"id": 2, "question": "How many trees does recycling one ton of paper save?", "options": ["Seven", "Seventeen", "Seventy"], "answer": 1},
            {"id": 3, "question": "Why did students feel better about themselves?", "options": ["They got prizes", "Their small actions matter", "The teacher praised them"], "answer": 1}
        ]
    },
    {
        "id": "L62", "day": 62,
        "title": "A New Recipe",
        "text": "My mother found a new recipe online for a healthy smoothie. She wanted to replace our usual sugary drinks with something better. The recipe required fresh fruit, yogurt, and a little honey. I helped her prepare the ingredients and we made it together. When my father tasted it, he responded with a big smile and said it was delicious. Now we make smoothies every morning. This small change has helped strengthen our family's health. My mother says that eating well is the foundation of a happy life.",
        "questions": [
            {"id": 1, "question": "What did the mother want to replace?", "options": ["Breakfast", "Sugary drinks", "Dinner recipes"], "answer": 1},
            {"id": 2, "question": "What ingredients does the smoothie need?", "options": ["Vegetables and rice", "Fresh fruit, yogurt, and honey", "Bread and milk"], "answer": 1},
            {"id": 3, "question": "How did the father respond?", "options": ["He was angry", "He smiled and said it was delicious", "He refused to try"], "answer": 1}
        ]
    },
    {
        "id": "L63", "day": 63,
        "title": "Climate Change and Us",
        "text": "Climate change is one of the biggest challenges facing our planet. The distance between what we know and what we do is still too large. Scientists say that the global temperature has been rising because of too much carbon dioxide in the air. This affects everything: the weather, the oceans, and even our food. Many young people desire to make a change. They function as voices for the environment by joining climate marches and sharing information online. Every small action we take can help slow down climate change.",
        "questions": [
            {"id": 1, "question": "What causes global temperature to rise?", "options": ["Too much water", "Too much carbon dioxide", "Too many trees"], "answer": 1},
            {"id": 2, "question": "What do many young people want to do?", "options": ["Ignore the problem", "Make a change", "Move to another planet"], "answer": 1},
            {"id": 3, "question": "How do young people function as voices for the environment?", "options": ["By staying silent", "By joining marches and sharing info online", "By watching TV"], "answer": 1}
        ]
    },
    {
        "id": "L64", "day": 64,
        "title": "A Cultural Exchange Program",
        "text": "Our school organized a cultural exchange program with a school in England. Students from both countries could communicate through video calls. At first, some of us felt a sense of loneliness because we didn't know anyone. But as we talked more, we found many shared interests. The English students were curious about Chinese calligraphy, and we wanted to learn about their music. This experience helped expand our view of the world. The expression on everyone's face showed how much they enjoyed the exchange. Increasingly, more students want to join the program.",
        "questions": [
            {"id": 1, "question": "How did students communicate?", "options": ["Through letters", "Through video calls", "By visiting each other"], "answer": 1},
            {"id": 2, "question": "What were the English students curious about?", "options": ["Chinese food", "Chinese calligraphy", "Chinese movies"], "answer": 1},
            {"id": 3, "question": "What was the result of the exchange?", "options": ["Students lost interest", "More students want to join", "The program was cancelled"], "answer": 1}
        ]
    },
    {
        "id": "L65", "day": 65,
        "title": "After-School Activities",
        "text": "Our school offers many extracurricular activities. Students can choose from sports, music, art, and science clubs. Being independent means making your own choices about what to learn outside of class. I joined the robotics club because I want to study a major in engineering when I grow up. In the club, we interact with students from different grades and learn from each other. Last week, we built a small car that could follow a line on the floor. The experience helped us develop practical skills that we can't learn from textbooks alone.",
        "questions": [
            {"id": 1, "question": "What extracurricular activity did the speaker join?", "options": ["Music club", "Art club", "Robotics club"], "answer": 2},
            {"id": 2, "question": "What does being independent mean in this context?", "options": ["Staying alone", "Making your own choices", "Leaving school"], "answer": 1},
            {"id": 3, "question": "What did they build in the club?", "options": ["A robot dog", "A small car", "A computer"], "answer": 1}
        ]
    },
    {
        "id": "L66", "day": 66,
        "title": "Virtual Reality in Education",
        "text": "Virtual reality technology is changing the way we learn. With VR glasses, students can access information in a completely new way. For example, instead of just reading about the ocean, you can virtually dive into it and see fish swimming around you. Our school recently got a VR system, and we used it to learn about carbon emissions and climate change. The technology helped us adapt to new ways of thinking about complex topics. Some people worry about cyber attacks on school networks, but our IT teacher says the system is very safe.",
        "questions": [
            {"id": 1, "question": "What can VR glasses help students do?", "options": ["Play games only", "Access information in a new way", "Replace teachers"], "answer": 1},
            {"id": 2, "question": "What topic did they learn about using VR?", "options": ["History", "Carbon emissions and climate change", "Music"], "answer": 1},
            {"id": 3, "question": "What concern do some people have?", "options": ["VR is too expensive", "Cyber attacks on networks", "Students don't like it"], "answer": 1}
        ]
    },
    {
        "id": "L67", "day": 67,
        "title": "Learning from Mistakes",
        "text": "Everyone makes mistakes, but what matters is how we react to them. A reasonable person knows that mistakes are part of learning. Last month, I made a big mistake during a math exam. I didn't check my answers before handing in the paper. When I got my results, I felt terrible. But instead of giving up, I developed a strategy for future exams: always leave ten minutes to review my work. I also learned to release my stress by talking to friends. Now I stare at my exam papers with confidence, knowing I have a plan.",
        "questions": [
            {"id": 1, "question": "What mistake did the speaker make?", "options": ["Forgot to bring a pen", "Didn't check answers", "Arrived late"], "answer": 1},
            {"id": 2, "question": "What strategy did the speaker develop?", "options": ["Skip difficult questions", "Leave time to review", "Copy from friends"], "answer": 1},
            {"id": 3, "question": "How does the speaker release stress?", "options": ["By sleeping", "By talking to friends", "By eating snacks"], "answer": 1}
        ]
    },
    {
        "id": "L68", "day": 68,
        "title": "Understanding Different Concepts",
        "text": "In our history class, we learned about how societies have changed over the past decade. The teacher explained that understanding different concepts helps us think more clearly. For example, the concept of democracy means that people can vote and have a voice. Our textbook also contained information about ancient civilizations. One characteristic that all great civilizations share is their love of learning. A student made an interesting comment: 'Maybe a thousand years from now, people will study us the same way we study ancient Rome.'",
        "questions": [
            {"id": 1, "question": "What does the concept of democracy mean?", "options": ["Only leaders can decide", "People can vote and have a voice", "Everyone must agree"], "answer": 1},
            {"id": 2, "question": "What characteristic do great civilizations share?", "options": ["Their love of war", "Their love of learning", "Their love of money"], "answer": 1},
            {"id": 3, "question": "What did the student comment about?", "options": ["Future people studying us", "Ancient food recipes", "Modern technology"], "answer": 0}
        ]
    },
    {
        "id": "L69", "day": 69,
        "title": "Social Media and Mental Health",
        "text": "Social media platforms have become a big part of our lives. Everyone has a preference for different apps. However, research in psychology shows that spending too much time on social media can affect our mental health. The constant presence of perfect photos and happy stories can make us feel that our own lives are not good enough. It's important to remember that most people only share their best moments online. A good range of offline activities, like sports and reading, can help us stay healthy and happy.",
        "questions": [
            {"id": 1, "question": "What does psychology research show about social media?", "options": ["It's always good for us", "Too much can affect mental health", "Everyone should use it more"], "answer": 1},
            {"id": 2, "question": "Why might social media make people feel bad?", "options": ["Too many ads", "Constant perfect photos and stories", "Slow internet"], "answer": 1},
            {"id": 3, "question": "What helps us stay healthy according to the text?", "options": ["More screen time", "A range of offline activities", "Posting more photos"], "answer": 1}
        ]
    },
    {
        "id": "L70", "day": 70,
        "title": "The School Bake Sale",
        "text": "Our class organized a bake sale to raise money for charity. At first, some students were not willing to admit that they didn't know how to bake. But our teacher said it was absolutely fine to be a beginner. She taught us how to bake simple cookies and cupcakes. The results were awesome! We sold everything within two hours. Some customers said our cookies were so good that they wanted the recipe. The bake sale was a great success and showed us that even small acts of kindness can make a big difference.",
        "questions": [
            {"id": 1, "question": "Why did they organize a bake sale?", "options": ["For a school party", "To raise money for charity", "To compete with other classes"], "answer": 1},
            {"id": 2, "question": "What did the teacher say about being a beginner?", "options": ["It's embarrassing", "It's absolutely fine", "It's not allowed"], "answer": 1},
            {"id": 3, "question": "How long did it take to sell everything?", "options": ["One hour", "Two hours", "All day"], "answer": 1}
        ]
    },
    {
        "id": "L71", "day": 71,
        "title": "Healthy Eating Choices",
        "text": "Making healthy eating choices is not always easy. Many teenagers face the demand of choosing between fast food and nutritious meals. My friend loves desserts, especially chocolate cake. But her doctor told her that too much sugar can cause discomfort and health problems. At first, she felt discouraged when she had to give up her favorite treats. However, she found that healthy food can also be delicious. Now she enjoys salads and fruit smoothies. The economic cost of eating healthy is sometimes higher, but the benefits are worth it.",
        "questions": [
            {"id": 1, "question": "What challenge do teenagers face with food?", "options": ["Cooking for themselves", "Choosing between fast food and nutritious meals", "Not having enough food"], "answer": 1},
            {"id": 2, "question": "What did the doctor warn about?", "options": ["Too much water", "Too much sugar", "Too much sleep"], "answer": 1},
            {"id": 3, "question": "How did the friend feel at first?", "options": ["Excited", "Discouraged", "Angry"], "answer": 1}
        ]
    },
    {
        "id": "L72", "day": 72,
        "title": "The Lantern Festival",
        "text": "The Lantern Festival marks the end of the Chinese New Year celebrations. On this night, people hang beautiful lanterns of different colors and shapes. Some lanterns are so creative that they look like works of art. The innovation in lantern design has improved greatly over the years. At our local festival, they even installed electronic lanterns that could change colors. My grandmother told me about the interpersonal relationships that are strengthened during this festival, as families and friends gather to solve riddles written on the lanterns. The length of each riddle varies, but they are all fun to solve.",
        "questions": [
            {"id": 1, "question": "What does the Lantern Festival mark?", "options": ["The start of school", "The end of Chinese New Year", "A sports event"], "answer": 1},
            {"id": 2, "question": "What innovation was mentioned?", "options": ["Paper lanterns", "Electronic color-changing lanterns", "Flying lanterns"], "answer": 1},
            {"id": 3, "question": "What do people do with the riddles?", "options": ["Write them as homework", "Solve them together", "Ignore them"], "answer": 1}
        ]
    },
    {
        "id": "L73", "day": 73,
        "title": "Becoming a Professional",
        "text": "My older brother wants to become a professional musician. He practices guitar for two hours every day. His teacher says his playing is becoming more realistic and expressive. During religious festivals, he often performs for the community, which helps him gain experience. He finds performing very relaxing once he gets used to being on stage. Many people think becoming a professional in any field requires only talent, but my brother says hard work is more important. He told me that the key to success is practicing even when you don't feel like it.",
        "questions": [
            {"id": 1, "question": "How long does the brother practice guitar daily?", "options": ["One hour", "Two hours", "Three hours"], "answer": 1},
            {"id": 2, "question": "What does the brother think is more important than talent?", "options": ["Luck", "Hard work", "Good equipment"], "answer": 1},
            {"id": 3, "question": "When does the brother perform for the community?", "options": ["Every weekend", "During religious festivals", "Only in summer"], "answer": 1}
        ]
    },
    {
        "id": "L74", "day": 74,
        "title": "Protecting Ocean Life",
        "text": "The ocean is home to amazing creatures like whales and dolphins. However, human activities are causing many problems. Plastic waste weakens the health of marine animals. Some whales have been found with plastic bags in their stomachs. Scientists are working to update their research methods to better understand how we can help. The latest version of their ocean monitoring system can track whale movements across thousands of kilometers. When I watched a documentary about this, I couldn't help but wander through thoughts about what I could do. Even small actions like refusing plastic straws can make a difference.",
        "questions": [
            {"id": 1, "question": "What problem does plastic waste cause for marine animals?", "options": ["It makes them stronger", "It weakens their health", "It helps them swim"], "answer": 1},
            {"id": 2, "question": "What can the new monitoring system do?", "options": ["Clean the ocean", "Track whale movements", "Remove plastic"], "answer": 1},
            {"id": 3, "question": "What small action is suggested?", "options": ["Eating more fish", "Refusing plastic straws", "Swimming in the ocean"], "answer": 1}
        ]
    },
    {
        "id": "L75", "day": 75,
        "title": "A Science Breakthrough",
        "text": "Last month, scientists announced a breakthrough in solar energy technology. They found a way to make solar panels cheaper, which means more families can afford them. The calculation showed that a family could save up to thirty percent on their electricity bill. This award-winning research was associated with a university in Beijing. The team worked with a limited budget but achieved amazing results. Many experts say this could change how we produce energy in the future. Clean energy is not just a dream anymore; it's becoming reality.",
        "questions": [
            {"id": 1, "question": "What was the breakthrough about?", "options": ["Nuclear energy", "Solar energy technology", "Wind power"], "answer": 1},
            {"id": 2, "question": "How much could a family save on electricity?", "options": ["Ten percent", "Twenty percent", "Thirty percent"], "answer": 2},
            {"id": 3, "question": "What was special about the research team?", "options": ["They had unlimited money", "They worked with a limited budget", "They were all students"], "answer": 1}
        ]
    },
    {
        "id": "L76", "day": 76,
        "title": "School Curriculum Changes",
        "text": "Our school recently updated its curriculum to include more practical subjects. The department of education decided that students need skills for real life, not just textbook knowledge. The new curriculum focuses on defense against misinformation, financial literacy, and digital skills. Students who are dependable and show determination will have more opportunities. My teacher said these changes require our cooperation. She believes that with hard work, every student can succeed. The updated curriculum starts next semester, and everyone is looking forward to it.",
        "questions": [
            {"id": 1, "question": "Why was the curriculum updated?", "options": ["To make school easier", "To teach practical skills", "To reduce homework"], "answer": 1},
            {"id": 2, "question": "What new subjects are included?", "options": ["More math and science", "Financial literacy and digital skills", "More PE classes"], "answer": 1},
            {"id": 3, "question": "When does the new curriculum start?", "options": ["This week", "Next semester", "Next year"], "answer": 1}
        ]
    },
    {
        "id": "L77", "day": 77,
        "title": "A Generous Gift",
        "text": "My grandmother is one of the most generous people I know. Last year, she donated her old furniture to a charity that helps families in need. She also set up a small foundation to support students who cannot afford school supplies. Although she is old and sometimes seems fragile, her spirit is incredibly strong. When I told her I was frightened about starting high school, she gave me the best advice. She said that every new beginning is scary, but it's also an exciting opportunity. Her generosity extends beyond money; she gives her time and wisdom too.",
        "questions": [
            {"id": 1, "question": "What did the grandmother donate?", "options": ["Money", "Old furniture", "New clothes"], "answer": 1},
            {"id": 2, "question": "What did she set up?", "options": ["A school", "A foundation for students", "A shop"], "answer": 1},
            {"id": 3, "question": "What advice did she give about new beginnings?", "options": ["Avoid them", "They're scary but exciting", "Wait until ready"], "answer": 1}
        ]
    },
    {
        "id": "L78", "day": 78,
        "title": "The Power of Knowledge",
        "text": "Knowledge is the most powerful tool we have. A knowledgeable person can solve problems that seem impossible. In our school library, we have access to thousands of books on every subject. Last week, I read about the internal workings of a computer. The information seemed irrelevant to my daily life at first, but then I realized that understanding technology helps me use it better. My teacher says that good judgment comes from learning about many different topics. She encourages us to read widely and think deeply.",
        "questions": [
            {"id": 1, "question": "What did the speaker read about?", "options": ["Cooking recipes", "Internal workings of a computer", "Sports history"], "answer": 1},
            {"id": 2, "question": "What does good judgment come from?", "options": ["Being older", "Learning about many topics", "Having rich parents"], "answer": 1},
            {"id": 3, "question": "What does the teacher encourage?", "options": ["Reading widely and thinking deeply", "Only studying for exams", "Playing more games"], "answer": 0}
        ]
    },
    {
        "id": "L79", "day": 79,
        "title": "Understanding Different Perspectives",
        "text": "Seeing things from different perspectives is an important skill. In debate class, we practice looking at every issue from multiple sides. Last week, we discussed a phenomenon that many teenagers experience: the pressure to fit in. Some students felt passionate about expressing their opinions, while others preferred to listen first. Our teacher used a plain example to explain: just like a photograph looks different from different angles, every problem has more than one solution. This exercise helped us understand that there is rarely a single right answer.",
        "questions": [
            {"id": 1, "question": "What topic did they discuss in debate class?", "options": ["Climate change", "Pressure to fit in", "School uniforms"], "answer": 1},
            {"id": 2, "question": "What example did the teacher use?", "options": ["A math problem", "A photograph from different angles", "A sports game"], "answer": 1},
            {"id": 3, "question": "What lesson did the exercise teach?", "options": ["There's only one right answer", "Problems have more than one solution", "Debates are boring"], "answer": 1}
        ]
    },
    {
        "id": "L80", "day": 80,
        "title": "The Future of Energy",
        "text": "Solar energy is becoming increasingly popular around the world. Scientists believe that in the future, solar panels could provide most of our electricity. The key is to stimulate more research and investment in clean energy. Some talented young engineers have already created new types of solar panels that are more efficient. They can even summarize complex data to show how much energy each panel produces. The spiritual drive behind this movement is simple: we want to protect our planet for future generations. Clean energy is not just about technology; it's about caring for the Earth.",
        "questions": [
            {"id": 1, "question": "What is becoming increasingly popular?", "options": ["Nuclear energy", "Solar energy", "Coal energy"], "answer": 1},
            {"id": 2, "question": "What have talented young engineers created?", "options": ["New types of cars", "More efficient solar panels", "Better computers"], "answer": 1},
            {"id": 3, "question": "What is the spiritual drive behind clean energy?", "options": ["Making money", "Protecting the planet", "Winning awards"], "answer": 1}
        ]
    }
]

# ===== 完形填空数据 Day 59-80 + Day 26 补缺 =====
new_cloze = [
    # Day 26 补缺
    {
        "id": "C_D26", "day": 26,
        "title": "A Space Dream",
        "text": "My dream is to {1} in space one day. I often read books about {2} and the universe. Scientists have made great {3} in this field. They have sent many {4} into orbit. The latest {5} is truly amazing.",
        "blanks": [
            {"id": 1, "options": ["travel", "trouble", "trust"], "answer": 0},
            {"id": 2, "options": ["exploration", "explanation", "expression"], "answer": 0},
            {"id": 3, "options": ["discoveries", "discussions", "directions"], "answer": 0},
            {"id": 4, "options": ["satellites", "subjects", "systems"], "answer": 0},
            {"id": 5, "options": ["technology", "tradition", "temperature"], "answer": 0}
        ]
    },
    # Day 59
    {
        "id": "C59", "day": 59,
        "title": "Staying Positive",
        "text": "It's important to stay {1} even when things are hard. We should try to {2} stress by doing exercise. A healthy {3} lifestyle helps us feel better. Music can also {4} us to keep going. Small changes can {5} our life greatly.",
        "blanks": [
            {"id": 1, "options": ["positive", "plastic", "physical"], "answer": 0},
            {"id": 2, "options": ["reduce", "replace", "recycle"], "answer": 0},
            {"id": 3, "options": ["physical", "personal", "peaceful"], "answer": 0},
            {"id": 4, "options": ["motivate", "measure", "mention"], "answer": 0},
            {"id": 5, "options": ["improve", "ignore", "include"], "answer": 0}
        ]
    },
    # Day 60
    {
        "id": "C60", "day": 60,
        "title": "Working Together",
        "text": "Finding a good {1} takes teamwork. How pollution {2} our city is a big question. The {3} student can make a difference. Building a strong {4} between people helps us cooperate. Even small efforts bring {5} to our community.",
        "blanks": [
            {"id": 1, "options": ["solution", "situation", "subject"], "answer": 0},
            {"id": 2, "options": ["affects", "affords", "allows"], "answer": 0},
            {"id": 3, "options": ["average", "ancient", "angry"], "answer": 0},
            {"id": 4, "options": ["connection", "collection", "condition"], "answer": 0},
            {"id": 5, "options": ["comfort", "conflict", "control"], "answer": 0}
        ]
    },
    # Day 61
    {
        "id": "C61", "day": 61,
        "title": "Save the Earth",
        "text": "We should {1} paper and plastic to save our planet. Natural {2} are limited and precious. Getting into an {3} about it won't help. Instead, we should build self-{4} by taking action. Even preventing one {5} to nature makes a difference.",
        "blanks": [
            {"id": 1, "options": ["recycle", "refuse", "remove"], "answer": 0},
            {"id": 2, "options": ["resources", "results", "reasons"], "answer": 0},
            {"id": 3, "options": ["argument", "agreement", "adventure"], "answer": 0},
            {"id": 4, "options": ["esteem", "energy", "effort"], "answer": 0},
            {"id": 5, "options": ["injury", "interest", "income"], "answer": 0}
        ]
    },
    # Day 62
    {
        "id": "C62", "day": 62,
        "title": "A Kitchen Experiment",
        "text": "My mom followed a new {1} she found online. She decided to {2} sugar with honey. When I tasted the result, I {3} with a smile. Good food can {4} family bonds. It's also a way to check our health {5}.",
        "blanks": [
            {"id": 1, "options": ["recipe", "record", "report"], "answer": 0},
            {"id": 2, "options": ["replace", "repeat", "require"], "answer": 0},
            {"id": 3, "options": ["responded", "refused", "returned"], "answer": 0},
            {"id": 4, "options": ["strengthen", "struggle", "suggest"], "answer": 0},
            {"id": 5, "options": ["status", "system", "style"], "answer": 0}
        ]
    },
    # Day 63
    {
        "id": "C63", "day": 63,
        "title": "Our Changing Planet",
        "text": "The {1} is getting warmer each year. Many people have a strong {2} to help. The {3} between cities and nature is growing. Some animals may stop to {4} in certain areas. Every {5} of nature needs our protection.",
        "blanks": [
            {"id": 1, "options": ["climate", "culture", "custom"], "answer": 0},
            {"id": 2, "options": ["desire", "design", "demand"], "answer": 0},
            {"id": 3, "options": ["distance", "difference", "direction"], "answer": 0},
            {"id": 4, "options": ["exist", "expect", "express"], "answer": 0},
            {"id": 5, "options": ["function", "fashion", "feature"], "answer": 0}
        ]
    },
    # Day 64
    {
        "id": "C64", "day": 64,
        "title": "Global Connections",
        "text": "A cultural {1} program helps students see the world. We can {2} our knowledge by meeting people from other countries. Every facial {3} tells a story. The feeling of {4} goes away when we make new friends. {5}, more schools are offering these programs.",
        "blanks": [
            {"id": 1, "options": ["exchange", "example", "exercise"], "answer": 0},
            {"id": 2, "options": ["expand", "explain", "explore"], "answer": 0},
            {"id": 3, "options": ["expression", "experience", "experiment"], "answer": 0},
            {"id": 4, "options": ["loneliness", "laziness", "loudness"], "answer": 0},
            {"id": 5, "options": ["Increasingly", "Immediately", "Impossibly"], "answer": 0}
        ]
    },
    # Day 65
    {
        "id": "C65", "day": 65,
        "title": "Beyond the Classroom",
        "text": "Joining {1} activities is a great way to learn. Being {2} helps you grow as a person. You can {3} with students from all grades. One {4} benefit is developing teamwork. Choosing the right {5} in life starts early.",
        "blanks": [
            {"id": 1, "options": ["extracurricular", "extraordinary", "external"], "answer": 0},
            {"id": 2, "options": ["independent", "impossible", "impolite"], "answer": 0},
            {"id": 3, "options": ["interact", "interrupt", "introduce"], "answer": 0},
            {"id": 4, "options": ["major", "minor", "middle"], "answer": 0},
            {"id": 5, "options": ["path", "part", "place"], "answer": 0}
        ]
    },
    # Day 66
    {
        "id": "C66", "day": 66,
        "title": "The Digital World",
        "text": "{1} reality is changing education. Students can {2} information from anywhere. They need to {3} to new technologies quickly. Protecting against cyber {4} is important. We must also reduce our {5} footprint.",
        "blanks": [
            {"id": 1, "options": ["Virtual", "Various", "Valuable"], "answer": 0},
            {"id": 2, "options": ["access", "accept", "achieve"], "answer": 0},
            {"id": 3, "options": ["adapt", "adopt", "admit"], "answer": 0},
            {"id": 4, "options": ["attacks", "actions", "attempts"], "answer": 0},
            {"id": 5, "options": ["carbon", "common", "central"], "answer": 0}
        ]
    },
    # Day 67
    {
        "id": "C67", "day": 67,
        "title": "A Better Approach",
        "text": "How you {1} to a problem matters. Be {2} when making decisions. Sometimes you need to {3} old habits. Don't just {4} at the problem — take action. Having a good {5} helps you succeed.",
        "blanks": [
            {"id": 1, "options": ["react", "refuse", "repeat"], "answer": 0},
            {"id": 2, "options": ["reasonable", "religious", "realistic"], "answer": 0},
            {"id": 3, "options": ["release", "replace", "remain"], "answer": 0},
            {"id": 4, "options": ["stare", "start", "stand"], "answer": 0},
            {"id": 5, "options": ["strategy", "struggle", "structure"], "answer": 0}
        ]
    },
    # Day 68
    {
        "id": "C68", "day": 68,
        "title": "A History Lesson",
        "text": "Understanding key {1} helps us think clearly. One {2} of great leaders is their courage. The {3} of history is complex. In the last {4}, technology has changed a lot. Every period {5} important lessons.",
        "blanks": [
            {"id": 1, "options": ["concepts", "comments", "contests"], "answer": 0},
            {"id": 2, "options": ["characteristic", "celebration", "competition"], "answer": 0},
            {"id": 3, "options": ["concept", "content", "context"], "answer": 0},
            {"id": 4, "options": ["decade", "design", "detail"], "answer": 0},
            {"id": 5, "options": ["contains", "controls", "continues"], "answer": 0}
        ]
    },
    # Day 69
    {
        "id": "C69", "day": 69,
        "title": "Online Life Balance",
        "text": "Social media {1} are everywhere today. Everyone has a {2} for different apps. Our {3} online should be positive. Research in {4} warns us about too much screen time. A good {5} of activities keeps us balanced.",
        "blanks": [
            {"id": 1, "options": ["platforms", "problems", "programs"], "answer": 0},
            {"id": 2, "options": ["preference", "pressure", "promise"], "answer": 0},
            {"id": 3, "options": ["presence", "patience", "purpose"], "answer": 0},
            {"id": 4, "options": ["psychology", "philosophy", "photography"], "answer": 0},
            {"id": 5, "options": ["range", "rate", "role"], "answer": 0}
        ]
    },
    # Day 70
    {
        "id": "C70", "day": 70,
        "title": "School Charity Event",
        "text": "It takes courage to {1} you need help. The results were {2} amazing. Everyone thought the cookies were {3}. Students learned to {4} simple treats. Even small acts of kindness are never a sign of {5}.",
        "blanks": [
            {"id": 1, "options": ["admit", "avoid", "argue"], "answer": 0},
            {"id": 2, "options": ["absolutely", "actually", "already"], "answer": 0},
            {"id": 3, "options": ["awesome", "awful", "awkward"], "answer": 0},
            {"id": 4, "options": ["bake", "break", "bring"], "answer": 0},
            {"id": 5, "options": ["aggression", "agreement", "attention"], "answer": 0}
        ]
    },
    # Day 71
    {
        "id": "C71", "day": 71,
        "title": "Eating Well",
        "text": "The {1} for healthy food is growing. Too much {2} is bad for you. Sugar {3} can cause stomach problems. Don't be {4} by the difficulty of changing habits. The {5} benefits of eating well are huge.",
        "blanks": [
            {"id": 1, "options": ["demand", "design", "detail"], "answer": 0},
            {"id": 2, "options": ["dessert", "dinner", "drink"], "answer": 0},
            {"id": 3, "options": ["discomfort", "discovery", "distance"], "answer": 0},
            {"id": 4, "options": ["discouraged", "disappointed", "disabled"], "answer": 0},
            {"id": 5, "options": ["economic", "electronic", "emotional"], "answer": 0}
        ]
    },
    # Day 72
    {
        "id": "C72", "day": 72,
        "title": "Festival Lights",
        "text": "The {1} in lantern design has been amazing. Workers {2} lights along the streets. Good {3} skills help people cooperate. Beautiful {4} of all sizes light up the night. The {5} of the festival parade is impressive.",
        "blanks": [
            {"id": 1, "options": ["innovation", "invitation", "information"], "answer": 0},
            {"id": 2, "options": ["install", "include", "increase"], "answer": 0},
            {"id": 3, "options": ["interpersonal", "international", "interesting"], "answer": 0},
            {"id": 4, "options": ["lanterns", "letters", "lessons"], "answer": 0},
            {"id": 5, "options": ["length", "level", "limit"], "answer": 0}
        ]
    },
    # Day 73
    {
        "id": "C73", "day": 73,
        "title": "The Road to Excellence",
        "text": "Becoming a {1} takes years of practice. Keeping expectations {2} helps us avoid stress. Listening to music is very {3}. During {4} celebrations, artists often perform. His guitar playing sounds {5} and natural.",
        "blanks": [
            {"id": 1, "options": ["professional", "personal", "practical"], "answer": 0},
            {"id": 2, "options": ["realistic", "random", "regular"], "answer": 0},
            {"id": 3, "options": ["relaxing", "remaining", "removing"], "answer": 0},
            {"id": 4, "options": ["religious", "regular", "remote"], "answer": 0},
            {"id": 5, "options": ["pure", "plain", "poor"], "answer": 0}
        ]
    },
    # Day 74
    {
        "id": "C74", "day": 74,
        "title": "Ocean Guardians",
        "text": "Scientists regularly {1} their research on marine life. The latest {2} of the report shows serious problems. Pollution can {3} ocean ecosystems. Huge {4} are especially at risk. Our minds sometimes {5} to thoughts about the future of our seas.",
        "blanks": [
            {"id": 1, "options": ["update", "upload", "unite"], "answer": 0},
            {"id": 2, "options": ["version", "value", "voice"], "answer": 0},
            {"id": 3, "options": ["weaken", "widen", "wonder"], "answer": 0},
            {"id": 4, "options": ["whales", "waves", "walls"], "answer": 0},
            {"id": 5, "options": ["wander", "wonder", "waste"], "answer": 0}
        ]
    },
    # Day 75
    {
        "id": "C75", "day": 75,
        "title": "Clean Energy Future",
        "text": "A recent {1} in solar technology is exciting. The {2} shows it can save families money. This research is {3} with a top university. The team worked within a tight {4}. Their careful {5} proved the new panels work better.",
        "blanks": [
            {"id": 1, "options": ["breakthrough", "breakdown", "breakout"], "answer": 0},
            {"id": 2, "options": ["calculation", "celebration", "collection"], "answer": 0},
            {"id": 3, "options": ["associated", "abandoned", "absorbed"], "answer": 0},
            {"id": 4, "options": ["budget", "burden", "barrier"], "answer": 0},
            {"id": 5, "options": ["award", "advice", "attempt"], "answer": 0}
        ]
    },
    # Day 76
    {
        "id": "C76", "day": 76,
        "title": "New School Rules",
        "text": "The school {1} now includes practical life skills. The education {2} made this decision. Self-{3} against false information is a new focus. Being {4} is valued by teachers. Students need {5} to face new challenges.",
        "blanks": [
            {"id": 1, "options": ["curriculum", "custom", "culture"], "answer": 0},
            {"id": 2, "options": ["department", "development", "discussion"], "answer": 0},
            {"id": 3, "options": ["defense", "design", "desire"], "answer": 0},
            {"id": 4, "options": ["dependable", "desperate", "different"], "answer": 0},
            {"id": 5, "options": ["determination", "decoration", "destination"], "answer": 0}
        ]
    },
    # Day 77
    {
        "id": "C77", "day": 77,
        "title": "A Kind Heart",
        "text": "The {1} of our school charity is strong. Old {2} can be donated to those in need. Although some things seem {3}, they still have value. Feeling {4} is natural when facing something new. The most {5} gift is your time.",
        "blanks": [
            {"id": 1, "options": ["foundation", "function", "fashion"], "answer": 0},
            {"id": 2, "options": ["furniture", "figures", "flowers"], "answer": 0},
            {"id": 3, "options": ["fragile", "familiar", "formal"], "answer": 0},
            {"id": 4, "options": ["frightened", "frustrated", "forgotten"], "answer": 0},
            {"id": 5, "options": ["generous", "gentle", "genuine"], "answer": 0}
        ]
    },
    # Day 78
    {
        "id": "C78", "day": 78,
        "title": "Seeking Knowledge",
        "text": "Understanding the {1} workings of machines is useful. Some information may seem {2} at first. But good {3} comes from broad learning. Being {4} opens many doors. Even a single {5} move can change the game.",
        "blanks": [
            {"id": 1, "options": ["internal", "important", "immediate"], "answer": 0},
            {"id": 2, "options": ["irrelevant", "interesting", "impossible"], "answer": 0},
            {"id": 3, "options": ["judgment", "journey", "justice"], "answer": 0},
            {"id": 4, "options": ["knowledgeable", "kindhearted", "keen"], "answer": 0},
            {"id": 5, "options": ["logical", "local", "lonely"], "answer": 0}
        ]
    },
    # Day 79
    {
        "id": "C79", "day": 79,
        "title": "Seeing Clearly",
        "text": "Being {1} about a topic helps you speak well. Seeing things from different {2} is a valuable skill. Climate change is a {3} that affects everyone. Sometimes the truth is {4} and simple. Put your ideas on a {5} and share them.",
        "blanks": [
            {"id": 1, "options": ["passionate", "patient", "peaceful"], "answer": 0},
            {"id": 2, "options": ["perspectives", "positions", "purposes"], "answer": 0},
            {"id": 3, "options": ["phenomenon", "philosophy", "photograph"], "answer": 0},
            {"id": 4, "options": ["plain", "pleasant", "precious"], "answer": 0},
            {"id": 5, "options": ["plate", "place", "page"], "answer": 0}
        ]
    },
    # Day 80
    {
        "id": "C80", "day": 80,
        "title": "Energy for Tomorrow",
        "text": "{1} energy from the sun is clean and free. We need to {2} more research in this area. Many {3} engineers are working on it. They can {4} data to show progress. The {5} drive to save our planet inspires us all.",
        "blanks": [
            {"id": 1, "options": ["Solar", "Social", "Simple"], "answer": 0},
            {"id": 2, "options": ["stimulate", "struggle", "suggest"], "answer": 0},
            {"id": 3, "options": ["talented", "terrible", "typical"], "answer": 0},
            {"id": 4, "options": ["summarize", "separate", "support"], "answer": 0},
            {"id": 5, "options": ["spiritual", "special", "standard"], "answer": 0}
        ]
    }
]

if __name__ == "__main__":
    added_l = append_json('listening_data.json', new_listening)
    added_c = append_json('cloze_data.json', new_cloze)
    print(f"✅ 成功添加 {added_l} 天听力数据 和 {added_c} 天完形填空数据！")

    # 验证覆盖范围
    import json
    with open('listening_data.json') as f:
        l_data = json.load(f)
    with open('cloze_data.json') as f:
        c_data = json.load(f)

    l_days = sorted(set(d['day'] for d in l_data))
    c_days = sorted(set(d['day'] for d in c_data))

    print(f"\n📊 听力数据覆盖: Day {l_days[0]} - Day {l_days[-1]}，共 {len(l_days)} 天")
    print(f"📊 完形数据覆盖: Day {c_days[0]} - Day {c_days[-1]}，共 {len(c_days)} 天")

    # 检查缺口
    l_missing = [d for d in range(1, max(l_days)+1) if d not in l_days]
    c_missing = [d for d in range(1, max(c_days)+1) if d not in c_days]
    if l_missing:
        print(f"⚠️ 听力缺失天数: {l_missing}")
    else:
        print("✅ 听力无缺口")
    if c_missing:
        print(f"⚠️ 完形缺失天数: {c_missing}")
    else:
        print("✅ 完形无缺口")
