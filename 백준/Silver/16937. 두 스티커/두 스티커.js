const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const HW = input[0].split(" ");
const H = Number(HW[0]);
const W = Number(HW[1]);
const N = Number(input[1]);

const stickerArr = [];
//console.log(input);
for (let i = 2; i < input.length; i++) {
  stickerArr.push(input[i].split(" ").map((v) => Number(v)));
}
//console.log("s", stickerArr);
let paper = Array.from(Array(H), () => Array(W).fill(0));

//스티커들을 넓이 큰 순으로 나열
stickerArr.sort((a, b) => b[0] * b[1] - a[0] * a[1]);

let maxCount = 0;

//console.log("s", stickerArr);
// 2개 뽑는 조합
for (let i = 0; i < stickerArr.length; i++) {
  for (let j = i + 1; j < stickerArr.length; j++) {
    let stickerA = stickerArr[i];
    let stickerB = stickerArr[j];
    let stickerA_row = stickerA[0];
    let stickerA_column = stickerA[1];
    let stickerB_row = stickerB[0];
    let stickerB_column = stickerB[1];
    let count = 0;
    paper = Array.from(Array(H), () => Array(W).fill(0));
    if (checkA(H, W, stickerA_row, stickerA_column, paper)) {
      if (checkB(H, W, stickerB_row, stickerB_column, paper)) {
        count = countNum(paper);
      }
    }
    //console.log(count, maxCount);
    if (count > maxCount) {
      maxCount = count;
    }
  }
}

//B회전
for (let i = 0; i < stickerArr.length; i++) {
  for (let j = i + 1; j < stickerArr.length; j++) {
    let stickerA = stickerArr[i];
    let stickerB = stickerArr[j];
    let stickerA_row = stickerA[0];
    let stickerA_column = stickerA[1];
    let stickerB_row = stickerB[1];
    let stickerB_column = stickerB[0];
    let count = 0;
    paper = Array.from(Array(H), () => Array(W).fill(0));
    if (checkA(H, W, stickerA_row, stickerA_column, paper)) {
      if (checkB(H, W, stickerB_row, stickerB_column, paper)) {
        count = countNum(paper);
      }
    }

    if (count > maxCount) {
      maxCount = count;
    }

    // console.log("회전", stickerA, stickerB, count, maxCount);
  }
}

//A회전
for (let i = 0; i < stickerArr.length; i++) {
  for (let j = i + 1; j < stickerArr.length; j++) {
    let stickerA = stickerArr[i];
    let stickerB = stickerArr[j];
    let stickerA_row = stickerA[1];
    let stickerA_column = stickerA[0];
    let stickerB_row = stickerB[0];
    let stickerB_column = stickerB[1];
    let count = 0;
    paper = Array.from(Array(H), () => Array(W).fill(0));
    if (checkA(H, W, stickerA_row, stickerA_column, paper)) {
      if (checkB(H, W, stickerB_row, stickerB_column, paper)) {
        count = countNum(paper);
      }
    }

    if (count > maxCount) {
      maxCount = count;
    }
  }
}

//A회전B회전
for (let i = 0; i < stickerArr.length; i++) {
  for (let j = i + 1; j < stickerArr.length; j++) {
    let stickerA = stickerArr[i];
    let stickerB = stickerArr[j];
    let stickerA_row = stickerA[1];
    let stickerA_column = stickerA[0];
    let stickerB_row = stickerB[1];
    let stickerB_column = stickerB[0];
    let count = 0;
    paper = Array.from(Array(H), () => Array(W).fill(0));
    if (checkA(H, W, stickerA_row, stickerA_column, paper)) {
      if (checkB(H, W, stickerB_row, stickerB_column, paper)) {
        count = countNum(paper);
      }
    }

    if (count > maxCount) {
      maxCount = count;
    }
  }
}

function checkA(H, W, stickerA_row, stickerA_column, paper) {
  if (stickerA_row > H || stickerA_column > W) {
    //에러 발생
    return false;
  }
  for (let x = 0; x < stickerA_row; x++) {
    for (let y = 0; y < stickerA_column; y++) {
      paper[x][y] = 1;
    }
  }
  return paper;
}

function checkB(H, W, stickerB_row, stickerB_column, paper) {
  // console.log(H, W, stickerB_row, stickerB_column, paper);
  if (stickerB_row > H || stickerB_column > W) {
    return false;
  }
  for (let p = H - 1; p >= H - stickerB_row; p--) {
    for (let q = W - 1; q >= W - stickerB_column; q--) {
      if (paper[p][q] === 1) {
        return false;
      }
      paper[p][q] = 1;
    }
  }
  return paper;
}

function countNum(paper) {
  let count = 0;
  for (let i = 0; i < paper.length; i++) {
    for (let j = 0; j < paper[i].length; j++) {
      if (paper[i][j] === 1) {
        count++;
      }
    }
  }
  return count;
}

console.log(maxCount);
