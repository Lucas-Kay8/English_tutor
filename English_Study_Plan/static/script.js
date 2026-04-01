/**
 * VocabQuest - Oli的单词冒险
 * 多邻国风格词汇学习系统
 * 全中文界面
 */

// ===== 状态管理 =====
const state = {
    // 进度数据
    progress: null,
    vocabulary: [],

    // 会话数据
    currentDay: 1,
    streak: 0,
    xp: 0,
    hearts: 5,
    maxHearts: 5,
    currentUser: 'oli', // 'oli' or 'test'

    // 测试数据
    currentView: 'loading',
    quizMode: 'day',      // 'day', 'review', 'grand'
    quizWords: [],
    currentQuestion: 0,
    sessionScore: 0,
    sessionMistakes: [],
    streakCount: 0,       // 连击计数
    startTime: null,

    // 预习模式数据
    studyWords: [],
    studyIndex: 0,
    studyDay: 1,

    // 体验优化状态
    currentWeek: 1,

    // 题型
    questionTypes: ['choice', 'spell', 'listen', 'fill']
};

// ===== 常量 =====
const XP_PER_CORRECT = 10;
const XP_STREAK_BONUS = 5;  // 连击额外加成
const DAY_LABELS = [
    '万能动词', '万能名词', '日常动词', '情感形容词', '描述形容词',
    '抽象名词', '具体名词', '动作动词', '感官动词', '交流动词',
    '频率副词', '程度副词', '方式副词', '介词短语', '连词',
    '疑问词', '代词', '数量词', '时间词', '地点词',
    '综合复习', '健康生活', '社区服务', '自然风暴', '动物保护',
    '阶段复习 I', '科学发现', '礼仪尊重', '环境保护', '意志挑战',
    '太空探索', '传统文化', '公民责任', '职业规划', '终极挑战',
    '智能生活', '绿色可持续', '逆境与毅力', '职业素质', '共情与交流'
];

// ===== 初始化 =====
async function init() {
    try {
        // 初始化用户
        const savedUser = localStorage.getItem('vocab-quest-user');
        if (savedUser) {
            state.currentUser = savedUser;
            document.getElementById('user-select').value = savedUser;
        }

        // 加载数据
        const [vocabRes, progressRes] = await Promise.all([
            fetch('/api/vocabulary'),
            fetch(`/api/progress?user=${state.currentUser}`)
        ]);

        state.vocabulary = await vocabRes.json();
        state.progress = await progressRes.json();

        // 初始化状态
        loadProgressData();

        // 绑定事件
        bindEvents();

        // 渲染首页
        showView('home');
        renderDashboard();

    } catch (error) {
        console.error('初始化失败:', error);
        alert(`加载数据失败: ${error.message}。请刷新页面重试`);
    }
}

// ===== 加载进度数据 =====
function loadProgressData() {
    const p = state.progress;

    // 基础数据
    state.xp = p.xp || 0;
    state.streak = p.streak || 0;
    state.hearts = p.hearts ?? 5;

    // 计算当前天数（基于已完成的天数）
    const completedDays = p.completedDays || [];
    state.currentDay = completedDays.length + 1;
    
    const maxDayInVocab = state.vocabulary.length > 0 ? Math.max(...state.vocabulary.map(v => v.day)) : 21;
    if (state.currentDay > maxDayInVocab) state.currentDay = maxDayInVocab;

    // 根据当前天数初始化当前周 (1-7天为周1, 以此类推)
    state.currentWeek = Math.ceil(state.currentDay / 7);

    // 计算生命值上限 (基础5 + 每完成1关+1，上限10)
    state.maxHearts = Math.min(10, 5 + completedDays.length);

    // 检查连击（是否昨天有学习）
    const lastStudy = p.lastStudyDate;
    if (lastStudy) {
        try {
            const today = new Date().toDateString();
            const yesterday = new Date(Date.now() - 86400000).toDateString();
            const lastDateObj = new Date(lastStudy);

            if (!isNaN(lastDateObj.getTime())) {
                const lastDate = lastDateObj.toDateString();
                if (lastDate !== today && lastDate !== yesterday) {
                    // 连击中断
                    state.streak = 0;
                }
            }
        } catch (e) {
            console.warn("Date parsing error", e);
        }
    }
}

// ===== 视图控制 =====
function showView(viewName) {
    state.currentView = viewName;
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    const view = document.getElementById(`${viewName}-view`);
    if (view) view.classList.add('active');
}

// ===== 计算等级称号 =====
function calculateRank(xp) {
    if (xp < 100) return '新手冒险家';
    if (xp < 500) return '初级魔法学徒';
    if (xp < 1000) return '见习法师';
    if (xp < 2500) return '中级法师';
    if (xp < 5000) return '高级法师';
    if (xp < 10000) return '大魔法师';
    if (xp < 20000) return '魔导士';
    if (xp < 50000) return '大魔导士';
    return '传奇大法师';
}

// ===== 获取虚拟形象配置 =====
function getAvatarConfig(xp) {
    if (xp < 100) return { img: 'stage_1.png', emoji: '🐣', bg: 'linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)', rankBg: 'linear-gradient(135deg, #9ca3af, #d1d5db)', rankColor: 'white' };
    if (xp < 500) return { img: 'stage_1.png', emoji: '🦉', bg: 'linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%)', rankBg: 'linear-gradient(135deg, #60a5fa, #3b82f6)', rankColor: 'white' };
    if (xp < 1000) return { img: 'stage_2.png', emoji: '🦊', bg: 'linear-gradient(135deg, #fef08a 0%, #fde047 100%)', rankBg: 'linear-gradient(135deg, #fbbf24, #f59e0b)', rankColor: 'white' };
    if (xp < 2500) return { img: 'stage_2.png', emoji: '🦁', bg: 'linear-gradient(135deg, #fecaca 0%, #fca5a5 100%)', rankBg: 'linear-gradient(135deg, #f87171, #ef4444)', rankColor: 'white' };
    if (xp < 5000) return { img: 'stage_3.png', emoji: '🦄', bg: 'linear-gradient(135deg, #e9d5ff 0%, #d8b4fe 100%)', rankBg: 'linear-gradient(135deg, #c084fc, #a855f7)', rankColor: 'white' };
    if (xp < 10000) return { img: 'stage_3.png', emoji: '🦅', bg: 'linear-gradient(135deg, #fed7aa 0%, #fdba74 100%)', rankBg: 'linear-gradient(135deg, #fb923c, #f97316)', rankColor: 'white' };
    if (xp < 20000) return { img: 'stage_4.png', emoji: '🐺', bg: 'linear-gradient(135deg, #a7f3d0 0%, #6ee7b7 100%)', rankBg: 'linear-gradient(135deg, #34d399, #10b981)', rankColor: 'white' };
    if (xp < 50000) return { img: 'stage_4.png', emoji: '🐉', bg: 'linear-gradient(135deg, #fbcfe8 0%, #f9a8d4 100%)', rankBg: 'linear-gradient(135deg, #f472b6, #ec4899)', rankColor: 'white' };
    return { img: 'stage_4.png', emoji: '👑', bg: 'linear-gradient(135deg, #ffedd5 0%, #fed7aa 100%)', rankBg: 'linear-gradient(135deg, #fbbf24, #d97706)', rankColor: 'white' };
}

// ===== 获取某天最佳成绩 =====
function getDayBestScore(day) {
    const history = state.progress.history || [];
    // 筛选该天的 day 模式记录，且 total > 0
    const dayRecords = history.filter(h => h.day === day && h.mode === 'day' && h.total > 0);
    if (dayRecords.length === 0) return null;

    let best = null;
    for (const r of dayRecords) {
        const acc = Math.round((r.score / r.total) * 100);
        if (!best || acc > best.accuracy) {
            best = { score: r.score, total: r.total, accuracy: acc };
        }
    }
    best.attempts = dayRecords.length;
    return best;
}

// ===== 获取整体学习统计 =====
function getOverallStats() {
    const history = state.progress.history || [];
    // 只统计 day 模式且有效的记录
    const validRecords = history.filter(h => h.mode === 'day' && h.total > 0);
    if (validRecords.length === 0) return { avgAccuracy: 0, totalSessions: 0, hasData: false };

    // 对每一天取最佳成绩后计算平均
    const completedDays = state.progress.completedDays || [];
    let totalAcc = 0;
    let daysWithData = 0;
    for (const day of completedDays) {
        const best = getDayBestScore(day);
        if (best) {
            totalAcc += best.accuracy;
            daysWithData++;
        }
    }

    return {
        avgAccuracy: daysWithData > 0 ? Math.round(totalAcc / daysWithData) : 0,
        totalSessions: validRecords.length,
        daysCompleted: completedDays.length,
        hasData: daysWithData > 0
    };
}

// ===== 获取正确率颜色样式 =====
function getAccuracyColor(acc) {
    if (acc >= 90) return { cssClass: 'accuracy-high', color: '#58CC02', label: '优秀' };
    if (acc >= 70) return { cssClass: 'accuracy-mid', color: '#FF9600', label: '良好' };
    return { cssClass: 'accuracy-low', color: '#FF4B4B', label: '需加强' };
}

