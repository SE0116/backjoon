function solution(babbling) {
    var answer = 0;
    const nephew = ["aya", "ye", "woo", "ma"];
    
    for ( var i = 0 ; i < babbling.length ; i++ ) {
        let bab = babbling[i];
        
        for ( var j = 0 ; j < nephew.length ; j++ ) {
                if ( bab.includes(nephew[j].repeat(2)) ) {
                break;
                }
            bab = bab.split(nephew[j]).join(" ");
            }
        if ( bab.split(" ").join("").length === 0 ) {
            answer ++
        }
    }
    return answer;
}