function solution(arr) {
    let answer = [];
    let answer_idx = 0;
    
    for ( let i = 0 ; i < arr.length ; i++ ) {
        if ( arr[i] < arr[answer_idx] ) {
            answer_idx = i;
        }
        console.log(answer_idx);
    }
    for ( let i = 0 ; i < arr.length ; i++ ) {
        if ( i === answer_idx ) {
            continue;
        }
        answer.push(arr[i]);
    }
    
    if ( answer.length === 0 ) {
        answer.push(-1);
    }
    return answer;
}