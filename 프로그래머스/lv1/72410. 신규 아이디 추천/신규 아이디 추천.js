function solution(new_id) {
    var answer = '';
    new_id = new_id.toLowerCase()
   // console.log(new_id)
    
    let regex1 = /[^a-z0-9-_.]/g
    new_id = new_id.replace(regex1,"")
    //console.log(new_id)
    
    let regex2 = /\.{2,}/g
    new_id = new_id.replace(regex2,".")
    //console.log(new_id)
    
    let regex3 = /^\.|\.$/g
    new_id = new_id.replace(regex3,"")
   // console.log(new_id)
    
    let regex4 = /(^$)/g
    new_id = new_id.replace(regex4,"a")
    //console.log(new_id)
    
    new_id = new_id.slice(0,15)
    //console.log(new_id)
    let regex5 = /\.$/g
    new_id = new_id.replace(regex5,"")
    //console.log(new_id)
    
    
    while(new_id.length<=2) {
        new_id += new_id.charAt(new_id.length-1)
    }
    
    //console.log(new_id)
    
    return new_id;
}