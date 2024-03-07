function solution(sizes) {
    let answer = 0;
    let max_row = 0;
    let max_col = 0;
    
    for ( let i = 0 ; i < sizes.length ; i++ ) {
        sizes[i].sort((a, b) => b - a);
        
        if ( sizes[i][0] > max_row ) {
            max_row = sizes[i][0];
        }
        
        if ( sizes[i][1] > max_col ) {
            max_col = sizes[i][1];
        }
    }
    answer = max_row * max_col;

    return answer;
}