// ===== 渲染首页 =====
function renderDashboard() {
    // 连击徽章
    document.getElementById('streak-days').textContent = state.streak;

    // 进度环
    const mastery = calculateMastery();
    document.getElementById('mastery-pct').textContent = Math.round(mastery) + '%';
    updateProgressRing(mastery);

    // 统计卡片
    document.getElementById('hearts-count').textContent = state.hearts;
    document.getElementById('xp-count').textContent = state.xp;
    document.getElementById('review-count').textContent = getReviewCount();

    // 渲染头像与称号
    const avatarEmojiEl = document.getElementById('user-avatar-emoji');
    const avatarImgEl = document.getElementById('user-avatar-img');
    const headerRankEl = document.getElementById('header-user-rank');
    if (headerRankEl && avatarEmojiEl) {
        const rankTitle = calculateRank(state.xp);
        const avatarConfig = getAvatarConfig(state.xp);

        headerRankEl.textContent = rankTitle;
        headerRankEl.style.background = avatarConfig.rankBg;
        headerRankEl.style.color = avatarConfig.rankColor || 'white';

        if (avatarImgEl) {
            avatarImgEl.src = `/static/avatars/${avatarConfig.img}`;
            avatarImgEl.onerror = () => {
                avatarImgEl.style.display = 'none';
                avatarEmojiEl.style.display = 'flex';
                avatarEmojiEl.textContent = avatarConfig.emoji;
                avatarEmojiEl.style.background = avatarConfig.bg;
            };
            avatarImgEl.onload = () => {
                avatarImgEl.style.display = 'block';
                avatarEmojiEl.style.display = 'none';
            };
        } else {
            avatarEmojiEl.textContent = avatarConfig.emoji;
            avatarEmojiEl.style.background = avatarConfig.bg;
        }
    }

    // 兼容可能遗留的旧称号节点
    const oldRankEl = document.getElementById('user-rank');
    if (oldRankEl) {
        oldRankEl.style.display = 'none';
    }

    // 渲染学习评估横幅
    renderLearningAssessment();

    // 更新引导卡片
    updateHeroCard();

    // 渲染周次选择
    renderWeekSelector();

    // 学习路径
    renderPathList();

    // 动态标题
    const maxDay = state.vocabulary.length > 0 ? Math.max(...state.vocabulary.map(v => v.day)) : 21;
    const pathTotalEl = document.getElementById('path-total-days');
    if (pathTotalEl) pathTotalEl.textContent = `共 ${maxDay} 天`;
}

// ===== 更新引导卡片 (Apple Hero) =====
function updateHeroCard() {
    const heroTitle = document.getElementById('hero-title');
    const heroSubtitle = document.getElementById('hero-subtitle');
    const heroBtn = document.getElementById('btn-hero-start');

    if (!heroTitle || !heroSubtitle) return;

    const currentDayLabel = DAY_LABELS[state.currentDay - 1] || '词汇挑战';
    
    // 如果今天已完成
    const isTodayDone = state.progress.completedDays && state.progress.completedDays.includes(state.currentDay);
    
    if (isTodayDone) {
        heroTitle.textContent = "今天任务已达成！";
        heroSubtitle.textContent = "明天记得继续回来冒险哦 🏆";
        heroBtn.innerHTML = '<span>回顾今日</span> <span class="arrow">→</span>';
    } else {
        heroTitle.textContent = "继续你的冒险";
        heroSubtitle.textContent = `第 ${state.currentDay} 天：${currentDayLabel}`;
        heroBtn.innerHTML = '<span>开启挑战</span> <span class="arrow">→</span>';
    }

    heroBtn.onclick = () => {
        // 自动切换到正确的周并滚动
        state.currentWeek = Math.ceil(state.currentDay / 7);
        renderWeekSelector();
        renderPathList();
        
        // 滚动到列表
        document.getElementById('path-list').scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        if (!isTodayDone) {
            startDayQuiz(state.currentDay);
        }
    };
}

// ===== 渲染周次选择 (Segmented Control) =====
function renderWeekSelector() {
    const selector = document.getElementById('week-selector');
    if (!selector) return;

    const maxDay = state.vocabulary.length > 0 ? Math.max(...state.vocabulary.map(v => v.day)) : 21;
    const totalWeeks = Math.ceil(maxDay / 7);

    let html = '';
    for (let w = 1; w <= totalWeeks; w++) {
        const isActive = w === state.currentWeek;
        const start = (w - 1) * 7 + 1;
        const end = Math.min(w * 7, maxDay);
        
        html += `<div class="segment ${isActive ? 'active' : ''}" onclick="selectWeek(${w})">第${w}周</div>`;
    }
    selector.innerHTML = html;
}

window.selectWeek = function(week) {
    state.currentWeek = week;
    renderWeekSelector();
    renderPathList();
};

// ===== 渲染学习评估横幅 =====
function renderLearningAssessment() {
    const overall = getOverallStats();
    let container = document.getElementById('learning-assessment');

    // 动态创建容器（如果不存在）
    if (!container) {
        container = document.createElement('div');
        container.id = 'learning-assessment';
        container.className = 'learning-assessment';
        // 插入到进度环下方
        const progressRing = document.querySelector('.progress-ring-container');
        if (progressRing && progressRing.parentNode) {
            progressRing.parentNode.insertBefore(container, progressRing.nextSibling);
        }
    }

    if (!overall.hasData) {
        container.innerHTML = `
            <div class="assessment-content">
                <span class="assessment-emoji">⏸️</span>
                <div class="assessment-text">
                    <div class="assessment-title">还没有学习记录</div>
                    <div class="assessment-subtitle">完成第一天的学习后，这里会显示学习评估</div>
                </div>
            </div>`;
        container.className = 'learning-assessment assessment-neutral';
        return;
    }

    const avg = overall.avgAccuracy;
    let emoji, title, subtitle, levelClass;

    if (avg >= 85) {
        emoji = '🌟';
        title = '表现优秀！';
        subtitle = `平均正确率 ${avg}%，已完成 ${overall.daysCompleted} 天，太棒了！`;
        levelClass = 'assessment-excellent';
    } else if (avg >= 70) {
        emoji = '👍';
        title = '表现不错';
        subtitle = `平均正确率 ${avg}%，已完成 ${overall.daysCompleted} 天，继续保持！`;
        levelClass = 'assessment-good';
    } else {
        emoji = '💪';
        title = '需要加油';
        subtitle = `平均正确率 ${avg}%，建议多复习错题再挑战新关卡`;
        levelClass = 'assessment-weak';
    }

    container.className = `learning-assessment ${levelClass}`;
    container.innerHTML = `
        <div class="assessment-content">
            <span class="assessment-emoji">${emoji}</span>
            <div class="assessment-text">
                <div class="assessment-title">${title}</div>
                <div class="assessment-subtitle">${subtitle}</div>
            </div>
            <div class="assessment-score">${avg}%</div>
        </div>`;
}

// ===== 获取待复习单词 =====
function getDueReviewWords() {
    const wordStats = state.progress.wordStats || {};
    const now = Date.now();
    const dueWords = [];

    for (const word of state.vocabulary) {
        const stats = wordStats[word.word];
        if (stats && stats.nextReview && stats.nextReview <= now) {
            dueWords.push(word);
        }
    }
    return dueWords;
}

// ===== 计算掌握度 =====
// ===== 计算掌握度 (Leitner System) =====
function calculateMastery() {
    const wordStats = state.progress.wordStats || {};
    const totalWords = state.vocabulary.length;
    if (totalWords === 0) return 0;

    let masteredCount = 0;
    for (const word of state.vocabulary) {
        const stats = wordStats[word.word];
        // Box 5 视为掌握
        if (stats && stats.box >= 5) {
            masteredCount++;
        }
    }

    return (masteredCount / totalWords) * 100;
}

// ===== 获取待复习数量 =====
function getReviewCount() {
    // 优先显示 Leitner 系统待复习数量
    const dueCount = getDueReviewWords().length;
    if (dueCount > 0) return dueCount;

    const mistakes = state.progress.mistakes || [];
    return mistakes.length;
}

// ===== 更新进度环 =====
function updateProgressRing(percentage) {
    const circle = document.getElementById('progress-circle');
    const circumference = 2 * Math.PI * 68; // r=68
    const offset = circumference - (percentage / 100) * circumference;
    circle.style.strokeDashoffset = offset;
}

// ===== 渲染学习路径 (分页逻辑) =====
function renderPathList() {
    const pathList = document.getElementById('path-list');
    const completedDays = state.progress.completedDays || [];
    const maxDay = state.vocabulary.length > 0 ? Math.max(...state.vocabulary.map(v => v.day)) : 21;

    // 计算当前页显示的起始和结束天数
    const weekStart = (state.currentWeek - 1) * 7 + 1;
    const weekEnd = Math.min(state.currentWeek * 7, maxDay);

    let html = '';
    for (let day = weekStart; day <= weekEnd; day++) {
        const isCompleted = completedDays.includes(day);
        const isCurrent = day === state.currentDay;
        const isLocked = day > state.currentDay;

        let statusClass = isLocked ? 'locked' : (isCompleted ? 'completed' : (isCurrent ? 'current' : ''));
        let nodeIcon = isLocked ? '🔒' : (isCompleted ? '✓' : '★');

        const dayWords = state.vocabulary.filter(w => w.day === day);
        const bestScore = isCompleted ? getDayBestScore(day) : null;
        let scoreHTML = '';
        let statusText = isLocked ? '未解锁' : (isCurrent ? '进行中' : '已完成');

        if (bestScore) {
            const accColor = getAccuracyColor(bestScore.accuracy);
            statusText = '';
            scoreHTML = `
                <div class="path-score-section">
                    <div class="accuracy-badge ${accColor.cssClass}">
                        🎯 ${bestScore.accuracy}%
                    </div>
                    <div class="mini-bar">
                        <div class="mini-bar-fill ${accColor.cssClass}" style="width: ${bestScore.accuracy}%"></div>
                    </div>
                </div>
            `;
        }

        html += `
            <div class="path-item ${statusClass}" data-day="${day}">
                <div class="node">${nodeIcon}</div>
                <div class="info">
                    <div class="title">Day ${day}: ${DAY_LABELS[day - 1] || '词汇'}</div>
                    <div class="subtitle">${dayWords.length} 个单词</div>
                </div>
                ${scoreHTML}
                <div class="status">${statusText}</div>
            </div>
        `;
    }

    pathList.innerHTML = html;

    // 绑定点击
    pathList.querySelectorAll('.path-item:not(.locked)').forEach(item => {
        item.addEventListener('click', () => {
            const day = parseInt(item.dataset.day);
            startDayQuiz(day);
        });
    });
}

