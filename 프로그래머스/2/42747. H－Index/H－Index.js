function solution(citations) {
    let answer = 0;
    
    citations.sort((a,b) => {
        return b - a;
    });
    
    let len = citations.length;
    
    for( let i = 0 ; i < len ; i++ ) {
        if( i + 1 <= citations[i] ) {
            answer += 1;
        }
    }
    return answer;
}