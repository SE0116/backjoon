function solution(n, costs) {
    costs.sort((a, b) => a[2] - b[2]);
    const parent = Array.from({ length: n }, (_, i) => i);
    let answer = 0;
    
    for ( const [start, end, cost] of costs ) {
        if ( !isSameParent(parent, start, end) ) {
            answer += cost;
            union(parent, start, end);
        }
    }
    return answer;
}

function union(parent, a, b) {
    a = find(parent, a);
    b = find(parent, b);
    
    if ( a < b ) {
        parent[b] = a;
    }
    else {
        parent[a] = b;
    }
}

function isSameParent(parent, a, b) {
    a = find(parent, a);
    b = find(parent, b);
    return a === b;
}

function find(parent, x) {
    if ( parent[x] === x ) {
        return x;
    }
    
    return parent[x] = find(parent, parent[x]);
}