// ===== 绑定事件 =====
function bindEvents() {
    // 开始学习 (Smart Start)
    document.getElementById('btn-start').addEventListener('click', () => {
        startSmartReview();
    });

    // 错题复习
    document.getElementById('btn-review').addEventListener('click', startReviewQuiz);

    // 全量测试
    document.getElementById('btn-grand').addEventListener('click', startGrandQuiz);

    // 家长报告
    document.getElementById('btn-parent').addEventListener('click', () => {
        showView('parent');
        renderParentDashboard();
    });

    // 用户切换
    document.getElementById('user-select').addEventListener('change', (e) => {
        switchUser(e.target.value);
    });

    // 退出测试
    document.getElementById('btn-quit').addEventListener('click', confirmQuit);

    // 发音按钮
    document.getElementById('btn-audio').addEventListener('click', playCurrentWord);

    // 输入框回车
    document.getElementById('answer-input').addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const feedbackBar = document.getElementById('feedback-bar');
            if (feedbackBar && feedbackBar.classList.contains('show')) {
                nextQuestion();
            } else {
                checkAnswer();
            }
        }
    });

    // 全局回车（处理非输入框焦点的情况，如选择题）
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            // 如果焦点在输入框，由上面的监听器处理，避免重复触发
            if (document.activeElement === document.getElementById('answer-input')) {
                return;
            }

            const feedbackBar = document.getElementById('feedback-bar');
            if (feedbackBar && feedbackBar.classList.contains('show')) {
                nextQuestion();
            }
        }
    });

    // 继续按钮
    document.getElementById('btn-continue').addEventListener('click', nextQuestion);

    // 返回首页
    document.getElementById('btn-home').addEventListener('click', () => {
        showView('home');
        renderDashboard();
    });

    // 查看错题
    document.getElementById('btn-review-mistakes').addEventListener('click', () => {
        document.getElementById('mistakes-section').classList.toggle('hidden');
    });

    // 关闭家长报告
    document.getElementById('btn-parent-close').addEventListener('click', () => {
        showView('home');
    });

    // ===== 听力模块逻辑 =====
    let listeningData = [];
    let currentListeningIndex = 0;
    let isPlaying = false;

    async function startListening() {
        try {
            const res = await fetch('/api/listening');
            listeningData = await res.json();
        } catch (e) {
            console.error("Failed to load listening data", e);
            listeningData = [];
        }

        if (listeningData.length === 0) {
            alert("暂无听力内容");
            return;
        }

        // 根据已完成天数过滤可用文章
        const completedDays = state.progress.completedDays || [];
        // Day 1 的听力默认解锁
        const unlockedDays = [1, ...completedDays];
        const available = listeningData.filter(l => unlockedDays.includes(l.day));

        if (available.length === 0) {
            alert("完成每日单词学习后解锁对应听力！先去学习 Day 1 的单词吧 🎯");
            return;
        }

        showView('listening');

        // 显示文章选择列表
        const quizArea = document.getElementById('listening-quiz-area');
        document.getElementById('listening-title').textContent = '选择听力练习';
        document.getElementById('listening-script').classList.add('hidden');

        // 隐藏播放按钮（选文章时不需要）
        document.getElementById('btn-play-article').style.display = 'none';
        document.getElementById('btn-show-script').style.display = 'none';

        const completedListening = state.progress.completedListeningDays || [];
        quizArea.innerHTML = `
            <div class="listening-article-list">
                ${available.map(article => {
            const isDone = completedListening.includes(article.day);
            return `
                    <div class="listening-article-item" onclick="selectListeningArticle(${article.day})" style="
                        background: white;
                        padding: 16px 20px;
                        border-radius: var(--radius-lg, 12px);
                        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
                        margin-bottom: 10px;
                        cursor: pointer;
                        display: flex;
                        align-items: center;
                        gap: 12px;
                        transition: transform 0.15s;
                        ${isDone ? 'border-left: 4px solid #58cc02;' : ''}
                    ">
                        <div style="
                            width: 44px; height: 44px;
                            border-radius: 12px;
                            background: ${isDone ? 'linear-gradient(135deg, #a0d911, #7cb305)' : 'linear-gradient(135deg, #58cc02, #46a302)'};
                            display: flex; align-items: center; justify-content: center;
                            color: white; font-weight: 700; font-size: 16px;
                            flex-shrink: 0;
                        ">${isDone ? '✅' : 'D' + article.day}</div>
                        <div>
                            <div style="font-weight: 600; font-size: 15px;">${article.title}${isDone ? ' <span style="color:#58cc02;font-size:12px;">已完成</span>' : ''}</div>
                            <div style="font-size: 12px; color: #999; margin-top: 2px;">📝 ${article.questions.length} 道题</div>
                        </div>
                        <div style="margin-left: auto; color: #ccc; font-size: 18px;">›</div>
                    </div>
                `}).join('')}
            </div>
            <p style="text-align:center; color:#999; font-size:13px; margin-top:12px;">
                🔒 完成更多天的单词学习，解锁更多听力
            </p>
        `;
    }

    // 选择某篇文章后进入听力模式
    window.selectListeningArticle = function (day) {
        currentListeningIndex = listeningData.findIndex(l => l.day === day);
        if (currentListeningIndex < 0) return;

        // 恢复播放按钮
        document.getElementById('btn-play-article').style.display = '';
        document.getElementById('btn-show-script').style.display = '';

        renderListeningSession();
    };

    // 存储用户选择
    let listeningAnswers = {};

    function renderListeningSession() {
        const data = listeningData[currentListeningIndex];
        listeningAnswers = {}; // 重置选择
        document.getElementById('listening-title').textContent = data.title;
        document.getElementById('listening-script').textContent = data.text;
        document.getElementById('listening-script').classList.add('hidden');

        // 渲染题目
        const quizArea = document.getElementById('listening-quiz-area');
        quizArea.innerHTML = data.questions.map((q, idx) => `
        <div class="listening-question" id="lq-${q.id}">
            <h3>${idx + 1}. ${q.question}</h3>
            <div class="choices-grid">
                ${q.options.map((opt, optIdx) => `
                    <button class="choice-btn" data-qid="${q.id}" data-idx="${optIdx}" onclick="selectListeningAnswer(${q.id}, ${optIdx}, this)">
                        ${['A', 'B', 'C'][optIdx]}. ${opt}
                    </button>
                `).join('')}
            </div>
        </div>
    `).join('');

        // 添加提交按钮
        quizArea.innerHTML += `
            <button class="btn-audio-control" id="btn-submit-listening" style="width:100%; margin-top:16px; opacity:0.5; pointer-events:none;">
                📝 提交答案 (0/${data.questions.length})
            </button>
            <div id="listening-result" class="listening-result-card" style="display:none;"></div>
        `;
    }

    // 选择答案（不立即判分）
    window.selectListeningAnswer = function (qId, optIdx, btn) {
        listeningAnswers[qId] = optIdx;

        // 高亮选中项，取消同题其他选中
        const parent = btn.closest('.listening-question');
        parent.querySelectorAll('.choice-btn').forEach(b => {
            b.classList.remove('selected');
        });
        btn.classList.add('selected');

        // 更新提交按钮状态
        const data = listeningData[currentListeningIndex];
        const total = data.questions.length;
        const answered = Object.keys(listeningAnswers).length;
        const submitBtn = document.getElementById('btn-submit-listening');
        submitBtn.textContent = `📝 提交答案 (${answered}/${total})`;

        if (answered >= total) {
            submitBtn.style.opacity = '1';
            submitBtn.style.pointerEvents = 'auto';
            submitBtn.onclick = submitListeningAnswers;
        }
    };

    // 提交并判分
    function submitListeningAnswers() {
        const data = listeningData[currentListeningIndex];
        let correct = 0;

        data.questions.forEach(q => {
            const userAnswer = listeningAnswers[q.id];
            const questionEl = document.getElementById(`lq-${q.id}`);
            const btns = questionEl.querySelectorAll('.choice-btn');

            // 禁用所有按钮
            btns.forEach(b => b.disabled = true);

            if (userAnswer === q.answer) {
                correct++;
                btns[userAnswer].classList.add('correct');
            } else {
                if (userAnswer !== undefined) btns[userAnswer].classList.add('wrong');
                btns[q.answer].classList.add('correct');
            }
        });

        // 加分
        const xpEarned = correct * 10;
        state.xp += xpEarned;

        // 判断是否通过（≥60%）
        const total = data.questions.length;
        const pct = Math.round(correct / total * 100);
        const passed = pct >= 60;
        let passMsg = '';

        if (passed) {
            // 记录听力完成状态
            if (!state.progress.completedListeningDays) {
                state.progress.completedListeningDays = [];
            }
            if (!state.progress.completedListeningDays.includes(data.day)) {
                state.progress.completedListeningDays.push(data.day);
                passMsg = '<div style="color:#58cc02; font-weight:600; margin-top:4px;">🎯 听力已标记为完成！</div>';
            } else {
                passMsg = '<div style="color:#999; font-size:13px; margin-top:4px;">该听力已完成过</div>';
            }
        } else {
            passMsg = '<div style="color:#ff6b6b; font-size:13px; margin-top:4px;">💡 正确率需达到 60% 才能标记为完成，再试一次吧！</div>';
        }

        saveProgress();

        // 隐藏提交按钮，显示结果
        document.getElementById('btn-submit-listening').style.display = 'none';
        const resultEl = document.getElementById('listening-result');
        const emoji = pct === 100 ? '🎉' : pct >= 60 ? '👍' : '💪';

        resultEl.style.display = 'block';
        resultEl.innerHTML = `
            <div class="listening-score">${emoji} ${correct}/${total} 正确 (${pct}%)</div>
            <div class="listening-xp">⭐ +${xpEarned} XP</div>
            ${passMsg}
            <button class="btn-audio-control" onclick="showView('home')" style="width:100%; margin-top:12px;">
                🏠 返回首页
            </button>
        `;

        if (correct === total) {
            playSound('correct');
        } else {
            playSound('wrong');
        }
    }

    // Audio Control
    const speechSynth = window.speechSynthesis;
    let speechUtterance = null;

    document.getElementById('btn-play-article').addEventListener('click', () => {
        if (isPlaying) {
            speechSynth.cancel();
            isPlaying = false;
            document.getElementById('btn-play-article').textContent = '▶️ 播放短文';
        } else {
            const text = listeningData[currentListeningIndex].text;
            speechUtterance = new SpeechSynthesisUtterance(text);
            speechUtterance.lang = 'en-US';
            speechUtterance.rate = 0.9;

            speechUtterance.onend = () => {
                isPlaying = false;
                document.getElementById('btn-play-article').textContent = '▶️ 播放短文';
            };

            speechSynth.speak(speechUtterance);
            isPlaying = true;
            document.getElementById('btn-play-article').textContent = '⏹ 停止播放';
        }
    });

    document.getElementById('btn-show-script').addEventListener('click', () => {
        document.getElementById('listening-script').classList.toggle('hidden');
    });

    document.getElementById('btn-listening-close').addEventListener('click', () => {
        speechSynth.cancel();
        showView('home');
    });

    // Event Listeners for Dashboard
    document.getElementById('btn-listening').addEventListener('click', startListening);
    // 退出预习
    document.getElementById('btn-study-quit').addEventListener('click', () => {
        if (confirm('确定要退出学习吗？')) {
            showView('home');
        }
    });

    // 发音按钮
    document.getElementById('btn-study-audio').addEventListener('click', (e) => {
        e.stopPropagation();
        playStudyWord();
    });

    // 翻转卡片
    document.getElementById('flashcard').addEventListener('click', () => {
        document.getElementById('flashcard').classList.toggle('flipped');
    });

    // 上一个
    document.getElementById('btn-study-prev').addEventListener('click', prevStudyCard);

    // 下一个
    document.getElementById('btn-study-next').addEventListener('click', nextStudyCard);

    // 开始测试
    document.getElementById('btn-start-quiz').addEventListener('click', () => {
        startQuizAfterStudy();
    });

    // 再学一遍
    document.getElementById('btn-study-again').addEventListener('click', () => {
        state.studyIndex = 0;
        showStudyCard();
        document.getElementById('study-complete').classList.add('hidden');
        document.querySelector('.flashcard-container').classList.remove('hidden');
        document.querySelector('.study-actions').classList.remove('hidden');
    });
    // 切换用户
    document.getElementById('user-select').addEventListener('change', (e) => {
        switchUser(e.target.value);
    });
}

