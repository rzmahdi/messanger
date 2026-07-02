async function load_messages(){
    const res = await fetch(`/rooms/${room_id}/messages?limit=20&offset=0`);
    const messages = await res.json();

    const container = document.getElementById("messgaes");

    messages.reverse().forEach(message => {
        add_message(message);
    });
}
