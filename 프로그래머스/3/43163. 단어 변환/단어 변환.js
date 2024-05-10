function solution(begin, target, words){
    let answer = 0;
    let ch = Array.from({length: words.length}, ()=>false);

    function dfs(cur, target, step){
        if ( cur === target ) {
            if ( answer === 0 || answer > step ) {
                answer = step;
            }
            return;
        }

        for ( let i = 0 ; i < words.length ; i++ ) {
            if ( ch[i] ) {
                continue;
            }
            
            let diffCount = 0;

            for ( let k = 0 ; k < words[i].length ; k++ ) {
                if ( words[i][k] !== cur[k] ) {
                    diffCount += 1;
                }
            }

            if ( diffCount === 1 ) {
                ch[i] = true;
                dfs(words[i], target, step + 1);
                ch[i] = false;
            }
        }
    }
    
    dfs(begin, target, 0);

    return answer;
}