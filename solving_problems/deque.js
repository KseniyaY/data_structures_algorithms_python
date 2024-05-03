//Deques are useful in various scenarios, such as –

//managing states in applications, for example its useful in undo operations in applications like Microsoft Word.
//problems where elements need to be manipulated from both ends efficiently.
//storing history, recently visited links are inserted at the front of deque, 
//and as per certain size limit of deque, links keeps getting removed from rear of the deque.

export class Deque {
    constructor(){
        this.deque = [];
    }
    //front is the left-end of the deque
    addFront(el){
       if(!el) return;
       this.deque.unshift(el);
    }
    //rear is the right-side/end of the deque
    addRear(el) {
        if(!el) return;
        this.deque.push(el);
    }

    isEmpty() {
        return !!this.deque.length;
    }

    size(){
        return this.deque.length;
    }

    removeFront(){
        if(this.isEmpty()) return null;
        this.deque.shift();
    }

    removeRear(){
        if(this.isEmpty()) return null;
        this.deque.pop();
    }

    getFront(){
        if(this.isEmpty()) return null;
        return this.deque[0];
    }

    getRear(){
        if(this.isEmpty()) return null;
        return this.deque[this.size()-1];
    }
}

const deque = new Deque();

//Add 10 and 20 to the end of deque
deque.addRear(10);
deque.addRear(20);

//Add 5 to the front of deque
deque.addRear(5);

//log the deque array from the current deque class instance/object
console.log(deque.deque);

// Get first element of deque
console.log(deque.getFront());

// Get last element of deque 
console.log(deque.getRear());

// Removing item at the front of array
deque.removeFront();
console.log(deque.deque);

// Removing item at the end of array 
deque.removeRear();
console.log(deque.deque);


//Output
//[ 5, 10, 20 ]
//5
//20
//[ 10, 20 ]
//[ 10 ]

