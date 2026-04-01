// Simulate the environment and logic
const state = {
    quizWords: [{word: 'a'}, {word: 'b'}],
    currentQuestion: 0,
    hearts: 5
};

function nextQuestion() {
    console.log('nextQuestion called', {
        current: state.currentQuestion,
        total: state.quizWords.length,
        hearts: state.hearts
    });

    if (state.hearts <= 0) {
        console.log('Hearts <= 0, finishing');
        return;
    }

    state.currentQuestion++;
    renderQuestion();
}

function renderQuestion() {
    const q = state.quizWords[state.currentQuestion];
    if (!q) {
        console.log('No question found, finishing quiz');
        return;
    }
    console.log('Rendering question', state.currentQuestion);
}

// Simulate flow
console.log('Initial state:', state);
renderQuestion(); // Q1

// User answers correct
console.log('User answers correct, hits Next');
nextQuestion(); // Should go to Q2

// User answers correct
console.log('User answers correct, hits Next');
nextQuestion(); // Should finish
