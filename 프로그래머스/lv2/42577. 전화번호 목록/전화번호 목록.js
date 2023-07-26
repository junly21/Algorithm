function solution(phone_book) {
    var answer = true;
    // 시간초과
    // phone_book.sort()
    // console.log(phone_book)
    // while(phone_book.length>1){
    //     let val = phone_book.shift()
    //     for (let i = 0; i<phone_book.length; i++) {
    //         //console.log(phone_book[i].slice(0,val.length+1), val)
    //         if (phone_book[i].slice(0,val.length) == val) {
    //         return false
    //             }
    //     }
    // }
    var mset = {} 
    phone_book.sort()
    phone_book.forEach(v=>{
        //console.log(v)
        for(let i =1; i<v.length; i++) {
            mset[v.slice(0,i)] = 'check'
            //console.log(mset)
        }
    })
    phone_book.forEach(v=>{
        if (v in mset) {
            answer = false
        }
    })
    return answer;
}