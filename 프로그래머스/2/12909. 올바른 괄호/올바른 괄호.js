function solution(s){
    var answer = true;
    s = s.split('');
    var cnt = 0
    
    for ( let i = 0 ; i < s.length ; i++ ) {
        if ( s[i] === ')' ) {
            // 닫힐 괄호가 없는데 닫으려 하면 false로 변경 후 반복문 탈출
            if ( cnt === 0 ) {
                answer = false;                 
                break;
            } 
            else cnt -= 1;
        }
        // 여는 괄호면 cnt +1
        else cnt += 1;    
    }
    
    // 괄호가 완전히 닫히지 않았으면 false 반환
    if ( cnt !== 0 ) answer = false;

    return answer;
}