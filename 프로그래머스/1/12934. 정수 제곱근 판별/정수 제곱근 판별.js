function solution(n) {
    let answer = 0;
    
    for ( let i = 1 ; i <= Math.floor(n / 2) ; i++ ) {
        if ( i**2 === n ) {
            answer = (i + 1) ** 2;
            break;
        }
        else if ( i ** 2 > n ) {
            break;
        }
    }
    if ( answer === 0 ) {
        if ( n === 1 ) {
            answer = 4;
        }
        else {
            answer = -1;        
        }
    }
    return answer;
}