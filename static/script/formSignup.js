let userType = document.getElementById('user_type');

let studentInputsConainerNotArray = document.getElementsByClassName('student-input-conainer');
let studentInputsConainer = Array.from(studentInputsConainerNotArray);

let studentInputsNotArray = document.getElementsByClassName('student-input');
let studentInputs = Array.from(studentInputsNotArray);

// let description = document.getElementById('');
// let address = document.getElementById('');
// let city = document.getElementById('');
// let region = document.getElementById('');
// let department = document.getElementById('');
// let zipCode = document.getElementById('');
// let picture = document.getElementById('');
let schoolInputsConainerNotArray = document.getElementsByClassName('school-input-container');
let schoolInputsConainer = Array.from(schoolInputsConainerNotArray);

let schoolInputsNotArray = document.getElementsByClassName('school-input');
let schoolInputs = Array.from(schoolInputsNotArray);

let schoolDescription = document.getElementById('description');
let countdownChar = document.getElementById('countdownChar');

function selectInput() {
    if(userType.value == 'student') {
        studentInputsConainer.forEach(studentInput => {
            studentInput.classList.remove("hide-input");
        });
        studentInputs.forEach(studentInput => {
            studentInput.required = true;
        });
        schoolInputsConainer.forEach(schoolInput => {
            schoolInput.classList.add("hide-input");
        });
        schoolInputs.forEach(schoolInput => {
            schoolInput.required = false;
        });
    } else if(userType.value == 'school') {
        studentInputsConainer.forEach(studentInput => {
            studentInput.classList.add("hide-input");
        });
        studentInputs.forEach(studentInput => {
            studentInput.required = false;
        });
        schoolInputsConainer.forEach(schoolInput => {
            schoolInput.classList.remove("hide-input");
        });
        schoolInputs.forEach(schoolInput => {
            schoolInput.required = true;
        });
    }
}

function updateCountdownChar() {
    width = schoolDescription.value.length;
    countdownChar.innerHTML = `${width} / 255`;
}

selectInput()

userType.addEventListener("change", selectInput);
schoolDescription.addEventListener("input", updateCountdownChar);