function solution(n, m) {
    const answer = [];
    
    for ( let i = Math.min(n, m) ; i >= 1 ; i--) {
        if ( n % i === 0 && m % i === 0 ) {
            answer.push(i);
            break;
        }
    }
    
    for ( let i = Math.max(n, m) ; i <= n * m ; i++) {
        if ( i % n === 0 && i % m === 0 ) {
            answer.push(i);
            break;
        }
    }
    return answer;
}