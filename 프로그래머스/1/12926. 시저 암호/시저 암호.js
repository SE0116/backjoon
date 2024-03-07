function solution(s, n) {
    let answer = '';
    console.log(String.fromCharCode('s'.charCodeAt() + 2));
    for ( letter of s ) {
        if ( letter === ' ' ) {
            answer += letter;
        }
        else if ( (letter.charCodeAt() <= 90 && letter.charCodeAt() + n > 90) || (letter.charCodeAt() <= 122 && letter.charCodeAt() + n > 122) ) {
            answer += String.fromCharCode(letter.charCodeAt() + n - 26);
        }
        else {
            answer += String.fromCharCode(letter.charCodeAt() + n);
        }
    }
    return answer;
}