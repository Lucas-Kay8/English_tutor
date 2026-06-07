# -*- coding: utf-8 -*-
import os

# 精心设计 Day 81 到 Day 100 的 200 个高频纲外提升词汇（每天 10 个）
extend_vocab = {
    81: {
        "title": "科技前沿与智能时代 (Smart Tech)",
        "words": [
            ("concept", "[ˈkɒnsept]", "n.概念；观念", 3, "Understanding the concept of AI is essential for the future.", "理解人工智能的概念对未来至关重要。"),
            ("digital", "[ˈdɪdʒɪtl]", "adj.数字的；数码的", 3, "We are living in a fast-growing digital era.", "我们生活在一个快速发展的数字时代。"),
            ("device", "[dɪˈvaɪs]", "n.设备；仪器", 3, "Smart devices make our daily lives much easier.", "智能设备让我们的日常生活变得更加便利。"),
            ("network", "[ˈnetwɜːk]", "n.网络；网状系统", 3, "The school has built a secure local network for students.", "学校为学生建立了一个安全的本地网络。"),
            ("security", "[sɪˈkjʊərəti]", "n.安全；保护", 3, "We must pay high attention to personal information security.", "我们必须高度重视个人信息安全。"),
            ("access", "[ˈækses]", "v./n.使用；获取；通道", 3, "All students have free access to the online library.", "所有学生都可以免费使用在线图书馆。"),
            ("innovation", "[ˌɪnəˈveɪʃn]", "n.创新；革新", 3, "Scientific innovation is the key to social progress.", "科技创新是社会进步的关键。"),
            ("automatic", "[ˌɔːtəˈmætɪk]", "adj.自动的", 2, "The automatic door opens when you stand close to it.", "当你靠近时，自动门就会打开。"),
            ("intelligence", "[ɪnˈtelɪdʒəns]", "n.智力；智慧", 3, "Artificial intelligence is changing the way we learn.", "人工智能正在改变我们学习的方式。"),
            ("efficient", "[ɪˈfɪʃnt]", "adj.高效的", 3, "Developing efficient habits helps us save precious time.", "养成高效的习惯有助于我们节省宝贵的时间。")
        ]
    },
    82: {
        "title": "环境保护与低碳生活 (Green Living)",
        "words": [
            ("climate", "[ˈklaɪmət]", "n.气候", 3, "Global warming has caused major changes in the world climate.", "全球变暖已导致世界气候发生重大变化。"),
            ("pollution", "[pəˈluːʃn]", "n.污染", 3, "Plastic pollution is a big threat to ocean creatures.", "塑料污染是对海洋生物的一大威胁。"),
            ("recycle", "[ˌriːˈsaɪkl]", "v.回收；循环利用", 3, "We should learn how to recycle paper and plastic bottles.", "我们应该学会如何回收纸张和塑料瓶。"),
            ("resource", "[rɪˈsɔːs]", "n.资源", 3, "Water is a vital natural resource that we must protect.", "水是人类必须保护的重要自然资源。"),
            ("preserve", "[prɪˈzɜːv]", "v.保护；保存", 3, "It is our duty to preserve wild animals and their homes.", "保护野生动物及其家园是我们的职责。"),
            ("renewable", "[rɪˈnjuːəbl]", "adj.可再生的", 3, "Solar energy is a clean and renewable power resource.", "太阳能是一种清洁、可再生的动力资源。"),
            ("sustainable", "[səˈsteɪnəbl]", "adj.可持续的", 2, "Green travel is a key step towards sustainable living.", "绿色出行是迈向可持续生活方式的关键一步。"),
            ("eco-friendly", "[ˈiːkəʊˌfrendli]", "adj.环保的", 3, "Using eco-friendly shopping bags can reduce waste.", "使用环保购物袋可以减少垃圾。"),
            ("harmony", "[ˈhɑːməni]", "n.和谐；融洽", 2, "Humans should live in perfect harmony with nature.", "人类应当与大自然和谐共处。"),
            ("consumption", "[kənˈsʌmpʃn]", "n.消耗；消耗量", 2, "Reducing energy consumption is essential to combat warming.", "降低能耗对应对全球变暖至关重要。")
        ]
    },
    83: {
        "title": "心理健康与自我管理 (Mind & Will)",
        "words": [
            ("attitude", "[ˈætɪtjuːd]", "n.态度；看法", 3, "A positive attitude can help us overcome daily challenges.", "积极的态度可以帮助我们战胜日常的挑战。"),
            ("pressure", "[ˈpreʃə(r)]", "n.压力；挤压", 3, "Doing sports is a great way to relieve exam pressure.", "做运动是缓解考试压力的好方法。"),
            ("confidence", "[ˈkɒnfɪdəns]", "n.信心；信任", 3, "Taking part in activities can boost self-confidence.", "参加活动可以增强自信心。"),
            ("focus", "[ˈfəʊkəs]", "v./n.聚焦；集中注意力", 3, "We need to focus on our weak subjects to improve.", "我们需要集中精力在薄弱学科上以求提高。"),
            ("patience", "[ˈpeɪʃns]", "n.耐心；毅力", 3, "Learning a new language requires great patience.", "学习一门新语言需要极大的耐心。"),
            ("motivation", "[ˌməʊtɪˈveɪʃn]", "n.动力；积极性", 3, "Clear goals provide strong motivation for hard study.", "明确的目标为刻苦学习提供强大的动力。"),
            ("courage", "[ˈkʌrɪdʒ]", "n.勇气；胆量", 3, "Having the courage to speak English is the first step.", "有勇气开口说英语是第一步。"),
            ("discipline", "[ˈdɪsəplɪn]", "n.自律；纪律", 2, "Self-discipline is highly important for online learning.", "自律对于在线学习非常重要。"),
            ("emotion", "[ɪˈməʊʃn]", "n.情绪；情感", 3, "Writing a diary is a good way to express our emotions.", "写日记是表达我们情绪的一个好方法。"),
            ("balance", "[ˈbæləns]", "n./v.平衡", 3, "We must keep a healthy balance between study and play.", "我们必须在学习与娱乐之间保持健康的平衡。")
        ]
    },
    84: {
        "title": "艺术审美与经典传承 (Art & Heritage)",
        "words": [
            ("masterpiece", "[ˈmɑːstəpiːs]", "n.杰作；名著", 3, "The Mona Lisa is a world-famous art masterpiece.", "《蒙娜丽莎》是一件世界著名的艺术杰作。"),
            ("appreciation", "[əˌpriːʃiˈeɪʃn]", "n.欣赏；感激", 3, "Visiting museums can improve our art appreciation.", "参观博物馆可以提高我们的艺术欣赏力。"),
            ("heritage", "[ˈherɪtɪdʒ]", "n.遗产；传统", 3, "Peking Opera is a vital part of Chinese cultural heritage.", "京剧是中国文化遗产的重要组成部分。"),
            ("creativity", "[ˌkriːeɪˈtɪvəti]", "n.创造力；创造性", 3, "Painting allows children to express their creativity.", "绘画能够让孩子们展现出他们的创造力。"),
            ("exhibition", "[ˌeksɪˈbɪʃn]", "n.展览；展览会", 3, "Our school is holding an annual student art exhibition.", "我们学校正在举办一年一度的学生艺术展。"),
            ("perspective", "[pəˈspektɪv]", "n.视角；观点", 2, "Art helps us see the colorful world from new perspectives.", "艺术帮助我们从全新的视角去看这个多彩的世界。"),
            ("sculpture", "[ˈskʌlptʃə(r)]", "n.雕塑；雕刻", 3, "This unique sculpture was made by a talented artist.", "这座独特的雕塑是由一位天才艺术家制作的。"),
            ("inspire", "[ɪnˈspaɪə(r)]", "v.启发；鼓舞", 3, "Beautiful nature scenery can inspire many painters.", "美丽的大自然风景能启发许多画家。"),
            ("classical", "[ˈklæsɪkl]", "adj.古典的；经典的", 3, "Listening to classical music helps me stay calm.", "听古典音乐能帮我保持平静。"),
            ("performance", "[pəˈfɔːməns]", "n.表演；表现", 3, "The actors gave an amazing performance on the stage.", "演员们在舞台上带来了精彩的表演。")
        ]
    },
    85: {
        "title": "国际视野与跨文化交际 (Global Vision)",
        "words": [
            ("diversity", "[daɪˈvɜːsəti]", "n.多样性", 3, "Cultural diversity makes the modern world more colorful.", "文化多样性让现代世界变得更加丰富多彩。"),
            ("global", "[ˈɡləʊbl]", "adj.全球的；世界的", 3, "English is a global language used by millions of people.", "英语是一门被数百万人使用的全球性语言。"),
            ("communicate", "[kəˈmjuːnɪkeɪt]", "v.交流；沟通", 3, "We use body language to communicate with foreigners.", "我们用肢体语言同外国人交流。"),
            ("cooperation", "[kəʊˌɒpəˈreɪʃn]", "n.合作；协作", 3, "International cooperation is key to solving global issues.", "国际合作是解决全球性问题的关键。"),
            ("respect", "[rɪˈspekt]", "v./n.尊重；敬重", 3, "We must learn to respect customs of different countries.", "我们必须学会尊重不同国家的习俗。"),
            ("citizen", "[ˈsɪtɪzn]", "n.公民；市民", 3, "We should behave politely as a good global citizen.", "作为一名优秀的全球公民，我们应该表现得有礼貌。"),
            ("connection", "[kəˈnekʃn]", "n.连接；联系", 3, "The internet built a strong connection among people.", "互联网在人们之间建立了紧密的连接。"),
            ("tourism", "[ˈtʊərɪzəm]", "n.旅游业", 2, "Local tourism has developed very fast in recent years.", "近年来，当地的旅游业发展得非常迅速。"),
            ("harmony", "[ˈhɑːməni]", "n.和谐；融洽", 2, "We hope all countries can live in peace and harmony.", "我们希望所有国家都能和平和谐地共处。"),
            ("exchange", "[ɪksˈtʃeɪndʒ]", "v./n.交换；交流", 3, "The school organized a cultural exchange program last term.", "上学期学校组织了一次文化交流项目。")
        ]
    },
    86: {
        "title": "高频核心动词提升 I (Almighty Verbs I)",
        "words": [
            ("adopt", "[əˈdɒpt]", "v.采用；采纳；收养", 3, "Our school decided to adopt a new English textbook.", "我们学校决定采用一本新的英语教科书。"),
            ("analyze", "[ˈænəlaɪz]", "v.分析", 3, "We need to analyze our mistakes carefully in exams.", "在考试中我们需要仔细分析我们的错误。"),
            ("deliver", "[dɪˈlɪvə(r)]", "v.递送；发表(演讲)", 3, "The principal will deliver a speech at the ceremony.", "校长将在典礼上发表讲话。"),
            ("evaluate", "[ɪˈvæljueɪt]", "v.评估；评价", 2, "Teachers evaluate our progress through daily quizzes.", "老师们通过日常小测验来评估我们的进步。"),
            ("illustrate", "[ˈɪləstreɪt]", "v.说明；插图", 2, "She used several examples to illustrate her opinion.", "她用了几个例子来阐明自己的观点。"),
            ("recommend", "[ˌrekəˈmend]", "v.推荐；建议", 3, "My teacher recommended this useful grammar book to me.", "我老师向我推荐了这本有用的语法书。"),
            ("transform", "[trænsˈfɔːm]", "v.改变；改造", 3, "Education can transform a person's life completely.", "教育可以彻底改变一个人的生活。"),
            ("guarantee", "[ˌɡærənˈtiː]", "v./n.保证；担保", 2, "Hard work alone cannot guarantee absolute success.", "单靠努力工作并不能保证绝对的成功。"),
            ("absorb", "[əbˈzɔːb]", "v.吸收；理解", 3, "Active reading helps students absorb useful knowledge.", "主动阅读能帮助学生吸收有用的知识。"),
            ("maintain", "[meɪnˈteɪn]", "v.维持；保持", 3, "We must maintain good study habits in the summer.", "在暑假里我们必须保持良好的学习习惯。")
        ]
    },
    87: {
        "title": "高频核心动词提升 II (Almighty Verbs II)",
        "words": [
            ("observe", "[əbˈzɜːv]", "v.观察；遵守", 3, "Students are asked to observe the growth of plants.", "学生们被要求观察植物的生长。"),
            ("possess", "[pəˈzes]", "v.拥有；具备", 2, "She possesses great talent for writing short stories.", "她具备写短篇小说的极大天赋。"),
            ("motivate", "[ˈməʊtɪveɪt]", "v.激发；激励", 3, "A good coach knows how to motivate the players.", "一个优秀的教练知道如何激励队员。"),
            ("expand", "[ɪkˈspænd]", "v.扩张；扩大", 3, "Reading is a superb way to expand vocabulary.", "阅读是扩大词汇量的极佳方法。"),
            ("purchase", "[ˈpɜːtʃəs]", "v./n.购买", 3, "We can purchase various stationery online easily.", "我们可以很容易地在网上购买各种文具。"),
            ("convey", "[kənˈveɪ]", "v.表达；传递", 2, "A red envelope can convey deep love from families.", "红包能传递来自家人的深厚的爱。"),
            ("accomplish", "[əˈkʌmplɪʃ]", "v.完成；实现", 3, "We can accomplish major goals through teamwork.", "我们可以通过团队合作实现重大的目标。"),
            ("strengthen", "[ˈstreŋθn]", "v.加强；增强", 3, "Daily exercises can strengthen our body and mind.", "每日锻炼可以增强我们的身心健康。"),
            ("confirm", "[kənˈfɜːm]", "v.确认；证实", 3, "Please check the time to confirm the date of exam.", "请检查时间以确认考试日期。"),
            ("adjust", "[əˈdʒʌst]", "v.调整；适应", 3, "It takes time to adjust to high school life.", "适应高中生活需要一些时间。")
        ]
    },
    88: {
        "title": "高频核心名词提升 I (Almighty Nouns I)",
        "words": [
            ("obstacle", "[ˈɒbstəkl]", "n.障碍；阻碍", 3, "Language should not be an obstacle to friendship.", "语言不应该是友谊的障碍。"),
            ("outcome", "[ˈaʊtkʌm]", "n.结果；成果", 3, "We are all waiting anxiously for the exam outcomes.", "我们都在焦急地等待着考试结果。"),
            ("strategy", "[ˈstrætədʒi]", "n.策略；战术", 3, "Using the right strategy can improve test scores.", "使用正确的策略可以提高测试成绩。"),
            ("colleague", "[ˈkɒliːɡ]", "n.同事；同僚", 3, "My father works closely with his friendly colleagues.", "我父亲与他友好的同事们紧密共事。"),
            ("evidence", "[ˈevɪdəns]", "n.证据；证明", 3, "Scientists gathered strong evidence to prove warming.", "科学家们收集了强有力的证据来证明全球变暖。"),
            ("advantage", "[ədˈvɑːntɪdʒ]", "n.优势；利益", 3, "Speaking fluent English is a major job advantage.", "英语流利是一项重大的职业优势。"),
            ("curriculum", "[kəˈrɪkjələm]", "n.课程", 3, "The school designed a colorful sports curriculum.", "学校设计了丰富多彩的体育课程。"),
            ("solution", "[səˈluːʃn]", "n.解决方案", 3, "We finally found a clever solution to the math problem.", "我们最终找到了这个数学难题的巧妙解法。"),
            ("perspective", "[pəˈspektɪv]", "n.视角；观点", 2, "Travel can enrich our minds by offering new perspectives.", "旅行通过提供崭新的视角来丰富我们的思想。"),
            ("industry", "[ˈɪndəstri]", "n.工业；行业", 3, "The local tourism industry has grown very fast.", "当地的旅游行业发展得非常迅速。")
        ]
    },
    89: {
        "title": "高频核心名词提升 II (Almighty Nouns II)",
        "words": [
            ("destination", "[ˌdestɪˈneɪʃn]", "n.目的地；终点", 3, "Paris is a popular travel destination for families.", "巴黎是广大家庭喜爱的旅游目的地。"),
            ("process", "[ˈprəʊses]", "n.过程；进程", 3, "Learning is a gradual process that takes years.", "学习是一个需要花费数年的渐进过程。"),
            ("ambition", "[æmˈbɪʃn]", "n.野心；抱负", 3, "Her ambition is to study medicine in university.", "她的抱负是在大学里学习医学。"),
            ("resource", "[rɪˈsɔːs]", "n.资源", 3, "Libraries offer valuable resources for self-study.", "图书馆为自学提供了宝贵的资源。"),
            ("benefit", "[ˈbenɪfɪt]", "n./v.益处；得益于", 3, "Regular reading brings endless benefits to our writing.", "规律的阅读给我们的写作带来无尽的益处。"),
            ("conflict", "[ˈkɒnflɪkt]", "n./v.冲突；争执", 3, "Communication is key to resolving student conflicts.", "沟通是解决学生冲突的关键。"),
            ("consequence", "[ˈkɒnsɪkwəns]", "n.后果；影响", 3, "Obey rules, or you must face the consequences.", "遵守规则，否则你必须承担后果。"),
            ("talent", "[ˈtælənt]", "n.天赋；才华", 3, "Oli has an amazing talent for playing the violin.", "Oli在拉小提琴方面有惊人的天赋。"),
            ("atmosphere", "[ˈætməsfɪə(r)]", "n.大气；氛围", 3, "The restaurant has a cosy and warm atmosphere.", "这家餐厅有着舒适而温馨的氛围。"),
            ("milestone", "[ˈmaɪlstəʊn]", "n.里程碑", 2, "Entering junior high is a vital milestone in life.", "步入初中是人生中一个至关重要的里程碑。")
        ]
    },
    90: {
        "title": "高频核心形容词提升 I (Almighty Adjs I)",
        "words": [
            ("accurate", "[ˈækjərət]", "adj.准确的；精准的", 3, "Please make sure your translation is accurate.", "请确保你的翻译是准确的。"),
            ("sensitive", "[ˈsensətɪv]", "adj.敏感的；体贴的", 3, "She is a sensitive girl who easily gets hurt.", "她是一个很容易受到伤害的敏感女孩。"),
            ("professional", "[prəˈfeʃənl]", "adj./n.专业的；职业人", 3, "You need professional advice to learn coding.", "你需要专业的建议来学习编程。"),
            ("stable", "[ˈsteɪbl]", "adj.稳定的；稳固的", 3, "Keep a stable mindset during the final exams.", "在期末考试期间保持稳定的心态。"),
            ("capable", "[ˈkeɪpəbl]", "adj.有能力的", 3, "Every student is capable of accomplishing goals.", "每个学生都有能力实现自己的目标。"),
            ("generous", "[ˈdʒenərəs]", "adj.大方的；慷慨的", 3, "He was generous enough to share all his notes.", "他很大方，分享了他所有的笔记。"),
            ("precious", "[ˈpreʃəs]", "adj.宝贵的；珍贵的", 3, "Time is precious, so don't waste it on games.", "时间是宝贵的，所以不要把它浪费在游戏上。"),
            ("flexible", "[ˈfleksəbl]", "adj.灵活的；可变通的", 3, "A flexible study plan is easier to follow.", "灵活的学习计划更容易坚持下去。"),
            ("diverse", "[daɪˈvɜːs]", "adj.多种多样的；不同的", 3, "The store sells a diverse range of textbooks.", "这家商店出售琳琅满目的教科书。"),
            ("constant", "[ˈkɒnstənt]", "adj.恒定的；不断的", 3, "Regular practice is the constant path to success.", "规律的练习是通往成功的恒定不变之路。")
        ]
    },
    91: {
        "title": "高频核心形容词提升 II (Almighty Adjs II)",
        "words": [
            ("delighted", "[dɪˈlaɪtɪd]", "adj.高兴的；开心的", 3, "Oli was delighted to hear the excellent news.", "Oli听到这个极好的消息感到非常高兴。"),
            ("outstanding", "[aʊtˈstændɪŋ]", "adj.杰出的；显著的", 3, "He got an award for his outstanding sports record.", "他因其杰出的体育纪录而获得奖项。"),
            ("responsible", "[rɪˈspɒnsəbl]", "adj.负责的", 3, "We must be responsible for our own behaviors.", "我们必须对自己的行为负责。"),
            ("temporary", "[ˈtemprəri]", "adj.临时的", 3, "Failure is only temporary if you never give up.", "如果你永不放弃，失败就只是暂时的。"),
            ("urgent", "[ˈɜːdʒənt]", "adj.紧急的", 3, "I have to leave right now as there is an urgent task.", "因为有一项紧急任务，我不得不立刻离开。"),
            ("skeptical", "[ˈskeptɪkl]", "adj.怀疑的", 2, "Scientists are skeptical of unproven theories.", "科学家们对未经证实的理论持怀疑态度。"),
            ("optimistic", "[ˌɒptɪˈmɪstɪk]", "adj.乐观的", 3, "Staying optimistic helps us overcome hardships.", "保持乐观能帮助我们克服艰难险阻。"),
            ("creative", "[kriˈeɪtɪv]", "adj.有创造力的", 3, "Our teacher used a creative way to explain grammar.", "我们老师用了一种很有创意的方法来讲解语法。"),
            ("artificial", "[ˌɑːtɪˈfɪʃl]", "adj.人造的；人工的", 3, "This playground is covered with artificial grass.", "这个操场铺满了人造草坪。"),
            ("worthwhile", "[ˌwɜːθˈwaɪl]", "adj.值得的", 3, "Helping children learn is a worthwhile experience.", "帮助孩子们学习是一次非常值得的体验。")
        ]
    },
    92: {
        "title": "核心副词与逻辑连词 (Connectors & Adverbs)",
        "words": [
            ("gradually", "[ˈɡrædʒuəli]", "adv.逐渐地", 3, "The cold weather is gradually warming up.", "寒冷的天气正在逐渐变暖。"),
            ("absolutely", "[ˈæbsəluːtli]", "adv.绝对地；完全地", 3, "You are absolutely right about the answer.", "关于这个答案你绝对是正确的。"),
            ("constantly", "[ˈkɒnstəntli]", "adv.不断地", 3, "She is constantly reading books to gain knowledge.", "她不断地看书以获取知识。"),
            ("frequently", "[ˈfriːkwəntli]", "adv.频繁地", 3, "Students are frequently asked to present in class.", "学生们频繁地被要求在课堂上做演示。"),
            ("eventually", "[ɪˈventʃuəli]", "adv.最终地", 3, "Keep practicing and you will eventually succeed.", "坚持练习，你最终会成功的。"),
            ("therefore", "[ˈðeəfɔː(r)]", "adv.因此；所以", 3, "The road is wet; therefore, you must drive slowly.", "路面很湿，因此你必须开得慢一些。"),
            ("nevertheless", "[ˌnʌvəðəˈles]", "adv.然而；不过", 3, "It was raining hard; nevertheless, they went out.", "雨下得很大，然而他们还是出去了。"),
            ("moreover", "[mɔːrˈəʊvə(r)]", "adv.而且；此外", 3, "The book is cheap; moreover, it is highly useful.", "这本书很便宜，而且它非常有用。"),
            ("meanwhile", "[ˈmiːnwaɪl]", "adv.同时", 3, "I will clean the room; meanwhile, you wash plates.", "我会打扫房间，同时你来洗盘子。"),
            ("definitely", "[ˈdefɪnətli]", "adv.必定地；确实地", 3, "We will definitely attend your birthday party.", "我们必定会参加你的生日派对。")
        ]
    },
    93: {
        "title": "纲外阻碍词特训 I (Key Verbs III)",
        "words": [
            ("guarantee", "[ˌɡærənˈtiː]", "v.保证", 3, "A high score can guarantee a seat in senior high.", "高分能保证获得高中的一席之地。"),
            ("purchase", "[ˈpɜːtʃəs]", "v.购买", 3, "You can purchase modern gadgets easily online.", "你可以在网上轻松购买到现代电子小玩意。"),
            ("recommend", "[ˌrekəˈmend]", "v.推荐", 3, "I recommend everyone to read this famous novel.", "我推荐每个人都读一读这本著名的小说。"),
            ("evaluate", "[ɪˈvæljueɪt]", "v.评估", 2, "How do teachers evaluate our homework progress?", "老师们是如何评估我们的作业进度的？"),
            ("maintain", "[meɪnˈteɪn]", "v.维持", 3, "It is vital to maintain regular sports routines.", "保持规律的体育锻炼程序是至关重要的。"),
            ("adopt", "[əˈdɒpt]", "v.采用", 3, "The company decided to adopt new clean energy.", "该公司决定采用全新的清洁能源。"),
            ("strengthen", "[ˈstreŋθn]", "v.增强", 3, "We must strengthen cooperation to finish tasks.", "我们必须加强合作以完成任务。"),
            ("expand", "[ɪkˈspænd]", "v.扩大", 3, "Travel helps expand our horizons and knowledge.", "旅行有助于扩大我们的眼界和知识。"),
            ("confirm", "[kənˈfɜːm]", "v.确认", 3, "The doctor will confirm the health report tomorrow.", "医生将在明天确认这份健康报告。"),
            ("adjust", "[əˈdʒʌst]", "v.调整", 3, "We should adjust our sails when the wind changes.", "当风向改变时，我们应当调整我们的风帆。")
        ]
    },
    94: {
        "title": "纲外阻碍词特训 II (Key Nouns III)",
        "words": [
            ("colleague", "[ˈkɒliːɡ]", "n.同事", 3, "Friendly colleagues make the workplace happy.", "友好的同事能让工作场所变得快乐。"),
            ("strategy", "[ˈstrætədʒi]", "n.策略", 3, "An efficient strategy leads to double outcomes.", "高效的的策略能带来双倍的成果。"),
            ("evidence", "[ˈevɪdəns]", "n.证据", 3, "There is no evidence to prove his silly theory.", "没有证据能证明他那愚蠢的理论。"),
            ("curriculum", "[kəˈrɪkjələm]", "n.课程", 3, "A varied curriculum helps students grow fully.", "多元化的课程能帮助学生全面成长。"),
            ("solution", "[səˈluːʃn]", "n.解决方案", 3, "Finding a quick solution is what we need now.", "寻找一个快速的解决方案是目前我们所需要的。"),
            ("industry", "[ˈɪndəstri]", "n.工业；行业", 3, "The IT industry is attracting many young graduates.", "IT行业正在吸引许多年轻的毕业生。"),
            ("destination", "[ˌdestɪˈneɪʃn]", "n.目的地", 3, "We finally arrived at our camping destination.", "我们最终到达了我们的露营目的地。"),
            ("consequence", "[ˈkɒnsɪkwəns]", "n.后果", 3, "Every action has a corresponding consequence.", "每一个行为都有相应的后果。"),
            ("atmosphere", "[ˈætməsfɪə(r)]", "n.氛围", 3, "Libraries have a quiet and academic atmosphere.", "图书馆有一种安静和学术的氛围。"),
            ("milestone", "[ˈmaɪlstəʊn]", "n.里程碑", 2, "Entering university is a milestone in my life.", "步入大学是我人生中的一个里程碑。")
        ]
    },
    95: {
        "title": "纲外阻碍词特训 III (Key Adjs III)",
        "words": [
            ("accurate", "[ˈækjərət]", "adj.准确的", 3, "An accurate map is necessary for hikers.", "一份精准的地图对徒步旅行者来说是必要的。"),
            ("sensitive", "[ˈsensətɪv]", "adj.敏感的", 3, "Cats are sensitive to any small movements.", "猫对任何细小的动作都非常敏感。"),
            ("professional", "[prəˈfeʃənl]", "adj.专业的", 3, "Her professional skills helped resolve the crisis.", "她的专业技能帮助解决了这场危机。"),
            ("stable", "[ˈsteɪbl]", "adj.稳定的", 3, "Stable emotions help you perform better in exams.", "稳定的情绪能帮你更好地应对考试。"),
            ("generous", "[ˈdʒenərəs]", "adj.大方的", 3, "She is always generous with her praise for kids.", "她对孩子们的赞美总是毫不吝啬。"),
            ("precious", "[ˈpreʃəs]", "adj.珍贵的", 3, "Water is precious in dry desert regions.", "在干旱的沙漠地区，水资源是极其珍贵的。"),
            ("flexible", "[ˈfleksəbl]", "adj.灵活的", 3, "We should keep our travel dates flexible.", "我们应该让我们的旅行日期保持灵活。"),
            ("optimistic", "[ˌɒptɪˈmɪstɪk]", "adj.乐观的", 3, "An optimistic mind always sees the bright side.", "乐观的心态总是能看到积极的一面。"),
            ("artificial", "[ˌɑːtɪˈfɪʃl]", "adj.人造的", 3, "This vase is filled with beautiful artificial flowers.", "这个花瓶里插满了美丽的人造花。"),
            ("worthwhile", "[ˌwɜːθˈwaɪl]", "adj.值得的", 3, "Teaching kids English is a worthwhile job.", "教孩子们英语是一份极其值得的工作。")
        ]
    },
    96: {
        "title": "阅读理解高频态度词 (Reading Attitudes)",
        "words": [
            ("supportive", "[səˈpɔːtɪv]", "adj.支持的；鼓励的", 3, "My parents are highly supportive of my decisions.", "我父母对我的决定非常支持。"),
            ("skeptical", "[ˈskeptɪkl]", "adj.怀疑的", 2, "Many people remain skeptical about the new project.", "许多人仍然对这个新项目持怀疑态度。"),
            ("neutral", "[ˈnjuːtrəl]", "adj.中立的", 2, "A good reporter must keep a neutral position.", "一名优秀的记者必须保持中立的立场。"),
            ("critical", "[ˈkrɪtɪkl]", "adj.批判的；挑剔的", 3, "The article was highly critical of the government.", "这篇文章对政府提出了严厉的批评。"),
            ("approving", "[əˈpruːvɪŋ]", "adj.赞许的；赞成的", 2, "The teacher gave an approving nod to my answer.", "老师对我的回答赞许地点了点头。"),
            ("objective", "[əbˈdʒektɪv]", "adj.客观的", 3, "We should make objective decisions based on facts.", "我们应该基于事实做出客观的决定。"),
            ("subjective", "[səbˈdʒektɪv]", "adj.主观的", 2, "Taste in music is highly subjective for everyone.", "对音乐的品味对每个人来说都是非常主观的。"),
            ("concerned", "[kənˈsɜːnd]", "adj.担心的；关切的", 3, "We are all concerned about the safety of survivors.", "我们都非常担心幸存者的安全。"),
            ("indifferent", "[ɪnˈdɪfrənt]", "adj.冷漠的；不关心的", 2, "She seemed indifferent to the outcome of the match.", "她似乎对比赛的结果漠不关心。"),
            ("doubtful", "[ˈdaʊtfl]", "adj.怀疑的；不确定的", 3, "I am highly doubtful about the success of his plan.", "我对他的计划能否成功持高度怀疑态度。")
        ]
    },
    97: {
        "title": "阅读理解高频转折与让步 (Reading Connectors)",
        "words": [
            ("however", "[haʊˈevə(r)]", "adv.然而", 3, "He was very tired; however, he kept running.", "他非常累，然而他依然坚持奔跑。"),
            ("although", "[ɔːlˈðəʊ]", "conj.虽然；尽管", 3, "Although it was raining, they played football.", "尽管正在下雨，他们还是去踢足球了。"),
            ("nevertheless", "[ˌnʌvəðəˈles]", "adv.然而", 3, "The task is tough; nevertheless, we must finish it.", "任务很艰巨，然而我们必须完成它。"),
            ("despite", "[dɪˈspaɪt]", "prep.尽管；不管", 3, "They won the match despite the terrible weather.", "尽管天气糟糕，他们还是赢得了比赛。"),
            ("instead", "[ɪnˈsted]", "adv.代替；相反", 3, "I didn't go shopping; instead, I read at home.", "我没有去购物，相反，我在家读书。"),
            ("otherwise", "[ˈʌðəwaɪz]", "adv.否则", 3, "Wear your coat; otherwise, you will catch cold.", "穿上外套，否则你会感冒的。"),
            ("though", "[ðəʊ]", "conj./adv.虽然；然而", 3, "The exam was tough; I think I passed it, though.", "考试很难，不过我觉得我还是通过了。"),
            ("whereas", "[ˌweərˈæz]", "conj.然而；但是", 2, "I love green tea, whereas my sister prefers coffee.", "我喜欢绿茶，然而我姐姐更偏爱咖啡。"),
            ("conversely", "[ˈkɒnvɜːsli]", "adv.相反地", 2, "Some kids love science; conversely, others hate it.", "一些孩子喜爱科学，相反地，另一些孩子却讨厌它。"),
            ("nonetheless", "[ˌnʌnðəˈles]", "adv.然而；不过", 2, "We made errors; nonetheless, we learned valuable lessons.", "我们犯了错，不过我们吸取了宝贵的教训。")
        ]
    },
    98: {
        "title": "完形填空高频近义词辨析 I (Cloze Boost I)",
        "words": [
            ("cooperate", "[kəʊˈɒpəreɪt]", "v.合作", 3, "We must cooperate to achieve the maximum outcomes.", "我们必须精诚合作以取得最大的成果。"),
            ("compete", "[kəmˈpiːt]", "v.竞争", 3, "Many companies compete for the new digital market.", "许多公司都在竞逐崭新的数字市场。"),
            ("contribute", "[kənˈtrɪbjuːt]", "v.贡献；捐助", 3, "Every volunteer contributed to the success of program.", "每一个志愿者都为项目的成功做出了贡献。"),
            ("protect", "[prəˈtekt]", "v.保护", 3, "Wearing masks can protect us from severe diseases.", "戴口罩能保护我们免受严重疾病的伤害。"),
            ("provide", "[prəˈvaɪd]", "v.提供", 3, "The hotel provides free breakfast for all guests.", "这家酒店为所有客人提供免费的早餐。"),
            ("produce", "[prəˈdjuːs]", "v.生产；制造", 3, "The local factory produces high-quality stationery.", "当地工厂生产高质量的文具。"),
            ("express", "[ɪkˈspres]", "v.表达", 3, "Art is a key way to express our inner thoughts.", "艺术是表达我们内心思想的重要途径。"),
            ("explain", "[ɪkˈspleɪn]", "v.解释", 3, "Can you explain the meaning of this complex idiom?", "你能解释一下这个复杂成语的含义吗？"),
            ("expect", "[ɪkˈspekt]", "v.期待；预料", 3, "Parents always expect their kids to study hard.", "父母总是期待着他们的孩子努力学习。"),
            ("accomplish", "[əˈkʌmplɪʃ]", "v.实现", 3, "Oli accomplished her dream by winning the violin contest.", "Oli通过在小提琴比赛中夺冠实现了自己的梦想。")
        ]
    },
    99: {
        "title": "完形填空高频近义词辨析 II (Cloze Boost II)",
        "words": [
            ("influence", "[ˈɪnfluəns]", "n./v.影响", 3, "Parents have a strong influence on kids' behavior.", "父母对孩子的行为有着强烈的的影响。"),
            ("inspiration", "[ˌɪnspəˈreɪʃn]", "n.灵感", 3, "Beautiful classical music gave the author inspiration.", "优美的古典音乐带给作者创作灵感。"),
            ("impression", "[ɪmˈpreʃn]", "n.印象", 3, "His amazing speech left a deep impression on me.", "他精彩的演讲给我留下了深刻的印象。"),
            ("strategy", "[ˈstrætədʒi]", "n.策略", 3, "We need a new strategy to tackle the challenge.", "我们需要一个新的策略来应对挑战。"),
            ("strength", "[streŋθ]", "n.力量；优势", 3, "Patience is a major strength of a good teacher.", "耐心是一名优秀教师的主要优势。"),
            ("struggle", "[ˈstrʌɡl]", "n./v.奋斗；挣扎", 3, "The team struggled hard to win the championship.", "队员们为夺冠付出了艰苦的努力。"),
            ("attentive", "[əˈtentɪv]", "adj.专注的", 2, "Attentive students learn much faster in the classroom.", "专注的学生在课堂上学得更快。"),
            ("aggressive", "[əˈɡresɪv]", "adj.好斗的；进取的", 2, "A good salesperson must be energetic and aggressive.", "一名优秀的销售人员必须精力充沛且锐意进取。"),
            ("attractive", "[əˈtræktɪv]", "adj.有吸引力的", 3, "The ancient town is an attractive travel destination.", "这座古老的城镇是一个极具吸引力的旅游目的地。"),
            ("curious", "[ˈkjʊəriəs]", "adj.好奇的", 3, "Children are always curious about mysterious nature.", "孩子们总是对神秘的大自然充满好奇。")
        ]
    },
    100: {
        "title": "百日冲刺与终极愿景 (Grand Milestone)",
        "words": [
            ("milestone", "[ˈmaɪlstəʊn]", "n.里程碑", 2, "Reaching Day 100 is a brilliant milestone for Oli.", "达到第100天对Oli来说是一个光辉的里程碑。"),
            ("accomplishment", "[əˈkʌmplɪʃmənt]", "n.成就；完成", 3, "We felt a great sense of accomplishment on graduation.", "在毕业典礼上，我们感到一种强烈的成就感。"),
            ("willpower", "[ˈwɪlpaʊə(r)]", "n.意志力", 3, "Oli showed remarkable willpower in studying vocabulary.", "Oli在学习词汇上展露了非凡的意志力。"),
            ("determine", "[dɪˈtɜːmɪn]", "v.决心；决定", 3, "We are determined to pursue our global college dreams.", "我们下定决心去追寻我们全球大学的梦想。"),
            ("victory", "[ˈvɪktəri]", "n.胜利", 3, "We celebrated our final victory with loud cheers.", "我们用响亮的欢呼声庆祝了我们最终的胜利。"),
            ("courage", "[ˈkʌrɪdʒ]", "n.勇气", 3, "Have the courage to speak up and express yourself.", "拿出勇气，大声说出并表达你自己。"),
            ("persistent", "[pəˈsɪstənt]", "adj.坚持不懈的", 3, "Persistent efforts will eventually lead to breakthroughs.", "坚持不懈的努力最终将引导我们取得突破。"),
            ("master", "[ˈmɑːstə(r)]", "v./n.精通；主人", 3, "By studying every day, Oli mastered 1000 key words.", "通过坚持每天学习，Oli精通了1000个重点词汇。"),
            ("grand", "[ɡrænd]", "adj.宏伟的；盛大的", 3, "The school held a grand ceremony to praise outstanding students.", "学校举办了一场盛大的典礼来表彰优秀学生。"),
            ("worthwhile", "[ˌwɜːθˈwaɪl]", "adj.值得的", 3, "Looking back, every single day of practice was worthwhile.", "回首过去，每一天坚持练习都是非常值得的。")
        ]
    }
}

# 目标文件路径
filepath = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/beijing_zhongkao_vocab_21days.md"

def extend_markdown():
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found!")
        return

    # 生成 Markdown 文本
    md_lines = []
    
    for day, info in sorted(extend_vocab.items()):
        md_lines.append(f"\n### Day {day}: {info['title']}\n")
        for idx, word_info in enumerate(info['words'], 1):
            word, phonetic, meaning, freq, ex_en, ex_cn = word_info
            
            # 使用标准的格式写入
            md_lines.append(f"{idx}. **{word}** - {phonetic} {meaning} (词频: {freq})")
            md_lines.append(f"    * *{ex_en}* ({ex_cn})")
    
    final_append_text = "\n".join(md_lines)
    
    # 追加到文件末尾
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(final_append_text)
        
    print(f"Successfully extended beijing_zhongkao_vocab_21days.md to Day 100!")

if __name__ == "__main__":
    extend_markdown()
