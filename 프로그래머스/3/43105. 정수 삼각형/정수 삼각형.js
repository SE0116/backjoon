function solution(triangle) {

    for ( let i = 1 ; i < triangle.length ; i++) {
        for ( let j = 0 ; j < triangle[i].length ; j++) {
            // 삼각형의 왼쪽 또는 오른쪽 대각선에 있는 숫자면
            // 이동 가능한 칸이 한 칸밖에 없으니까 그대로 더해주기
            if ( j === 0 ) {
                triangle[i][j] += triangle[i-1][j];
            }
            else if ( j === triangle[i].length - 1 ) {
                triangle[i][j] += triangle[i-1][j-1];
            // 대각선이 아닌 내부의 숫자들은 위에서 더 큰 수를 비교해서 더해주기
            }
            else {
                triangle[i][j] += Math.max(triangle[i-1][j-1], triangle[i-1][j]);
            }
        }
    }

    var answer = Math.max(...triangle[triangle.length-1]);

    return answer;
}