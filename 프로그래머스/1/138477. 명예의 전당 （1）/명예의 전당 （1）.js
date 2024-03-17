function solution(k, score) {
    const answer = [];
    const nums = [];

    score.forEach( num => {
        nums.push(num);
        nums.sort((a, b) => b - a).splice(k);
        
        answer.push(Math.min.apply(null, nums));
    });

    return answer;
}