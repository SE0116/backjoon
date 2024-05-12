function solution(sequence, k) {
    let answer = [];
    let left = 0, right = 0;
    let sum = sequence[0];
    
    const len = sequence.length;
    
    while ( right < len && left <= right ) {
        if ( sum === k ) {
            answer.push([left, right])
            sum -= sequence[left++];
        }
        if ( sum > k ) {
            sum -= sequence[left++];
        }
        if ( sum < k ) {
            sum += sequence[++right]
        }
    }

    answer.sort((a,b) => {
        if ( a[1] - a[0] > b[1] - b[0] ) {
            return 1;
        }
        
        else if ( a[1] - a[0] < b[1] - b[0] ) {
            return -1;
        }
        
        else {
            return a[1] > b[1] ? 1: -1;
        }
    })
    
    return answer[0];
}