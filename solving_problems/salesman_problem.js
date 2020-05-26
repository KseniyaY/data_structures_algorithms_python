let cities = [];
let totalCities = 4;

let order = [];
let totalPermutations;
let count = 0;
let recordDistance;
let bestEver;

function setup() {
    createCanvas(600, 800);
    for (let i = 0; i < totalCities; i++) {
        v = createVector(random(width), random(height / 2));
        cities[i] = v;
        order[i] = i;
    }

    let d = calcDistance(cities, order);
    recordDistance = d;
    bestEver = order.slice();
}

function draw() {
    background(0);
    frameRate(5);
    fill(255);
    for (let i = 0; i < cities.length; i++) {
        ellipse(cities[i].x, cities[i].y, 8, 8)
    }

    stroke(255);
    strokeWeight(1);
    noFill();
    beginShape();
    for (let i = 0; i < order.length; i++) {
        let n = order[i];
        vertex(cities[n].x, cities[n].y)
    }
    endShape();

    translate(0, height / 2);
    stroke(255, 0, 255);
    strokeWeight(4);
    noFill();
    beginShape();
    for (let i = 0; i < order.length; i++) {
        let n = bestEver[i];
        vertex(cities[n].x, cities[n].y)
    }
    endShape();

    let d = calcDistance(cities, order);
    if (d < recordDistance) {
        recordDistance = d;
        bestEver = order.slice();
        totalPermutations = factorial(totalCities);
        console.log(recordDistance);
        console.log(totalPermutations);
    }

    textSize(48);
    var s = '';
    let percent = 100 * (count / totalPermutations);
    for (let i = 0; i < order.length; i++) {
        s += order[i];
    }
    fill(255);
    text(s, 20, height / 2 - 20);
    textSize(22);
    text("current combination is ", 20, height / 2 - 100);

    textSize(22);
    fill(255);
    text(nf(percent, 0, 2) + "% completed", 20, height / 2 - 150);

    nextOrder();

}

function swap(a, i, j) {
    let temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

function calcDistance(points, order) {
    var sum = 0;
    for (let i = 0; i < order.length - 1; i++) {
        let cityAIdx = order[i];
        let cityA = points[cityAIdx];
        let cityBIdx = order[i + 1];
        let cityB = points[cityBIdx];
        let d = dist(cityA.x, cityA.y, cityB.x, cityB.y);
        sum += d;
    }
    console.log("total distance of this route is " + sum);
    return sum;
}

//the lexical order algorithm
function nextOrder() {
    // STEP1
    let largestI = -1;
    for (let i = 0; i < order.length - 1; i++) {
        if (order[i] < order[i + 1]) {
            largestI = i;
        }
    }
    if (largestI == -1) {
        noLoop();
        console.log('finished');
    }

    //STEP 2
    let largestJ = -1;
    for (let j = 0; j < order.length; j++) {
        if (order[largestI] < order[j]) {
            largestJ = j;
        }
    }

    //STEP3
    swap(order, largestI, largestJ);

    //STEP4: reverse from largestI + 1 to the end
    let endArray = order.splice(largestI + 1);
    endArray.reverse();
    order = order.concat(endArray);
    count++;
}

function factorial(n) {
    if (n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

