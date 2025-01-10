document.getElementById('request-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const sessionId = document.getElementById('session-id').value;
    const songName = document.getElementById('song-name').value;
    const requester = document.getElementById('requester').value;

    const response = await fetch('http://localhost:5000/request-song', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            session_id: sessionId,
            password: password,
            song_name: songName,
            requester: requester,
        }),
    });

    const messageElement = document.getElementById('message');
    if (response.ok) {
        messageElement.textContent = 'Request sent successfully!';
        messageElement.style.color = 'green';
    } else {
        const error = await response.json();
        messageElement.textContent = error.error || 'Failed to send request.';
        messageElement.style.color = 'red';
    }
});
