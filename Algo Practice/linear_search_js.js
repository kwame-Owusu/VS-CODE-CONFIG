function linearSearch(array, len, target) {
  for (let i = 0 ; i < len ; i++){ 
   if (array[i] == target) {
    return i;
   }
  }
   
  return -1

}

let array = [1,2,4,5,6,7];
let size = array.length;
let result = linearSearch(array, size, 7);


// another way to write if else statements in javascript.
result == -1 ? console.log('Element not in array') : console.log(`Element in array at index ${result}`)

// if (result == -1){
//  console.log("Element not in array")
// }
// else {
//  console.log(`Element in array at index ${result}`)
// }