// ===== 切换用户 =====
async function switchUser(userId) {
    if (confirm(`确定要切换到 ${userId === 'oli' ? 'Oli' : '测试模式'} 吗？当前学习进度会自动保存。`)) {
        // 保存当前进度
        await saveProgress();

        // 切换用户
        state.currentUser = userId;
        localStorage.setItem('vocab-quest-user', userId);

        // 重新加载页面以刷新数据
        location.reload();
    } else {
        // 恢复选择
        document.getElementById('user-select').value = state.currentUser;
    }
}

// ===== 开始每日学习（先预习再测试） =====
function startDayQuiz(day) {
    // 检查生命值
    if (state.hearts <= 0) {
        showRescueModal();
        return;
    }

    state.studyDay = day;
    state.studyWords = state.vocabulary.filter(w => w.day === day);

    if (state.studyWords.length === 0) {
        // 如果该天没有单词（如 Day 21 复习页），标记为完成以允许解锁后续天数
        markDayCompleted(day);
        saveProgress();
        renderDashboard();

        // 显示特别说明
        if (confirm(`第 ${day} 天是专门的复习/总结日，没有新单词。该天已标记为“通过”！\n\n是否现在开始“全量测试”来查漏补缺？`)) {
            startGrandQuiz();
        }
        return;
    }

    // 进入预习模式
    state.studyIndex = 0;
    showView('study');
    showStudyCard();
}

// ===== 智能开始 (Smart Review) =====
function startSmartReview() {
    // 检查生命值
    if (state.hearts <= 0) {
        showRescueModal();
        return;
    }

    // 1. 获取待复习单词 (Leitner)
    const dueWords = getDueReviewWords();

    // 2. 如果复习词太多(>10)，优先复习
    if (dueWords.length >= 10) {
        if (confirm(`你有 ${dueWords.length} 个单词需要复习。要现在开始复习吗？`)) {
            state.quizMode = 'review';
            state.quizWords = dueWords;
            shuffleArray(state.quizWords);
            // 限制单次复习数量
            if (state.quizWords.length > 20) state.quizWords = state.quizWords.slice(0, 20);
            startQuiz();
            return;
        }
    }

    // 3. 否则进入今天的学习 (Day X)
    startDayQuiz(state.currentDay);
}

// ===== 开始复习测试 =====
function startReviewQuiz() {
    // 检查生命值
    if (state.hearts <= 0) {
        showRescueModal();
        return;
    }

    const mistakes = state.progress.mistakes || [];
    if (mistakes.length === 0) {
        alert('暂无错题，继续保持！');
        return;
    }

    state.quizMode = 'review';
    state.quizWords = mistakes.map(w =>
        state.vocabulary.find(v => v.word === w) || { word: w, meaning: '未知' }
    ).filter(w => w);

    shuffleArray(state.quizWords);

    // 限制数量，防止一次做得太累
    if (state.quizWords.length > 30) {
        state.quizWords = state.quizWords.slice(0, 30);
    }

    startQuiz();
}

// ===== 开始全量测试 =====
function startGrandQuiz() {
    // 检查生命值
    if (state.hearts <= 0) {
        showRescueModal();
        return;
    }

    state.quizMode = 'grand';
    state.quizWords = [...state.vocabulary];
    shuffleArray(state.quizWords);

    // 限制数量
    if (state.quizWords.length > 30) {
        state.quizWords = state.quizWords.slice(0, 30);
    }

    startQuiz();
}

// ===== 开始测试 =====
function startQuiz() {
    state.currentQuestion = 0;
    state.sessionScore = 0;
    state.sessionMistakes = [];
    state.streakCount = 0;
    state.startTime = Date.now();

    showView('quiz');
    updateHeartsDisplay();
    renderQuestion();
}

// ===== 更新生命值显示 =====
function updateHeartsDisplay() {
    const container = document.getElementById('hearts-display');
    let html = '';
    for (let i = 0; i < state.maxHearts; i++) {
        html += `<span class="heart ${i < state.hearts ? '' : 'empty'}">${i < state.hearts ? '❤️' : '💔'}</span>`;
    }
    container.innerHTML = html;
}

// ===== 渲染问题 =====
function renderQuestion() {
    const q = state.quizWords[state.currentQuestion];
    if (!q) {
        finishQuiz();
        return;
    }

    // 更新进度条
    const progress = (state.currentQuestion / state.quizWords.length) * 100;
    document.getElementById('quiz-progress').style.width = progress + '%';

    // 随机题型
    const type = state.questionTypes[Math.floor(Math.random() * state.questionTypes.length)];

    // 重置UI
    hideFeedback();
    document.getElementById('input-mode').classList.add('hidden');
    document.getElementById('choice-mode').classList.add('hidden');
    document.getElementById('btn-audio').classList.add('hidden');
    document.getElementById('question-example').classList.add('hidden');

    switch (type) {
        case 'choice':
            renderChoiceQuestion(q);
            break;
        case 'spell':
            renderSpellQuestion(q);
            break;
        case 'listen':
            renderListenQuestion(q);
            break;
        case 'fill':
            renderFillQuestion(q);
            break;
    }
}

// ===== 选择题 =====
function renderChoiceQuestion(q) {
    document.getElementById('question-type').textContent = '选择正确释义';
    document.getElementById('question-content').textContent = q.word;

    // 生成选项（1正3错）
    const choices = [q.meaning];
    const others = state.vocabulary.filter(w => w.word !== q.word);
    shuffleArray(others);

    for (let i = 0; i < 3 && i < others.length; i++) {
        choices.push(others[i].meaning);
    }
    shuffleArray(choices);

    const choiceContainer = document.getElementById('choice-mode');
    choiceContainer.classList.remove('hidden');
    choiceContainer.innerHTML = choices.map((c, i) => `
        <button class="choice-btn" data-choice="${c}">${c}</button>
    `).join('');

    // 绑定点击
    choiceContainer.querySelectorAll('.choice-btn').forEach(btn => {
        btn.addEventListener('click', () => selectChoice(btn, q.meaning));
    });
}

// ===== 拼写题 =====
function renderSpellQuestion(q) {
    document.getElementById('question-type').textContent = '拼写单词';
    document.getElementById('question-content').textContent = q.meaning;

    if (q.example) {
        const example = document.getElementById('question-example');
        example.textContent = q.example.replace(new RegExp(q.word, 'gi'), '_____');
        example.classList.remove('hidden');
    }

    const inputMode = document.getElementById('input-mode');
    inputMode.classList.remove('hidden');

    const input = document.getElementById('answer-input');
    input.value = '';
    input.className = 'input-answer';
    input.placeholder = '输入单词...';
    input.focus();

    // 存储正确答案
    input.dataset.answer = q.word.toLowerCase();
}

// ===== 听力题 =====
// ===== 听力题 =====
function renderListenQuestion(q) {
    document.getElementById('question-type').textContent = '听写单词';
    document.getElementById('question-content').textContent = '点击播放，听写单词';

    // 显示例句上下文 (解决同音词歧义)
    if (q.example) {
        const example = document.getElementById('question-example');
        // 将单词替换为下划线 (忽略大小写)
        const maskedExample = q.example.replace(new RegExp(q.word, 'gi'), '_____');
        example.textContent = maskedExample;
        example.classList.remove('hidden');
    }

    const audioBtn = document.getElementById('btn-audio');
    audioBtn.classList.remove('hidden');
    audioBtn.dataset.word = q.word;

    // 自动播放一次
    setTimeout(() => playCurrentWord(), 500);

    const inputMode = document.getElementById('input-mode');
    inputMode.classList.remove('hidden');

    const input = document.getElementById('answer-input');
    input.value = '';
    input.className = 'input-answer';
    input.placeholder = '输入你听到的单词...';
    input.focus();

    input.dataset.answer = q.word.toLowerCase();
}

