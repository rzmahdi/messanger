const register_form = document.getElementById("register-form");
const passwords_not_match_span = document.getElementById("passwords-not-match");

function check_password(password, confirm_password){
    return password === confirm_password
}


register_form.addEventListener("submit", async (e)=>{
    e.preventDefault();
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;
    const confirm_password = document.getElementById("register-confirm-password").value;

    if(check_password(password, confirm_password)){
        passwords_not_match_span.classList.remove("error");
        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password,
            })
        })
    }else{
        passwords_not_match_span.classList.add("error");
    }
})
