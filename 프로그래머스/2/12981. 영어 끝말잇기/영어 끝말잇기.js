function solution(n, words) {
    // 탈락자가 없을 경우를 대비해 초기값을 [0, 0]으로 설정
    let answer = [0, 0];
    
    for ( let i = 0 ; i < words.length ; i++ ) {
        let word = words[i];
        let cnt = Math.ceil((i + 1) / n);
        
        if ( i > 0 ) {
            let lastLetter = words[i - 1].split('').pop();
            
            // 이전 단어의 마지막 글자와 이어지지 않거나
            // 이미 사용한 단어를 말했을 때 해당 순서 저장
            if ( i > words.indexOf(word) || words[i][0] !== lastLetter ) {
                answer = [i % n + 1, cnt];
                break;
            }
        }
    }
    return answer;
}