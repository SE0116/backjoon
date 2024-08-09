function solution(n, roads, sources, destination) {
    const visited = new Array(n+1).fill(Infinity);
    const connect = new Array(n+1).fill(0).map(_ => []);
    const queue = [destination];
    
    roads.forEach(([from, to]) => {
        connect[from].push(to);
        connect[to].push(from);
    })

    visited[destination] = 0;
    
    while ( queue.length ) {
        const now = queue.shift();

        for ( const next of connect[now] ) {
            if ( visited[now] + 1 < visited[next] ) {
                visited[next] = visited[now] + 1;
                queue.push(next);
            }
        }
    }
    
    return sources.map(a => visited[a] !== Infinity ? visited[a] : -1);
}