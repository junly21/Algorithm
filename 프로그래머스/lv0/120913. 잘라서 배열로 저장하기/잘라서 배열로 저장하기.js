// function solution(my_str, n) {
//     var answer = [];
//     let a = my_str.match(new RegExp(`.{1,${n}}`,'g'))
//     console.log(a)
//     return a;
// }
function solution(my_str, n) {
    var answer = [];
    let k = my_str.split('')
    let i = 0
    while(k.length>0) {
        let j = k.splice(i,n).join('')
        answer.push(j) 

    }
    
    return answer;
}