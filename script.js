document.getElementById('emojiForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const userText = document.getElementById('user_text').value;
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_text: userText }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const results = document.getElementById('results');

        results.innerHTML = '';
        
        data.forEach(item => {
            const p = document.createElement('p');
            p.textContent = `Emoji: ${item[0]} - Decoded: ${item[1]} - Info: ${JSON.stringify(item[2])}`;
            results.appendChild(p);
        });
    })
    .catch(error => console.error('Error:', error));
});