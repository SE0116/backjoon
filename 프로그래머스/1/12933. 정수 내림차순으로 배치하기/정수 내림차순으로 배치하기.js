function solution(n) {
    let answer = 0;
    const swap = [];
    
    while ( Math.floor(n / 10) ) {
        swap.push(n % 10);
        n = Math.floor(n / 10);
    }
    swap.push(n);
    swap.sort();
    
    for ( let i = 0 ; i < swap.length ; i++ ) {
        answer += swap[i] * (10**i);
    }
    
    return answer;
}