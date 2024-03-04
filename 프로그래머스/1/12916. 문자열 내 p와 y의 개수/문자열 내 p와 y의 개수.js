function solution(s){
    let answer = true;
    let numP = 0;
    let numY = 0;
    
    for ( letter of s ) {
        if ( letter === 'p' || letter === 'P') {
            numP += 1;
        }
        if ( letter === 'y' || letter === 'Y') {
            numY += 1;
        }
    }
    
    if ( numP != numY ) {
        answer = false;
    }
    
    return answer;
}