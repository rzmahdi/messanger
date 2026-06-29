const h3 = document.getElementById("h3");

async function check_login(){
    const token = localStorage.getItem("access_token");
    
    if(!token){
        window.location.href = "/login";
        return
    }
    
    const response = await fetch("/me", {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })

    if(response.status === 401){
        localStorage.removeItem("access_token");
        window.location.href = "/login";
        return
    }
    
    if(response.ok){
        const user = await response.json();
        h3.textContent = user.username;
    }
}

check_login();