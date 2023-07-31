function solution(priorities, location) {
    var answer = 0;
    //인덱스 배열
    let idx_arr = []    
    for(let i =0; i<priorities.length; i++) {
        idx_arr.push(i)
    }
    
    while(priorities.length>0) {
        let max = Math.max(...priorities)
        //console.log(max)
        
            if (priorities[0] < max) {
                //console.log(priorities[0] , max)
                priorities.push(priorities.shift())
                idx_arr.push(idx_arr.shift())
                //console.log(priorities, idx_arr)
                
            }
            else if(priorities[0] >= max) {
                priorities.shift()
                let idx = idx_arr.shift()
                if (idx === location) {
                answer += 1     
                return answer
                }
                else {
                    answer += 1
                }
            }
        }
    
    
   
    
    
    return answer;
}