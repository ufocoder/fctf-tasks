fetch('/xhr.php', { method: 'GET' }).then(() => {
    setInterval(() => {
        const hashes = ["#one", "#of", "#them"];
        window.location = hashes[Math.round(Math.random() * (hashes.length - 1))];
    }, 1000);
})
