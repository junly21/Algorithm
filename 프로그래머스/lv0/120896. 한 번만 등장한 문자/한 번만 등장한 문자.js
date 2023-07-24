function solution(s) {
    var answer = '';
    let a = [...s]
    let c = a.filter(v=>s.split(v).length == 2)
    
    answer = c.sort().join('')
    
    return answer;
}