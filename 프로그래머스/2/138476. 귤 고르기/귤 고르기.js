function solution(k, tangerine) {
    // 귤의 크기별 개수를 담을 map 생성
    let answer = 0;
    const len = new Map();
    
    // 크기별 개수 세기
    tangerine.forEach( cnt => {
        len.set(cnt, len.has(cnt) ? len.get(cnt) + 1 : 1);
    });

    // 귤의 개수를 내림차순 정렬
    const sortArr = [... len].sort((a, b) => b[1] - a[1]);
    
    // 상자에 담기
    sortArr.forEach( arr => {
        // k가 0보다 클 때만 상자에 담기
        if(k > 0) {
            k -= arr[1];    
            answer += 1;
        } 
    });
    
    return answer;
};