// ===== 填空题 =====
function renderFillQuestion(q) {
    document.getElementById('question-type').textContent = '填空补全';

    if (q.example) {
        document.getElementById('question-content').textContent = q.meaning;
        const example = document.getElementById('question-example');
        example.textContent = q.example.replace(new RegExp(q.word, 'gi'), '_____');
        example.classList.remove('hidden');
    } else {
        // 没有例句就变成拼写题
        document.getElementById('question-content').textContent = q.meaning;
    }

    const inputMode = document.getElementById('input-mode');
    inputMode.classList.remove('hidden');

    const input = document.getElementById('answer-input');
    input.value = '';
    input.className = 'input-answer';
    input.placeholder = '填入正确单词...';
    input.focus();

    input.dataset.answer = q.word.toLowerCase();
}

// ===== 播放发音 =====
// ===== 播放发音 =====
function playCurrentWord() {
    // 优先使用 DOM 绑定的词（听力题），如果没有则使用当前题目
    let word = document.getElementById('btn-audio').dataset.word;

    // 如果不在听力题（或者按钮隐藏），直接获取当前题目的单词
    if (!word || document.getElementById('btn-audio').classList.contains('hidden')) {
        const q = state.quizWords[state.currentQuestion];
        if (q) word = q.word;
    }

    if (word && 'speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = 'en-US';
        utterance.rate = 0.8;
        speechSynthesis.speak(utterance);
    }
}

// ===== 选择答案 =====
function selectChoice(btn, correctAnswer) {
    const selected = btn.dataset.choice;
    const isCorrect = selected === correctAnswer;

    // 禁用所有按钮
    document.querySelectorAll('.choice-btn').forEach(b => {
        b.disabled = true;
        if (b.dataset.choice === correctAnswer) {
            b.classList.add('correct');
        }
    });

    if (isCorrect) {
        handleCorrect();
    } else {
        btn.classList.add('wrong');
        handleWrong(state.quizWords[state.currentQuestion]);
    }
}

// ===== 检查输入答案 =====
function checkAnswer() {
    const input = document.getElementById('answer-input');
    const answer = input.value.trim().toLowerCase();
    const correct = input.dataset.answer;

    if (!answer) return;

    const isCorrect = answer === correct;

    if (isCorrect) {
        input.classList.add('correct');
        handleCorrect();
    } else {
        // Debug
        console.log('Wrong answer:', answer, 'Expected:', correct);
        console.log('Codes:', answer.split('').map(c => c.charCodeAt(0)), 'Expected:', correct.split('').map(c => c.charCodeAt(0)));
        if (answer.trim() == correct.trim() || answer.length == correct.length) {
            alert(`Debug: Info\nInput: '${answer}' (${answer.split('').map(c => c.charCodeAt(0))})\nCorrect: '${correct}' (${correct.split('').map(c => c.charCodeAt(0))})`);
        }

        input.classList.add('wrong');
        handleWrong(state.quizWords[state.currentQuestion]);
    }
}

// ===== 处理正确 =====
function handleCorrect() {
    state.sessionScore++;
    state.streakCount++;

    // 计算XP
    let xpGain = XP_PER_CORRECT;
    if (state.streakCount >= 3) {
        xpGain += XP_STREAK_BONUS;
    }
    state.xp += xpGain;

    // 更新单词统计
    const word = state.quizWords[state.currentQuestion].word;
    updateWordStats(word, true);

    // 显示XP弹出
    showXPPopup(xpGain);

    // 🔊感官反馈：答对自动发音
    playCurrentWord();

    // 显示连击
    if (state.streakCount >= 2) {
        showStreakIndicator();
    }

    // 显示反馈
    if (state.quizMode === 'rescue') {
        state.rescueProgress++;
        showFeedback(true, '救援行动', `进度：${state.rescueProgress}/${state.rescueTarget}`);

        if (state.rescueProgress >= state.rescueTarget) {
            setTimeout(showRescueSuccess, 1000);
        }
    } else {
        showFeedback(true, '太棒了！', `+${xpGain} 经验值`);
    }
}

// ===== 处理错误 =====
function handleWrong(question) {
    state.streakCount = 0;
    state.hearts--;

    // 记录错题
    state.sessionMistakes.push(question);

    // 更新单词统计
    updateWordStats(question.word, false);

    // 添加到全局错题
    addToMistakes(question.word);

    // 👻 Ghost Review:错题重现机制
    // 如果不在救援模式，且当前题目不是最后一道，则将错题插入到队列后方
    if (state.quizMode !== 'rescue') {
        // 插入到当前位置 + 3 的位置，或者队尾
        const insertIndex = Math.min(state.quizWords.length, state.currentQuestion + 4);
        // 克隆问题对象，标记为重试（可选：不给XP，或者少给）
        const retryQuestion = { ...question, isRetry: true };
        state.quizWords.splice(insertIndex, 0, retryQuestion);
        console.log(`Ghost Review: '${question.word}' re-inserted at index ${insertIndex}`);

        // 更新总数显示（如果有的话）
        const quizProgress = document.getElementById('quiz-progress');
        if (quizProgress) {
            // 重新计算进度条基准可能比较复杂，这里暂不处理，
            // 或者让进度条回退一点点，给用户"路变长了"的感觉
        }
    }

    // 更新心形显示
    updateHeartsDisplay();

    // 显示反馈
    showFeedback(false, '再接再厉！', `正确答案: ${question.word}`);

    // 检查生命值
    if (state.hearts <= 0) {
        if (state.quizMode === 'rescue') {
            // 救援模式下失败
            showRescueFail();
        } else {
            //以此处触发救援邀请
            showRescueModal();
        }
    }
}

// ===== 显示救援邀请 =====
function showRescueModal() {
    document.getElementById('rescue-modal').classList.remove('hidden');

    // 绑定救援按钮
    document.getElementById('btn-start-rescue').onclick = startRescueMode;
    document.getElementById('btn-quit-rescue').onclick = () => {
        document.getElementById('rescue-modal').classList.add('hidden');
        finishQuiz();
    };
}

// ===== 开始救援模式 =====
function startRescueMode() {
    try {
        document.getElementById('rescue-modal').classList.add('hidden');

        // 设置救援状态
        state.quizMode = 'rescue';
        state.rescueTarget = 3;
        state.rescueProgress = 0;
        state.sessionScore = 0; // 重置分数
        state.startTime = Date.now();
        state.streakCount = 0;
        state.currentQuestion = 0; // 重置当前题目索引

        // 切换到测试视图
        showView('quiz');
        updateHeartsDisplay();

        // 准备救援词汇
        // 1. 获取错题
        let poolStrings = [...(state.progress.mistakes || [])];

        // 2. 如果不够，从词库随机补充
        if (poolStrings.length < 10 && state.vocabulary.length > 0) {
            const allWords = state.vocabulary.map(v => v.word);
            const others = allWords.filter(w => !poolStrings.includes(w));
            shuffleArray(others);
            poolStrings = poolStrings.concat(others.slice(0, 10));
        }

        // 3. 转换为对象
        let poolObjects = poolStrings.map(w =>
            state.vocabulary.find(v => v.word === w) || { word: w, meaning: '未知' }
        );

        // 4. 筛选题目
        state.quizWords = [];
        if (poolObjects.length === 0) {
            alert('词库为空，无法开始救援！');
            showView('home');
            return;
        }

        while (state.quizWords.length < 10 && poolObjects.length > 0) {
            const idx = Math.floor(Math.random() * poolObjects.length);
            state.quizWords.push(poolObjects[idx]);
            poolObjects.splice(idx, 1);
        }

        console.log('Rescue words prepared:', state.quizWords.length);

        // 更新UI提示
        showFeedback(true, '救援行动开始！', '目标：连续答对3题');

        renderQuestion();

    } catch (error) {
        console.error('Start Rescue failed:', error);
        alert('启动救援模式失败，请刷新重试');
        showView('home');
    }
}

// ===== 显示救援失败 =====
function showRescueFail() {
    document.getElementById('rescue-fail-modal').classList.remove('hidden');

    document.getElementById('btn-retry-rescue').onclick = () => {
        document.getElementById('rescue-fail-modal').classList.add('hidden');
        startRescueMode();
    };

    document.getElementById('btn-quit-fail').onclick = () => {
        document.getElementById('rescue-fail-modal').classList.add('hidden');
        finishQuiz();
    };
}

// ===== 显示救援成功 =====
function showRescueSuccess() {
    document.getElementById('rescue-success-modal').classList.remove('hidden');

    document.getElementById('btn-continue-rescue').onclick = () => {
        document.getElementById('rescue-success-modal').classList.add('hidden');
        // 恢复满血
        state.hearts = state.maxHearts;
        updateHeartsDisplay();

        // 返回首页 或者 这里其实应该根据需求决定是继续还是回首页
        // 简单起见，救援成功视为“通关”，返回首页
        showView('home');
        renderDashboard();
    };
}


// ===== 更新单词统计 (Leitner System) =====
function updateWordStats(word, isCorrect) {
    if (!state.progress.wordStats) {
        state.progress.wordStats = {};
    }

    if (!state.progress.wordStats[word]) {
        state.progress.wordStats[word] = {
            correct: 0,
            wrong: 0,
            lastStudy: null,
            box: 0, // Leitner Box (0-5)
            nextReview: 0
        };
    }

    const stats = state.progress.wordStats[word];
    const now = Date.now();
    stats.lastStudy = new Date().toISOString();

    if (isCorrect) {
        stats.correct++;
        // 升级 Box
        stats.box = Math.min(5, (stats.box || 0) + 1);

        // 计算下次复习时间
        // Interval: 1, 3, 7, 15, 30 days
        const intervals = [0, 1, 3, 7, 15, 30];
        const daysToAdd = intervals[stats.box];
        stats.nextReview = now + (daysToAdd * 24 * 60 * 60 * 1000);

    } else {
        stats.wrong++;
        // 降级 Box (回到 Box 1，而不是 0，避免完全从头开始)
        stats.box = 1;
        // 立即/明日复习
        stats.nextReview = now;
    }
}

// ===== 添加到全局错题本 =====
function addToMistakes(word) {
    if (!state.progress.mistakes) {
        state.progress.mistakes = [];
    }
    if (!state.progress.mistakes.includes(word)) {
        state.progress.mistakes.push(word);
    }
}

