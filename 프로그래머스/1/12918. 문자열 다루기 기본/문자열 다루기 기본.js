function solution(s) {
    let answer = true;
    let cnt = 0;

    for ( letter of s ) {
        if ( isNaN(letter) ) {
            answer = false;
            break;
        }
        cnt++;
    }
    
    if ( cnt !== 4 && cnt !== 6 ) {
        answer = false;
    }
    return answer;
}