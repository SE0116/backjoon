function solution(n, lost, reserve) {
    let lostLength = lost.length;
    let answer =  n - lostLength;
    let tmp = [];
    
    for ( let i = 0 ; i < lostLength ; i ++ ) {
        if ( reserve.includes(lost[i]) ) {
            reserve = reserve.filter((ele) => ele !== lost[i])
            answer += 1;
        }
        else {
            tmp.push(lost[i]);
        }
    }
    
    lost = tmp.sort();
    
    for ( let i = 0 ; i < lostLength ; i ++ ) {
        if ( reserve.includes(lost[i] - 1 ) ) {
            answer += 1;
            reserve = reserve.filter ((ele) => ele !== lost[i] - 1 )
        }
        else if ( reserve.includes(lost[i] + 1) ) {
            answer += 1;
            reserve = reserve.filter((ele) => ele !== lost[i] + 1)
        }
    }
    
    return answer;
}