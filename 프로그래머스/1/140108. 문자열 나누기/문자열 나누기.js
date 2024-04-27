function solution(s) {
    let answer = 0;
    let leftChar = 0;
    let rightChar = 0;
    let temp = '';
    let isMatch = true;

    for ( let i = 0 ; i < s.length ; i++ ) {
        if ( isMatch ) {
            temp = s[i];
        }
        
        if ( temp == s[i] ) {
            leftChar += 1;
            isMatch = false;
        }

        else {
            rightChar += 1;

        }

        if ( leftChar === rightChar ) {
            answer += 1;
            leftChar = 0;
            rightChar = 0;
            isMatch = true;
        }
    }

    if ( leftChar !== 0 || rightChar !== 0 ) {
        return answer += 1;
    }

    return answer;
}