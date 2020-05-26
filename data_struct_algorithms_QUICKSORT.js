// let values = [];
// let w = 10;

// let states = [];

// function setup() {
//   values = new Array(floor(width / w));
//   for (let i = 0; i < values.length; i++) {
//     values[i] = random(height);
//     states[i] = -1;
//   }
//   quickSort(values, 0, values.length - 1);
// }

// async function quickSort(arr, start, end) {
//   if (start >= end) {
//     return;
//   }
//   let index = await partition(arr, start, end);
//   states[index] = -1;

//   await Promise.all([
//     quickSort(arr, start, index - 1),
//     quickSort(arr, index + 1, end)
//   ]);
// }

// async function partition(arr, start, end) {
//   for (let i = start; i < end; i++) {
//     states[i] = 1;
//   }

//   let pivotValue = arr[end];
//   let pivotIndex = start;
//   states[pivotIndex] = 0;
//   for (let i = start; i < end; i++) {
//     if (arr[i] < pivotValue) {
//       await swap(arr, i, pivotIndex);
//       states[pivotIndex] = -1;
//       pivotIndex++;
//       states[pivotIndex] = 0;
//     }
//   }
//   await swap(arr, pivotIndex, end);

//   for (let i = start; i < end; i++) {
//     if (i != pivotIndex) {
//       states[i] = -1;
//     }
//   }

//   return pivotIndex;
// }

// async function swap(arr, a, b) {
//   let temp = arr[a];
//   arr[a] = arr[b];
//   arr[b] = temp;
// }

class Quicksort {
  partition(arr, low, high) {
    let i = low;
    let j = high + 1;
    let v = arr[low];

    while (true) {
      while (arr[++i] < v) {
        if (i == high) break;
      }
      while (v < arr[--j]) {
        if (j == low) break;
      }

      if (i >= j) break;
      this.swap(arr, i, j);
    }
    this.swap(arr, low, j);
    return j;
  }

  swap(arr, i, pivotIdx) {
    let temp = arr[i];
    arr[i] = arr[pivotIdx];
    arr[pivotIdx] = temp;
  }

  sort(arr, low, high) {
    if (high <= low) return;
    let pivotIdx = this.partition(arr, low, high);
    this.sort(arr, low, pivotIdx - 1);
    this.sort(arr, pivotIdx + 1, high);
    this.isSorted(arr, low, high);
  }

  isSorted(arr, low, high) {
    for (let i = low + 1; i < high; i++) {
      if (arr[i] < arr[i - 1]) return false;
    }
    return true;
  }
  startSorted(arr) {
    this.sort(arr, 0, arr.length - 1);
    console.log(arr);
  }
}

var sorting = new Quicksort();
var arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14];
sorting.startSorted(arr);
