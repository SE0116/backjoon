function solution(clothes) {
    const map = new Map()
    let answer = 1
    
    for ( const [name, type] of clothes ) {
        if ( map.get(type) ) map.set(type,map.get(type) + 1)
        else map.set(type, 1)
    }

    for ( const [key, val] of map ) {
        answer *= val + 1
    }
    
    return answer - 1
}