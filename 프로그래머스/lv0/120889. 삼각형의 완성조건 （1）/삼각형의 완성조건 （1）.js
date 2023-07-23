function solution(sides) {
    var answer = 0;
    sides.sort((a,b)=>{return a-b})
    let maxVal = sides.pop()
    let sum = sides.reduce((acum,cur) => acum+cur)
    if (sum > maxVal){
        answer = 1
    }
    else {
        answer = 2
    }
    return answer;
}