function solution(arr) {
    let answer = 0;
    for ( var i = 0 ; i < arr.length ; i++ ) {
        answer += arr[i];
    }
    answer /= i;
    return answer;
}