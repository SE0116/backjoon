function solution(left, right) {
    let answer = 0;
    
    function isEven(num) {
        if ( Math.floor(Math.sqrt(num)) ** 2 === num ) {
            return false;
        }
        return true;
    }
    
    for ( let i = left ; i <= right ; i++ ) {
        if ( isEven(i) ) {
            answer += i;
        }
        else {
            answer -= i;
        }
    }
    
    return answer;
}