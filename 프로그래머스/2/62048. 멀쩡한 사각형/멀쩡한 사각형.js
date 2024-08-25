function solution(w, h) {
    let answer = w * h;
    let cut = w + h - gcd(w, h);

    return answer - cut;
}

function gcd(a, b) {
    if ( b === 0 ) {
        return a;
    }
    
    return gcd(b, a % b);
}