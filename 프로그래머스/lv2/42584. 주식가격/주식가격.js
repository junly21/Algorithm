function solution(prices) {
    var answer = [];
    
    for(let i = 0; i<prices.length-1; i++) {
        target = prices[i]
        let sec = 0
        
        for(let j =i+1; j<prices.length; j++) {    
            sec += 1
            if(prices[j]<target){
                break
            }
        }
        answer.push(sec)
        
    }
    answer.push(0)        
    return answer;
}