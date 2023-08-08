function solution(brown, yellow) {
    var answer = [];
    
    let total = brown + yellow
    
    for (let i = 3; i<Math.sqrt(total)+1; i++) {
        
        if (total % i === 0) {
            let x = total / i
            if(((x-2)*(i-2) === yellow) && (x*i === total)  ) {
                answer.push(x)
                answer.push(i)
                return answer
            }
        }
    }
    // (x-2)*(y-2) = yellow
    // x*y = brown + yellow
    
    return answer;
}