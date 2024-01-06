function solution(n) {
    // 예시의 15 = 15와 같은 경우는 예외처리를 위해 계산 전에 +1
    let answer = 1;
    
    // (N/2)보다 큰 수를 두 개 이상 더하면 무조건 N보다 커지기 때문에 두 개 이상을 더하지 않게 범위 설정
    for ( let i = 1 ; i <= n / 2 ; i++) {
        let total = 0;
        // i부터 순차적으로 더했을 때 값을 비교
        for ( let j = i ; j <= n / 2 + 1; j++ ) {
            total += j;
            if ( total > n ) {
                break;
            }

            if ( total === n ) {
                answer += 1;
                break;       
            }
        }
    }
    return answer;
}