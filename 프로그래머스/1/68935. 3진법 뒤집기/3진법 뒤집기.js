function solution(n) {
    let answer = 0;
    const swap = [];
    
    while ( n >= 3 ) {
        swap.push( n % 3 );
        n = Math.floor(n / 3);
    }
    swap.push(n);
    
    for ( let i = 0 ; i < swap.length ; i++ ) {
        answer += swap[swap.length - i - 1] * 3**i;
    }
    return answer;
}