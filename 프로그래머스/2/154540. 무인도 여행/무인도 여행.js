function solution(maps) {
    let answer = [];
    
    maps = maps.map((m) => m.split(""));
    
    function dfs(dx,dy) {
            if ( dx < 0 || dy < 0 || dx >= maps.length || dy >= maps[0].length || maps[dx][dy] === "X" ) {
                return 0;
            }
            else {
                var num = parseInt(maps[dx][dy]);
                maps[dx][dy] = "X";
                return num + dfs(dx-1, dy)+ dfs(dx+1, dy)+ dfs(dx, dy-1)+ dfs(dx, dy+1);
            }
    }

    for ( var row = 0 ; row < maps.length ; row++ ) {
        for ( var col = 0 ; col < maps[0].length ; col++ ) {
            if ( maps[row][col] !== "X" ) {
                answer.push(dfs(row,col));
            }
        }
    }
    
    if ( answer.length === 0 ) {
        return [-1];
    }
    
    else {
        answer = answer.sort((a,b) => a - b);
        return answer;   
    }
}