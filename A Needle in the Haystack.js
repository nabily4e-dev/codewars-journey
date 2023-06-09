// function findNeedle(haystack) {
//   for (let i = 0; i < haystack.length; i++){
//     if (haystack[i] === 'needle'){
//       return `found the needle at position ` + i
//     }
//   }
// }

// function findNeedle(haystack) {
//   let foundIndex = -1
  
//   haystack.forEach(function (element, index){
//     if (element == 'needle'){
//       foundIndex = index
//     }
//   })
  
//   if (foundIndex == -1){
//     return "needle not found!"
//   } else {
//     return 'found the needle at position ' + foundIndex
//   }
// }

// function findNeedle(haystack) {
//   const index = haystack.findIndex(function(element){
//     return element === 'needle'
//   })
//   return index === -1 ? 'needle not found' : `found the needle at position ${index}`
// }

const findNeedle = haystack => `found the needle at position ${haystack.indexOf('needle')}`;


!! /////////////////////
// Community solutions!

// function findNeedle(haystack) {
//     return "found the needle at position " + haystack.indexOf("needle");
//   }
