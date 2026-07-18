function isTokenExpiringSoon(token, buffer_seconds=60){
    const payload = parseJwt(token);
    if(!payload || !payload.exp) return true;

    const now = Math.floor(Date.now() / 1000);
    return payload.exp - now < buffer_seconds;
}