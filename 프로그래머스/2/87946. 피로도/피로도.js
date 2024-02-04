function solution(k, dungeons) {
    let answer = 0;
    
    const visited = Array.from({ length: dungeons.length }, () => false);
    
    function dfs(n, cnt) {
        for ( let i = 0 ; i < dungeons.length ; i++ ) {
            if ( visited[i] === false && n >= dungeons[i][0] ) {
                visited[i] = true;
                dfs(n - dungeons[i][1], cnt + 1);
                visited[i] = false;
            }
        }
        answer = Math.max(answer, cnt);
    }
    dfs(k, 0)
    return answer;
}