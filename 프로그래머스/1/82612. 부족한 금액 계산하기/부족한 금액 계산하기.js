function solution(price, money, count) {
    let answer = 0;
    let total = 0;
    
    for ( let i = 1 ; i <= count ; i++ ) {
        total += i * price;
    }
    
    if ( total > money ) {
        answer = total - money;
    }
    
    return answer;
}