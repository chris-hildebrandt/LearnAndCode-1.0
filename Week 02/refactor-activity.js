let a = [];

// Function to add a user object to the array
function b(n, ag, ad) {
    let c = { d: n, e: ag, f: ad };
    a.push(c);
}

// Function to find a user object by name
function g(n) {
    for (let i = 0; i < a.length; i++) {
        if (a[i].d === n) {
            return a[i];
        }
    }
    return null;
}

// Function to update a user object's age and email by name
function h(n, new_ag, new_ad) {
    for (let i = 0; i < a.length; i++) {
        if (a[i].d === n) {
            a[i].e = new_ag;
            a[i].f = new_ad;
        }
    }
}

// Function to delete a user object by name
function j(n) {
    for (let i = 0; i < a.length; i++) {
        if (a[i].d === n) {
            a.splice(i, 1);
            return;
        }
    }
}

// Add some data
b('John', 30, 'john@doe.com');
b('Jane', 25, 'jane@doe.com');
b('Bob', 35, 'bob@doe.com');

// Print data
for (let i = 0; i < a.length; i++) {
    console.log('Name: ' + a[i].d + ', Age: ' + a[i].e + ', Email: ' + a[i].f);
}

// Find a user
let k = g('Jane');
if (k != null) {
    console.log('Found user: ' + k.d + ', Age: ' + k.e + ', Email: ' + k.f);
}

// Update a user
h('John', 31, 'john@doe.com');
