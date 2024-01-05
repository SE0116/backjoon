function solution(A,B){
    var answer = 0;

    // 각 배열의 가장 큰 수와 가장 작은 수부터 하나씩 곱해줄 때가 누적된 값이 최소가 되기 때문에
    // 각 배열을 반대로 정렬
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    
    for ( let i = 0 ; i < A.length ; i++ ) {
        answer += A[i] * B[i];
    }

    return answer;
}