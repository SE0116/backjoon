function solution(numbers, target) {
    let answer = 0;

    function dfs ( cnt, total ) {
        
        if ( cnt === numbers.length ) {
            if ( total === target ) {
                answer += 1;
            }
             return;
        }
        dfs(cnt + 1, total + numbers[cnt]);
        dfs(cnt + 1, total - numbers[cnt]);
    }

    dfs(0, 0);  
    
    return answer;
}