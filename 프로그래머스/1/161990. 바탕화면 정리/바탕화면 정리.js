function solution(wallpaper) {
    const answer = [];
    const result = [];
    
    for ( let i = 0 ; i < wallpaper.length ; i++ ) {
        for ( let j = 0 ; j < wallpaper[i].length ; j++ ) {
            wallpaper[i][j] == '#' ? result.push([i, j]) : '';
        }
    }
    
    let minX = Math.min(...result.map((data) => data[0]));
    let minY = Math.min(...result.map((data) => data[1]));
    let maxX = Math.max(...result.map((data) => data[0]));
    let maxY = Math.max(...result.map((data) => data[1]));
    
    answer.push(minX, minY, maxX + 1, maxY + 1);
    
    return answer;
}