// ===== 显示XP弹出 =====
function showXPPopup(xp) {
    const popup = document.getElementById('xp-popup');
    popup.textContent = `+${xp} XP`;
    popup.classList.add('show');

    setTimeout(() => {
        popup.classList.remove('show');
    }, 800);
}

// ===== 显示连击提示 =====
function showStreakIndicator() {
    const indicator = document.getElementById('streak-indicator');
    document.getElementById('streak-count').textContent = state.streakCount;
    indicator.classList.add('show');

    setTimeout(() => {
        indicator.classList.remove('show');
    }, 1500);
}

// ===== 显示反馈栏 =====
function showFeedback(isCorrect, title, detail) {
    const bar = document.getElementById('feedback-bar');
    bar.className = `feedback-bar show ${isCorrect ? 'correct' : 'wrong'}`;

    document.getElementById('feedback-icon').textContent = isCorrect ? '✓' : '✗';
    document.getElementById('feedback-title').textContent = title;
    document.getElementById('feedback-detail').textContent = detail;
}

// ===== 隐藏反馈栏 =====
function hideFeedback() {
    document.getElementById('feedback-bar').classList.remove('show');
}

// ===== 下一题 =====
function nextQuestion() {
    // 只有在非救援模式下，生命值耗尽才结束
    if (state.hearts <= 0 && state.quizMode !== 'rescue') {
        finishQuiz();
        return;
    }

    state.currentQuestion++;
    renderQuestion();
}

// ===== 完成测试 =====
function finishQuiz() {
    // 计算结果
    const total = state.quizWords.length;
    const correct = state.sessionScore;
    const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0;
    const xpEarned = correct * XP_PER_CORRECT;
    const elapsed = Math.round((Date.now() - state.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;

    // 更新连击
    updateStreak();

    // 标记当天完成
    if (state.quizMode === 'day') {
        markDayCompleted(state.currentDay);
    }

    // 保存进度
    saveProgress();

    // 渲染结果
    showView('result');

    const titles = ['太棒了！', '做得好！', '继续努力！', '不要放弃！'];
    const titleIndex = accuracy >= 90 ? 0 : (accuracy >= 70 ? 1 : (accuracy >= 50 ? 2 : 3));

    document.getElementById('result-title').textContent = titles[titleIndex];
    document.getElementById('result-score').textContent = `${correct}/${total} 正确`;
    document.getElementById('result-xp').innerHTML = `⭐ +${xpEarned} 经验值`;
    document.getElementById('result-streak').textContent = state.streak + ' 天';
    document.getElementById('result-time').textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    document.getElementById('result-accuracy').textContent = accuracy + '%';

    // 渲染错题
    const mistakesSection = document.getElementById('mistakes-section');
    const mistakesList = document.getElementById('mistakes-list');

    if (state.sessionMistakes.length > 0) {
        mistakesList.innerHTML = state.sessionMistakes.map(m => `
            <div class="mistake-item">
                <span class="word">${m.word}</span>
                <span class="meaning">${m.meaning}</span>
            </div>
        `).join('');
    } else {
        mistakesSection.classList.add('hidden');
    }
}

// ===== 更新连击天数 =====
function updateStreak() {
    const today = new Date().toDateString();
    const lastStudy = state.progress.lastStudyDate;

    if (lastStudy) {
        const lastDate = new Date(lastStudy).toDateString();
        if (lastDate !== today) {
            const yesterday = new Date(Date.now() - 86400000).toDateString();
            if (lastDate === yesterday) {
                state.streak = (state.streak || 0) + 1;
            } else {
                state.streak = 1;
            }
        }
        // 如果 lastDate === today，说明今天已经学过了，保持原样即可
        if (state.streak === 0) {
            state.streak = 1; // 首次恢复
        }
    } else {
        state.streak = 1;
    }

    state.progress.lastStudyDate = new Date().toISOString();
    state.progress.streak = state.streak;
}

// ===== 标记当天完成 =====
function markDayCompleted(day) {
    if (!state.progress.completedDays) {
        state.progress.completedDays = [];
    }

    if (!state.progress.completedDays.includes(day)) {
        state.progress.completedDays.push(day);

        // 首次完成，增加生命值上限
        if (state.maxHearts < 10) {
            state.maxHearts++;
            state.hearts++; // 奖励一颗心
            showFeedback(true, '生命上限提升！', `当前上限：${state.maxHearts} ❤️`);
        }
    }
}


// ===== 保存进度 =====
async function saveProgress() {
    state.progress.xp = state.xp;
    state.progress.hearts = state.hearts;

    // 添加历史记录
    if (!state.progress.history) {
        state.progress.history = [];
    }

    // 只保存有效的学习记录 (总数 > 0)
    if (state.quizWords.length > 0) {
        state.progress.history.push({
            date: new Date().toISOString(),
            mode: state.quizMode,
            day: state.currentDay,
            score: state.sessionScore,
            total: state.quizWords.length,
            xp: state.sessionScore * XP_PER_CORRECT
        });
    }

    try {
        await fetch('/api/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                user: state.currentUser,
                progress: state.progress
            })
        });
    } catch (error) {
        console.error('保存进度失败:', error);
    }
}

// ===== 确认退出 =====
function confirmQuit() {
    if (confirm('确定要退出测试吗？进度将被保存。')) {
        saveProgress();
        showView('home');
        renderDashboard();
    }
}

// ===== 渲染家长仪表板 =====
function renderParentDashboard() {
    const p = state.progress;
    const completedDays = p.completedDays || [];

    // 统计已学单词
    const masteredWords = Object.keys(p.wordStats || {}).filter(w => {
        const s = p.wordStats[w];
        return s.correct > 0 && s.correct >= s.wrong * 2;
    }).length;

    document.getElementById('parent-words').textContent = masteredWords;
    document.getElementById('parent-streak').textContent = state.streak;

    // 构建每天最佳成绩数组（按天数排序）
    const dayScores = [];
    for (const day of completedDays) {
        const best = getDayBestScore(day);
        if (best) {
            dayScores.push({ day, ...best });
        }
    }
    dayScores.sort((a, b) => a.day - b.day);

    // 平均正确率
    const avgAcc = dayScores.length > 0
        ? Math.round(dayScores.reduce((sum, d) => sum + d.accuracy, 0) / dayScores.length)
        : 0;
    document.getElementById('parent-avg-acc').textContent = avgAcc + '%';

    // 渲染趋势横幅
    renderTrendBanner(dayScores);

    // 渲染趋势折线图
    renderTrendChart(dayScores);

    // 渲染每日成绩卡片
    renderDailyCards(dayScores);

    // 错词排行
    const topMistakes = document.getElementById('top-mistakes');
    const wordStats = p.wordStats || {};
    const sortedWords = Object.entries(wordStats)
        .filter(([_, s]) => s.wrong > 0)
        .sort((a, b) => b[1].wrong - a[1].wrong)
        .slice(0, 10);

    topMistakes.innerHTML = sortedWords.map(([word, stats]) => `
        <div class="mistake-item">
            <span class="word">${word}</span>
            <span class="meaning">错 ${stats.wrong} 次</span>
        </div>
    `).join('') || '<p style="color:var(--text-muted);text-align:center;">暂无错词</p>';

    // 绑定折叠按钮
    const toggleBtn = document.getElementById('btn-toggle-analysis');
    if (toggleBtn && !toggleBtn._bound) {
        toggleBtn._bound = true;
        toggleBtn.addEventListener('click', () => {
            const body = document.getElementById('analysis-body');
            const arrow = document.getElementById('collapse-arrow');
            body.classList.toggle('hidden');
            arrow.textContent = body.classList.contains('hidden') ? '▼' : '▲';
        });
    }

    // 渲染深度分析
    renderDeepAnalytics();
}

// ===== 渲染趋势横幅 =====
function renderTrendBanner(dayScores) {
    const banner = document.getElementById('report-trend-banner');
    if (dayScores.length < 2) {
        banner.innerHTML = '';
        return;
    }

    // 对比最近部分 vs 之前部分
    const midpoint = Math.max(1, dayScores.length - 5);
    const recent = dayScores.slice(midpoint);
    const earlier = dayScores.slice(0, midpoint);

    const recentAvg = Math.round(recent.reduce((s, d) => s + d.accuracy, 0) / recent.length);

    if (earlier.length === 0) {
        banner.innerHTML = `
            <div class="trend-banner trend-neutral">
                <span class="trend-icon">📊</span>
                <div class="trend-text">
                    <div class="trend-title">最近 ${recent.length} 天平均正确率 ${recentAvg}%</div>
                    <div class="trend-subtitle">继续学习更多天后可以看到趋势变化</div>
                </div>
            </div>`;
        return;
    }

    const earlierAvg = Math.round(earlier.reduce((s, d) => s + d.accuracy, 0) / earlier.length);
    const diff = recentAvg - earlierAvg;

    let icon, title, subtitle, trendClass;
    if (diff > 5) {
        icon = '📈'; title = '进步明显！';
        subtitle = `最近正确率 ${recentAvg}%，比之前 ${earlierAvg}% 提升了 ${diff} 个百分点`;
        trendClass = 'trend-up';
    } else if (diff < -5) {
        icon = '📉'; title = '需要关注';
        subtitle = `最近正确率 ${recentAvg}%，比之前 ${earlierAvg}% 下降了 ${Math.abs(diff)} 个百分点`;
        trendClass = 'trend-down';
    } else {
        icon = '➡️'; title = '保持稳定';
        subtitle = `最近正确率 ${recentAvg}%，与之前 ${earlierAvg}% 基本持平`;
        trendClass = 'trend-stable';
    }

    banner.innerHTML = `
        <div class="trend-banner ${trendClass}">
            <span class="trend-icon">${icon}</span>
            <div class="trend-text">
                <div class="trend-title">${title}</div>
                <div class="trend-subtitle">${subtitle}</div>
            </div>
        </div>`;
}

