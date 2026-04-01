import json
import os

# New Listening Data (Day 36-40)
new_listening = [
    {
        "id": "L36",
        "day": 36,
        "title": "The Impact of Technology",
        "text": "Technology has changed our lives in many ways. In the past, people wrote letters to keep in touch with friends and family. It often took several days or even weeks for a letter to arrive. Nowadays, we can send messages and make video calls instantly using smartphones and the Internet. However, technology also brings some challenges. For example, some people spend too much time on their phones and forget to talk to those around them. We should learn to use technology wisely. It is important to find a balance between the digital world and real life. Technology should be a tool to help us, not something that controls us.",
        "questions": [
            {
                "id": 1,
                "question": "How did people keep in touch in the past?",
                "options": ["By making video calls", "By writing letters", "By using smartphones"],
                "answer": 1
            },
            {
                "id": 2,
                "question": "What is a challenge brought by technology?",
                "options": ["It is too expensive", "People spend too much time on phones", "It is hard to learn"],
                "answer": 1
            },
            {
                "id": 3,
                "question": "What does the speaker think about technology?",
                "options": ["It's better to live without it", "It should control our lives", "It should be used wisely as a tool"],
                "answer": 2
            }
        ]
    },
    {
        "id": "L37",
        "day": 37,
        "title": "Environmental Volunteering",
        "text": "Last Saturday, a group of students from our school joined a volunteering activity at the local park. Our goal was to clean up the trash and plant more flowers. We were divided into small teams. Some students picked up plastic bottles and paper on the grass, while others watered the newly planted trees. Our teacher, Mr. Smith, told us that small actions can make a big difference to our environment. By the end of the afternoon, the park looked much cleaner and more beautiful. We felt tired but very happy. This experience taught us the importance of protecting nature and working together for a common goal. We plan to do this once a month.",
        "questions": [
            {
                "id": 1,
                "question": "What was the main goal of the activity?",
                "options": ["To play games", "To clean the park and plant flowers", "To have a picnic"],
                "answer": 1
            },
            {
                "id": 2,
                "question": "What did students do during the activity?",
                "options": ["Built a new playground", "Watered trees and picked up trash", "Sold flowers"],
                "answer": 1
            },
            {
                "id": 3,
                "question": "How often do they plan to do this again?",
                "options": ["Once a week", "Once a month", "Once a year"],
                "answer": 1
            }
        ]
    },
    {
        "id": "L38",
        "day": 38,
        "title": "A Story of Thomas Edison",
        "text": "Thomas Edison was one of the greatest inventors in history. He is most famous for inventing the light bulb, but he actually failed many times before he succeeded. It is said that he tried over a thousand materials for the filament before finding the right one. When people asked him why he didn't give up, he replied that he hadn't failed; he had just found a thousand ways that didn't work. His story teaches us that persistence and hard work are essential for success. Edison also invented many other things, like the phonograph and the motion picture camera. He once said that genius is one percent inspiration and ninety-nine percent perspiration.",
        "questions": [
            {
                "id": 1,
                "question": "What is Edison most famous for?",
                "options": ["The airplane", "The light bulb", "The telephone"],
                "answer": 1
            },
            {
                "id": 2,
                "question": "How did Edison feel about his failures?",
                "options": ["He was very disappointed", "He saw them as ways that didn't work", "He decided to stop"],
                "answer": 1
            },
            {
                "id": 3,
                "question": "According to Edison, what is genius mainly made of?",
                "options": ["Inspiration", "Perspiration (hard work)", "Luck"],
                "answer": 1
            }
        ]
    },
    {
        "id": "L39",
        "day": 39,
        "title": "Future Career Planning",
        "text": "Choosing a career is one of the most important decisions in life. When I was younger, I wanted to be an astronaut. However, as I grew up, I realized that I am more interested in medicine. My dream now is to become a doctor. To achieve this goal, I need to study hard, especially in science subjects like biology and chemistry. I also plan to volunteer at a hospital during my summer vacation to learn more about how doctors help people. Being a doctor requires not only medical knowledge but also a kind heart and patience. I know the path will be difficult, but I am determined to work hard and make my dream come true.",
        "questions": [
            {
                "id": 1,
                "question": "What did the speaker want to be when he was younger?",
                "options": ["A doctor", "An astronaut", "A teacher"],
                "answer": 1
            },
            {
                "id": 2,
                "question": "What subjects does he need to study hard?",
                "options": ["Math and Art", "History and Geography", "Biology and Chemistry"],
                "answer": 2
            },
            {
                "id": 3,
                "question": "What quality does he think a doctor should have?",
                "options": ["A funny character", "A kind heart and patience", "A lot of money"],
                "answer": 1
            }
        ]
    },
    {
        "id": "L40",
        "day": 40,
        "title": "A New Friendship",
        "text": "Last semester, a new student named Anna joined our class. She was from Italy and didn't speak much Chinese at first. She seemed quite shy and sat alone during breaks. I decided to talk to her and help her get used to the new environment. I introduced her to my friends and invited her to join our English club. We soon discovered that we both love painting and dancing. Anna's Chinese improved quickly with our help, and she taught us some Italian words. Making friends with Anna taught me that language is not a barrier when people are kind and have common interests. I'm glad that I reached out to her.",
        "questions": [
            {
                "id": 1,
                "question": "Where was Anna from?",
                "options": ["USA", "Italy", "France"],
                "answer": 1
            },
            {
                "id": 2,
                "question": "What common interests do they share?",
                "options": ["Cooking and reading", "Painting and dancing", "Sports and music"],
                "answer": 1
            },
            {
                "id": 3,
                "question": "What did the speaker learn from this experience?",
                "options": ["Italian is hard to learn", "Language is not a barrier for friendship", "It is better to be shy"],
                "answer": 1
            }
        ]
    }
]

