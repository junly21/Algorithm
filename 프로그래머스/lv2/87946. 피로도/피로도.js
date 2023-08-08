function solution(k, dungeons) {
    var answer = -1;
    const visited = new Array(dungeons.length).fill(0)
    
    function dfs(k,depth) {
        //던전 반복
        for(let i =0; i<dungeons.length; i++) {
            
            //미방문, 시작조건 만족시
            if( (visited[i] === 0) && k >= dungeons[i][0]) {
                //방문처리
                visited[i] = 1
                dfs(k-dungeons[i][1], depth + 1)
                
                //다 끝나고 오면
                visited[i] = 0
            }
        }
        
        answer = Math.max(answer, depth);
        
    }
    dfs(k,0)
    return answer;
    
    
}