// ===== 渲染 SVG 趋势折线图 =====
function renderTrendChart(dayScores) {
    const container = document.getElementById('trend-chart-area');

    if (dayScores.length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted);text-align:center;padding:20px;">完成学习后这里会显示正确率趋势图</p>';
        return;
    }

    // 数据采样：针对 40 天过长的情况，仅展示最近 14 次的学习趋势，确保 Apple 式的清晰感
    const displayScores = dayScores.length > 14 ? dayScores.slice(-14) : dayScores;
    const dayScoresFinal = displayScores;

    const W = 540, H = 200;
    const padL = 40, padR = 20, padT = 20, padB = 40;
    const chartW = W - padL - padR;
    const chartH = H - padT - padB;

    // 计算坐标点
    const points = dayScoresFinal.map((d, i) => {
        const x = padL + (dayScoresFinal.length === 1 ? chartW / 2 : (i / (dayScoresFinal.length - 1)) * chartW);
        const y = padT + chartH - (d.accuracy / 100) * chartH;
        return { x, y, ...d };
    });

    // 折线路径
    const linePath = points.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' ');

    // 渐变填充区域
    const areaPath = linePath +
        ` L ${points[points.length - 1].x.toFixed(1)} ${padT + chartH}` +
        ` L ${points[0].x.toFixed(1)} ${padT + chartH} Z`;

    // Y轴刻度线
    const yLines = [0, 25, 50, 75, 100].map(v => {
        const y = padT + chartH - (v / 100) * chartH;
        return `<line x1="${padL}" y1="${y}" x2="${W - padR}" y2="${y}" stroke="#eee" stroke-width="1"/>
                <text x="${padL - 8}" y="${y + 4}" text-anchor="end" fill="#aaa" font-size="11">${v}%</text>`;
    }).join('');

    // 70%参考线
    const refY = padT + chartH - (70 / 100) * chartH;
    const refLine = `<line x1="${padL}" y1="${refY}" x2="${W - padR}" y2="${refY}" stroke="#FFD93D" stroke-width="1" stroke-dasharray="4,3"/>`;

    // 数据点 + X轴标签
    const dotsAndLabels = points.map(p => {
        const color = p.accuracy >= 90 ? '#58CC02' : (p.accuracy >= 70 ? '#FF9600' : '#FF4B4B');
        return `
            <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="5" fill="${color}" stroke="white" stroke-width="2"/>
            <text x="${p.x.toFixed(1)}" y="${padT + chartH + 20}" text-anchor="middle" fill="#999" font-size="11">D${p.day}</text>
            <text x="${p.x.toFixed(1)}" y="${p.y.toFixed(1) - 10}" text-anchor="middle" fill="${color}" font-size="11" font-weight="600">${p.accuracy}%</text>
        `;
    }).join('');

    container.innerHTML = `
        <svg viewBox="0 0 ${W} ${H}" style="width:100%;height:auto;max-height:220px;" preserveAspectRatio="xMidYMid meet">
            <defs>
                <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#58CC02" stop-opacity="0.2"/>
                    <stop offset="100%" stop-color="#58CC02" stop-opacity="0.02"/>
                </linearGradient>
            </defs>
            ${yLines}
            ${refLine}
            <path d="${areaPath}" fill="url(#areaGrad)"/>
            <path d="${linePath}" fill="none" stroke="#58CC02" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            ${dotsAndLabels}
        </svg>
        <div style="text-align:center;font-size:11px;color:#bbb;margin-top:4px;">虚线为70%及格线</div>
    `;
}

// ===== 渲染每日成绩卡片 =====
function renderDailyCards(dayScores) {
    const container = document.getElementById('daily-cards-area');

    if (dayScores.length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted);text-align:center;padding:20px;">还没有已完成的每日学习记录</p>';
        return;
    }

    // 最近完成的排在前面
    const sorted = [...dayScores].sort((a, b) => b.day - a.day);

    container.innerHTML = sorted.map(d => {
        const accColor = getAccuracyColor(d.accuracy);
        const barColor = d.accuracy >= 90 ? '#58CC02' : (d.accuracy >= 70 ? '#FF9600' : '#FF4B4B');

        return `
            <div class="daily-card">
                <div class="daily-card-header">
                    <div class="daily-card-day">第${d.day}天</div>
                    <div class="daily-card-label">${DAY_LABELS[d.day - 1] || '词汇'}</div>
                    <div class="daily-card-acc ${accColor.cssClass}">${d.accuracy}%</div>
                </div>
                <div class="daily-card-bar">
                    <div class="daily-card-bar-fill" style="width:${d.accuracy}%;background:${barColor};"></div>
                </div>
                <div class="daily-card-meta">
                    <span>✅ ${d.score}/${d.total} 正确</span>
                    <span>🔄 练习 ${d.attempts} 次</span>
                </div>
            </div>
        `;
    }).join('');
}

// ===== 深度分析模块 =====
const TOPIC_MAP = {
    // Verbs
    1: '核心动词', 2: '核心动词', 3: '核心动词',
    // Adjectives
    4: '形状描述', 5: '感官形容词', 6: '情感形容词', 7: '性格描述',
    // Topics
    22: '健康生活', 23: '社区服务', 24: '自然科学', 25: '动物保护',
    27: '科学发现', 28: '社交礼仪', 29: '环境保护', 30: '挑战与意志',
    31: '太空探索', 32: '传统文化', 33: '公民责任', 34: '职业规划', 35: '终极挑战',
    36: '智能技术', 37: '可持续发展', 38: '意志与追求', 39: '职业素养', 40: '文化交流'
};

let wordToDayMap = null;

async function ensureWordMap() {
    if (wordToDayMap) return;
    try {
        const res = await fetch('/api/vocabulary'); // Returns [{word, meaning, day}, ...]
        const data = await res.json();
        wordToDayMap = {};
        data.forEach(item => {
            wordToDayMap[item.word] = item.day;
        });
    } catch (e) {
        console.error("Failed to load vocabulary map", e);
        wordToDayMap = {};
    }
}

async function renderDeepAnalytics() {
    await ensureWordMap();
    const p = state.progress;
    const stats = p.wordStats || {};

    // 1. Calculate Topic Stats
    const topicStats = {};
    const hardestWords = [];

    Object.entries(stats).forEach(([word, s]) => {
        const day = wordToDayMap[word];
        if (!day) return; // Skip unknown words

        const topic = TOPIC_MAP[day] || '其他';
        if (!topicStats[topic]) {
            topicStats[topic] = { correct: 0, wrong: 0, total: 0 };
        }
        topicStats[topic].correct += s.correct;
        topicStats[topic].wrong += s.wrong;
        topicStats[topic].total += (s.correct + s.wrong);

        // Identify Hardest Words (Total >= 3 && Accuracy < 60%)
        const total = s.correct + s.wrong;
        if (total >= 3 && (s.correct / total) < 0.6) {
            hardestWords.push({ word, acc: Math.round(s.correct / total * 100), total });
        }
    });

    // 2. Render Radar (Bars)
    const radarContainer = document.getElementById('topic-radar');
    const sortedTopics = Object.entries(topicStats).sort((a, b) => b[1].total - a[1].total); // Sort by volume

    radarContainer.innerHTML = sortedTopics.map(([topic, s]) => {
        if (s.total === 0) return '';
        const acc = Math.round(s.correct / s.total * 100);
        let colorClass = 'high';
        let colorHex = 'var(--duo-green)';

        if (acc < 60) { colorClass = 'weak'; colorHex = '#FF6B6B'; }
        else if (acc < 80) { colorClass = 'medium'; colorHex = '#FFD93D'; }

        return `
            <div class="radar-item">
                <div class="radar-label">${topic}</div>
                <div class="radar-bar-bg">
                    <div class="radar-bar-fill ${colorClass}" style="width: ${acc}%; background-color: ${colorHex};"></div>
                </div>
                <div class="radar-value">${acc}%</div>
            </div>
        `;
    }).join('') || '<p style="color:var(--text-muted);text-align:center;font-size:12px;">暂无足够数据分析</p>';

    // 3. Render Hardest Words
    const hardestContainer = document.getElementById('hardest-words');
    hardestWords.sort((a, b) => a.acc - b.acc); // Lowest acc first

    hardestContainer.innerHTML = hardestWords.slice(0, 5).map(w => `
        <div class="mistake-item hard">
            <span class="word">${w.word}</span>
            <span class="meaning">正确率 ${w.acc}% (${w.total}次)</span>
        </div>
    `).join('') || '<div class="mistake-item"><span class="meaning">🎉 暂无顽固错词，太棒了！</span></div>';

    // 4. Generate AI Advice
    const adviceBox = document.getElementById('ai-advice');
    let advice = "";

    // Logic for advice
    const weakTopics = Object.entries(topicStats)
        .filter(([_, s]) => s.total >= 5 && (s.correct / s.total) < 0.7) // Valid sample size & < 70%
        .map(([t]) => t);

    if (weakTopics.length > 0) {
        advice += `⚠️ <strong>关注弱项</strong>：您的 <strong>${weakTopics.join('、')}</strong> 需要加强。建议多朗读相关例句，增强语感。<br>`;
    } else {
        advice += `🌟 <strong>表现优异</strong>：您的各项能力发展均衡！<br>`;
    }

    if (hardestWords.length > 0) {
        advice += `🔥 <strong>重点突破</strong>：今天请特别复习 <strong>"${hardestWords[0].word}"</strong>${hardestWords[1] ? ` 和 <strong>"${hardestWords[1].word}"</strong>` : ''}。`;
    } else {
        advice += `🚀 <strong>保持势头</strong>：目前没有顽固错词，尝试挑战更多新词吧！`;
    }

    adviceBox.innerHTML = advice;
}

// 显示当前学习卡片
function showStudyCard() {
    const word = state.studyWords[state.studyIndex];
    if (!word) return;

    // 更新进度
    const progress = ((state.studyIndex + 1) / state.studyWords.length) * 100;
    document.getElementById('study-progress').style.width = progress + '%';
    document.getElementById('study-current').textContent = state.studyIndex + 1;
    document.getElementById('study-total').textContent = state.studyWords.length;

    // 更新卡片内容
    document.getElementById('study-word').textContent = word.word;
    document.getElementById('study-meaning').textContent = word.meaning;
    document.getElementById('study-example').textContent = word.example || '暂无例句';
    document.getElementById('study-example-cn').textContent = '';

    // 重置卡片为正面
    document.getElementById('flashcard').classList.remove('flipped');

    // 更新按钮状态
    document.getElementById('btn-study-prev').disabled = state.studyIndex === 0;

    // 自动播放发音
    setTimeout(() => playStudyWord(), 300);
}

