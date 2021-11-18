/* TODO: Decide on wether or not this scrit will be used for all the forms in the app or 
only for login, register and change password. 

Other forms that might appear in the app: search for indeces, checking histoery? etc
*/

let forms = document.querySelectorAll("form.form--validate");
forms.forEach(element => element.setAttribute("novalidate", true))

function check_validity(field) {
    let validity = field.validity

    if (field.disabled || field.type === "file" || field.type === "reset" || field.type === "button") {
        return
    }

    else {
        if (validity.valid) return;

        if (validity.vaulueMissing) return "Please fill out this field."

        if (validity.typeMismatch) {
            if (field.type === "email") return "Please provide a valid email address"

            //If other field types arise, add here.
        }

        if (validity.tooShort) return $`Your {field.getAttribute("name")} should be at least {field.getAttribute("minlength")} characters long.`

        if (validity.tooLong) return $`Your {field.getAttribute("name")} should have a maximum of {field.getAttribute("maxlength")} characters.`

        if (validity.patternMismatch) return "Please match the requested format."
    }



}

//Listen to blur events, process those coming from forms w. class ".validate"
document.addEventListener("focusout", (e) => {
    if (!e.target.form.classList.contains("form--validate")) {
        return;
    }

    let field = e.target;
    let error = check_validity(field);

    if (error) {
        field.classList.toggle("is-invalid")
        //TODO: show error function
    }

})


