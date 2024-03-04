function solution(n) {
    const answer = [];
    while ( Math.floor(n / 10) ) {
        answer.push(n % 10);
        n = Math.floor(n / 10);
    }
    answer.push(n);
    return answer;
}