function solution(n, arr1, arr2) {
    const answer = [];
    for ( let i = 0 ; i < arr1.length ; i++ ) {
        arr1[i] = arr1[i].toString(2).padStart(n, '0');
        arr2[i] = arr2[i].toString(2).padStart(n, '0');
        let answer_elem = '';
        for ( let j = 0 ; j < n ; j++ ) {
            if ( arr1[i][j] === '1' || arr2[i][j] === '1' ) {
                answer_elem += '#';
            }
            else {
                answer_elem += ' ';
            }
        }
        answer.push(answer_elem);
    }
    return answer;
}