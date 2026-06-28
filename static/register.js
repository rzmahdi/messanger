const register_form = document.getElementById("register-form");
const passwords_not_match_span = document.getElementById("passwords-not-match");
const register_notif_modal = document.getElementById("register-modal-overlay-notif");
const register_notif_text = document.getElementById("register-notif-modal-text");

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

        if(response.ok){
            register_notif_modal.classList.add("show");
            register_notif_text.innerHTML = "User successfuly created✅";
        }else if(response.status === 409){
            register_notif_modal.classList.add("show");
            register_notif_text.innerHTML = "User allready exists!❌";
        }
    }else{
        passwords_not_match_span.classList.add("error");
    }
})
