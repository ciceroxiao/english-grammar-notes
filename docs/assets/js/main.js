// 英语语法学习网站交互功能

// 切换答案显示/隐藏
function toggleAnswers() {
    const answersDiv = document.getElementById('answers');
    if (answersDiv.style.display === 'none') {
        answersDiv.style.display = 'block';
    } else {
        answersDiv.style.display = 'none';
    }
}

// 检查选择题答案
document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question[data-answer]');
    
    questions.forEach(q => {
        const correctAnswer = q.dataset.answer;
        const explanation = q.dataset.explanation;
        const inputs = q.querySelectorAll('input[type="radio"]');
        
        inputs.forEach(input => {
            input.addEventListener('change', function() {
                // 清除之前的反馈
                const oldFeedback = q.querySelector('.feedback');
                if (oldFeedback) {
                    oldFeedback.remove();
                }
                
                // 创建反馈元素
                const feedback = document.createElement('div');
                feedback.className = 'feedback';
                
                if (this.value === correctAnswer) {
                    feedback.style.color = 'var(--success-color)';
                    feedback.innerHTML = '✓ 正确！' + (explanation ? '<br><small>' + explanation + '</small>' : '');
                } else {
                    feedback.style.color = '#ef4444';
                    feedback.innerHTML = '✗ 错误。正确答案是：' + correctAnswer + 
                                         (explanation ? '<br><small>' + explanation + '</small>' : '');
                }
                
                q.appendChild(feedback);
            });
        });
    });
    
    // 填空题检查
    const fillInputs = document.querySelectorAll('.fill-input');
    fillInputs.forEach(input => {
        const questionDiv = input.closest('.question');
        const correctAnswer = questionDiv.dataset.answer;
        const explanation = questionDiv.dataset.explanation;
        
        // 添加检查按钮
        const checkBtn = document.createElement('button');
        checkBtn.textContent = '检查答案';
        checkBtn.style.marginTop = '0.5rem';
        checkBtn.style.padding = '0.25rem 0.75rem';
        checkBtn.style.background = 'var(--primary-color)';
        checkBtn.style.color = 'white';
        checkBtn.style.border = 'none';
        checkBtn.style.borderRadius = '4px';
        checkBtn.style.cursor = 'pointer';
        
        checkBtn.addEventListener('click', function() {
            const oldFeedback = questionDiv.querySelector('.feedback');
            if (oldFeedback) {
                oldFeedback.remove();
            }
            
            const userAnswer = input.value.trim();
            const feedback = document.createElement('div');
            feedback.className = 'feedback';
            feedback.style.marginTop = '0.5rem';
            
            if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
                feedback.style.color = 'var(--success-color)';
                feedback.innerHTML = '✓ 正确！' + (explanation ? '<br><small>' + explanation + '</small>' : '');
            } else {
                feedback.style.color = '#ef4444';
                feedback.innerHTML = '✗ 错误。正确答案是：' + correctAnswer + 
                                     (explanation ? '<br><small>' + explanation + '</small>' : '');
            }
            
            questionDiv.appendChild(feedback);
        });
        
        input.parentNode.appendChild(checkBtn);
    });
});

// 添加进度追踪（本地存储）
function markAsCompleted(pointId) {
    let completed = JSON.parse(localStorage.getItem('completed_points') || '[]');
    if (!completed.includes(pointId)) {
        completed.push(pointId);
        localStorage.setItem('completed_points', JSON.stringify(completed));
    }
}

function getProgress() {
    const completed = JSON.parse(localStorage.getItem('completed_points') || '[]');
    return {
        completed: completed,
        total: 24,
        percentage: Math.round((completed.length / 24) * 100)
    };
}
