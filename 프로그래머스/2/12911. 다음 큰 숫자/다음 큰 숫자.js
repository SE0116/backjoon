function solution(n) {
    // 입력받은 n을 2진수로 변환했을 때 1의 갯수를 저장
    let over = n.toString(2).split('1').length;
    
    while ( true ) {
        // n을 1씩 늘려가면서
        n++;
        
        // 증가한 값이 가진 1의 갯수와 원래 1의 갯수가 같아지면 증가시킨 값 반환
        if ( n.toString(2).split('1').length === over ) {
            return n;
        }
    }
}