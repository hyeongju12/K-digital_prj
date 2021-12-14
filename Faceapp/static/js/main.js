function init() {
    const divs = document.querySelectorAll('.gridBox');
    Array.from(divs).forEach(div => {
        div.addEventListener('click', classToggler);
    });

    loadEmotion();
};


const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];
let enumerator = -1;

function classToggler() {
    if (enumerator < colors.length) {
        enumerator++;
    }
    else {
        enumerator = 0
    };

    this.classList.add(colors[enumerator]); //this adds the color to divs Example: gridBox [field]  
    this.classList.remove(colors[enumerator - 1]);
    
    storeAnger(); // 함수호출
    storeEmbarrassment();
    storeHappy();
    storeNeutrality();
    storeSad();
    storeUnrest();
    graphNumbers();
    drawChart();

};

function loadClassToggler() {
    
    storeAnger(); // 함수호출
    storeEmbarrassment();
    storeHappy();
    storeNeutrality();
    storeSad();
    storeUnrest();
    graphNumbers();
    drawChart();

};

function storeAnger() {
    var className = document.getElementsByClassName('red');
    var IdStoreRed = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStoreRed.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("reds", JSON.stringify(IdStoreRed));
}

function storeEmbarrassment() {
    var className = document.getElementsByClassName('orange');
    var IdStoreOrange = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStoreOrange.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("oranges", JSON.stringify(IdStoreOrange));
}

function storeHappy() {
    var className = document.getElementsByClassName('yellow');
    var IdStoreYellow = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStoreYellow.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("yellows", JSON.stringify(IdStoreYellow));
}

function storeNeutrality() {
    var className = document.getElementsByClassName('green');
    var IdStoreGreen = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStoreGreen.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("greens", JSON.stringify(IdStoreGreen));
}

function storeSad() {
    var className = document.getElementsByClassName('blue');
    var IdStoreBlue = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStoreBlue.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("blues", JSON.stringify(IdStoreBlue));
}

function storeUnrest() {
    var className = document.getElementsByClassName('purple');
    var IdStorePurple = new Array();

    for (var j = 0; j < className.length; j++) {
        IdStorePurple.push(className[j].className.split(" ").splice(1, 1));
    }

    localStorage.setItem("purples", JSON.stringify(IdStorePurple));
}

function graphNumbers() {
    var reds = JSON.parse(localStorage.getItem("reds"));
    var oranges = JSON.parse(localStorage.getItem("oranges"));
    var yellows = JSON.parse(localStorage.getItem("yellows"));
    var greens = JSON.parse(localStorage.getItem("greens"));
    var blues = JSON.parse(localStorage.getItem("blues"));
    var purples = JSON.parse(localStorage.getItem("purples"));

    var total = reds.length + oranges.length + yellows.length + greens.length + blues.length + purples.length;
    console.log("you are happy " + greens.length + " times out of " + total + " days");
}

window.addEventListener('load', (event) => {
    var storedreds = JSON.parse(localStorage.getItem("reds"));
    for (var i = 0; i < storedreds.length; i++) {
        var redcolor = storedreds[i];
        var changecolor = document.getElementsByClassName(redcolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + redcolor + ' red');
    }

    var storedoranges = JSON.parse(localStorage.getItem("orange"));
    for (var i = 0; i < storedoranges.length; i++) {
        var orangecolor = storedoranges[i];
        var changecolor = document.getElementsByClassName(orangecolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + orangecolor + ' orange');
    }

    var storedyellows = JSON.parse(localStorage.getItem("yellows"));
    for (var i = 0; i < storedyellows.length; i++) {
        var yellowcolor = storedyellows[i];
        var changecolor = document.getElementsByClassName(yellowcolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + yellowcolor + ' yellow');
    }

    var storedgreens = JSON.parse(localStorage.getItem("greens"));
    for (var i = 0; i < storedgreens.length; i++) {
        var greencolor = storedgreens[i];
        var changecolor = document.getElementsByClassName(greencolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + greencolor + ' green');
    }

    var storedblues = JSON.parse(localStorage.getItem("blues"));
    for (var i = 0; i < storedblues.length; i++) {
        var bluecolor = storedblues[i];
        var changecolor = document.getElementsByClassName(bluecolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + bluecolor + ' blue');
    }

    var storedpurples = JSON.parse(localStorage.getItem("purples"));
    for (var i = 0; i < storedpurples.length; i++) {
        var purplecolor = storedpurples[i];
        var changecolor = document.getElementsByClassName(purplecolor)[0];
        changecolor.setAttribute('class', 'gridBox ' + purplecolor + ' purple');
    }

    // quoteRandom();
});

// function quoteRandom(){
//     const quotes = [];
//     quotes[0] = "“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein";
//     quotes[1] = "“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi";
//     quotes[2] = "“Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.” — Mark Twain";
//     quotes[3] = "“When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.”— Eleanor Roosevelt";
//     quotes[4] = "“When you change your thoughts, remember to also change your world.”—Norman Vincent Peale";
//     quotes[5] = "“It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest. —Walter Anderson";
//     quotes[6] = "“Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together.”—Diane McLaren";
//     quotes[7] = "“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau";
//     quotes[8] = "“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie";
//     quotes[9] = "“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers";
//     quotes[10] = "“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden";
//     quotes[11] = "“I never dreamed about success. I worked for it.” —Estée Lauder";
//     quotes[12] = "“Success is getting what you want, happiness is wanting what you get.” ―W. P. Kinsella";
//     quotes[13] = "“Don’t let yesterday take up too much of today.” — Will Rogers";
//     quotes[14] = "“If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you.” — Steve Jobs";    

//     var quote = quotes[Math.floor(Math.random()*quotes.length)];
//     document.getElementById("quotes").innerHTML = quote;
// }




