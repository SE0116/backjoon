function solution(s) {
    var answer = [0, 0];
    
    while ( s > 1 ) {
        // 현재 s의 길이를 임시로 저장
        let len = s.length;
        
        // s에 있는 0을 빈칸으로 바꾸기( 지우기 )
        s = s.replace(/0/g, '');
        
        // replace로 생긴 차이만큼 answer[1]에 더해주기
        answer[1] += len - s.length;
        
        // 임시 저장값 바꾸고 s를 다시 2진수로 치환
        len = s.length;
        s = len.toString(2);
        answer[0] += 1;
    }
    return answer;
}