import json
import os

def append_json(filepath, new_items):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    existing_days = {item['day'] for item in data}
    filtered_new = [item for item in new_items if item['day'] not in existing_days]
    data.extend(filtered_new)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return len(filtered_new)

def append_md(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("\n\n" + content)

# --- DATA GENERATION ---
# Days 54-58
new_listening = [
    {
        "id": "L54", "day": 54, "title": "Chinese Festivals",
        "text": "The Spring Festival is the most important traditional festival in China. During this time, families get together for a big dinner. We eat dumplings and set off fireworks. Children are always excited because they receive red envelopes with money. Nowadays, some traditions are changing. For example, people send digital red envelopes through their phones. Although modern life is fast, these festivals remind us of our history and family values. We should pass these traditions on to the next generation.",
        "questions": [
            {"id": 1, "question": "What do people eat during Spring Festival?", "options": ["Pizza", "Dumplings", "Bread"], "answer": 1},
            {"id": 2, "question": "Why are children excited?", "options": ["They have no homework", "They receive red envelopes", "They go to school"], "answer": 1},
            {"id": 3, "question": "What is changing about red envelopes?", "options": ["They are becoming larger", "People send digital ones", "They are no longer given"], "answer": 1}
        ]
    },
    {
        "id": "L55", "day": 55, "title": "The Spirit of Sports",
        "text": "Basketball is very popular among teenagers. It's not just about winning; it's about teamwork and persistence. When our team lost the game last week, we felt sad. But our coach told us that failure is a part of growth. We practiced harder and focused on our cooperation. In the next match, we played much better together and finally won. Sports teach us how to face challenges and support each other. Whether we win or lose, the spirit of never giving up is what matters most.",
        "questions": [
            {"id": 1, "question": "What is basketball mainly about according to the text?", "options": ["Just winning", "Teamwork and persistence", "Individual skills"], "answer": 1},
            {"id": 2, "question": "How did the team react to their loss?", "options": ["They gave up", "They practiced harder", "They blamed the coach"], "answer": 1},
            {"id": 3, "question": "What is the most important thing in sports?", "options": ["The trophy", "The spirit of never giving up", "Being famous"], "answer": 1}
        ]
    },
    {
        "id": "L56", "day": 56, "title": "Online Safety",
        "text": "The internet is a wonderful tool, but it also has risks. Many students spend hours on social media sharing their daily lives. We should be careful about our privacy. Never share your password or home address with strangers online. Also, we should be polite when posting comments. Cyberbullying can hurt people's feelings deeply. If you see something that makes you uncomfortable, tell your parents or teachers. Let's work together to create a safe and friendly online environment.",
        "questions": [
            {"id": 1, "question": "What should we be careful about on social media?", "options": ["Privacy", "Making friends", "Reading news"], "answer": 0},
            {"id": 2, "question": "What should you never share with strangers?", "options": ["Your favorite food", "Your password", "Your hobbies"], "answer": 1},
            {"id": 3, "question": "Who should you talk to if you feel uncomfortable online?", "options": ["Strangers", "Parents or teachers", "No one"], "answer": 1}
        ]
    },
    {
        "id": "L57", "day": 57, "title": "The Power of Art",
        "text": "Visiting an art gallery can be a relaxing experience. Art comes in many forms, such as painting, sculpture, and photography. It allows us to express our emotions and see the world from different perspectives. Last month, I visited a modern art exhibition. I was amazed by how the artists used bright colors to show happiness. You don't have to be a professional to enjoy art. Everyone can pick up a brush and start creating. Art enriches our souls and makes our lives more colorful.",
        "questions": [
            {"id": 1, "question": "What forms of art are mentioned?", "options": ["Singing and dancing", "Painting and sculpture", "Cooking and gardening"], "answer": 1},
            {"id": 2, "question": "What was the speaker amazed by at the exhibition?", "options": ["The price of the art", "The use of bright colors", "The size of the building"], "answer": 1},
            {"id": 3, "question": "Can anyone enjoy art?", "options": ["Only professionals", "Yes, everyone", "Only rich people"], "answer": 1}
        ]
    },
    {
        "id": "L58", "day": 58, "title": "Life on Mars?",
        "text": "Scientists have been exploring Mars for decades. They want to know if there was ever life on the Red Planet. Robots like 'Perseverance' are sent to collect soil samples. Although Mars is very cold and has no liquid water on the surface, some believe that humans might live there in the future. Imagine a city inside a giant glass dome! It sounds like a science fiction movie, but with the development of technology, it might come true one day. Space exploration helps us understand our place in the universe.",
        "questions": [
            {"id": 1, "question": "What are scientists looking for on Mars?", "options": ["Gold", "Signs of life", "Alien spaceships"], "answer": 1},
            {"id": 2, "question": "What is the environment of Mars like?", "options": ["Hot and rainy", "Very cold", "Full of oceans"], "answer": 1},
            {"id": 3, "question": "How might humans live on Mars in the future?", "options": ["In tents", "Inside glass domes", "Underground"], "answer": 1}
        ]
    }
]

new_cloze = [
    {
        "id": "C54", "day": 54, "title": "Tradition and Change",
        "text": "Traditional festivals are very {1} in China. During Spring Festival, families gather {2} to enjoy a big meal. We eat dumplings and {3} red envelopes. Although life is changing {4}, we should still {5} our culture.",
        "blanks": [
            {"id": 1, "options": ["important", "impossible", "impolite"], "answer": 0},
            {"id": 2, "options": ["together", "towards", "twice"], "answer": 0},
            {"id": 3, "options": ["receive", "refuse", "repeat"], "answer": 0},
            {"id": 4, "options": ["rapidly", "rarely", "roughly"], "answer": 0},
            {"id": 5, "options": ["respect", "remove", "replace"], "answer": 0}
        ]
    },
    {
        "id": "C55", "day": 55, "title": "Team Effort",
        "text": "Sports are more than just {1}. They teach us how to {2} with others. Even if we {3} a match, we should keep a positive {4}. Persistence and hard work will {5} to success eventually.",
        "blanks": [
            {"id": 1, "options": ["games", "goals", "gifts"], "answer": 0},
            {"id": 2, "options": ["cooperate", "compete", "complain"], "answer": 0},
            {"id": 3, "options": ["lose", "lack", "leave"], "answer": 0},
            {"id": 4, "options": ["attitude", "ability", "action"], "answer": 0},
            {"id": 5, "options": ["lead", "last", "look"], "answer": 0}
        ]
    },
    {
        "id": "C56", "day": 56, "title": "Internet Manners",
        "text": "When we use the internet, we should {1} our privacy. Don't tell your {2} to anyone. We must also be {3} when talking to others online. Cyberbullying is a serious {4}. Let's make the web a {5} place for everyone.",
        "blanks": [
            {"id": 1, "options": ["protect", "provide", "produce"], "answer": 0},
            {"id": 2, "options": ["password", "payment", "project"], "answer": 0},
            {"id": 3, "options": ["kind", "keen", "knowing"], "answer": 0},
            {"id": 4, "options": ["problem", "process", "program"], "answer": 0},
            {"id": 5, "options": ["safer", "slower", "smaller"], "answer": 0}
        ]
    },
    {
        "id": "C57", "day": 57, "title": "Creative Art",
        "text": "Art is a way to {1} our feelings. Some people like {2} while others prefer music. It helps us see the {3} in life. You can try to {4} something new every day. Creativity is a {5} that everyone has.",
        "blanks": [
            {"id": 1, "options": ["express", "expect", "explain"], "answer": 0},
            {"id": 2, "options": ["painting", "parking", "playing"], "answer": 0},
            {"id": 3, "options": ["beauty", "break", "belief"], "answer": 0},
            {"id": 4, "options": ["create", "catch", "choose"], "answer": 0},
            {"id": 5, "options": ["talent", "target", "title"], "answer": 0}
        ]
    },
    {
        "id": "C58", "day": 58, "title": "Space Travel",
        "text": "Many people {1} of traveling to space. Scientists are {2} Mars to see if we can live there. Technology is {3} very fast. In the future, we might {4} cities on other planets. The universe is full of {5}.",
        "blanks": [
            {"id": 1, "options": ["dream", "doubt", "decide"], "answer": 0},
            {"id": 2, "options": ["exploring", "entering", "expecting"], "answer": 0},
            {"id": 3, "options": ["developing", "describing", "depending"], "answer": 0},
            {"id": 4, "options": ["build", "borrow", "break"], "answer": 0},
            {"id": 5, "options": ["mysteries", "mistakes", "members"], "answer": 0}
        ]
    }
]

vocab_md = """
### Day 54: 传统文化与现代生活 (Traditional Culture & Modern Life)

1. **tradition** - 传统
    * *The Spring Festival is a Chinese **tradition**.* (春节是中国的传统。)
2. **festival** - 节日
    * *What's your favorite **festival**?* (你最喜欢的节日是什么？)
3. **culture** - 文化
    * *Learning a language is learning its **culture**.* (学习语言就是学习它的文化。)
4. **generation** - 一代人
    * *This story has been told for **generations**.* (这个故事已经被传颂了几代人。)
5. **custom** - 习俗
    * *It's a **custom** to eat dumplings on New Year's Eve.* (除夕吃饺子是一种习俗。)
6. **celebrate** - 庆祝
    * *How do you **celebrate** your birthday?* (你如何庆祝你的生日？)
7. **value** - 价值观；价值
    * *Family **values** are very important to us.* (家庭价值观对我们非常重要。)
8. **symbol** - 象征
    * *The dragon is a **symbol** of China.* (龙是中国的象征。)
9. **modern** - 现代的
    * ***Modern** life is fast and busy.* (现代生活既快又忙碌。)
10. **ancient** - 古老的
    * *China has an **ancient** history.* (中国有古老的历史。)
11. **gather** - 聚集
    * *The whole family **gathers** together for dinner.* (全家人聚在一起吃晚饭。)
12. **remind** - 提醒
    * *The photos **remind** me of my childhood.* (这些照片让我想起了我的童年。)
13. **heritage** - 遗产
    * *The Great Wall is a world cultural **heritage**.* (长城是世界文化遗产。)
14. **envelope** - 信封
    * *I received a red **envelope** from my grandma.* (我收到了奶奶给的一个红包。)
15. **digital** - 数字的
    * *We live in a **digital** age.* (我们生活在数字时代。)
16. **respect** - 尊重
    * *We should **respect** the elderly.* (我们应该尊重老人。)
17. **represent** - 代表
    * *The stars on the flag **represent** the states.* (旗上的星星代表州。)
18. **influence** - 影响
    * *Music has a great **influence** on people.* (音乐对人有很大的影响。)
19. **preserve** - 保护；保存
    * *We must **preserve** traditional arts.* (我们必须保护传统艺术。)
20. **meaningful** - 有意义的
    * *Volunteering is a **meaningful** activity.* (志愿者活动是一项有意义的活动。)

### Day 55: 体育竞技与团队协作 (Sports & Teamwork)

1. **sport** - 体育运动
    * *Football is a popular **sport**.* (足球是一项受欢迎的运动。)
2. **teamwork** - 团队协作
    * *Success depends on **teamwork**.* (成功取决于团队协作。)
3. **cooperate** - 合作
    * *We need to **cooperate** to finish the project.* (我们需要合作完成这个项目。)
4. **match** - 比赛
    * *Did you watch the football **match**?* (你看足球比赛了吗？)
5. **coach** - 教练
    * *The **coach** trained the team very hard.* (教练对队伍训练得非常刻苦。)
6. **athlete** - 运动员
    * *He is a professional **athlete**.* (他是一名职业运动员。)
7. **competition** - 竞赛
    * *I entered a speech **competition**.* (我参加了一个演讲比赛。)
8. **spirit** - 精神
    * *The Olympic **spirit** is about friendship.* (奥运精神关乎友谊。)
9. **score** - 得分
    * *What's the final **score** of the game?* (比赛的最终比分是多少？)
10. **victory** - 胜利
    * *The team celebrated their **victory**.* (队伍庆祝了他们的胜利。)
11. **defeat** - 打败；失败
    * *Don't be afraid of **defeat**.* (不要害怕失败。)
12. **training** - 训练
    * ***Training** is necessary for improvement.* (为了进步，训练是必要的。)
13. **persistent** - 坚持不懈的
    * *Be **persistent**, and you will win.* (坚持不懈，你就会赢。)
14. **stadium** - 体育场
    * *The **stadium** was full of fans.* (体育场里坐满了歌迷。)
15. **championship** - 冠军赛
    * *They won the world **championship**.* (他们赢得了世界冠军。)
16. **practice** - 练习
    * ***Practice** makes perfect.* (熟能生巧。)
17. **cooperation** - 合作
    * *Good **cooperation** leads to success.* (良好的合作导向成功。)
18. **challenge** - 挑战
    * *Facing a **challenge** is part of sports.* (面对挑战是体育的一部分。)
19. **support** - 支持
    * *We should **support** each other.* (我们应该互相支持。)
20. **fair** - 公平的
    * *The game must be **fair** for everyone.* (比赛对每个人都必须公平。)

### Day 56: 社交媒体与人际关系 (Social Media & Relationships)

1. **internet** - 互联网
    * *The **internet** has changed the world.* (互联网改变了世界。)
2. **media** - 媒体
    * *Social **media** is very popular now.* (社交媒体现在非常流行。)
3. **online** - 在线的
    * *I enjoy shopping **online**.* (我喜欢网上购物。)
4. **privacy** - 隐私
    * *Protect your **privacy** when using the web.* (使用网络时保护你的隐私。)
5. **password** - 密码
    * *Never share your **password** with others.* (永远不要把密码告诉别人。)
6. **privacy** - 隐私
    * *Protect your **privacy**.* (保护你的隐私。)
7. **comment** - 评论
    * *Please leave a **comment** below.* (请在下方留下评论。)
8. **share** - 分享
    * *Feel free to **share** your ideas.* (尽管分享你的想法。)
9. **stranger** - 陌生人
    * *Don't talk to **strangers** online.* (不要在网上和陌生人聊天。)
10. **polite** - 有礼貌的
    * *Be **polite** when you post online.* (上网发布内容时要有礼貌。)
11. **cyberbullying** - 网络欺凌
    * ***Cyberbullying** can hurt people deeply.* (网络欺凌会深深伤害人。)
12. **uncomfortable** - 不舒服的
    * *Tell someone if you feel **uncomfortable**.* (如果你感到不舒服，告诉别人。)
13. **risk** - 风险
    * *Everything has a certain **risk**.* (凡事都有一定的风险。)
14. **relationship** - 关系
    * *Good communication builds a strong **relationship**.* (良好的沟通建立牢固的关系。)
15. **connected** - 连接的
    * *We are all **connected** by technology.* (我们都被科技连接在一起。)
16. **platform** - 平台
    * *Which social **platform** do you use most?* (你最常用哪个社交平台？)
17. **profile** - 个人资料
    * *Update your **profile** picture.* (更新你的个人资料照片。)
18. **community** - 社区
    * *Join our online learning **community**.* (加入我们的在线学习社区。)
19. **interact** - 互动
    * *Social media lets us **interact** with fans.* (社交媒体让我们能与粉丝互动。)
20. **safety** - 安全
    * *Online **safety** is very important.* (网络安全非常重要。)

### Day 57: 艺术欣赏与创造力 (Art Appreciation & Creativity)

1. **art** - 艺术
    * ***Art** is everywhere in our life.* (艺术在我们的生活中无处不在。)
2. **gallery** - 美术馆
    * *We visited an art **gallery** last week.* (上周我们参观了一个美术馆。)
3. **sculpture** - 雕塑
    * *The **sculpture** is made of stone.* (这个雕塑是用石头做的。)
4. **photography** - 摄影
    * ***Photography** is a popular hobby.* (摄影是一个受欢迎的爱好。)
5. **exhibition** - 展览
    * *The museum is holding an **exhibition**.* (博物馆正在举办一场展览。)
6. **creative** - 有创造力的
    * *She is a very **creative** student.* (她是一个非常有创造力的学生。)
7. **creativity** - 创造力
    * ***Creativity** is important for solving problems.* (创造力对于解决问题很重要。)
8. **perspective** - 视角
    * *Art gives us a new **perspective**.* (艺术给了我们一个新的视角。)
9. **emotion** - 情感
    * *Music can express deep **emotions**.* (音乐可以表达深层的情感。)
10. **expression** - 表达
    * *Drawing is a form of self-**expression**.* (绘画是一种自我表达的形式。)
11. **bright** - 明亮的
    * *The artist used **bright** colors.* (艺术家使用了鲜艳的颜色。)
12. **amazed** - 惊讶的
    * *I was **amazed** by the beautiful painting.* (我被那幅美丽的画惊呆了。)
13. **relaxing** - 令人放松的
    * *Listening to music is **relaxing**.* (听音乐很放松。)
14. **colorful** - 色彩丰富的
    * *Life should be **colorful** and fun.* (生活应该是丰富多彩且有趣的。)
15. **masterpiece** - 杰作
    * *The Mona Lisa is a famous **masterpiece**.* (《蒙娜丽莎》是一件著名的杰作。)
16. **brush** - 画笔
    * *Pick up your **brush** and start painting.* (拿起你的画笔，开始画画。)
17. **inspire** - 启发
    * *Nature **inspires** many artists.* (大自然启发了许多艺术家。)
18. **imagination** - 想象力
    * *Use your **imagination** to write a story.* (发挥你的想象力写一个故事。)
19. **appreciate** - 欣赏
    * *We should learn to **appreciate** art.* (我们应该学会欣赏艺术。)
20. **enrich** - 使充实；使丰富
    * *Reading **enriches** our knowledge.* (阅读丰富了我们的知识。)

### Day 58: 宇宙探索与科学幻想 (Space Exploration & Science Fiction)

1. **space** - 太空
    * ***Space** travel is no longer a dream.* (太空旅行不再是梦想。)
2. **exploration** - 探索
    * ***Exploration** is part of human nature.* (探索是人类天性的一部分。)
3. **universe** - 宇宙
    * *The **universe** is huge and mysterious.* (宇宙巨大而神秘。)
4. **planet** - 行星
    * *Mars is often called the Red **Planet**.* (火星常被称为红色的行星。)
5. **scientist** - 科学家
    * ***Scientists** are searching for life on Mars.* (科学家们正在火星上寻找生命。)
6. **robot** - 机器人
    * *The **robot** was sent to collect rocks.* (机器人被派去收集石头。)
7. **sample** - 样本
    * *The soil **sample** was tested in the lab.* (土壤样本在实验室里接受了测试。)
8. **surface** - 表面
    * *The **surface** of the Moon is dry.* (月球表面很干燥。)
9. **liquid** - 液体的
    * *There is no **liquid** water on Mars.* (火星上没有液态水。)
10. **future** - 未来
    * *The **future** belongs to the young.* (未来属于年轻人。)
11. **technology** - 科技
    * ***Technology** makes our life easier.* (科技使我们的生活更简单。)
12. **fiction** - 小说；虚构
    * *I love reading science **fiction**.* (我喜欢读科幻小说。)
13. **imagine** - 想象
    * ***Imagine** living on another planet!* (想象一下住在另一个行星上！)
14. **dome** - 圆顶
    * *They live inside a glass **dome**.* (他们住在一个玻璃圆顶里。)
15. **discover** - 发现
    * *When was America **discovered**?* (美洲是什么时候被发现的？)
16. **mystery** - 神秘事物
    * *The ocean is full of **mysteries**.* (海洋充满了神秘。)
17. **astronaut** - 宇航员
    * *He wants to be an **astronaut**.* (他想成为一名宇航员。)
18. **rocket** - 火箭
    * *The **rocket** was launched last night.* (火箭昨晚发射了。)
19. **alien** - 外星人
    * *Do you believe in **aliens**?* (你相信有外星人吗？)
20. **mission** - 任务
    * *The **mission** to Mars was successful.* (火星任务获得了成功。)
"""

if __name__ == "__main__":
    added_l = append_json('listening_data.json', new_listening)
    added_c = append_json('cloze_data.json', new_cloze)
    append_md('beijing_zhongkao_vocab_21days.md', vocab_md)
    print(f"Successfully added {added_l} listening days and {added_c} cloze days and vocab data!")
