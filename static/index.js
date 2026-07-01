const display_username = document.getElementById("display-username");
const rooms_container = document.getElementById("rooms-container");

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString();
}

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
        display_username.textContent = user.username;
    }
}


async function display_rooms(){
    rooms_response = await fetch("/rooms");
    rooms = await rooms_response.json();

    rooms.forEach(room => {
    const div = document.createElement("div");

    div.className = "room";
    div.dataset.room_id = room.id;

    div.innerHTML = `
            <div class="room-info">
                <h3>${room.name}</h3>
                <span>Created by ${room.creator.username}</span>
            </div>

            <span class="room-date">${formatDate(room.created_at)}</span>
    `;

    div.addEventListener("click", ()=>{
        location.href = `/rooms/${room.id}`
    });

    rooms_container.appendChild(div);
});
}

check_login();
display_rooms();