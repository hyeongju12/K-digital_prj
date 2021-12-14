let addBtn = document.getElementById("addNote");
let clearBtn = document.getElementById("clearNote")
let addtitle = document.getElementById("title");
let addnote = document.getElementById("note");

addBtn.addEventListener("click", (e) => {
    if (addtitle.value == "" || addnote.value == "") {
        return alert("Add title and description");
    }
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesObj = [];
    } else {
        notesObj = JSON.parse(notes);
    }
    let myObj = {
        title: addtitle.value,
        note: addnote.value
    }
    notesObj.push(myObj);

    localStorage.setItem("notes", JSON.stringify(notesObj));
    addtitle.value = "";
    addnote.value = "";

    showNotes();
});

clearBtn.addEventListener("click", (e) => {
    title.value = "";
    note.value = "";
})

function showNotes() {
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesObj = [];
    } else {
        notesObj = JSON.parse(notes);
    }

    let html = "";
    notesObj.forEach(function (element, index) {
        html += `
        <div id="notes" class="notes">
            <div class="savedNotes">
                <h3 class="title">${element.title}</h3>
                <p class="text">${element.note}</p>
                <button id="${index}" onclick="deleteNote(this.id)" class="delete"><i class="fas fa-trash"></i></button>
            </div>
        </div>
        `;
    });

    let noteElem = document.getElementById("savednotesContainer");
    if (notesObj.length != 0) {
        noteElem.innerHTML = html;
    } else {
        noteElem.innerHTML = "No Notes Yet";
    }
}

function deleteNote(index) {
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesObj = [];
    } else {
        notesObj = JSON.parse(notes);
    }

    notesObj.splice(index, 1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    showNotes();
}


showNotes();