# New Cloze Data (Day 36-40)
new_cloze = [
    {
        "id": "C36",
        "day": 36,
        "title": "Digital Life",
        "text": "Nowadays, technology {1} every part of our lives. We use smartphones to {2} with friends and find {3} easily. Although it's very {4}, we shouldn't spend too much time online. Real communication is more {5} than virtual messages.",
        "blanks": [
            {"id": 1, "options": ["affects", "appears", "agrees"], "answer": 0},
            {"id": 2, "options": ["communicate", "consider", "control"], "answer": 0},
            {"id": 3, "options": ["information", "instruction", "instrument"], "answer": 0},
            {"id": 4, "options": ["convenient", "common", "certain"], "answer": 0},
            {"id": 5, "options": ["important", "impossible", "interesting"], "answer": 0}
        ]
    },
    {
        "id": "C37",
        "day": 37,
        "title": "Protecting Nature",
        "text": "Our environment is in {1} because of pollution. We must take {2} to protect the Earth. For example, we should {3} water and reduce waste. Everyone should be a {4} to help the community. Small efforts will {5} to a better future.",
        "blanks": [
            {"id": 1, "options": ["danger", "doubt", "distance"], "answer": 0},
            {"id": 2, "options": ["action", "advice", "attention"], "answer": 0},
            {"id": 3, "options": ["save", "spend", "share"], "answer": 0},
            {"id": 4, "options": ["volunteer", "visitor", "villager"], "answer": 0},
            {"id": 5, "options": ["lead", "leave", "look"], "answer": 0}
        ]
    },
    {
        "id": "C38",
        "day": 38,
        "title": "A Great Inventor",
        "text": "Edison was a famous {1}. He showed that {2} is very important for success. Even if you {3} many times, you shouldn't {4}. His hard work has {5} the whole world.",
        "blanks": [
            {"id": 1, "options": ["inventor", "instrument", "information"], "answer": 0},
            {"id": 2, "options": ["persistence", "pressure", "poverty"], "answer": 0},
            {"id": 3, "options": ["fail", "follow", "forget"], "answer": 0},
            {"id": 4, "options": ["give up", "get up", "grow up"], "answer": 0},
            {"id": 5, "options": ["changed", "closed", "called"], "answer": 0}
        ]
    },
    {
        "id": "C39",
        "day": 39,
        "title": "Career Choice",
        "text": "It is {1} to choose a suitable career. You should {2} your interests and skills. If you want to be a doctor, you need to study {3} hard. Don't be afraid of the {4} path. Success {5} on your determination.",
        "blanks": [
            {"id": 1, "options": ["essential", "excellent", "empty"], "answer": 0},
            {"id": 2, "options": ["consider", "control", "call"], "answer": 0},
            {"id": 3, "options": ["science", "subject", "service"], "answer": 0},
            {"id": 4, "options": ["difficult", "different", "dangerous"], "answer": 0},
            {"id": 5, "options": ["depends", "decides", "discusses"], "answer": 0}
        ]
    },
    {
        "id": "C40",
        "day": 40,
        "title": "True Friendship",
        "text": "A good friend will {1} you when you're in trouble. You should share your {2} with them. True friendship is {3} on trust and support. It is more {4} than money. We should {5} our friends carefully.",
        "blanks": [
            {"id": 1, "options": ["help", "hurt", "hire"], "answer": 0},
            {"id": 2, "options": ["feelings", "failures", "forces"], "answer": 0},
            {"id": 3, "options": ["based", "built", "broken"], "answer": 0},
            {"id": 4, "options": ["valuable", "various", "visible"], "answer": 0},
            {"id": 5, "options": ["choose", "catch", "change"], "answer": 0}
        ]
    }
]

def append_data(filepath, new_items):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Ensure no duplicates
    existing_days = {item['day'] for item in data}
    filtered_new = [item for item in new_items if item['day'] not in existing_days]
    
    data.extend(filtered_new)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return len(filtered_new)

if __name__ == "__main__":
    added_l = append_data('listening_data.json', new_listening)
    added_c = append_data('cloze_data.json', new_cloze)
    print(f"Successfully added {added_l} listening days and {added_c} cloze days!")
