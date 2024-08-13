function solution(stones, k) {
    let start = 1;
    let end = 200000000;
    
    while ( start !== end ) {
        let mid = Math.floor((start+end) / 2)
        let is_foward = true;
        let cnt = 0;
        
        for ( let stone of stones ) {
            if ( stone <= mid ) {
                cnt++;
            }
            
            else {
                cnt = 0;
            }
            
            if ( cnt >= k ) {
                is_foward = false;
                break;
            }
        }
        
        if ( is_foward ) {
            start = mid + 1;
        }
        
        else {
            end = mid;
        }
    }
    
    return start;
}