function solution(seoul) {
    
    for ( var i = 0 ; i < seoul.length ; i++ ) {
        if ( seoul[i] === 'Kim' ) {
            break;
        }
    }
    
    return '김서방은 ' + i + '에 있다';
}