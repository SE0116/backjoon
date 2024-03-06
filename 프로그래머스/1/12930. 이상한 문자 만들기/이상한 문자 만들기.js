function solution(s) {
    let answer = '';
    let i = 0;
    let cnt = 0;

    while ( i < s.length ) {
        if ( s[i] === ' ' ) {
            cnt = 0;
            i++;
            answer += ' ';
            continue;
        }
        if ( cnt % 2 === 0 ) {
            answer += s[i].toUpperCase();
        }
        
        else {
            answer += s[i].toLowerCase();
        }
        cnt++;
        i++;
    }
    
    return answer;
}