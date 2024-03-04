function solution(x) {
    let answer = true;
    let harshad = 0;
    let x_sub = x;
    
    while ( Math.floor(x_sub / 10) ) {
        harshad += x_sub % 10;
        x_sub = Math.floor(x_sub / 10);
    }
    harshad += x_sub;
    if ( x % harshad !== 0 ) {
        answer = false;
    }
    return answer;
}