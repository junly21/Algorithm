function solution(emergency) {
    var answer = [];
    let dict = {
        
    }
    let len = emergency.length
    let save = [...emergency]
    let i = 1
    while (i < len+1) {
        let maxv = Math.max(...emergency)
        dict[maxv] = i
        emergency = emergency.filter(v=> v !== maxv)

        i += 1
    }

    save.forEach(v=>{
                answer.push(dict[v])})
    return answer;
}