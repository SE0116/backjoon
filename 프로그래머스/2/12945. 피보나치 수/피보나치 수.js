function solution(n) {
    let fibo = [0, 1];
    for ( let i = 0 ; i <= n ; i++ ) {
        if ( i < 2 ) {
            continue;
        }
        else {
            if ( i % 2 ) {
                fibo[1] = (fibo[0] + fibo[1]) % 1234567;
            }
            else {
                fibo[0] = (fibo[0] + fibo[1]) % 1234567;
            }
        }
    }
    return fibo[n%2];
}