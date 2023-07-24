function solution(spell, dic) {
    var answer = 0;
        for (let i =0; i<dic.length; i++) {

            if (spell.sort().join('') === [...dic[i]].sort().join(''))
            {   
                return 1
            }
        }
        return 2
    
}