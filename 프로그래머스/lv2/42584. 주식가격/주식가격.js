// function solution(prices) {
//     var answer = [];
    
//     while(prices.length>0) {
//         target = prices.shift()
//         let sec = 0
//         for(let j =0; j<prices.length; j++) {    
//             sec += 1
//             if(prices[j]<target){
//                 break
//             }
//         }
//         answer.push(sec)
//     }      
//     return answer;
// }

function solution(prices) {
    var answer = [];
    
    for (let i =0 ; i<prices.length; i++) {
        target = prices[i]
        let sec = 0
        for(let j = i+1; j<prices.length; j++) {    
            sec += 1
            if(prices[j]<target){
                break
            }
        }
        answer.push(sec)
    }      
    return answer;
}