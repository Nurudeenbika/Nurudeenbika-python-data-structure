const solution = (arr = [], x, y) => {
    let firstX = -1, firstY = -1, lastX = -1, lastY = -1;
    let countX = 0, countY = 0;
  
    let i = 0;
    do {
    const num = arr[i];
    if (num === x) {
        countX++;
        if (firstX === -1) firstX = i;
        lastX = i;
    } else if (num === y) {
        countY++;
        if (firstY === -1) firstY = i;
        lastY = i;
    }
    i++;
    } while (i < arr.length);

  
    // Adjust for excess occurrences properly
    if (countX > countY) { 
        const excess = countX - countY;
        let tempCount = 0;
        let i = lastX;
      
        do {
          if (arr[i] === x) tempCount++;
          if (tempCount > excess) {
            lastX = i;
            break;
          }
          i--;
        } while (i >= 0);
      
    } else if (countY > countX) {
        const excess = countY - countX;
        let tempCount = 0;
        let i = lastY;
      
        do {
          if (arr[i] === y) tempCount++;
          if (tempCount > excess) {
            lastY = i;
            break;
          }
          i--;
        } while (i >= 0);
    }
      
    return Math.max(lastX, lastY) - Math.min(firstX, firstY) + 1;
  };
  const arr = [1, 2, 3, 2, 3, 1, 3, 2, 1];
  const arr2 = [4, 5, 4, 6, 4, 5, 5, 4, 5, 6, 5, 4, 6, 1, 2, 7, 5, 4, 5, 4, 6, 4, 5, 4, 5, 5, 6, 5, 7, 8, 9, 5];
  console.log(solution(arr, 2, 3));  // 7 
  console.log(solution(arr2, 4, 5)); // 25