// 下一张卡片
function nextStudyCard() {
    if (state.studyIndex < state.studyWords.length - 1) {
        state.studyIndex++;
        showStudyCard();
    } else {
        // 学习完成
        showStudyComplete();
    }
}

// 上一张卡片
function prevStudyCard() {
    if (state.studyIndex > 0) {
        state.studyIndex--;
        showStudyCard();
    }
}

// 播放当前学习单词发音
function playStudyWord() {
    const word = state.studyWords[state.studyIndex];
    if (word && 'speechSynthesis' in window) {
        speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(word.word);
        utterance.lang = 'en-US';
        utterance.rate = 0.8;
        speechSynthesis.speak(utterance);
    }
}

// 显示学习完成界面
function showStudyComplete() {
    document.querySelector('.flashcard-container').classList.add('hidden');
    document.querySelector('.study-actions').classList.add('hidden');
    document.getElementById('study-complete').classList.remove('hidden');
    document.getElementById('studied-count').textContent = state.studyWords.length;
}

// 预习完成后开始测试
function startQuizAfterStudy() {
    state.quizMode = 'day';
    state.currentDay = state.studyDay;
    state.quizWords = [...state.studyWords];

    // 随机打乱
    shuffleArray(state.quizWords);

    // 重置预习界面
    document.querySelector('.flashcard-container').classList.remove('hidden');
    document.querySelector('.study-actions').classList.remove('hidden');
    document.getElementById('study-complete').classList.add('hidden');

    startQuiz();
}

// ===== 工具函数 =====
function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}

// ===== 完型填空模块逻辑 =====
let clozeData = [];
let currentClozeIndex = 0;
let userClozeAnswers = {};

async function startCloze() {
    try {
        const res = await fetch('/api/cloze');
        clozeData = await res.json();
    } catch (e) {
        console.error("Failed to load cloze data", e);
        clozeData = [];
    }

    if (clozeData.length === 0) {
        alert("暂无完型填空内容");
        return;
    }

    showView('cloze');

    const quizArea = document.getElementById('cloze-quiz-area');
    document.getElementById('cloze-title').textContent = '选择完型填空练习';

    const completedCloze = state.progress.completedClozeDays || [];
    const completedDays = state.progress.completedDays || [];
    // Day 1 默认解锁
    const unlockedDays = [1, ...completedDays];
    const available = clozeData.filter(c => unlockedDays.includes(c.day));

    if (available.length === 0) {
        alert("完成每日单词学习后解锁对应完型填空！🎯");
        showView('home');
        return;
    }

    quizArea.innerHTML = `
        <div class="listening-article-list">
            ${available.map(article => {
                const isDone = completedCloze.includes(article.day);
                return `
                <div class="listening-article-item" onclick="selectClozeArticle(${article.day})" style="
                    background: #f8f9fa;
                    padding: 16px 20px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    transition: all 0.2s;
                    border: 1px solid #eee;
                    ${isDone ? 'border-left: 4px solid #58cc02;' : ''}
                ">
                    <div style="
                        width: 44px; height: 44px;
                        border-radius: 12px;
                        background: ${isDone ? '#58cc02' : '#ff9600'};
                        display: flex; align-items: center; justify-content: center;
                        color: white; font-weight: 700;
                    ">${isDone ? '✅' : article.day}</div>
                    <div>
                        <div style="font-weight: 600;">${article.title}</div>
                        <div style="font-size: 12px; color: #666;">📝 ${article.blanks.length} 个空格</div>
                    </div>
                    <div style="margin-left: auto; color: #ccc;">›</div>
                </div>`;
            }).join('')}
        </div>
    `;
}

window.selectClozeArticle = function(day) {
    currentClozeIndex = clozeData.findIndex(c => c.day === day);
    if (currentClozeIndex < 0) return;
    renderClozeSession();
};

function renderClozeSession() {
    const data = clozeData[currentClozeIndex];
    userClozeAnswers = {};
    document.getElementById('cloze-title').textContent = data.title;

    const quizArea = document.getElementById('cloze-quiz-area');
    
    // 渲染正文（带输入/选择位置）
    let textHtml = data.text;
    data.blanks.forEach(b => {
        const placeholder = `{${b.id}}`;
        const replacement = `<span class="cloze-blank" id="cloze-b-${b.id}" data-id="${b.id}" style="
            display: inline-block;
            min-width: 80px;
            border-bottom: 2px solid #ddd;
            text-align: center;
            margin: 0 4px;
            cursor: pointer;
            color: #1cb0f6;
            font-weight: 600;
        ">( ${b.id} )</span>`;
        textHtml = textHtml.replace(placeholder, replacement);
    });

    quizArea.innerHTML = `
        <div class="cloze-text" style="font-size: 18px; line-height: 2.2; margin-bottom: 30px; text-align: justify;">
            ${textHtml}
        </div>
        <div id="cloze-options-area" class="cloze-options-area" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
            <!-- 这里由点击空格时动态显示该空格的选项 -->
            <p style="grid-column: 1/-1; text-align: center; color: #999;">点击上方的括号选择答案</p>
        </div>
        <button id="btn-submit-cloze" class="btn-primary" style="width: 100%; margin-top: 30px; opacity: 0.5; pointer-events: none;">提交答案 (0/${data.blanks.length})</button>
        <div id="cloze-result" style="display:none; margin-top: 20px;"></div>
    `;

    // 绑定空格点击事件
    quizArea.querySelectorAll('.cloze-blank').forEach(blank => {
        blank.onclick = () => showClozeOptions(blank.dataset.id);
    });
}

function showClozeOptions(blankId) {
    const data = clozeData[currentClozeIndex];
    const blank = data.blanks.find(b => b.id == blankId);
    const optionsArea = document.getElementById('cloze-options-area');
    
    // 高亮当前选中的空格
    document.querySelectorAll('.cloze-blank').forEach(b => b.style.backgroundColor = 'transparent');
    document.getElementById(`cloze-b-${blankId}`).style.backgroundColor = '#e1f5fe';

    optionsArea.innerHTML = `
        <div style="grid-column: 1/-1; font-weight: 600; color: #666; margin-bottom: 5px;">空格 ${blankId} 的选项：</div>
        ${blank.options.map((opt, idx) => `
            <button class="choice-btn ${userClozeAnswers[blankId] === idx ? 'selected' : ''}" 
                    onclick="selectClozeAnswer(${blankId}, ${idx}, '${opt}')"
                    style="margin: 0; width: 100%;">
                ${['A', 'B', 'C', 'D'][idx]}. ${opt}
            </button>
        `).join('')}
    `;
}

window.selectClozeAnswer = function(blankId, optIdx, text) {
    userClozeAnswers[blankId] = optIdx;
    
    // 更新文中显示
    const blankEl = document.getElementById(`cloze-b-${blankId}`);
    blankEl.textContent = text;
    blankEl.style.color = '#1cb0f6';
    
    // 重新渲染选项区域（更新选中状态）
    showClozeOptions(blankId);
    
    // 检查提交按钮
    const data = clozeData[currentClozeIndex];
    const answeredCount = Object.keys(userClozeAnswers).length;
    const submitBtn = document.getElementById('btn-submit-cloze');
    submitBtn.textContent = `提交答案 (${answeredCount}/${data.blanks.length})`;
    
    if (answeredCount === data.blanks.length) {
        submitBtn.style.opacity = '1';
        submitBtn.style.pointerEvents = 'auto';
        submitBtn.onclick = submitClozeAnswers;
    }
}

function submitClozeAnswers() {
    const data = clozeData[currentClozeIndex];
    let correct = 0;

    data.blanks.forEach(b => {
        const userIdx = userClozeAnswers[b.id];
        const isRight = userIdx === b.answer;
        const blankEl = document.getElementById(`cloze-b-${b.id}`);
        
        if (isRight) {
            correct++;
            blankEl.style.color = '#58cc02';
        } else {
            blankEl.style.color = '#ff4b4b';
            blankEl.innerHTML = `<span style="text-decoration: line-through;">${blankEl.textContent}</span> <span style="font-weight: 800;">(${b.options[b.answer]})</span>`;
        }
    });

    const xpEarned = correct * 10;
    state.xp += xpEarned;

    const pct = Math.round(correct / data.blanks.length * 100);
    const passed = pct >= 60;

    if (passed) {
        if (!state.progress.completedClozeDays) state.progress.completedClozeDays = [];
        if (!state.progress.completedClozeDays.includes(data.day)) {
            state.progress.completedClozeDays.push(data.day);
        }
    }

    saveProgress();

    document.getElementById('btn-submit-cloze').style.display = 'none';
    document.getElementById('cloze-options-area').style.display = 'none';
    
    const resultEl = document.getElementById('cloze-result');
    resultEl.style.display = 'block';
    resultEl.innerHTML = `
        <div style="background: #f0fdf4; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid #58cc02;">
            <h3 style="color: #58cc02; margin-top: 0;">练习完成！</h3>
            <div style="font-size: 24px; font-weight: 800; margin: 10px 0;">${correct} / ${data.blanks.length} 正确</div>
            <div style="color: #666; margin-bottom: 20px;">获得 ⭐ +${xpEarned} XP</div>
            <button class="btn-primary" onclick="showView('home'); renderDashboard();" style="width: 100%;">返回首页</button>
        </div>
    `;

    if (passed) playSound('correct');
    else playSound('wrong');
}

// 绑定首页按钮
document.getElementById('btn-cloze').addEventListener('click', startCloze);
document.getElementById('btn-cloze-close').addEventListener('click', () => showView('home'));

// ===== 启动 =====
document.addEventListener('DOMContentLoaded', init);
