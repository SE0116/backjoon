function solution(answers) {
    const answer = [];
    let a = [1, 2, 3, 4, 5];
    let b = [2, 1, 2, 3, 2, 4, 2, 5];
    let c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let cnt = [0, 0, 0];
    
    for ( let i = 0 ; i < answers.length ; i++ ) {
        if ( answers[i] === a[i%5] ) {
            cnt[0]++;
        }
        if ( answers[i] === b[i%8] ) {
            cnt[1]++;
        }
        if ( answers[i] === c[i%10] ) {
            cnt[2]++;
        }
    }
    const maxCnt = Math.max.apply(null, cnt);
    
    for ( let i = 0 ; i < 3 ; i++ ) {
        if ( cnt[i] === maxCnt ) {
            answer.push(i + 1); 
        }
    }
    return answer;
}